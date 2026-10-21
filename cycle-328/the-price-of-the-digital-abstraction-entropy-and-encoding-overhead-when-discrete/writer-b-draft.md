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

Digitization of continuous systems incurs measurable overheads, as illustrated by several domains:

* The emergence of digital‑twin models shows how mapping physical systems to digital representations introduces engineering effort and cost [1].  
* Building digital archives for fashion trends demonstrates the challenge of transforming continuous cultural data into discrete digital forms [2].  
* The MPEG‑21 Digital Item Declaration standard exemplifies the engineering work required to represent compound digital assets in a discrete XML format [3].  
* Proposals to use data lakes for heterogeneous datasets highlight the transformation effort needed to manage continuous‑to‑discrete data pipelines [4].  
* Digital‑democracy initiatives rely on discrete digital infrastructures, showing how design choices affect civic participation [5].  
* Constructing realistic digital‑forensic challenge corpora is arduous, underscoring difficulties in synthesizing continuous evidence into discrete artifacts [6].  
* The locale‑framework maps continuous‑variable claims in quantum computing to discrete representations, providing a conceptual tool for our analysis [9].  
* $S_{\mathrm{Base}}(d)=\ln(d/2)$ is defined as a base truncation entropy for comparison, following the discussion of approximation entropy in [10].  
* A resource‑budget and energy analysis for magic‑state distillation exemplifies how detailed accounting can reveal hidden costs of discrete quantum protocols [11].

These observations motivate a quantitative treatment of the overheads associated with forcing a continuous bosonic hardware model onto a discrete Pauli error framework.

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
* $S_{\mathrm{Base}}(d)=\ln(d/2)$: the base truncation entropy proposed in [10] (nats).  
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

We have quantified, with fully shown arithmetic, four faces of the cost of imposing a digital abstraction on bosonic quantum hardware: a register‑entropy floor of $\log_2 12\approx3.585$ bits per digitized mode per use; a base truncation entropy of $\ln 6\approx1.792$ nats ($\approx2.585$ bits) as proposed in [10]; a binary‑encoding inefficiency $\eta\approx0.896$ with dimension overhead $4/3$; and a Pauli‑twirling entropy distortion of $1.5\times10^{-3}$ bits per use (ratio $\approx1.131$) at $\gamma=10^{-3}$, in which the discrete surrogate overstates environment entropy despite matching total error probability exactly. The exact linear law $\Delta H=3\gamma/2$ shows that the distortion vanishes proportionally to the damping probability. A negative result bounds discarded leakage weight at $\approx3.20\times10^{-13}$ for cold modes. These quantities support the conjecture that the digital abstraction carries a measurable, computable price. Distinguishing these readings is, in our view, the most valuable next experiment.

## References

[1] arXiv:2107.14109v1 | Digital Twin As A Cost Reduction Method  
[2] arXiv:2107.08351v2 | A Novel Approach to Analyze Fashion Digital Archive from Humanities  
[3] arXiv:cs/0508065v1 | Representing Digital