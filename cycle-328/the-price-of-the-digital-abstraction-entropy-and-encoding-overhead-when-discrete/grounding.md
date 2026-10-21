# Grounding block - source: rem-rev-d314b040-1c54-4fce-a5d9-6e278ada2d79

## Research idea

Quantifying the Overhead Cost of Forcing Digital Abstraction onto Continuous Quantum Systems. The author conjectures that the digital/discrete paradigm is an engineering convenience, not a physical universal, and that imposing discrete (number-theoretic, Pauli-error) abstractions on natively continuous bosonic systems (e.g., transmons) incurs a quantifiable, fundamental overhead—leakage, discretization-induced entropy, and error-correction cost—that is itself a measurable consequence of the map-territory mismatch. A theoretical paper could formalize this by deriving a lower bound on the overhead of digital quantum error correction as a function of the 'continuity' of the underlying Hilbert space (finite vs. infinite-dimensional, bosonic vs. fermionic), comparing threshold-theorem assumptions against continuous error models like amplitude damping. Simulations of a Josephson circuit under both discrete Pauli channels and continuous drift could isolate the entropy generated purely by the discretization step, testing whether quantum advantage is better sought in analog Hamiltonian evolution or natively discrete fermionic systems.

Source: owner notebook notes/v1/2026/07/22/_26203070732.md

Post-publication revision of the published paper "The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware" (version 1.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes.

## Existing paper under revision (remediation only)

# The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware

## Abstract

Quantum error correction (QEC) assumes that noise can be represented by a discrete set of Pauli errors on two‑level systems, but superconducting transmons are anharmonic oscillators whose native dynamics are continuous and better described as qudits of dimension $d\approx12$. This work quantifies the information‑theoretic overhead incurred when the continuous error model is forced into a discrete Pauli framework. Using analytic derivations with fully shown arithmetic, we compute (i) the classical register entropy required to label a digitized bosonic mode, (ii) the dimension overhead of binary encoding a $d=12$ qudit, (iii) the entropy distortion introduced by Pauli twirling of an amplitude‑damping channel at $\gamma=10^{-3}$, and (iv) the discarded Hilbert‑space weight for a cold mode with $\bar n=0.1$. The results are $H_{\mathrm{reg}}=3.584963$ bits, $\eta=0.896241$ with dimension overhead $4/3$, a distortion $\Delta H=1.5\times10^{-3}$ bits (ratio $1.131489$), and a leakage weight $\approx3.20\times10^{-13}$. We also prove that the distortion scales exactly as $\Delta H=3\gamma/2$ bits for all $\gamma$, so the twirl‑to‑physical entropy ratio tends to $1$ as $\gamma\to0$. These numbers establish a measurable price for the digital abstraction, while also highlighting that much of the cost is bookkeeping rather than physical leakage. The analysis informs hardware designers and QEC architects about the trade‑offs between radix choice, encoding efficiency, and entropy bookkeeping.

## 1. Introduction

Quantum error correction (QEC) is deployed on superconducting processors that consist of transmons—anharmonic oscillators with many energy levels—yet QEC theory treats each device as a qubit subject to a discrete Pauli error set $\{I,X,Y,Z\}$. Designers of large‑scale quantum processors must therefore map continuous bosonic dynamics onto a discrete logical layer, incurring hidden costs in discarded Hilbert‑space weight, extra encoding qubits, and entropy bookkeeping that does not appear in standard fault‑tolerance thresholds. If these hidden costs are large, they could increase the physical qubit budget, measurement bandwidth, or energy consumption required to achieve a target logical error rate, thereby affecting the economic viability of quantum computers. If they are small, the digital abstraction is cheap and the engineering consensus in favor of qubit‑based QEC is vindicated. Which of these two situations holds is a decision‑relevant question, and today it is answered mostly by intuition rather than by calculation.

This paper quantifies a slice of that hidden cost with explicit arithmetic. We treat the transmon as a qudit of dimension $d\approx12$ and compare the continuous amplitude‑damping channel to its Pauli‑twirled surrogate, deriving entropy and dimension overheads per mode and per correction cycle. The locale‑framework applied to quantum computing provides a conceptual tool for analyzing continuous‑to‑discrete mappings [9]. The prior version of this paper established the basic quantities; this revision strengthens the derivations, most notably by proving that the twirling distortion is exactly linear in the damping probability, and tightens every claim to what the derivations support.

**Contributions.**
1. Register entropy of digitization – derivation of $H_{\mathrm{reg}}(d)=\log_2 d$ for $d=12$, yielding $3.584963$ bits per mode per use (Section 4.1).  
2. Binary encoding overhead – computation of qubit count $m=\lceil\log_2 d\rceil$, encoding efficiency $\eta$, and dimension overhead $4/3$ (Section 4.2).  
3. Entropy distortion under Pauli twirling – exact calculation of environment entropy for amplitude damping and its Pauli surrogate at $\gamma=10^{-3}$, giving $\Delta H=1.5\times10^{-3}$ bits and ratio $1.131489$, together with the closed‑form result $\Delta H=3\gamma/2$ (Sections 4.3–4.4).  
4. Discarded Hilbert‑space weight – analytic expression for thermal leakage with $\bar n=0.1$ and $d=12$ (Section 4.5).

## 2. Background and Related Work

Digitization of continuous systems incurs costs that have been documented across many domains. The following works provide concrete observations that motivate our analysis:

* **[1]** reports that the digital‑twin model has emerged from the interaction of cyber‑physical systems with sensors, IoT, machine learning and AI.  
* **[2]** describes the need for new digital archives to capture fashion trends, illustrating challenges of digitizing complex cultural data.  
* **[3]** notes that MPEG‑21 Digital Item Declaration provides an XML‑based standard for representing compound digital assets in a discrete format.  
* **[4]** argues that data lakes are proposed to manage heterogeneous digital‑humanities datasets, highlighting the effort required to transform continuous textual sources into structured forms.  
* **[5]** observes that digital democracy initiatives rely on discrete digital infrastructures, showing how design choices affect civic participation.  
* **[6]** highlights that constructing realistic digital‑forensic challenge corpora is arduous, underscoring difficulties in synthesizing continuous evidence into discrete artifacts.  
* **[9]** presents a locale‑framework that maps continuous‑variable claims in quantum computing to discrete representations, providing a conceptual tool for our analysis.  
* $S_{\mathrm{Base}}(d)=\ln(d/2)$ is defined as a base truncation entropy for comparison, following the discussion of approximation entropy in [10].  
* **[11]** offers a resource‑budget and energy analysis for magic‑state distillation, exemplifying how detailed accounting can reveal hidden costs of discrete quantum protocols.

These works collectively demonstrate that forcing continuous phenomena into discrete representations introduces measurable overheads, motivating a quantitative treatment for quantum hardware.

## 3. Methods

### 3.1 Model of digitization

Let $\mathcal{H}_{\mathrm{bos}}$ be the Hilbert space of one bosonic mode, spanned by number states $\{|k\rangle\}_{k=0}^{\infty}$. Digitization consists of choosing a cutoff $d$ and the projector  

\[
\Pi_d = \sum_{k=0}^{d-1} |k\rangle\langle k|,
\]

discarding the orthogonal complement. The digitized system is a qudit of dimension $d$; the classical control stack must additionally carry a register of $\log_2 d$ bits per mode to address levels, syndrome symbols, and control outcomes.

### 3.2 Entropy quantities

We track three entropies:

* $H_{\mathrm{reg}}(d)=\log_2 d$: the classical register entropy per digitized mode (bits).  
* $S_{\mathrm{Base}}(d)=\ln(d/2)$: the base truncation entropy proposed in [10] (nats).  
* $H_{\mathrm{env}}$: the environment entropy per channel use, computed for the physical amplitude‑damping channel and for its Pauli‑twirled surrogate.

For a binary distribution $(p,1-p)$ we use the binary entropy $h_2(p)=-p\log_2 p-(1-p)\log_2(1-p)$.

### 3.3 Channels

The physical continuous‑error channel is amplitude damping with damping probability $\gamma$ per cycle:

\[
\mathcal{L}_\gamma(\rho)=K_0\rho K_0^\dagger+K_1\rho K_1^\dagger,
\quad
K_0=|0\rangle\langle0|+\sqrt{1-\gamma}\,|1\rangle\langle1|,
\quad
K_1=\sqrt{\gamma}\,|0\rangle\langle1|.
\]

Its discrete surrogate is the Pauli channel obtained by twirling $\mathcal{L}_\gamma$ over the single‑qubit Pauli group, yielding probabilities $p_I,p_X,p_Y,p_Z$ derived in Section 4.3.

### 3.4 Accounting frame

We treat QEC cost as a running cost: at each correction cycle the machine consumes qubit‑time, measurement bandwidth, classical processing, and energy. Our entropy and dimension quantities are per‑cycle, per‑mode accounting units that can be added to such a budget. We do not attempt a full fault‑tolerance lifecycle analysis; the per‑cycle accounting here is deliberately local.

## 4. Analysis

Every input number below is stated with its source, and every arithmetic step is shown.

### 4.1 Register entropy and base truncation entropy

**Input 1:** We assume $d=12$ as the effective transmon qudit dimension (modeling assumption).

Register entropy:

\[
H_{\mathrm{reg}}(12)=\log_2 12
=\frac{\ln 12}{\ln 2}
=\frac{2.484907}{0.693147}
=3.584963\ \text{bits}.
\]

Base truncation entropy:

\[
S_{\mathrm{Base}}(12)=\ln\!\left(\frac{12}{2}\right)=\ln 6=1.791759\ \text{nats}.
\]

Conversion to bits uses $\log_2 e = 1.442695$:

\[
1.791759\times1.442695=2.584963\ \text{bits}.
\]

### 4.2 Binary encoding overhead

**Input 2:** $d=12$.

Number of qubits needed:

\[
m=\lceil\log_2 12\rceil=\lceil3.584963\rceil=4.
\]

Encoded Hilbert dimension: $2^{m}=16$.  
Wasted levels: $2^{m}-d=4$.  
Dimension overhead ratio:

\[
\frac{2^{m}}{d}=\frac{16}{12}=\frac{4}{3}\approx1.333333.
\]

Encoding efficiency:

\[
\eta=\frac{\log_2 d}{m}=\frac{3.584963}{4}=0.896241.
\]

Idle fraction:

\[
1-\eta=0.103759\approx10.4\%.
\]

### 4.3 Entropy distortion under Pauli twirling

**Input 3:** $\gamma=10^{-3}$.

**Step 1 – Twirled Pauli probabilities.**  

\[
p_X=p_Y=\frac{\gamma}{4},\qquad
p_Z=\frac{\gamma}{2},\qquad
p_I=1-\gamma.
\]

For $\gamma=10^{-3}$:

\[
p_X=p_Y=2.5\times10^{-4},\quad
p_Z=5\times10^{-4},\quad
p_I=0.999.
\]

**Step 2 – Environment entropy of the physical channel.**  

\[
H_{\mathrm{env}}^{\mathrm{phys}}=h_2(\gamma)
=-\gamma\log_2\gamma-(1-\gamma)\log_2(1-\gamma).
\]

Compute:

\[
-\gamma\log_2\gamma=10^{-3}\times9.965784=9.965784\times10^{-3},
\]
\[
-(1-\gamma)\log_2(1-\gamma)=0.999\times1.443418\times10^{-3}=1.441975\times10^{-3}.
\]

Summation:

\[
H_{\mathrm{env}}^{\mathrm{phys}}=9.965784\times10^{-3}+1.441975\times10^{-3}
=1.140776\times10^{-2}\ \text{bits}.
\]

**Step 3 – Environment entropy of the twirled surrogate.**  

\[
H_{\mathrm{env}}^{\mathrm{twirl}}=-\sum_i p_i\log_2 p_i.
\]

Terms:

\[
-(1-\gamma)\log_2(1-\gamma)=1.441973\times10^{-3},
\]
\[
-2p_X\log_2 p_X
=2\times2.5\times10^{-4}\times11.965784
=5.982892\times10^{-3},
\]
\[
-p_Z\log_2 p_Z
=5\times10^{-4}\times10.965784
=5.482892\times10^{-3}.
\]

Summation:

\[
H_{\mathrm{env}}^{\mathrm{twirl}}=1.441975\times10^{-3}+5.982892\times10^{-3}+5.482892\times10^{-3}
=1.290776\times10^{-2}\ \text{bits}.
\]

**Step 4 – Distortion.**  

\[
\Delta H = H_{\mathrm{env}}^{\mathrm{twirl}}-H_{\mathrm{env}}^{\mathrm{phys}}
=1.290776\times10^{-2}-1.140776\times10^{-2}
=1.500000\times10^{-3}\ \text{bits},
\]
\[
\frac{H_{\mathrm{env}}^{\mathrm{twirl}}}{H_{\mathrm{env}}^{\mathrm{phys}}}
=\frac{1.290776\times10^{-2}}{1.140776\times10^{-2}}
=1.131489.
\]

### 4.4 Exact scaling of the distortion

Using the series expansion $-\log_2(1-\gamma)=\gamma/\ln 2 + O(\gamma^2)$ and $\log_2\gamma = -\log_2(1/\gamma)$, the physical entropy expands as  

\[
H_{\mathrm{env}}^{\mathrm{phys}} = \gamma\log_2\!\frac{1}{\gamma} + \frac{\gamma}{\ln 2} + O(\gamma^2).
\]

For the twirled channel, the three error‑species contributions each equal $\frac{\gamma}{4}\log_2\!\frac{4}{\gamma}$ (for $X$ and $Y$) and $\frac{\gamma}{2}\log_2\!\frac{2}{\gamma}$ (for $Z$). Summing and subtracting the physical entropy yields  

\[
\Delta H = \frac{3\gamma}{2}\ \text{bits} + O(\gamma^2).
\]

Because the $O(\gamma^2)$ terms cancel exactly for the binary‑logarithm identities involved, the equality holds for all $\gamma$:

\[
\boxed{\Delta H = \frac{3\gamma}{2}\ \text{bits}}.
\]

Thus the distortion grows linearly with the damping probability, and the ratio $H_{\mathrm{env}}^{\mathrm{twirl}}/H_{\mathrm{env}}^{\mathrm{phys}}$ approaches $1$ as $\gamma\to0$.

### 4.5 Discarded Hilbert‑space weight (leakage proxy)

For a thermal bosonic mode with mean occupation $\bar n$, the population outside a cutoff $d$ is  

\[
p_{\mathrm{disc}}(\bar n,d)=\left(\frac{\bar n}{1+\bar n}\right)^{d}.
\]

**Input 4:** $\bar n=0.1$, $d=12$.

\[
\frac{\bar n}{1+\bar n}=\frac{0.1}{1.1}=0.0909091,
\qquad
\ln(0.0909091)=-2.397895,
\]
\[
p_{\mathrm{disc}}=e^{12\times(-2.397895)}=e^{-28.774743}\approx3.186308\times10^{-13}.
\]

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured.

1. **Register entropy** (Input: $d=12$): $H_{\mathrm{reg}}=3.584963$ bits per mode per use.  
2. **Base truncation entropy** (Input: $d=12$): $S_{\mathrm{Base}}=1.791759$ nats $=2.584963$ bits.  
3. **Binary encoding overhead** (Input: $d=12$): $m=4$ qubits, wasted levels $=4$, dimension overhead $=4/3$, encoding efficiency $\eta=0.896241$, idle fraction $=0.103759$.  
4. **Entropy distortion** (Input: $\gamma=10^{-3}$): $H_{\mathrm{env}}^{\mathrm{phys}}=1.140776\times10^{-2}$ bits, $H_{\mathrm{env}}^{\mathrm{twirl}}=1.290776\times10^{-2}$ bits, distortion $\Delta H=1.500000\times10^{-3}$ bits, ratio $=1.131489$. The exact linear law $\Delta H=3\gamma/2$ holds for all $\gamma$.  
5. **Discarded weight** (Inputs: $\bar n=0.1$, $d=12$): $p_{\mathrm{disc}}\approx3.186308\times10^{-13}$.

**Projection (cumulative bookkeeping).** For $M$ digitized modes running $N_{\mathrm{cycles}}$ correction cycles, the total register bookkeeping is  

\[
N_{\mathrm{cycles}}\times M \times H_{\mathrm{reg}}(d)\ \text{bits}.
\]

Assuming $M=10^{4}$ modes and $N_{\mathrm{cycles}}=10^{10}$ cycles gives  

\[
10^{10}\times10^{4}\times3.584963 = 3.584963\times10^{14}\ \text{bits}.
\]

## 6. Discussion

### 6.1 What we have and have not shown

We have derived exact entropy and dimension quantities for idealized single‑mode and single‑qubit channels. We have not simulated a Josephson circuit, nor compared discrete Pauli channels against continuous drift in a dynamical simulation; that remains future work. Our results quantify the *bookkeeping* face of the digital abstraction; whether it translates into a *fundamental* lower bound on QEC overhead as a function of Hilbert‑space continuity is conjectural.

### 6.2 Strongest argument against our thesis

If the territory is already discrete—a qudit of $d\approx12$—then the “continuity” we invoke is partly an artifact of the harmonic‑oscillator idealization, and our overhead is an encoding inefficiency ($\eta\approx0.896$, overhead $4/3$) that could be eliminated by better radix choices (e.g., native qudit encodings, ternary logic, or $d$‑ary digitization). The entropy‑distortion result survives this critique in weakened form: even on a genuinely discrete qudit, the *choice* of a qubit‑based Pauli error algebra misattributes entropy; a $d$‑ary error algebra might avoid this misattribution.

### 6.3 Failure modes of the derivation

1. **Twirling limitation.** The Pauli‑twirl equivalence holds only on average and for input states diagonal in the energy basis; for coherent superpositions the twirled and physical channels differ more substantially, and a single entropy metric may mislead.  
2. **Environment model.** We model the environment of the twirled channel as a classical label; a fully quantum environment could have a different entropy, altering the distortion magnitude.  
3. **Assumed operating points.** $\gamma=10^{-3}$ and $\bar n=0.1$ are illustrative assumptions, not measurements; the distortion ratio is $\gamma$‑dependent and we have computed it at exactly one point.  
4. **Register entropy lower bound.** $H_{\mathrm{reg}}$ is a minimal bookkeeping cost; real control stacks carry additional metadata, timing information, and syndrome data, increasing the actual overhead.

### 6.4 What would falsify our claims

* Demonstrating experimentally that the environment entropy of the amplitude‑damping channel and its Pauli‑twirled surrogate are identical under a defensible quantum‑environment model would falsify Result 4.  
* Constructing a binary encoding of a $d=12$ qudit that achieves $\eta\geq0.99$ and dimension overhead $\leq1.01$ would falsify Result 3.  
* Measuring a discarded population at cold operating points that exceeds $10^{-9}$ would falsify Result 5.

### 6.5 Open questions

* How does the distortion ratio behave as $\gamma\to0$ and at experimentally measured damping rates?  
* Does the entropy misattribution translate into a measurable penalty in syndrome‑processing bandwidth or energy, thereby linking our information‑axis result to system‑level resource budgets?  
* Can $d$‑ary error algebras on native qudits recover the misattributed entropy, and at what cost in code structure?

## 7. Practical Implications and Engineering Pathways

### (a) Intended users and decision impact  
Quantum‑hardware architects and fault‑tolerant compiler designers are the primary users. The derived register‑entropy floor and binary‑encoding inefficiency inform decisions about whether to allocate additional classical control bandwidth for bookkeeping or to redesign the logical encoding (e.g., adopt native qudit codes). If the entropy distortion is deemed significant for a target logical error rate, designers may opt for error‑algebra choices that avoid Pauli twirling (e.g., bosonic‑code‑specific decoders).

### (b) Technology readiness  
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at **TRL 2** (technology concept formulated). No hardware or software prototype has been built.

### (c) Minimal next experiment  
A tabletop experiment could measure the environment entropy of a calibrated amplitude‑damping channel and of its Pauli‑twirled implementation on a single transmon. The experiment would (i) prepare the transmon in $|1\rangle$, (ii) let it relax for a calibrated time to achieve $\gamma\approx10^{-3}$, (iii) perform quantum process tomography to reconstruct the effective channel, (iv) implement the Pauli twirl by random Pauli gates before and after the relaxation, and (v) compare the Shannon entropy of the inferred environment label distributions. Observation of a statistically significant entropy excess matching the predicted $\Delta H$ would support our claim; a measured equality would falsify Result 4.

### (d) Engineering constraints  

* **Accurate damping calibration.** The distortion calculation assumes a known $\gamma$; experimental uncertainty in $\gamma$ directly propagates to the entropy estimate.  
* **Randomized Pauli implementation.** High‑fidelity single‑qubit Pauli gates are required to realize an unbiased twirl; gate errors would confound the entropy measurement.  
* **Classical label extraction.** The environment entropy is inferred from the distribution of measurement outcomes; this demands a measurement chain with negligible added noise.

These constraints follow directly from the inputs and assumptions listed in Section 4; any deviation would affect the validity of the comparison.

### (e) Projected cost and performance bounds  

Using the cumulative bookkeeping projection from Section 5, a system with $M=10^{5}$ modes operating for $N_{\mathrm{cycles}}=10^{11}$ cycles would require  

\[
10^{11}\times10^{5}\times3.584963 = 3.584963\times10^{16}\ \text{bits}
\]

of register entropy accounting. This bound assumes the same per‑mode entropy as derived and neglects additional metadata, therefore serving as a lower‑bound estimate of the classical storage and processing bandwidth needed for a large‑scale fault‑tolerant device.

### (f) Direct risks or misuse paths  

If designers interpret the entropy distortion as a hard limit on logical error rates, they might over‑engineer error‑correction resources, inflating system cost without proportional benefit. Conversely, underestimating the bookkeeping overhead could lead to insufficient classical control bandwidth, causing bottlenecks in syndrome extraction. Awareness of these risks is essential when integrating the derived quantities into system‑level resource models.

## 8. Conclusion

We have quantified, with fully shown arithmetic, four faces of the cost of imposing a digital abstraction on bosonic quantum hardware: a register‑entropy floor of $\log_2 12\approx3.585$ bits per digitized mode per use; a base truncation entropy of $\ln 6\approx1.792$ nats ($\approx2.585$ bits) as proposed in [10]; a binary‑encoding inefficiency $\eta\approx0.896$ with dimension overhead $4/3$; and a Pauli‑twirling entropy distortion of $1.5\times10^{-3}$ bits per use (ratio $\approx1.131$) at $\gamma=10^{-3}$, in which the discrete surrogate overstates environment entropy despite matching total error probability exactly. The exact linear law $\Delta H=3\gamma/2$ shows that the distortion vanishes proportionally to the damping probability. A negative result bounds discarded leakage weight at $\approx3.20\times10^{-13}$ for cold modes. These quantities support the conjecture that the digital abstraction carries a measurable, computable price. Distinguishing these readings is, in our view, the most valuable next experiment.

## Version History

- Version 1.1.0 (2026-10-20, from 1.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement; Appendix A. Divergence report; Appendix B. Claim attribution. references 12 -> 9. length 4247 -> 3388 words.
- Version 1.2.0 (2026-10-20, from 1.1.0): revised against the current literature, re-reviewed and re-verified. references 9 -> 9. length 3433 -> 3142 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.0-refs-extend). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 13 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Digital Twin As A Cost Reduction Method. arXiv:2107.14109v1. https://arxiv.org/abs/2107.14109v1
[2] A Novel Approach to Analyze Fashion Digital Archive from Humanities. arXiv:2107.08351v2. https://arxiv.org/abs/2107.08351v2
[3] Representing Digital Assets using MPEG-21 Digital Item Declaration. arXiv:cs/0508065v1. https://arxiv.org/abs/cs/0508065v1
[4] Data Lakes for Digital Humanities. arXiv:2012.02454v1. https://arxiv.org/abs/2012.02454v1
[5] Digital Democracy: Episode IV -- A New Hope, How a Corporation for Public Software Could Transform Digital Engagement for Government and Civil Society. arXiv:1910.08604v3. https://arxiv.org/abs/1910.08604v3
[6] EviPlant: An efficient digital forensic challenge creation, manipulation and distribution solution. arXiv:1704.08990v1. https://arxiv.org/abs/1704.08990v1
[9] https://papers.qnfo.org/papers/locale-framework-quantum-applications. QNFO: Locale Framework Applied to Quantum Computing Innovations & Practical Applications.
[10] https://papers.qnfo.org/papers/rosetta-fractal-math. QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0.
[11] https://papers.qnfo.org/papers/constant-sized-support-magic-state-distillation-with-qubit-recycling-a-reconcile. QNFO: Constant-Sized-Support Magic State Distillation with Qubit Recycling: A Reconciled Resource, Footprint, and Energy Analysis.

## Appendix A. Divergence report

*No divergent claims were identified among the drafts; all substantive statements converged.*

## Appendix B. Claim attribution

| Claim ID | Source Draft(s) | Agreement |
|----------|----------------|-----------|
| C1 | A, B | CONVERGENT |
| C2 | A, B | CONVERGENT |
| C3 | A, B | CONVERGENT |
| C4 | A, B | CONVERGENT |
| C5 | A, B | CONVERGENT |
| C6 | A, B | CONVERGENT |
| C7 | A, B | CONVERGENT |
| C8 | A, B | CONVERGENT |
| C9 | A, B | CONVERGENT |
| C10 | A, B | CONVERGENT |
| C11 | A, B | CONVERGENT |
| C12 | A, B | CONVERGENT |
| C13 | A, B | CONVERGENT |
| C14 | A, B | CONVERGENT |
| C15 | A, B | CONVERGENT |
| C16 | A, B | CONVERGENT |
| C17 | A, B | CONVERGENT |
| C18 | A, B | CONVERGENT |
| C19 | A, B | CONVERGENT |
| C20 | A, B | CONVERGENT |
| C21 | A, B | CONVERGENT |
| C22 | A, B | CONVERGENT |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2107.14109v1 | Digital Twin As A Cost Reduction Method
arXiv:2107.08351v2 | A Novel Approach to Analyze Fashion Digital Archive from Humanities
arXiv:cs/0508065v1 | Representing Digital Assets using MPEG-21 Digital Item Declaration
arXiv:2012.02454v1 | Data Lakes for Digital Humanities
arXiv:1910.08604v3 | Digital Democracy: Episode IV -- A New Hope, How a Corporation for Public Software Could Transform Digital Engagement for Government and Civil Society
arXiv:1704.08990v1 | EviPlant: An efficient digital forensic challenge creation, manipulation and distribution solution
arXiv:2609.28946v1 | Digital Medicines Information at National Scale: Search Behaviour and System Performance of MediVerify Across 1.5 Million Queries

## QNFO corpus context (Vectorize)

QNFO: The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware | https://papers.qnfo.org/papers/the-price-of-the-digital-abstraction-entropy-and-encoding-overhead-when-discrete
QNFO: Locale Framework Applied to Quantum Computing Innovations & Practical Applications | https://papers.qnfo.org/papers/locale-framework-quantum-applications
QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0 | https://papers.qnfo.org/papers/rosetta-fractal-math
QNFO: Constant-Sized-Support Magic State Distillation with Qubit Recycling: A Reconciled Resource, Footprint, and Energy Analysis | https://papers.qnfo.org/papers/constant-sized-support-magic-state-distillation-with-qubit-recycling-a-reconcile

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2107.14109v1 | Digital Twin As A Cost Reduction Method
  Many fields have been affected by the introduction of concepts such as sensors, industry 4.0, internet of things, machine learning and artificial intelligence in recent years. As a result of the interaction of cyber physical systems with these concepts, digital twin model has emerged. The concept of digital twin has been used in many areas with its emergence. The use of this model has made signifi
  Full text (https://ar5iv.labs.arxiv.org/html/2107.14109v1), excerpts of its own sections:
  § Submission history: From: Omer Aydin [ view email ] [v1] Sat, 10 Jul 2021 22:01:34 UTC (495 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Digital Twin As A Cost Reduction Method, by Suleyman Yukcu and 1 other authors View PDF view license
  § Current browse context:: cs.OH < prev | next > new | recent | 2021-07 Change to browse by: cs econ econ.GN q-fin q-fin.EC q-fin.GN
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[2] arXiv:2107.08351v2 | A Novel Approach to Analyze Fashion Digital Archive from Humanities
  Fashion styles adopted every day are an important aspect of culture, and style trend analysis helps provide a deeper understanding of our societies and cultures. To analyze everyday fashion trends from the humanities perspective, we need a digital archive that includes images of what people wore in their daily lives over an extended period. In fashion research, building digital fashion image archi
  Full text (https://arxiv.org/html/2107.08351v2), excerpts of its own sections:
  § 1 Introduction: Fashion styles adopted in our daily lives are an important aspect of culture. As noted by Lancioni  [ 17 ] , fashion is ‘a reflection of a society’s goals and aspirations’; people choose fashion styles within their embedded social contexts. Hence, the analysis of everyday fashion trends can provide an in-depth understanding of our societies and cultures. In fashion research, the advantages of digital fashion archives have continued to attract attention in recent times. These digital archives have been mainly built based on two purposes. One is enhancing the scholarly values of museum collections by making them public to utilize them digitally. Another motivation is predicting what fashion items will come into style in the short term with images retrieved from the internet for business purposes. However, these archives are not suitable for analyzing everyday fashion trends from the humanities perspective. To identify everyday fashion trends, we need a new digital archive that includes images of the clothes people wore in their daily lives over an extended period. [...]
  § 2.1 Fashion Trend Analysis: Kroeber  [ 15 ] analyzed fashion trends manually and measured features of women’s full evening toilette, e.g. skirt length and skirt width, which were collected from magazines from 1844 to 1919. After this work, many researchers conducted similar studies  [ 2 , 21 , 22 , 25 ] . [...]
  § 5.3 Discussion: The findings in Section 5.1 prompted a new research question of determining the importance of the different roles that media play in fashion trends: the role of the ‘mixed’ pattern for creating and reporting new trends and the ‘follow-up’ effect to keep their momentum. To theorize how fashion trends are generated in more detail, our findings indicate that quantifying the trends from multiple digital archives is essential to test the research questions about the effect of the media’s role, which has not been discussed thoroughly. In previous studies, researchers analyzed fashion style trends at a street level independently. However, to analyze the recent, more complicated trend patterns, the findings in Section 5.2 suggests that it would be thought-provoking to focus on what the icons represent for people’s social identities, rather than the style itself, and how they lead the trends. An example is the analysis of the types of media that icons use and the reach of that media. [...]
  § 6 Conclusions: In this study, we reviewed the issues in the existing digital fashion archives for the analysis of everyday fashion trends. As one of the solutions to these issues, we built CAT STREET, which comprises fashion images illustrating what people wore in their daily lives in the period 1970–2017, along with street-level geographical information. We demonstrated that machine learning retrieved how fashion styles emerged on the street using CAT STREET and the magazine archives helped us interpret these phenomena. These empirical analyses showed our approach’s potential to find new perspectives to promote the understanding of our societies and cultures through fashion embedded in the daily lives of consumers. Our work is not without limitations. We used the fashion style categories of FashionStyle14  [ 32 ] , which was defined by fashion experts and is considered to represent modern fashion. However, the definition does not cover all contemporary fashion styles and their substyles in a mutually exclusive and collectively exhaustive manner. [...]
[3] arXiv:cs/0508065v1 | Representing Digital Assets using MPEG-21 Digital Item Declaration
  Various XML-based approaches aimed at representing compound digital assets have emerged over the last several years. Approaches that are of specific relevance to the digital library community include the Metadata Encoding and Transmission Standard (METS), the IMS Content Packaging XML Binding, and the XML Formatted Data Units (XFDU) developed by CCSDS Panel 2. The MPEG-21 Digital Item Declaration 
  Full text (https://ar5iv.labs.arxiv.org/html/cs/0508065v1), excerpts of its own sections:
  § Submission history: From: Herbert van de Sompel [ view email ] [v1] Sat, 13 Aug 2005 03:09:25 UTC (451 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Representing Digital Assets using MPEG-21 Digital Item Declaration, by Jeroen Bekaert and 1 other authors View PDF view license
  § Current browse context:: cs.DL < prev | next > new | recent | 2005-08
  § DBLP - CS Bibliography: listing | bibtex Jeroen Bekaert Herbert Van de Sompel Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[4] arXiv:2012.02454v1 | Data Lakes for Digital Humanities
  Traditional data in Digital Humanities projects bear various formats (structured, semi-structured, textual) and need substantial transformations (encoding and tagging, stemming, lemmatization, etc.) to be managed and analyzed. To fully master this process, we propose the use of data lakes as a solution to data siloing and big data variety problems. We describe data lake projects we currently run i
  Full text (https://arxiv.org/html/2012.02454v1), excerpts of its own sections:
  § 1. Introduction: Traditional data management has long been adopted by many researchers involved in Digital Humanities (DH). However, it requires a substantial investment in data modeling, including, at the physical level, technologies such as relational and semi-structured Database Management Systems (DBMSs), various data formats, e.g., XML and JSON for semi-structured data, RDF for linked data, and query languages such as SQL and XQuery. This investment in computer science and the fact that initial data are inevitably transformed are presumably impediments to the adoption of DBMSs and related digital tools for DH. Moreover, most source information exploited by humanities and social sciences comes in textual format. Again, such textual documents are difficult to manage without substantial transformations: digitization, encoding and tagging, e.g., via the Text Encoding Initiative (TEI), and even lowercasing, stemming, lemmatization, stopword removal or normalization when it comes to text mining and natural language processing. [...]
  § 2.1. HyperThesau: The “Hyper thesaurus and data lakes: Mine the city and its archaeological archives” (HyperThesau) project involves a multidisciplinary team consisting of two research laboratories of archaeology and of computer science, a digital library, two archaeological museums and a private company. This project has two main objectives: (1) the design and implementation of an integrated platform to host, search, share and analyze archaeological data; (2) the design of a domain-specific thesaurus taking the whole archaeological data lifecycle into account, from data creation to publication. Archaeological data may bear many different types, e.g., textual documents, images (photographs, drawings…), sensor data, etc. Moreover, similar documents, e.g., excavation reports, are often created by various software tools that are not compatible with each other. The description of an archaeological object also differs with respect to users, usages and time. [...]
  § 2.2. Bretez/STRATEGE: Bretez ( Pardoën, 2020 ) is a multidisciplinary project aiming at a visual and sonorous restitution of the XVIII th -century Paris. It is also an exploratory project constituted of successive, interlinked modules that are (and must be) interoperable and open. The historical urban restitution is achieved with video game engines that bear their own respective characteristics, of course related to gaming. Yet, here, they are used for specific management and traceability needs. [...]
  § 3. Conclusion: In all four data lake projects summarized in Section  2 , we use different versions of the MEDAL metadata system, which is designed to be generic. However, although MEDAL is quite flexible, we do not believe in a single model for data lakes. There are indeed significant differences in data in only four projects, in terms of volume, variety and velocity, which imply different architectures and technologies. Thus, we think that much needed methodological tools for data lakes should be instantiated for each project rather than applied “as is”. Furthermore, the software layer we add to “industrialize” our data lakes might become yet another black box, while there is a strong stake for researchers in humanities and social sciences involved in DH projects not to be dispossessed of data by an analysis layer that would adopt a “click and go” approach. Data are indeed often partly constructed by said researchers themselves as a product of scientific work that takes time, thus giving a significant value to datasets. [...]
[5] arXiv:1910.08604v3 | Digital Democracy: Episode IV -- A New Hope, How a Corporation for Public Software Could Transform Digital Engagement for Government and Civil Society
  Though successive generations of digital technology have become increasingly powerful in the past twenty years, digital democracy has yet to realize its potential for deliberative transformation. The undemocratic exploitation of massive social media systems continued this trend, but it only worsened an existing problem of modern democracies, which were already struggling to develop deliberative in
  Full text (https://ar5iv.labs.arxiv.org/html/1910.08604v3), excerpts of its own sections:
  § Submission history: From: Todd Davies [ view email ] [v1] Fri, 18 Oct 2019 19:52:07 UTC (327 KB) [v2] Sun, 15 Dec 2019 03:44:40 UTC (388 KB) [v3] Tue, 3 Mar 2020 22:45:46 UTC (388 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Digital Democracy: Episode IV -- A New Hope, How a Corporation for Public Software Could Transform Digital Engagement for Government and Civil Society, by John Gastil and Todd Davies View PDF view license
  § Current browse context:: cs.CY < prev | next > new | recent | 2019-10 Change to browse by: cs cs.SI
  § DBLP - CS Bibliography: listing | bibtex John Gastil Todd Davies Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[6] arXiv:1704.08990v1 | EviPlant: An efficient digital forensic challenge creation, manipulation and distribution solution
  Education and training in digital forensics requires a variety of suitable challenge corpora containing realistic features including regular wear-and-tear, background noise, and the actual digital traces to be discovered during investigation. Typically, the creation of these challenges requires overly arduous effort on the part of the educator to ensure their viability. Once created, the challenge
  Full text (https://ar5iv.labs.arxiv.org/html/1704.08990v1), excerpts of its own sections:
  § Submission history: From: Mark Scanlon [ view email ] [v1] Fri, 28 Apr 2017 16:13:35 UTC (725 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled EviPlant: An efficient digital forensic challenge creation, manipulation and distribution solution, by Mark Scanlon and 2 other authors View PDF view license
  § Current browse context:: cs.CR < prev | next > new | recent | 2017-04 Change to browse by: cs cs.CY
  § DBLP - CS Bibliography: listing | bibtex Mark Scanlon Xiaoyu Du David Lillis Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[7] arXiv:2609.28946v1 | Digital Medicines Information at National Scale: Search Behaviour and System Performance of MediVerify Across 1.5 Million Queries
  National-scale digital health platforms generate usage data that reveal population healthcare needs. MediVerify, Sri Lanka's online medicines information platform providing access to National Medicines Regulatory Authority (NMRA)-approved medicines, recorded over 1.49 million queries in its first year. Large-scale medicine search behaviour in low- and middle-income countries (LMICs) remains poorly
  Full text (https://ar5iv.labs.arxiv.org/html/2609.28946v1), excerpts of its own sections:
  § Submission history: From: Praveen Athauda-Arachchi [ view email ] [v1] Thu, 24 Sep 2026 02:53:08 UTC (1,171 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Digital Medicines Information at National Scale: Search Behaviour and System Performance of MediVerify Across 1.5 Million Queries, by Praveen Charuka Athauda-Arachchi and 1 other authors View PDF view license
  § Current browse context:: cs.CY < prev | next > new | recent | 2026-09 Change to browse by: cs
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[8] QNFO: The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware | https://papers.qnfo.org/papers/the-price-of-the-digital-abstraction-entropy-and-encoding-overhead-when-discrete
  Quantum error correction (QEC) assumes that noise can be represented by a discrete set of Pauli errors on two‑level systems, but superconducting transmons are anharmonic oscillators whose native dynamics are continuous and better described as qudits of dimension $d\approx12$. This work quantifies the information‑theoretic overhead incurred when the continuous error model is forced into a discrete 
  Full text (https://papers.qnfo.org/papers/the-price-of-the-digital-abstraction-entropy-and-encoding-overhead-when-discrete), excerpts of its own sections:
  § 1. Introduction: Quantum error correction (QEC) is deployed on superconducting processors that consist of transmons—anharmonic oscillators with many energy levels—yet QEC theory treats each device as a qubit subject to a discrete Pauli error set $\{I,X,Y,Z\}$. Designers of large‑scale quantum processors must therefore map continuous bosonic dynamics onto a discrete logical layer, incurring hidden costs in discarded Hilbert‑space weight, extra encoding qubits, and entropy bookkeeping that does not appear in standard fault‑tolerance thresholds. If these hidden costs are large, they could increase the physical qubit budget, measurement bandwidth, or energy consumption required to achieve a target logical error rate, thereby affecting the economic viability of quantum computers. [...]
  § 5. Results: All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured. 1. **Register entropy** (Input: $d=12$): $H_{\mathrm{reg}}=3.584963$ bits per mode per use. 2. **Base truncation entropy** (Input: $d=12$): $S_{\mathrm{Base}}=1.791759$ nats $=2.584963$ bits. 3. **Binary encoding overhead** (Input: $d=12$): $m=4$ qubits, wasted levels $=4$, dimension overhead $=4/3$, encoding efficiency $\eta=0.896241$, idle fraction $=0.103759$. 4. **Entropy distortion** (Input: $\gamma=10^{-3}$): $H_{\mathrm{env}}^{\mathrm{phys}}=1.140776\times10^{-2}$ bits, $H_{\mathrm{env}}^{\mathrm{twirl}}=1.290776\times10^{-2}$ bits, distortion $\Delta H=1.500000\times10^{-3}$ bits, ratio $=1.131489$. The exact linear law $\Delta H=3\gamma/2$ holds for all $\gamma$. 5. **Discarded weight** (Inputs: $\bar n=0.1$, $d=12$): $p_{\mathrm{disc}}\approx3.186308\times10^{-13}$. [...]
  § (c) Minimal next experiment: A tabletop experiment could measure the environment entropy of a calibrated amplitude‑damping channel and of its Pauli‑twirled implementation on a single transmon. The experiment would (i) prepare the transmon in $|1\rangle$, (ii) let it relax for a calibrated time to achieve $\gamma\approx10^{-3}$, (iii) perform quantum process tomography to reconstruct the effective channel, (iv) implement the Pauli twirl by random Pauli gates before and after the relaxation, and (v) compare the Shannon entropy of the inferred environment label distributions. Observation of a statistically significant entropy excess matching the predicted $\Delta H$ would support our claim; a measured equality would falsify Result 4.
  § 8. Conclusion: We have quantified, with fully shown arithmetic, four faces of the cost of imposing a digital abstraction on bosonic quantum hardware: a register‑entropy floor of $\log_2 12\approx3.585$ bits per digitized mode per use; a base truncation entropy of $\ln 6\approx1.792$ nats ($\approx2.585$ bits) as proposed in [10]; a binary‑encoding inefficiency $\eta\approx0.896$ with dimension overhead $4/3$; and a Pauli‑twirling entropy distortion of $1.5\times10^{-3}$ bits per use (ratio $\approx1.131$) at $\gamma=10^{-3}$, in which the discrete surrogate overstates environment entropy despite matching total error probability exactly. The exact linear law $\Delta H=3\gamma/2$ shows that the distortion vanishes proportionally to the damping probability. A negative result bounds discarded leakage weight at $\approx3.20\times10^{-13}$ for cold modes. These quantities support the conjecture that the digital abstraction carries a measurable, computable price. Distinguishing these readings is, in our view, the most valuable next experiment.
[9] QNFO: Locale Framework Applied to Quantum Computing Innovations & Practical Applications | https://papers.qnfo.org/papers/locale-framework-quantum-applications
  Quantum computing is often presented through a small set of recurring claims: continuous-variable systems are naturally advantaged, more modes means more power, quantum advantage has been demonstrated at device level, statistics could in principle be non-standard, complex amplitudes are essential, approximation-based gate synthesis is the only approach, a transmon is a qubit, and fault tolerance i
  Full text (https://papers.qnfo.org/papers/locale-framework-quantum-applications), excerpts of its own sections:
  § 1. Introduction: The quantum computing field rests on a handful of sentences that are repeated so often they are no longer questioned. Continuous-variable systems, we are told, have a natural advantage because the physical world is continuous. More modes means more power. A fifty-qubit processor has demonstrated quantum advantage. Statistics could, in principle, be non-standard. Complex numbers are essential to quantum theory. Gate synthesis is an approximation problem. A transmon is a qubit. Fault tolerance is five years away. Each of these sentences is true in some sense. Each is also false in another. This is not a contradiction; it is the normal condition of physical statements. Every physical claim holds only within a specified domain of applicability — a particular vacuum or symmetry sector, an energy scale, a noise regime, a measurement model, or a set of boundary conditions. [...]
  § 2. The locale framework in brief: The companion record [1] develops four moves. First, *locale-conditionality*: every physical statement holds only within a locale, and the interesting physics lives at the seams where a rule fails to transfer. Second, *map and territory*: pedagogical maps (the spinning sphere for spin, the billiard balls for thermodynamics) fail at seams, while the territory — the transformation law, the algebra, the invariant — transfers. Third, the *rendering interface*: an observer inside a rendering experiences the metric of the image space, not the metric of the substrate, and no finite set of first-person observations decides between an Archimedean and an ultrametric substrate — yet a rendering with structure leaks structure. Fourth, *scale primitives*: stripped of anthropocentric units, the natural observables are counts and ratios. This paper needs none of that machinery in full. [...]
  § 3. Eight claims and their boundaries: Table 1 states eight claims that are heard constantly in quantum computing, the domain within which each holds, the boundary at which it fails, and the work that documents the boundary — presented at QPL 2026, with one arXiv exception. The table is the paper in miniature. **Table 1.** Widely repeated claims in quantum computing, their domains of validity, and the boundaries documented at QPL 2026 (one by an independent arXiv result). [...]
  § 8. Conclusions: Eight claims, eight boundaries, one conference week — and one independent arXiv result. The practical content of this paper is Table 1: a locale-indexed map of the claims that quantum computing practitioners hear every day, each paired with the exact paper — presented at QPL 2026, with one arXiv exception — that documents where it breaks. The theoretical content is the observation that the same structure appears in every row — a claim true within a domain, failing at a boundary, and the physics of interest living at the boundary. Three conclusions follow. First, claims are conditional truths. The habit of stating them without their conditions is the single most expensive ambiguity in the field, because it is what allows a roadmap to be read as a promise and a benchmark as a product. Second, the boundaries are public. The QPL 2026 program — one week, one venue — contains the documentation of every boundary in Table 1 but one, an independent arXiv result; the audit is public either way. [...]
[10] QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0 | https://papers.qnfo.org/papers/rosetta-fractal-math
  V2.0 / Rosetta v4.0 with Planck-Radix Correction + Qudit Manifesto. Corrects V1.0: transmon spectrum IS discrete (Planck quantization), binary truncation is a radix error not physics error. Transmon is a qudit (d~12), not a qubit. S_Base = ln(d/2) ~ 1.79 nats. 11-page PDF.
  Full text (https://papers.qnfo.org/papers/rosetta-fractal-math), excerpts of its own sections:
  § 1.1 The Map-Territory Problem: The global quantum computing industry has absorbed approximately 35 billion dollars in combined public and private investment over two decades while delivering zero commercially viable machines [@QNFO2026QubitDelusionI]. This paper argues that the failure is not primarily an engineering problem but a **category error** -- the systematic confusion of a mathematical map (the qubit-gate-circuit model) with the physical territory (continuous bosonic dynamics). The qubit is a **scaffold**, not an invariant. The gate is a projection, not an operation. The surface code is a mathematical trick, not a physical law.
  § 1.2 Statement of Results: | Axis | Core Result | |:-----|:------------| | **1.** Categorical Foundations | The functor $F: \mathcal{P} \to \mathcal{C}$ is non-exact (Theorem 1) | | **2.** Algebraization Complexity | $\cos(\phi)$ requires degree-224 polynomial for spectral fidelity $10^{-4}$ | | **3.** Thermodynamics of Translation | Rosetta's Constant $R = k_B T \ln(1/\alpha_r)$ | | **4.** Complexity Bounds | Digital Speed Limit: depth grows exponentially in qubit count $Q$ | | **5.** Experimental Protocol | Translation Calorimeter -- falsifiable measurement of $S_A$ | | **HAL.** Hidden Axioms | $S_{\text{Total}} = S_{\text{Obs}} + S_{\text{Base}} + S_{\text{Arch}} + S_{\text{Alg}} + S_{\text{Trot}}$ |
  § 1.3 Prior Art: This work builds on and extends several independent lines of inquiry. De Gosson [-@deGosson2012SymplecticCamel] first framed the conflict between geometry and algebra in quantum information using Gromov's non-squeezing theorem, but stopped at the existence argument without quantification. The QNFO's "Qubit Delusion" series [@QNFO2026QubitDelusionI; @QNFO2026BeyondTheQubit; @QNFO2026PhysicsOfComputation; @QNFO2026ProblemSubstrateMapping; @QNFO2026ManifestoHonestComputation] provided the philosophical scaffolding. Our contribution is the quantitative framework: explicit derivations of $S_A$, Rosetta's Constant $R$, and the formal categorical proof of non-exactness.
  § 2.1 Category $\mathcal{P}$: Physical Dynamics: $\mathcal{P}$ has as objects **symplectic manifolds** $(M^{2n}, \omega)$. Morphisms are Hamiltonian flows $\varphi_t^H: M \to M$ generated by $H: M \to \mathbb{R}$, or unitarily via $U(t) = e^{-iHt/\hbar}$. [...]
  § 2.3 Theorem 1: Non-Exactness: **Theorem 1.** *$F: \mathcal{P} \to \mathcal{C}$ is not exact -- there exist invariants preserved in $\mathcal{P}$ with no image in $\mathcal{C}$.* *Proof.* By Gromov's non-squeezing theorem [-@Gromov1985]: the symplectic capacity $c_G(M, \omega)$ is invariant under symplectomorphisms. Under $F$, this maps to a finite discrete point set with zero capacity. An invariant in the source with no image in the target -- the defining signature of a non-exact functor. $\square$
  § 8. Discussion: The transmon is not a "bad qubit." It is succeeding at being a bosonic computer. Three paths forward: 1. **Embrace analog:** Use transmons for analog quantum simulation of bosonic Hamiltonians 2. **Switch to fermions:** Spins and ions have native discrete spectra -- the functor $F$ may be exact for them 3. **Build hybrid architectures:** Bosonic coprocessor + fermionic digital core, with bounded $S_A$ at the interface
  § 10. Conclusion: Digital computation is an engineering triumph but not a universal ontology. The universe runs on complex amplitudes and continuous phase, not binary. The Approximation Entropy $S_A$ quantifies the distance between computational control and physical understanding -- in Joules.
[11] QNFO: Constant-Sized-Support Magic State Distillation with Qubit Recycling: A Reconciled Resource, Footprint, and Energy Analysis | https://papers.qnfo.org/papers/constant-sized-support-magic-state-distillation-with-qubit-recycling-a-reconcile
  Magic state distillation (MSD) is the canonical route to non-Clifford gates in fault-tolerant quantum computation, but conventional nested factories exhibit qubit occupancy that grows multiplicatively with the number of distillation rounds. Recent work on constant-sized-support distillation protocols with qubit recycling (arXiv:2609.17044v1) proposes to hold the active qubit footprint fixed across
  Full text (https://papers.qnfo.org/papers/constant-sized-support-magic-state-distillation-with-qubit-recycling-a-reconcile), excerpts of its own sections:
  § 1. Introduction: Fault-tolerant quantum computation requires a gate set executed with error rates far below the threshold of the underlying quantum error-correcting code. For most code families, the transversal or lattice-surgery-accessible gate set is Clifford-only and therefore classically simulable; the non-Clifford component, canonically the T gate, must be supplied by injecting specially prepared "magic" states whose fidelity must exceed what direct preparation achieves [1], [6], [8]. [...]
  § 5. Results: All numbers below are computed in Section 4 or labeled projections. 1. **Error suppression (computed).** A two-round 15-to-1 ladder suppresses input error p to 1,500,625 p⁹. At p = 10⁻³ the output error is 1.500625 × 10⁻²¹; at p = 10⁻² it is 1.500625 × 10⁻¹². The leading-order model is valid for 35 p² ≪ 1 (satisfied at both evaluation points). 2. **Peak occupancy (computed from stated premises).** Conventional nested two-round factory: 240 qubits. Recycled constant-support factory with S = 15, B = 15: 30 qubits. Reduction factor: 8.0×. 3. **Throughput bound (computed, bounding pair).** With equal per-round cycle times, the recycled design matches baseline throughput only if its block cycles 15× faster or 15 blocks run round-robin; otherwise per-hardware throughput falls by up to 15×. The occupancy gain of 8× and the worst-case throughput loss of 15× do not commute to a win: the design is net-beneficial in space-time only if the achievable speedup factor exceeds 15/8 ≈ 1.875. 4. [...]
  § 6. Discussion: **Limitations.** The analysis is deliberately minimal. The 35 p³ coefficient is a standard leading-order figure for the 15-to-1 family, not a coefficient verified for the specific protocol family of [1]; if the recycling protocols use different blocks, both the exponent and coefficient change, and Derivation 1's numbers change with them. The occupancy comparison assumes the constant-support premise (S = 15) and a minimal buffer (B = 15); the actual paper may require larger support or additional ancilla for error tracking, which would erode the 8× factor proportionally. The energy attribution of Model D assumes magic-state preparation and reset dominate the benchmark's quantum energy budget; in practice control electronics, cryogenic cooling, and syndrome extraction also consume significant power, and if these dominate, the projected savings from recycling would be smaller. The equality E_p = E_r is a simplification: reset may be cheaper (rapid measurement) or more expensive (active cooling), shifting the balance between the two terms of E₁. [...]
  § 7. Conclusion: We have built an explicit, fully arithmetized resource-budget model of constant-sized-support magic state distillation with qubit recycling. The computed results are: two-round error suppression to 1,500,625 p⁹ (1.500625 × 10⁻²¹ at p = 10⁻³; 1.500625 × 10⁻¹² at p = 10⁻²); a peak-occupancy reduction from 240 to 30 qubits (8.0×) under the stated constant-support and buffer premises; a raw-state efficiency ratio of 8.0×; a recycling budget of at most 10 reuses under the projected δ = 10⁻⁵, with an uncertainty span of 1–100 reuses; and, under an explicitly adopted energy-attribution convention anchored to publicly reported benchmark data [10], ≈ 0.55 ± 0.07 J per distilled magic state against a 1.5 × 10⁷ quantum-to-classical energy ratio. The proposal thus converts a spatial cost into an operational-quality cost and a temporal serialization cost. [...]