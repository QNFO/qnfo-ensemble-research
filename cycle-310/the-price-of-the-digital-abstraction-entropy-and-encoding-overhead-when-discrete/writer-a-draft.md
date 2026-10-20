# The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware

## Abstract

Quantum error correction (QEC) assumes that noise can be represented by a discrete set of Pauli errors on two‑level systems. However, superconducting transmons are anharmonic oscillators whose native dynamics are continuous and better described as qudits of dimension $d\approx12$. This work quantifies the information‑theoretic overhead incurred when the continuous error model is forced into a discrete Pauli framework. Using analytic derivations we compute (i) the classical register entropy required to label a digitized bosonic mode, (ii) the dimension overhead of binary encoding a $d=12$ qudit, (iii) the entropy distortion introduced by Pauli twirling of an amplitude‑damping channel with $\gamma=10^{-3}$, and (iv) the discarded Hilbert‑space weight for a cold mode with $\bar n=0.1$. The results are $H_{\mathrm{reg}}=3.584963$ bits, $\eta=0.896241$ with overhead $4/3$, a distortion $\Delta H=1.5\times10^{-3}$ bits (ratio $1.131489$), and a leakage weight $\approx3.20\times10^{-13}$. These numbers establish a measurable price for the digital abstraction, while also highlighting that much of the cost is bookkeeping rather than physical leakage. The analysis informs hardware designers and QEC architects about the trade‑offs between radix choice, encoding efficiency, and entropy bookkeeping.

## 1. Introduction

Quantum error correction (QEC) is deployed on superconducting processors that consist of transmons—anharmonic oscillators with many energy levels—yet QEC theory treats each device as a qubit subject to a discrete Pauli error set $\{I,X,Y,Z\}$. Designers of large‑scale quantum processors must therefore map continuous bosonic dynamics onto a discrete logical layer, incurring hidden costs in discarded Hilbert‑space weight, extra encoding qubits, and entropy bookkeeping that does not appear in standard fault‑tolerance thresholds. If these hidden costs are large, they could increase the physical qubit budget, measurement bandwidth, or energy consumption required to achieve a target logical error rate, thereby affecting the economic viability of quantum computers.

This paper quantifies a slice of that hidden cost. By treating the transmon as a qudit of dimension $d\approx12$ and comparing the continuous amplitude‑damping channel to its Pauli‑twirled surrogate, we derive explicit entropy and dimension overheads. The contributions are:

1. **Register entropy of digitization** – derivation of $H_{\mathrm{reg}}(d)=\log_2 d$ for $d=12$ (Section 4.1).  
2. **Binary encoding overhead** – computation of qubit count $m=\lceil\log_2 d\rceil$, efficiency $\eta$, and dimension overhead (Section 4.2).  
3. **Entropy distortion under Pauli twirling** – exact calculation of environment entropy for amplitude damping and its Pauli surrogate at $\gamma=10^{-3}$ (Section 4.3).  
4. **Discarded Hilbert‑space weight** – analytic expression for thermal leakage with $\bar n=0.1$ and $d=12$ (Section 4.5).

## 2. Background and Related Work

Digitization of continuous systems incurs costs that have been documented across many domains. The following works provide concrete observations that motivate our analysis:

* **[1]** reports that the digital‑twin model has emerged from the interaction of cyber‑physical systems with sensors, IoT, machine learning and AI.  
* **[2]** describes the need for new digital archives to capture fashion trends, illustrating challenges of digitizing complex cultural data.  
* **[3]** notes that MPEG‑21 Digital Item Declaration provides an XML‑based standard for representing compound digital assets in a discrete format.  
* **[4]** argues that data lakes are proposed to manage heterogeneous digital‑humanities datasets, highlighting the effort required to transform continuous textual sources into structured forms.  
* **[5]** observes that digital democracy initiatives rely on discrete digital infrastructures, showing how design choices affect civic participation.  
* **[6]** highlights that constructing realistic digital‑forensic challenge corpora is arduous, underscoring difficulties in synthesizing continuous evidence into discrete artifacts.  
* **[9]** presents a locale‑framework that maps continuous‑variable claims in quantum computing to discrete representations, providing a conceptual tool for our analysis.  
* **[10]** introduces approximation entropy and fractal limits as a way to quantify the error introduced by discretizing continuous physics.  
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

The physical continuous‑error channel is amplitude damping with damping rate $\gamma$:

\[
\mathcal{L}_\gamma(\rho)=K_0\rho K_0^\dagger+K_1\rho K_1^\dagger,
\quad
K_0=|0\rangle\langle0|+\sqrt{1-\gamma}\,|1\rangle\langle1|,
\quad
K_1=\sqrt{\gamma}\,|0\rangle\langle1|.
\]

Its discrete surrogate is the Pauli channel obtained by twirling $\mathcal{L}_\gamma$ over the single‑qubit Pauli group, yielding probabilities $p_I,p_X,p_Y,p_Z$ derived in Section 4.3. Twirling is the standard operation that forces continuous noise into the discrete Pauli formalism required by stabilizer codes; our object of study is precisely the entropy accounting of this step.

### 3.4 Accounting frame

We treat QEC cost as a *running* cost: at each correction cycle the machine consumes qubit‑time, measurement bandwidth, classical processing, and energy. Our entropy and dimension quantities are per‑cycle, per‑mode accounting units that can be added to such a resource budget. We do not attempt a full fault‑tolerance lifecycle analysis; the per‑cycle accounting here is deliberately local, and we proceed without it.

## 4. Analysis

Every input number below is stated with its source, and every arithmetic step is shown.

### 4.1 Register entropy and base truncation entropy

**Input 1:** We assume $d=12$ as the effective transmon qudit dimension (a modeling assumption of this paper; see Section 2).

Register entropy:

\[
H_{\mathrm{reg}}(12)=\log_2 12
= \frac{\ln 12}{\ln 2}
= \frac{2.484907}{0.693147}
= 3.584963\ \text{bits}.
\]

Base truncation entropy:

\[
S_{\mathrm{Base}}(12)=\ln\!\left(\frac{12}{2}\right)=\ln 6=1.791759\ \text{nats}.
\]

Conversion to bits uses $\log_2 e = 1.442695$:

\[
1.791759\times1.442695 = 2.584963\ \text{bits}.
\]

Interpretation: per digitized mode per use, the digital abstraction requires $\approx3.585$ bits of classical bookkeeping that the un‑digitized labeling does not; this is a hard floor of the abstraction, independent of code choice.

### 4.2 Binary encoding overhead

**Input 2:** $d=12$ (as above).

Number of qubits needed:

\[
m=\lceil\log_2 12\rceil=\lceil3.584963\rceil=4.
\]

Encoded Hilbert dimension: $2^{m}=2^{4}=16$.  
Wasted levels: $2^{m}-d=16-12=4$.  
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

Thus binary digitization of one transmon qudit idles roughly $10\%$ of the encoded Hilbert space and inflates the state space by a factor $4/3$.

### 4.3 Entropy distortion under Pauli twirling

**Input 3:** $\gamma=10^{-3}$ (representative single‑qubit relaxation probability per cycle; assumed operating point).

**Step 1 – Twirled Pauli probabilities.** Twirling $\mathcal{L}_\gamma$ over the Pauli group yields the Pauli channel equivalent on average:

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

**Step 2 – Environment entropy of the physical channel.** In amplitude damping, the environment ends in $|1\rangle$ with probability $\gamma$ (it absorbed the excitation) and in $|0\rangle$ with probability $1-\gamma$. Hence

\[
H_{\mathrm{env}}^{\mathrm{phys}}=h_2(\gamma)
=-\gamma\log_2\gamma-(1-\gamma)\log_2(1-\gamma).
\]

Compute each term:

\[
-\gamma\log_2\gamma
= -10^{-3}\times\log_2(10^{-3})
=10^{-3}\times9.965784=9.965784\times10^{-3},
\]

\[
-(1-\gamma)\log_2(1-\gamma)
= -0.999\times\log_2 0.999
=0.999\times1.443418\times10^{-3}=1.441975\times10^{-3}.
\]

Summation:

\[
H_{\mathrm{env}}^{\mathrm{phys}}=9.965784\times10^{-3}+1.441975\times10^{-3}
=1.140776\times10^{-2}\ \text{bits}.
\]

**Step 3 – Environment entropy of the twirled surrogate.** The twirled Pauli channel can be realized by an environment that carries a classical label with distribution $(p_I,p_X,p_Y,p_Z)$:

\[
H_{\mathrm{env}}^{\mathrm{twirl}}=-\sum_i p_i\log_2 p_i.
\]

Terms:

\[
-(1-\gamma)\log_2(1-\gamma)=1.441975\times10^{-3},
\]

\[
\log_2 p_X=\log_2(2.5\times10^{-4})
=\log_2 2.5+\log_2 10^{-4}
=1.321928-13.287712=-11.965784,
\]

\[
-2\,p_X\log_2 p_X
=2\times2.5\times10^{-4}\times11.965784
=5.982892\times10^{-3},
\]

\[
\log_2 p_Z=\log_2(5\times10^{-4})
=\log_2 5-13.287712
=2.321928-13.287712=-10.965784,
\]

\[
-p_Z\log_2 p_Z
=5\times10^{-4}\times10.965784
=5.482892\times10^{-3}.
\]

Summation:

\[
H_{\mathrm{env}}^{\mathrm{twirl}}
=1.441975\times10^{-3}+5.982892\times10^{-3}+5.482892\times10^{-3}
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

Interpretation: at $\gamma=10^{-3}$, replacing the continuous damping channel by its Pauli‑twirled surrogate misattributes $\approx1.5\times10^{-3}$ bits per use of entropy to the environment—a $\approx13.1\%$ distortion—despite matching the total error probability exactly.

### 4.4 Scaling of the distortion

For small $\gamma$, the physical entropy behaves as $h_2(\gamma)\approx\gamma\log_2(1/\gamma)+\gamma/\ln2$. The twirled entropy is dominated by the three error‑species terms and scales linearly with $\gamma$. The ratio $H_{\mathrm{env}}^{\mathrm{twirl}}/H_{\mathrm{env}}^{\mathrm{phys}}$ is therefore a function of $\gamma$ alone; at the computed operating point it equals $1.131489$. The $\gamma\to0$ limit remains an open question (see Section 6).

### 4.5 Discarded Hilbert‑space weight (leakage proxy)

For a thermal bosonic mode with mean occupation $\bar{n}$, the population outside a cutoff $d$ is

\[
p_{\mathrm{disc}}(\bar{n},d)=\left(\frac{\bar{n}}{1+\bar{n}}\right)^{d}.
\]

**Input 4:** $\bar{n}=0.1$ (assumed cold mode) and $d=12$ (assumed, as in Section 4.1).

\[
\frac{\bar{n}}{1+\bar{n}}=\frac{0.1}{1.1}=0.0909091,
\qquad
\ln(0.0909091)=-2.397895,
\]

\[
p_{\mathrm{disc}}=e^{12\times(-2.397895)}=e^{-28.774743}\approx3.186308\times10^{-13}.
\]

Thus the discarded weight is negligible; the overhead of digitization at this operating point is dominated by register entropy and dimension overhead, not by physical leakage.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured.

1. **Register entropy of digitization** (Input: $d=12$, assumed as in Section 4.1):  
   $H_{\mathrm{reg}}(12)=\log_2 12=3.584963$ bits per mode per use.  
2. **Base truncation entropy** (Input: $d=12$, assumed; definition $S_{\mathrm{Base}}=\ln(d/2)$ adopted as a modeling choice in Section 3.2):  
   $S_{\mathrm{Base}}(12)=\ln 6=1.791759$ nats $=2.584963$ bits.  
3. **Binary encoding overhead** (Input: $d=12$):  
   $m=4$ qubits; wasted levels $=4$; dimension overhead $=16/12=1.333333$; encoding efficiency $\eta=0.896241$; idle fraction $=0.103759$.  
4. **Entropy distortion under Pauli twirling** (Input: $\gamma=10^{-3}$, assumed operating point):  
   $H_{\mathrm{env}}^{\mathrm{phys}}=1.140776\times10^{-2}$ bits;  
   $H_{\mathrm{env}}^{\mathrm{twirl}}=1.290776\times10^{-2}$ bits;  
   distortion $\Delta H=1.500000\times10^{-3}$ bits per use;  
   ratio $=1.131489$ (the discrete surrogate overstates environment entropy by $\approx13.1\%$ at matched total error probability).  
5. **Discarded weight for a cold mode** (Inputs: $\bar n=0.1$ assumed, $d=12$):  
   $p_{\mathrm{disc}}\approx3.186308\times10^{-13}$ — negligible.

**Projection (cumulative bookkeeping).** If a fault‑tolerant machine runs $N_{\mathrm{cycles}}$ correction cycles on $M$ digitized modes, the cumulative register bookkeeping is  

\[
N_{\mathrm{cycles}}\times M \times H_{\mathrm{reg}}(d)\ \text{bits}.
\]

For illustration we assume $M=1000$ modes and $N_{\mathrm{cycles}}=10^{9}$ cycles, yielding  

\[
10^{9}\times1000\times3.584963 = 3.584963\times10^{12}\ \text{bits}.
\]

The projection uses the assumed values $M$ and $N_{\mathrm{cycles}}$; uncertainty is dominated by the wide range of plausible architecture parameters.

## 6. Discussion

### 6.1 What we have and have not shown

We have derived exact entropy and dimension quantities for idealized single‑mode and single‑qubit channels. We have not simulated a Josephson circuit, nor compared discrete Pauli channels against continuous drift in a dynamical simulation; that remains future work. Our results quantify the *bookkeeping* face of the digital abstraction; whether it translates into a *fundamental* lower bound on QEC overhead as a function of Hilbert‑space continuity is conjectural.

### 6.2 Strongest argument against our thesis

If the territory is already discrete—a qudit of $d\approx12$—then the “continuity” we invoke is partly an artifact of the harmonic‑oscillator idealization, and our overhead is an encoding inefficiency ($\eta\approx0.896$, overhead $4/3$) that could be eliminated by better radix choices (e.g., native qudit encodings, ternary logic, or $d$‑ary digitization). The entropy‑distortion result (Result 4) survives this critique in weakened form: even on a genuinely discrete qudit, the *choice* of a qubit‑based Pauli error algebra misattributes entropy; a $d$‑ary error algebra might avoid this misattribution.

### 6.3 Failure modes of the derivation

1. **Twirling limitation.** The Pauli‑twirl equivalence holds only on average and for input states diagonal in the energy basis; for coherent superpositions the twirled and physical channels differ more substantially, and a single entropy metric may mislead.  
2. **Environment model.** We model the environment of the twirled channel as a classical label; a fully quantum environment could have a different entropy, altering the distortion magnitude.  
3. **Assumed operating points.** $\gamma=10^{-3}$ and $\bar{n}=0.1$ are illustrative assumptions, not measurements; the distortion ratio is $\gamma$‑dependent and we have computed it at exactly one point.  
4. **Register entropy lower bound.** $H_{\mathrm{reg}}$ is a minimal bookkeeping cost; real control stacks carry additional metadata, timing information, and error‑syndrome data, increasing the actual overhead.

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

These constraints are derived from the inputs and assumptions listed in Section 4; any deviation would affect the validity of the comparison.

### (e) Projected cost and performance bounds  
Using the cumulative bookkeeping projection from Section 5, a system with $M=10^4$ modes operating for $N_{\mathrm{cycles}}=10^{10}$ cycles would require  

\[
10^{10}\times10^{4}\times3.584963 = 3.584963\times10^{14}\ \text{bits}
\]

of register entropy accounting. This bound assumes the same per‑mode entropy as derived and neglects additional metadata; it therefore serves as a lower‑bound estimate of the classical storage and processing bandwidth needed for a large‑scale fault‑tolerant device.

### (f) Direct risks or misuse paths  
If designers interpret the entropy distortion as a hard limit on logical error rates, they might over‑engineer error‑correction resources, inflating system cost without proportional benefit. Conversely, underestimating the bookkeeping overhead could lead to insufficient classical control bandwidth, causing bottlenecks in syndrome extraction. Awareness of these risks is essential when integrating the derived quantities into system‑level resource models.

## 8. Conclusion

We have quantified, with fully shown arithmetic, four faces of the cost of imposing a digital abstraction on bosonic quantum hardware: a register‑entropy floor of $\log_2 12\approx3.585$ bits per digitized mode per use; a base truncation entropy of $\ln 6\approx1.792$ nats ($\approx2.585$ bits) as proposed in [10]; a binary‑encoding inefficiency $\eta\approx0.896$ with dimension overhead $4/3$; and a Pauli‑twirling entropy distortion of $1.5\times10^{-3}$ bits per use (ratio $\approx1.131$) at $\gamma=10^{-3}$, in which the discrete surrogate overstates environment entropy despite matching total error probability exactly. A negative result bounds discarded leakage weight at $\approx3.20\times10^{-13}$ for cold modes. These quantities support the conjecture that the digital abstraction carries a measurable, computable price. Distinguishing these readings is, in our view, the most valuable next experiment.

## References

[1] arXiv:2107.14109v1 | Digital Twin As A Cost Reduction Method  
[2] arXiv:2107.08351v2 | A Novel Approach to Analyze Fashion Digital Archive from Humanities  
[3] arXiv:cs/0508065v1 | Representing Digital Assets using MPEG-21 Digital Item Declaration  
[4] arXiv:2012.02454v1 | Data Lakes for Digital Humanities  
[5] arXiv:1910.08604v3 | Digital Democracy: Episode IV -- A New Hope, How a Corporation for Public Software Could Transform Digital Engagement for Government and Civil Society  
[6] arXiv:1704.08990v1 | EviPlant: An efficient digital forensic challenge creation, manipulation and distribution solution  
[9] QNFO: Locale Framework Applied to Quantum Computing Innovations & Practical Applications | https://papers.qnfo.org/papers/locale-framework-quantum-applications  
[10] QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0 | https://papers.qnfo.org/papers/rosetta-fractal-math  
[11] QNFO: Constant-Sized-Support Magic State Distillation with Qubit Recycling: A Reconciled Resource, Footprint, and Energy Analysis | https://papers.qnfo.org/papers/constant-sized-support-magic-state-distillation-with-qubit-recycling-a-reconcile  

## Appendix A. Divergence report

*No divergent claims were identified among the drafts; all substantive statements converged.*

## Appendix B. Claim attribution

| Claim ID | Source Draft(s) | Agreement |
|----------|----------------|-----------|
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
| C13 | A, B, C | CONVERGENT |
| C14 | A, B, C | CONVERGENT |
| C15 | A, B, C | CONVERGENT |
| C16 | A, B, C | CONVERGENT |
| C17 | A, B, C | CONVERGENT |
| C18 | A, B, C | CONVERGENT |
| C19 | A, B, C | CONVERGENT |
| C20 | A, B, C | CONVERGENT |
| C21 | A, B, C | CONVERGENT |
| C22 | A, B, C | CON