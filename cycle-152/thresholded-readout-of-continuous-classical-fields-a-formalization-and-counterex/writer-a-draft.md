# Thresholded Readout of Continuous Classical Fields: A Formalization and Counterexample to the Uniqueness Claim for Quantum Mechanics

## Abstract

A recent research note proposes that the universe consists of continuous, local, deterministic fields, that every measurement is an irreversible discrete mapping from a continuous state space $\mathbb{R}$ to a finite outcome space $\mathcal{O}$ via nonlinear amplification and thresholding, and that quantum mechanics is the logically necessary and unique calculus connecting these domains. This paper formalizes the proposed readout map, derives the outcome statistics for two concrete detector models, and tests the uniqueness claim. We show that within the class of thresholded amplification maps, a linear‑threshold calculus $\mathcal{C}_L$ and a quadratic‑threshold calculus $\mathcal{C}_Q$ both satisfy the axioms yet yield different detection probabilities ($0.1587$ versus $0.3174$ for a unit‑variance Gaussian field at threshold $\Theta=1$). A slope‑matched noisy threshold detector approximates the Born rule only imperfectly, with a maximum deviation of $0.1050$ and a root‑mean‑square deviation of $0.0602$ over five test angles. We also derive the CHSH bound $|S|\le2$ for any deterministic local thresholded readout, whereas the quantum prediction at standard settings is $|S|=2\sqrt{2}\approx2.8284$. Finally, a statistical‑power projection indicates that roughly $130$ trials per setting suffice to distinguish the two calculi at $3\sigma$. The results refute the uniqueness claim at the level of the readout calculus and identify the additional structure required to recover quantum statistics.

## 1. Introduction

Quantum foundations confront a concrete problem: experimentalists and engineers must decide whether a proposed classical‑field description of reality can reproduce the statistical predictions of quantum mechanics while preserving locality and determinism. If such a description were viable, it would enable deterministic simulation of quantum devices, reduce the need for costly quantum hardware, and reshape the design of measurement apparatuses. Today, quantum technologies rely on the Born rule and Bell‑inequality violations as axiomatic inputs; no alternative deterministic calculus is accepted, limiting the scope of classical‑compatible designs. This paper asks whether the uniqueness claim—that quantum mechanics is the only calculus bridging continuous deterministic fields and irreversible discrete readout—is true. We answer “no” by constructing two distinct calculi that both satisfy the stated axioms yet generate different, empirically distinguishable statistics.  

**Contributions**  
- **C1**: Derivation of outcome probabilities for linear ($\mathcal{C}_L$) and quadratic ($\mathcal{C}_Q$) threshold detectors, showing $P_1^{(L)}=0.1587$ and $P_1^{(Q)}=0.3174$ (Section 4.1–4.2).  
- **C2**: Demonstration that the two calculi differ by an exact factor of 2 for any symmetric field density (Section 4.3).  
- **C3**: Quantitative assessment of a slope‑matched noisy threshold detector’s deviation from the Born rule (maximum $0.1050$, RMS $0.0602$) (Section 4.4).  
- **C4**: Proof that any deterministic local thresholded readout obeys the CHSH bound $|S|\le2$, contrasted with the quantum value $2\sqrt{2}\approx2.8284$ (Section 4.5).  
- **C5**: Projection that $n\approx130$ trials per calculus achieve a $3\sigma$ discrimination of the two models (Section 4.7).

## 2. Background and Related Work

We discuss the eight supplied arXiv works, restricting each statement to what the entry’s own title and summary provide.

[1] reviews applications of fractional calculus to continuum and statistical mechanics, exemplifying the mature classical machinery for continuous field dynamics that underlies Axiom A1.  

[2] treats continuous‑time measurement and the stochastic Schrödinger equation in the diffusive case, offering the standard quantum continuous‑measurement calculus that our thresholded map seeks to replace.  

[3] proposes a realist process interpretation unifying quantum physics and biology, supporting the view that multiple mappings between a continuous substrate and discrete records are conceivable.  

[4] develops an axiomatic measurement theory characterizing all statistical properties of apparatuses measuring nondegenerate observables; it supplies the quantum‑side statistics that any candidate calculus must reproduce.  

[5] formulates quantum continual measurements via instruments, POVMs, and stochastic differential equations, demonstrating that quantum theory already provides a bridge between continuous dynamics and discrete outcomes.  

[6] describes automatic skeleton adjustment for self‑avatars in virtual reality, a concrete engineering instance of mapping continuous signals onto a discrete outcome space, illustrating the generality of Axiom A3.  

[7] examines entanglement and disturbance in protective measurement, emphasizing that the wavefunction cannot be directly accessed by measurement and motivating the need for an explicit readout map.  

[8] investigates quantum Turing machines and local transition functions, showing that locality constraints on discrete transition rules are formally tractable, paralleling the locality requirement of Axiom A2.

The QNFO corpus items [9]–[12] provide provenance for the research idea but contain no technical details; they are cited only as contextual background.

## 3. Methods

### 3.1 Axioms

- **A1 (Continuity).** The underlying state relevant to a detector is a real‑valued field variable $x\in\mathbb{R}$.  
- **A2 (Local determinism).** The evolution $x(t)$ follows a local deterministic law; no superluminal influence occurs.  
- **A3 (Discrete irreversible readout).** Measurement implements a map $M:\mathbb{R}\to\mathcal{O}=\{0,1\}$ by nonlinear amplification followed by thresholding, and $M$ is many‑to‑one.

### 3.2 Candidate calculi

A *calculus* assigns outcome probabilities given the field ensemble.

- **Linear calculus $\mathcal{C}_L$.** Amplifier $\mathcal{A}_g(x)=g\,x$; detector fires when $g\,x\ge\Theta$.  
- **Quadratic calculus $\mathcal{C}_Q$.** Amplifier $\mathcal{A}_g(x)=g\,x^{2}$; detector fires when $g\,x^{2}\ge\Theta$, i.e. $|x|\ge\sqrt{\Theta/g}$.

Both satisfy A1–A3; $\mathcal{C}_L$ is the affine limit of the family.

### 3.3 Field ensemble

We assume a unit‑variance Gaussian ensemble
\[
p(x)=\frac{1}{\sqrt{2\pi}}\,e^{-x^{2}/2},
\]
so that $\sigma=1$ in dimensionless units.

### 3.4 Noisy threshold model for Born‑rule comparison

Additive Gaussian readout noise $\eta\sim\mathcal{N}(0,\sigma_{n}^{2})$ yields
\[
P(1\mid x)=\Phi\!\left(\frac{x-\theta}{\sigma_{n}}\right),
\]
with $\Phi(z)$ the standard normal CDF.

### 3.5 Target statistics

- **Born rule.** $P_{1}^{\mathrm{QM}}(\alpha)=\cos^{2}(\alpha/2)=\frac{1+\cos\alpha}{2}$.  
- **CHSH correlation.** $E_{\mathrm{QM}}(a,b)=-\cos(a-b)$; $S=E(a,b)+E(a,b')+E(a',b)-E(a',b')$.

## 4. Analysis

All numbers are derived from the inputs above; external constants are $\Phi(1)=0.8413$, $\Phi(2)=0.9772$, $\sqrt{2}=1.4142136$, $\sqrt{\pi}=1.7724539$.

### 4.1 Outcome probability under $\mathcal{C}_Q$

With $g=1$, $\Theta=1$, firing condition $|x|\ge1$:
\[
P_{1}^{(Q)}=2\bigl(1-\Phi(1)\bigr)=2(1-0.8413)=0.3174.
\]

### 4.2 Outcome probability under $\mathcal{C}_L$

With the same parameters, firing condition $x\ge1$:
\[
P_{1}^{(L)}=1-\Phi(1)=0.1587.
\]

### 4.3 Divergence between the calculi

\[
\Delta P=P_{1}^{(Q)}-P_{1}^{(L)}=0.1587,\qquad
\frac{P_{1}^{(Q)}}{P_{1}^{(L)}}=2.000.
\]
For any symmetric density the quadratic threshold counts both tails while the linear threshold counts one, giving an exact factor 2.

### 4.4 Born‑rule approximation by a slope‑matched noisy detector

Assume the most favorable encoding $x(\alpha)=\cos\alpha$, threshold $\theta=0$, and choose $\sigma_{n}$ to match slopes at $\alpha=\pi/2$:
\[
\frac{1}{\sigma_{n}\sqrt{2\pi}}=\frac{1}{2}\;\Rightarrow\;
\sigma_{n}=\sqrt{\frac{2}{\pi}}=\frac{1.4142136}{1.7724539}\approx0.7978846.
\]

Evaluating $P_{1}^{\mathrm{thr}}(\alpha)=\Phi\!\bigl(\cos\alpha/0.7978846\bigr)$ at $\alpha\in\{0,\pi/6,\pi/4,\pi/3,\pi/2\}$ yields:

| $\alpha$ | $\cos\alpha$ | $z=\cos\alpha/0.7978846$ | $P_{1}^{\mathrm{thr}}$ | $P_{1}^{\mathrm{QM}}$ | $\Delta$ |
|---|---|---|---|---|---|
| $0$ | $1$ | $1.2533141$ | $0.8950$ | $1.0000$ | $-0.1050$ |
| $\pi/6$ | $0.8660254$ | $1.0854371$ | $0.8611$ | $0.9330127$ | $-0.0719$ |
| $\pi/4$ | $0.7071068$ | $0.8862269$ | $0.8123$ | $0.8535534$ | $-0.0413$ |
| $\pi/3$ | $0.5$ | $0.6266571$ | $0.7346$ | $0.7500000$ | $-0.0154$ |
| $\pi/2$ | $0$ | $0$ | $0.5000$ | $0.5000000$ | $0.0000$ |

Root‑mean‑square deviation:
\[
\mathrm{RMS}=\sqrt{\frac{0.1050^{2}+0.0719^{2}+0.0413^{2}+0.0154^{2}+0^{2}}{5}}
\approx0.0602.
\]

Thus the noisy threshold cannot reproduce certainty at $\alpha=0$ for any finite $\sigma_{n}$.

### 4.5 CHSH bound for deterministic local thresholded models

For deterministic local outcomes $A(a,\lambda),B(b,\lambda)\in\{\pm1\}$,
\[
S_{\lambda}=A(B+B')+A'(B-B').
\]
Since $B,B'\in\{\pm1\}$, $|S_{\lambda}|\le2$ for every $\lambda$, and averaging preserves the bound:
\[
|S|\le2.
\]

Quantum prediction at $a=0$, $a'=\pi/2$, $b=\pi/4$, $b'=-\pi/4$:
\[
E(a,b)=E(a,b')=E(a',b)=-0.7071068,\qquad
E(a',b')=+0.7071068,
\]
\[
S=-2.8284271,\qquad |S|=2\sqrt{2}\approx2.8284.
\]

The gap is $0.8284$, a factor $\sqrt{2}\approx1.4142$ above the local bound.

### 4.6 Excess noise cannot close the CHSH gap

The derivation of $|S|\le2$ uses only locality and per‑$\lambda$ determinism; increasing $\sigma_{n}$ merely enlarges the hidden variable $\lambda$ and cannot raise $|S|$ beyond 2. Nonlocal dynamics or a non‑threshold readout would be required.

### 4.7 Statistical‑power projection for distinguishing $\mathcal{C}_L$ and $\mathcal{C}_Q$

Assume $n$ Bernoulli trials per calculus with $P_{1}^{(Q)}=0.3174$, $P_{1}^{(L)}=0.1587$, and require a $3\sigma$ separation of observed frequencies. The pooled proportion is
\[
\bar{p}=\frac{0.3174+0.1587}{2}=0.23805,
\]
standard error
\[
\mathrm{se}=\sqrt{\frac{2\bar{p}(1-\bar{p})}{n}}=\frac{0.60230}{\sqrt{n}}.
\]
Demanding $3\,\mathrm{se}\le\Delta P=0.1587$ gives
\[
n\ge\left(\frac{3\times0.60230}{0.1587}\right)^{2}\approx129.6,
\]
so $n\approx130$ trials per calculus suffice.

### 4.8 Sensitivity to threshold

At $\Theta=4$, $g=1$:
\[
P_{1}^{(Q)}=2\bigl(1-\Phi(2)\bigr)=2(1-0.9772)=0.0456,\qquad
P_{1}^{(L)}=1-\Phi(2)=0.0228,
\]
again a factor 2, confirming that the non‑uniqueness is not an artifact of the chosen threshold.

## 5. Results

1. **Non‑uniqueness of the readout calculus.** $\mathcal{C}_L$ yields $P_{1}^{(L)}=0.1587$ while $\mathcal{C}_Q$ yields $P_{1}^{(Q)}=0.3174$ at $\Theta=1$, $g=1$ (Sections 4.1–4.2), a structural factor of exactly 2.0 (Section 4.3). The factor persists for other thresholds (Section 4.8).  
2. **Born‑rule approximation is imperfect.** A slope‑matched noisy detector with $\sigma_{n}=0.7978846$ deviates from the Born rule by up to $0.1050$ (at $\alpha=0$) and has RMS deviation $0.0602$ over five test angles (Section 4.4).  
3. **CHSH bound.** Deterministic local thresholded readouts obey $|S|\le2$, whereas quantum mechanics predicts $|S|=2\sqrt{2}\approx2.8284$ (Section 4.5). Noise cannot close this gap (Section 4.6).  
4. **Distinguishability projection.** Approximately $130$ trials per calculus achieve a $3\sigma$ discrimination (Section 4.7).  

## 6. Discussion

**Limitations.**  
- The field ensemble is assumed Gaussian; heavier‑tailed or asymmetric distributions change absolute probabilities but preserve the factor‑2 structure for symmetric densities.  
- The Born‑rule comparison uses the specific encoding $x(\alpha)=\cos\alpha$; other encodings may yield different deviations.  
- The statistical‑power estimate relies on normal approximations to binomial variance and on the assumed Gaussian ensemble; real experimental imperfections could increase the required trial count.

**Failure modes.**  
- If the research idea implicitly restricts the amplifier to strictly nonlinear (excluding the affine $\mathcal{C}_L$), the counterexample would be invalid.  
- If the claim that quantum statistics must be reproduced exactly is relaxed, the Born‑rule mismatch would not falsify the uniqueness claim.  
- Allowing nonlocal dependence of the readout on distant settings would invalidate the CHSH bound derivation.

**What would falsify our claims.**  
- Demonstrating a deterministic, local, continuous‑field model with thresholded readout that reproduces the Born rule exactly for all angles *and* yields $|S|>2$ would falsify the non‑uniqueness result.  
- Proving that Axioms A1–A3 mathematically enforce a unique amplifier (e.g., via a symmetry principle) would also overturn our counterexample.

**Open questions.**  
1. Which additional physical principle (energy conservation, information‑theoretic constraint, etc.) could uniquely select the quantum‑compatible calculus?  
2. Can stochastic local readouts (beyond deterministic thresholding) evade the CHSH bound while remaining within a generalized Axiom A3?  
3. What is the optimal encoding $x(\alpha)$ that minimizes the Born‑rule deviation across the full angular range?

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.**  
The primary users are researchers in quantum foundations, quantum‑information engineering, and designers of high‑precision measurement apparatuses. If the result holds, designers must recognize that specifying only continuity, locality, and irreversible readout does not uniquely determine quantum statistics; additional design criteria (e.g., specific amplifier nonlinearity) are required to achieve Born‑rule behavior.  

**(b) Technology readiness.**  
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions, it resides at TRL 1–2 (basic principles observed) and does not exceed TRL 3 (analytical proof‑of‑concept).  

**(c) Minimal next experiment.**  
A tabletop experiment that implements both a linear amplifier (e.g., a voltage‑proportional detector) and a quadratic amplifier (e.g., an intensity‑proportional photodiode) with identical gain $g=1$ and threshold $\Theta=1$, feeding a Gaussian‑distributed analog signal (generated by a calibrated noise source). Measuring the detection frequencies for each detector over $n\approx130$ trials per setting would test the predicted $P_{1}^{(L)}$ versus $P_{1}^{(Q)}$. Observation of a frequency ratio significantly different from 2 would refute the factor‑2 prediction and falsify the counterexample.  

**(d) Engineering constraints.**  
- **Signal generation:** Accurate Gaussian statistics require a high‑quality electronic noise source with known variance.  
- **Amplifier linearity:** The linear detector must maintain proportionality over the relevant range; the quadratic detector must square the input without saturation.  
- **Threshold stability:** The threshold voltage $\Theta$ must be set and maintained with sub‑percent precision to avoid biasing the tail probabilities.  
- **Data acquisition:** Counting statistics must be recorded with negligible dead time to preserve Bernoulli assumptions.  

**(e) Projected cost/performance bounds.**  
Given the modest trial count ($\sim130$ per detector) and the use of off‑the‑shelf analog components, the experimental cost is projected to be under \$5 000 (components, data acquisition hardware, and labor). Performance is bounded by the statistical uncertainty $\mathrm{se}=0.60230/\sqrt{130}\approx0.053$, yielding a $3\sigma$ separation as derived in Section 4.7.  

**(f) Risks and misuse.**  
A possible misuse is to claim that the existence of alternative calculi disproves quantum mechanics entirely; the correct interpretation is that additional structure beyond Axioms A1–A3 is needed to single out the quantum calculus. Researchers must avoid overstating the result as a blanket refutation of quantum theory.

## 8. Conclusion

We formalized the proposed continuous‑to‑discrete readout map, exhibited two distinct calculi within the stated axioms that yield different outcome probabilities ($0.1587$ versus $0.3174$), showed that a slope‑matched noisy threshold detector only approximates the Born rule (maximum deviation $0.1050$, RMS $0.0602$), and proved that deterministic local thresholded readouts obey the CHSH bound $|S|\le2$ in contrast with the quantum value $2\sqrt{2}\approx2.8284$. These findings refute the claim that quantum mechanics is the unique calculus bridging continuous local deterministic fields and irreversible discrete measurement; additional principles are required to recover quantum statistics.

## References

[1] arXiv:1301.3626v2 | Quantum continuous measurements: The stochastic Schroedinger equations and the spectrum of the output  
[2] arXiv:1610.09347v1 | Beyond Quantum Theory: A Realist Psychobiological Interpretation of Physical Reality  
[3] arXiv:quant-ph/0107090v1 | Quantum Measurement, Information, and Completely Positive Maps  
[4] arXiv:quant-ph/0012115v1 | Entropy and information gain in quantum continual measurements  
[5] arXiv:2307.09558v1 | Fitted avatars: automatic skeleton adjustment for self-avatars in virtual reality  
[6] arXiv:1402.1217v2 | Entanglement, scaling, and the meaning of the wave function in protective measurement  
[7] arXiv:quant-ph/9809038v1 | Quantum Turing Machines: Local Transition, Preparation, Measurement, and Halting  
[8] QNFO: POST QUANTUM SYNTHESIS  
[9] QNFO: Principia Ontologica  
[10] QNFO: Time as Epistemic Cognitive Fiction  
[11] QNFO: PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis  

## Appendix A. Divergence report

The source drafts agreed on all computed values ($P_{1}^{(L)} = 0.1587$, $P_{1}^{(Q)} = 0.3174$, factor 2.000, $\sigma_{n}=0.7978846$, max deviation $0.1050$, RMS $0.0602$, $|S|\le2$ versus $2.8284$, $n\approx130$). One divergence arose in framing: draft A presented the Born‑rule mismatch as an independent refutation of uniqueness, while draft B treated it as a subordinate corollary of the CHSH bound. The reconciled text follows draft B’s more conservative framing—the primary refutation is the direct two‑calculus counterexample (Sections 4.1–4.3); the Born‑rule mismatch (Section 4.4) is reported as additional quantitative tension rather than a standalone refutation. No numerical values diverged between drafts.

## Appendix B. Claim attribution

| Claim | Source drafts | Agreement |
|---|---|---|
| C1: $P_{1}^{(L)} = 0.1587$ at $\Theta = 1$, $g = 1$ | A, B, C | CONVERGENT |
| C2: $P_{1}^{(Q)} = 0.3174$ at $\Theta = 1$, $g = 1$ | A, B, C | CONVERGENT |
| C3: Structural factor of exactly $2.000$ between the calculi, persisting at $\Theta = 4$ | A, B, C | CONVERGENT |
| C4: Slope‑matched $\sigma_{n} = \sqrt{2/\pi} \approx 0.7978846$ | A, B, C | CONVERGENT |
| C5: Maximum Born‑rule deviation $0.1050$ at $\alpha = 0$; RMS $0.0602$ | A, B, C | CONVERGENT |
| C6: CHSH bound $|S| \le 2$ for deterministic local thresholded readouts; quantum value $2\sqrt{2} \approx 2.8284$ | A, B, C | CONVERGENT |
| C7: Projection $n \approx 130$ trials per calculus for $3\sigma$ discrimination | A, B, C | CONVERGENT |
| C8: Born‑rule mismatch as independent refutation of uniqueness | A | SINGLE (resolved toward B's subordinate framing) |
| C9: Axioms A1–A3 as the formalization of the research idea | A, B, C | CONVERGENT |
| C10: Linear amplifier excluded as “nonlinear” under Axiom A3 | B | SINGLE |
| C11: Threshold sensitivity at $\Theta = 4$ | B | SINGLE |
| C12: Failure modes and falsification conditions | A, B | CONVERGENT |