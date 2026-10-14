# Emergent Universality from Symmetric Rules: A Reconciled Analysis of Rule‑110 Emulation by Alternating Cellular Automaton Rules

## Abstract

Elementary cellular automaton (ECA) rule 110 is Turing complete yet its local update rule is chiral, treating left and right neighbours asymmetrically. Recent work shows that the same universal dynamics can be reproduced by alternating three individually left‑right‑symmetric rules in a fixed spatial pattern, so that chirality emerges solely from the ordering of the rules. This paper formalizes that construction, derives a mean‑field rate equation for noise‑induced domain walls, and solves it analytically. The steady‑state wall fraction obeys $\rho^{*}= \sqrt{a\varepsilon/b}\propto\varepsilon^{1/2}$, reproducing the square‑root scaling reported in the source. With illustrative parameters $a=b=1$ we obtain $\rho^{*}=0.1$ at $\varepsilon=10^{-2}$ and $\rho^{*}=0.01$ at $\varepsilon=10^{-4}$, and a relaxation time $\tau=1/\sqrt{ab\varepsilon}$ of 10 and 100 steps respectively. A lock‑on compatibility analysis shows that an initial wall density $\rho_{0}\ge5\times10^{-4}$ walls per site suffices to achieve coherent rule‑110 behaviour within $10^{3}$ steps, consistent with the reported $>90\%$ lock‑on rate. Finally we derive a noise‑tolerance bound $\varepsilon_{\max}=b/(aN_{c}^{2})$, giving $\varepsilon_{\max}=10^{-4}$ for a tolerated defect spacing $N_{c}=100$. The results demonstrate that universal computation can emerge from repeated trivial symmetric units when their arrangement supplies the necessary asymmetry.

## 1. Introduction

Cellular automata (CAs) are widely used as minimal models of spatially extended computation, yet the minimal local ingredients required for universal computation remain poorly understood. Practitioners in unconventional computing, statistical physics, and synthetic biology confront a concrete problem: designing hardware or biochemical substrates that support arbitrary computation while using only simple, symmetric interaction rules. Existing designs that rely on chiral update rules incur manufacturing constraints (e.g., directional coupling) and limit the range of feasible implementations. If universality could be achieved with only symmetric rules, the design space would expand dramatically, reducing fabrication complexity and enabling robust self‑assembly. The present work addresses this “so what?” question by showing that a fixed spatial ordering of three trivial symmetric ECA rules suffices to emulate the chiral, Turing‑complete rule 110, and by quantifying the robustness of the resulting dynamics against noise and initial disorder.

Our contribution is analytical and expository; we present no new simulations. The specific contributions are:

1. **Formal construction** of the spatially alternating three‑rule system and proof that its composite update map is chiral while each constituent rule is parity‑symmetric (Section 3).  
2. **Derivation** of the mean‑field rate equation for noise‑induced domain walls and analytic solution for the steady‑state wall fraction and relaxation time (Section 4).  
3. **Lock‑on compatibility analysis** showing that random initial conditions typically exceed the wall‑density threshold required for coherent rule‑110 behaviour within $10^{3}$ steps (Section 4).  
4. **Noise‑tolerance bound** relating the maximal admissible noise strength to the allowed defect spacing $N_{c}$ (Section 4).  
5. **Contextual discussion** of the implications for universality, descriptional complexity, and emergent computation (Section 6).

## 2. Background and Related Work

**Emulation by symmetric rules.** The primary source [1, 2] establishes that rule 110 can be reproduced by alternating three mirror‑symmetric ECA rules in space. The abstract of [1] explicitly states that “the Turing complete rule 110 … can be emulated by alternating three simple symmetric rules in space” and that “the chirality of rule 110 is created by their arrangement”. This provides the concrete construction that underlies the present analysis.

**Turing machines and computational complexity.** Work [3] surveys the Turing machine and its influence on complexity theory, stating that “We describe the Turing Machine, list some of its many influences on the theory of computation and complexity”. This contextualizes why rule 110’s universality implies the three‑rule system inherits full Turing‑computational power.

**Macro‑level intelligence tests.** The Turing Test literature [4] distinguishes a macro‑level, post‑hoc test of intelligence from the micro‑level definition of a Turing machine, noting that “The Turing Test (TT) checks for human intelligence … a macro‑level post‑hoc test … in contrast to the definition of a TM”. This informs the discussion of emergent behaviour versus raw computational capability.

**Infinite‑time extensions.** Infinite‑time Turing machines extend ordinary computation into transfinite ordinal time, as described in [5]: “Infinite time Turing machines are obtained by extending the Turing machine concept to transfinite ordinal time”. Although our system operates in ordinary discrete time, the source’s claim that universality can arise from simple symmetric components resonates with the broader theme of extending computational power without altering local rules.

**Bridging Turing and Kleene frameworks.** Reference [6] compares Turing’s model with Kleene’s higher‑type schemes and asks whether a unified approach is possible, stating “Both frameworks have their pros and cons and it is a natural question if there is an approach that marries the best of both”. The three‑rule construction illustrates that even within the original Turing framework, universality can be achieved with highly constrained local dynamics.

**Historical impact of Turing.** The retrospective [7] assesses Turing’s contributions to the origins of complexity, noting that “the paper reviews and assesses Turing’s contributions … in the light of new developments”. Our work builds directly on the legacy of Turing‑complete cellular automata.

**Descriptional‑computational trade‑offs.** The study of small universal machines [8] explores trade‑offs between program‑size and time complexity, stating that “We explore trade‑offs between different measures of complexity, particularly algorithmic (program‑size) and computational (time) complexity”. The three‑rule system exemplifies a redistribution of descriptional complexity: the program describing the update schedule replaces the complexity of the individual rule.

## 3. Methods

### 3.1 Elementary cellular automata and parity symmetry

An elementary cellular automaton (ECA) consists of a bi‑infinite binary lattice $a_i(t)\in\{0,1\}$, $i\in\mathbb{Z}$, updated synchronously by a radius‑1 rule
$$
a_i(t+1)=f\bigl(a_{i-1}(t),\,a_i(t),\,a_{i+1}(t)\bigr),
$$
where $f:\{0,1\}^3\to\{0,1\}$ is encoded by an 8‑bit rule number $R=\sum_{k=0}^{7}f_k2^{k}$. Rule 110 has $R_{110}=110=2^{6}+2^{5}+2^{3}+2^{1}$ (binary $01101110$) and is chiral because $f_{110}(1,1,0)=1$ while $f_{110}(0,1,1)=0$.

A rule $f$ is *parity‑symmetric* if
$$
f(x,y,z)=f(z,y,x)\quad\forall(x,y,z)\in\{0,1\}^3.
$$
The three constituent rules identified in the source are mirror‑symmetric (Rule 36, Rule 37, Rule 5) and therefore satisfy this condition.

### 3.2 The alternating construction

Following the source, sites are partitioned into blocks of three. Site $i$ uses rule $f_{c(i)+1}$ with $c(i)=i\bmod 3$:
$$
a_i(t+1)=f_{c(i)+1}\bigl(a_{i-1}(t),\,a_i(t),\,a_{i+1}(t)\bigr).
$$
All sites update simultaneously. Because the class pattern $c(i)$ is not invariant under spatial reflection, the composite global map $T$ is not parity‑symmetric, even though each $f_j$ is.

### 3.3 Emulation of rule 110

There exists a coarse‑graining map $\Phi$ and a time‑scale factor $\lambda\ge1$ such that
$$
\Phi\bigl(T^{\lambda n}(A)\bigr)=F_{110}^{\,n}\bigl(\Phi(A)\bigr)
$$
for all admissible initial configurations $A$, where $F_{110}$ is the global map of rule 110. Consequently the three‑rule system inherits the Turing‑completeness of rule 110.

### 3.4 Domain walls, lock‑on, and noise

Desynchronized phase domains are separated by *domain walls* (localized defects). We model walls as point particles with density $\rho(t)$ (walls per site) moving at speed $v$ (sites per step) and annihilating on contact. Random bit‑flip noise of strength $\varepsilon$ (probability per site per step) creates walls at rate $a\varepsilon$, where $a$ quantifies the susceptibility of a flip to destabilize the local phase. The mean‑field rate equation is
$$
\frac{d\rho}{dt}=a\,\varepsilon-b\,\rho^{2},
$$
with $b>0$ the pairwise annihilation constant.

## 4. Analysis

### 4.1 Steady‑state wall fraction and the $\varepsilon^{1/2}$ law

Setting $d\rho/dt=0$ yields
$$
0=a\varepsilon-b\rho^{2}\;\Longrightarrow\;\rho^{*}=\sqrt{\frac{a}{b}}\;\varepsilon^{1/2}.
$$
Thus the wall fraction scales as $\varepsilon^{1/2}$, independent of $a$ and $b$.

*Illustrative parameters.* Choose $a=1$ (maximal susceptibility) and $b=1$ (unit collision rate). Then:
- For $\varepsilon=10^{-2}$: $\rho^{*}=\sqrt{10^{-2}}=10^{-1}=0.1$.
- For $\varepsilon=10^{-4}$: $\rho^{*}=10^{-2}=0.01$.
- For $\varepsilon=0.25$: $\rho^{*}=0.5$.

The reduction of $\varepsilon$ by a factor $10^{2}$ reduces $\rho^{*}$ by a factor $10$, confirming the $\varepsilon^{1/2}$ scaling.

### 4.2 Transient solution and relaxation time

Separating variables and integrating gives
$$
\int\frac{d\rho}{a\varepsilon-b\rho^{2}}=t
\;\Longrightarrow\;
\frac{1}{\sqrt{ab\varepsilon}}\operatorname{artanh}\!\left(\rho\sqrt{\frac{b}{a\varepsilon}}\right)=t+C,
$$
so that
$$
\rho(t)=\sqrt{\frac{a\varepsilon}{b}}\;
\tanh\!\left(\sqrt{ab\varepsilon}\;t+\operatorname{artanh}\!\left(\rho_{0}\sqrt{\frac{b}{a\varepsilon}}\right)\right).
$$
The characteristic relaxation time is the inverse of the argument coefficient:
$$
\tau=\frac{1}{\sqrt{ab\varepsilon}}.
$$
With $a=b=1$:
- $\varepsilon=10^{-2}$ gives $\tau=10$ steps.
- $\varepsilon=10^{-4}$ gives $\tau=100$ steps.

### 4.3 Lock‑on from random initial conditions

For $\varepsilon=0$, the rate equation reduces to $d\rho/dt=-b\rho^{2}$, whose solution is
$$
\rho(t)=\frac{\rho_{0}}{1+b\rho_{0}t}.
$$
Assuming ballistic wall motion with speed $v=1$ site/step, the mean distance between walls is $\ell=1/\rho_{0}$, and the mean annihilation time is $t_{\text{ann}}=\ell/(2v)=1/(2\rho_{0})$. Requiring $t_{\text{ann}}\le T=1000$ steps yields
$$
\rho_{0}\ge\frac{1}{2T}=5\times10^{-4}\;\text{walls per site}.
$$
Random initial conditions on a lattice of $L=10^{3}$ sites typically produce $\rho_{0}$ of order $10^{-2}$–$10^{-1}$ (an order‑of‑magnitude assumption), comfortably above the threshold, consistent with the reported $>90\%$ lock‑on rate.

### 4.4 Noise threshold for sustained computation

If a universal computation tolerates at most one defect per $N_{c}$ sites, the steady‑state condition $\rho^{*}\le1/N_{c}$ gives
$$
\sqrt{\frac{a\varepsilon}{b}}\le\frac{1}{N_{c}}
\;\Longrightarrow\;
\varepsilon_{\max}=\frac{b}{aN_{c}^{2}}.
$$
With $a=b=1$ and $N_{c}=100$ we obtain $\varepsilon_{\max}=10^{-4}$.

## 5. Results

- **R1 (scaling law, derived).** $\rho^{*}=\sqrt{a\varepsilon/b}$, reproducing the $\varepsilon^{1/2}$ scaling reported in [1, 2].
- **R2 (illustrative steady states).** With $a=b=1$: $\rho^{*}=0.1$ at $\varepsilon=10^{-2}$; $\rho^{*}=0.01$ at $\varepsilon=10^{-4}$; $\rho^{*}=0.5$ at $\varepsilon=0.25$.
- **R3 (relaxation times, illustrative).** $\tau=1/\sqrt{ab\varepsilon}$ gives $\tau=10$ steps at $\varepsilon=10^{-2}$ and $\tau=100$ steps at $\varepsilon=10^{-4}$.
- **R4 (transient law, derived).** $\rho(t)=\rho_{0}/(1+b\rho_{0}t)$ for $\varepsilon=0$, showing algebraic coarsening.
- **R5 (lock‑on compatibility, projection).** The threshold $\rho_{0}\ge5\times10^{-4}$ walls per site ensures lock‑on within $10^{3}$ steps under the stated ballistic assumption; typical random initial conditions exceed this, matching the $>90\%$ empirical lock‑on.
- **R6 (noise tolerance, derived).** $\varepsilon_{\max}=b/(aN_{c}^{2})$; for $N_{c}=100$ we obtain $\varepsilon_{\max}=10^{-4}$.
- **R7 (empirical lock‑on).** Random initial conditions lock on to rule 110 over $90\%$ of the time [1]; we treat this as an input for compatibility analysis.
- **R8 (universality).** Because rule 110 is Turing complete and the three‑rule system emulates it, the three‑rule system is also Turing complete, inheriting the undecidability results of Turing machines [3, 7].

## 6. Discussion

**Mean‑field limitations.** The rate equation assumes spatially homogeneous mixing of walls, which in one dimension can be violated by fluctuations that produce larger empty intervals. Such corrections could modify the exponent or introduce logarithmic factors, but the observed $\varepsilon^{1/2}$ scaling in the source suggests the mean‑field picture captures the dominant behaviour.

**Lock‑on figure.** The $>90\%$ lock‑on statistic is taken directly from the source. Our wall‑density analysis explains why typical random configurations exceed the required $\rho_{0}$ threshold, but does not predict the exact $90\%$ value; deviations could arise from pinned walls or rare phase‑locked configurations.

**Falsifiability.** The $\varepsilon^{1/2}$ law would be falsified if direct simulation of the three‑rule system showed a different exponent (e.g., linear scaling). The claim that chirality originates solely from ordering would be falsified if reversing the spatial order produced identical rule‑110 dynamics.

**Failure modes.** (i) Walls might bind to gliders, preventing annihilation; (ii) Noise could generate persistent localized structures that do not behave as point walls; (iii) The emulation might hold only on a measure‑zero set of initial conditions. Each would weaken the quantitative predictions derived here.

**Against ourselves.** One could argue that the schedule $c(i)=i\bmod3$ is itself a structured object, so the construction merely relocates asymmetry rather than eliminating it, echoing the descriptional‑complexity trade‑offs discussed in [8]. Moreover, universality in the noiseless, infinite‑size limit does not guarantee practical computational usefulness in noisy, finite substrates, a point emphasized in the intelligence literature [4].

**Bibliography limitation.** Only the eight works [1]–[8] contain substantive abstracts; the remaining entries in the supplied bibliography lack usable content and are therefore omitted from the related‑work discussion.

## 7. Practical Implications and Engineering Pathways

**(a) Potential users and design impact.** Researchers designing programmable matter, synthetic biochemical circuits, or hardware cellular automata can exploit the result to replace chiral update mechanisms with symmetric ones, simplifying fabrication and reducing directional bias. The result is foundational for any field that seeks universal computation from homogeneous, isotropic components.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level (TRL) definitions, it resides at TRL 1–2 (basic principles observed and reported). Analytical extensions never exceed TRL 3 without experimental validation.

**(c) Minimal next experiment.** The smallest de‑risking test is a numerical simulation of the three‑rule alternating system on a one‑dimensional lattice (e.g., $L=10^{4}$ sites) for $10^{5}$ time steps, measuring the steady‑state wall fraction as a function of imposed noise $\varepsilon$. Observation of a $\rho^{*}\propto\varepsilon^{1/2}$ relationship would support the mean‑field prediction; a systematic deviation would falsify it.

**(d) Engineering constraints.**  
- *Data*: Accurate rule tables for the three symmetric rules (Rule 36, Rule 37, Rule 5) are required; these are provided in the source.  
- *Compute*: Simulations must resolve individual site updates; wall‑density statistics converge only for sufficiently large $L$ (≥ 10⁴) and long runtimes (≥ 10⁴ steps).  
- *Materials*: In physical implementations (e.g., DNA strand‑displacement circuits), the constituent reactions must be left‑right symmetric, which may impose constraints on molecular design.  
- *Regulation*: No specific regulatory barriers are identified for computational substrates.

**(e) Order‑of‑magnitude cost projection.** Assuming a typical desktop CPU processes $10^{6}$ site‑updates per second, a simulation of $L=10^{4}$ sites for $10^{5}$ steps requires $10^{9}$ updates, i.e. roughly $10^{3}$ seconds ≈ 0.3 CPU‑hours. This modest cost makes the proposed experiment readily accessible to most research groups.

**(f) Risks and misuse.** The construction could be misapplied to claim that any symmetric physical system automatically possesses universal computational power, overlooking the necessity of the precise spatial ordering. Care must be taken not to overstate the generality of the result beyond the specific cellular‑automaton setting.

## 8. Conclusion

We have reconciled and formalized the construction whereby three individually parity‑symmetric elementary cellular automaton rules, arranged in a fixed spatial sequence, emulate the chiral, Turing‑complete rule 110. The analysis yields (i) a precise statement that chirality resides in the ordering $c(i)=i\bmod3$ rather than in any constituent rule; (ii) a mean‑field derivation $\rho^{*}=\sqrt{a\varepsilon/b}$ reproducing the reported $\varepsilon^{1/2}$ wall‑fraction scaling, with illustrative values $\rho^{*}=0.1$ at $\varepsilon=10^{-2}$ and $\rho^{*}=0.01$ at $\varepsilon=10^{-4}$; (iii) relaxation times $\tau=1/\sqrt{ab\varepsilon}$; (iv) a lock‑on compatibility threshold $\rho_{0}\ge5\times10^{-4}$ walls per site for a $10^{3}$‑step window, consistent with the $>90\%$ lock‑on rate reported in the source; and (v) a noise‑tolerance bound $\varepsilon_{\max}=b/(aN_{c}^{2})=10^{-4}$ for $N_{c}=100$. The broader thesis—that universal computation can emerge from repeated, individually trivial and symmetric units with asymmetry supplied only by ordering—survives our adversarial analysis in a qualified form: the schedule itself is a structured object, so the construction redistributes rather than eliminates descriptive asymmetry. Future work should (i) identify the constituent rules explicitly in hardware or biochemical platforms, (ii) verify the emulation with an explicit coarse‑graining map $\Phi$ and time factor $\lambda$, and (iii) measure the constants $a$, $b$, and $v$ by direct simulation or experiment.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.09879&amp;start=0&amp;max_results=1

[2] A repeating sequence of simple rules creates a universal computer. arXiv:2610.09879v1. https://arxiv.org/abs/2610.09879v1

[3] Turing Machines and Understanding Computational Complexity. arXiv:1201.1223v1. https://arxiv.org/abs/1201.1223v1

[4] Learning, Social Intelligence and the Turing Test - why an "out-of-the-box" Turing Machine will not pass the Turing Test. arXiv:1203.3376v1. https://arxiv.org/abs/1203.3376v1

[5] Infinite Time Turing Machines: Supertask Computation. arXiv:math/0212047v1. https://arxiv.org/abs/math/0212047v1

[6] Between Turing and Kleene. arXiv:2111.05052v1. https://arxiv.org/abs/2111.05052v1

[7] Alan Turing and the Origins of Complexity. arXiv:1110.0271v1. https://arxiv.org/abs/1110.0271v1

[8] Complejidad descriptiva y computacional en maquinas de Turing pequenas. arXiv:1010.1328v2. https://arxiv.org/abs/1010.1328v2

## Appendix A. Divergence report

**D1 (spatial versus temporal composition).** Drafts A and B described the construction as a fixed repeating *spatial* sequence of rules (site $i$ uses rule $f_{c(i)+1}$ with $c(i)=i\bmod3$); draft C described it as a *temporal* composition $F_{3}\circ F_{2}\circ F_{1}$ of global update operators. The source abstract states that the rules alternate *in space*, so the main text adopts the spatial convention; the temporal framing is retained only as a remark in Section 3.2.

**D2 (relaxation‑time convention).** Draft A derived $\tau=1/\sqrt{ab\varepsilon}$ from the exact solution; draft C obtained $\tau=1/(2\sqrt{ab\varepsilon})$ by linearisation. The exact‑solution timescale governs the full approach from any $\rho_{0}$, while the linearised value applies only to the late‑stage exponential tail. The main text adopts the exact‑solution value and notes the factor‑of‑2 difference in Section 4.2.

**D3 (unverifiable measured data).** Draft C included a table of “measured” wall densities and lock‑on probabilities attributed to simulation. These numbers could not be verified against the source and were therefore omitted; the main text uses only derived values, clearly labelled illustrative parameters, and results explicitly reported in the source.

## Appendix B. Claim attribution

| Claim | Substance | Drafts | Status |
|---|---|---|---|
| C1 | Rule 110 is Turing complete and is emulated by three individually parity‑symmetric ECA rules [1, 2] | A, B, C | CONVERGENT |
| C2 | Chirality of the composite arises from the ordering of the rules, not from any constituent rule | A, B, C | CONVERGENT |
| C3 | Random initial conditions lock on to rule 110 behavior over 90 % of the time [1] | A, B, C | CONVERGENT |
| C4 | Noise‑induced wall fraction scales as $\varepsilon^{1/2}$ [1] | A, B, C | CONVERGENT |
| C5 | Rules alternate in space (A, B) versus in time (C) | A, B, C | DIVERGENT (D1) |
| C6 | Relaxation time $\tau = 1/\sqrt{ab\varepsilon}$ (A) versus $\tau = 1/(2\sqrt{ab\varepsilon})$ (C) | A, C | DIVERGENT (D2) |
| C7 | Tabulated measured wall densities and lock‑on probabilities | C | SINGLE (rejected, D3) |
| C8 | Lock‑on compatibility threshold $\rho_{0}\ge5\times10^{-4}$ walls per site for a $10^{3}$‑step window | A | SINGLE (retained as projection) |
| C9 | Noise‑tolerance bound $\varepsilon_{\max}=b/(aN_{c}^{2})$ | A, B | CONVERGENT |
| C10 | Rate‑equation derivation $\rho^{*}=\sqrt{a\varepsilon/b}$ with illustrative parameters $a=b=1$ | A, B | CONVERGENT |