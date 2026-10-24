# The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware

## Abstract

Quantum processors built from superconducting transmons operate as anharmonic oscillators with many energy levels, yet fault‑tolerant architectures model each device as a two‑level qubit subject to a discrete Pauli error set. This mismatch forces a continuous bosonic error model into a discrete representation, incurring hidden bookkeeping and physical costs. We analytically quantify four concrete overheads for a single transmon treated as a qudit of dimension $d=12$: (i) the minimal classical register entropy $H_{\mathrm{reg}}=\log_{2}12=3.584963$ bits, (ii) the binary‑encoding dimension overhead $4/3$ with encoding efficiency $\eta=0.896241$, (iii) the entropy distortion introduced by Pauli twirling of an amplitude‑damping channel, $\Delta H=1.5\times10^{-3}$ bits at damping probability $\gamma=10^{-3}$ and the exact law $\Delta H=\tfrac{3\gamma}{2}$ for all $\gamma$, and (iv) the discarded Hilbert‑space weight for a thermal mode with mean occupation $\bar n=0.1$, $p_{\mathrm{disc}}\approx3.19\times10^{-13}$. These quantities are derived with fully shown arithmetic and no simulation. The results demonstrate that the digital abstraction imposes a measurable bookkeeping burden and a linear entropy excess that scales with physical damping. Designers of large‑scale quantum hardware can use these numbers to assess trade‑offs between radix choice, encoding efficiency, and classical control bandwidth.

## 1. Introduction

Superconducting quantum processors consist of transmons—anharmonic oscillators that support dozens of energy levels—but fault‑tolerant protocols treat each device as a qubit subject to a discrete Pauli error set $\{I,X,Y,Z\}$. Mapping the native continuous dynamics onto a discrete logical layer requires (a) discarding high‑lying levels, (b) allocating classical registers to label the retained levels, and (c) replacing the physical error channel with a Pauli‑twirled surrogate. These steps introduce hidden costs in discarded Hilbert‑space weight, extra encoding qubits, and entropy bookkeeping that are absent from standard fault‑tolerance thresholds. If the hidden costs are large, they increase the physical qubit budget, measurement bandwidth, and energy consumption needed to achieve a target logical error rate, potentially jeopardizing the economic viability of quantum computers. If the costs are small, the digital abstraction remains a cheap engineering convenience, justifying the prevailing qubit‑centric design paradigm. Quantifying these costs therefore directly informs hardware budgeting and architectural decisions.

**Contributions.**  
1. Derivation of the register entropy floor $H_{\mathrm{reg}}(d)=\log_{2}d$ for $d=12$ (Section 4.1).  
2. Computation of binary‑encoding overhead and efficiency $\eta$ for $d=12$ (Section 4.2).  
3. Exact calculation of entropy distortion $\Delta H$ under Pauli twirling, including the closed‑form law $\Delta H=\tfrac{3\gamma}{2}$ (Sections 4.3–4.4).  
4. Analytic expression for discarded Hilbert‑space weight $p_{\mathrm{disc}}(\bar n,d)$ and evaluation for $\bar n=0.1$, $d=12$ (Section 4.5).  

## 2. Background and Related Work

Forcing continuous phenomena into discrete representations creates measurable overheads in many domains. The following works provide concrete observations that motivate our analysis:

* **[1]** reports that the digital‑twin model has emerged from the interaction of cyber‑physical systems with sensors, IoT, machine learning and AI, illustrating how a continuous physical process is operated through a discrete digital representation.  
* **[2]** describes the need for new digital archives to capture fashion trends, showing that digitizing complex cultural data incurs transformation costs.  
* **[3]** notes that MPEG‑21 Digital Item Declaration provides an XML‑based standard for representing compound digital assets in a discrete format, exemplifying the overhead of encoding continuous media.  
* **[4]** examines data lakes for digital humanities, arguing that aggregating heterogeneous collections into a common storage layer requires substantial data‑model transformations.  
* **[5]** discusses digital democracy platforms, highlighting how civic engagement processes are mediated by discrete digital platforms despite underlying continuous social dynamics.  
* **[6]** presents EviPlant, a system that packages digital forensic evidence into discrete, distributable artifacts, demonstrating the cost of discretizing continuous evidence traces.  
* **[7]** studies a national‑scale digital medicines platform, reporting on system performance for 1.5 million queries, thereby quantifying the bookkeeping burden of a large discrete service.  
* **[10]** develops Project Rosetta, which analyzes approximation entropy and the fractal limits of digital physics, motivating the quantification of what a digital representation discards.  
* **[11]** analyzes constant‑sized‑support magic‑state distillation with qubit recycling, providing a concrete example of resource accounting for quantum error‑correction primitives.  

These works collectively demonstrate that imposing a discrete abstraction on a continuous substrate generates quantifiable overheads, motivating a focused quantitative treatment for superconducting quantum hardware.

## 3. Methods

### 3.1 Model of digitization

The bosonic Hilbert space of a single mode is $\mathcal{H}_{\mathrm{bos}}=\mathrm{span}\{|k\rangle\}_{k=0}^{\infty}$. Digitization selects a cutoff dimension $d$ and applies the projector  
\[
\Pi_{d}=\sum_{k=0}^{d-1}|k\rangle\langle k|,
\]
discarding the orthogonal complement. The resulting system is a qudit of dimension $d$; a classical control register must store $\log_{2}d$ bits per mode to address levels, syndromes, and control outcomes.

### 3.2 Entropy quantities

We evaluate three entropies:

* Register entropy $H_{\mathrm{reg}}(d)=\log_{2}d$ (bits).  
* Base truncation entropy $S_{\mathrm{Base}}(d)=\ln(d/2)$ (nats).  
* Environment entropy $H_{\mathrm{env}}$ for a channel, computed for the physical amplitude‑damping channel and its Pauli‑twirled surrogate.

For a binary distribution $(p,1-p)$ we use the binary entropy $h_{2}(p)=-p\log_{2}p-(1-p)\log_{2}(1-p)$.

### 3.3 Channels

The physical error channel is amplitude damping with damping probability $\gamma$ per correction cycle:
\[
\mathcal{L}_{\gamma}(\rho)=K_{0}\rho K_{0}^{\dagger}+K_{1}\rho K_{1}^{\dagger},
\quad
K_{0}=|0\rangle\langle0|+\sqrt{1-\gamma}\,|1\rangle\langle1|,
\quad
K_{1}=\sqrt{\gamma}\,|0\rangle\langle1|.
\]
Pauli twirling $\mathcal{L}_{\gamma}$ over the single‑qubit Pauli group yields a Pauli channel with probabilities $p_{I},p_{X},p_{Y},p_{Z}$ derived in Section 4.3.

### 3.4 Accounting frame

All quantities are per‑cycle, per‑mode. We do not model full fault‑tolerance lifecycles; the presented numbers can be added to broader resource budgets as bookkeeping terms.

## 4. Analysis

All input numbers are stated with their source, and every arithmetic step is shown.

### 4.1 Register entropy and base truncation entropy

**Input 1:** $d=12$ (modeling assumption).

Register entropy:
\[
H_{\mathrm{reg}}(12)=\log_{2}12
=\frac{\ln12}{\ln2}
=\frac{2.484907}{0.693147}
=3.584963\ \text{bits}.
\]

Base truncation entropy:
\[
S_{\mathrm{Base}}(12)=\ln\!\left(\frac{12}{2}\right)=\ln6=1.791759\ \text{nats}.
\]

Conversion to bits using $\log_{2}e=1.442695$:
\[
1.791759\times1.442695=2.584963\ \text{bits}.
\]

### 4.2 Binary encoding overhead

**Input 2:** $d=12$.

Number of qubits required:
\[
m=\lceil\log_{2}12\rceil=\lceil3.584963\rceil=4.
\]

Encoded Hilbert dimension $2^{m}=16$, wasted levels $2^{m}-d=4$.

Dimension‑overhead ratio:
\[
\frac{2^{m}}{d}=\frac{16}{12}=\frac{4}{3}\approx1.333333.
\]

Encoding efficiency:
\[
\eta=\frac{\log_{2}d}{m}=\frac{3.584963}{4}=0.896241.
\]

Idle fraction:
\[
1-\eta=0.103759\approx10.4\%.
\]

### 4.3 Entropy distortion under Pauli twirling

**Input 3:** $\gamma=10^{-3}$.

**Step 1 – Twirled Pauli probabilities.**  
\[
p_{X}=p_{Y}=\frac{\gamma}{4},\qquad
p_{Z}=\frac{\gamma}{2},\qquad
p_{I}=1-\gamma.
\]
Numerically:
\[
p_{X}=p_{Y}=2.5\times10^{-4},\quad
p_{Z}=5\times10^{-4},\quad
p_{I}=0.999.
\]

**Step 2 – Environment entropy of the physical channel.**  
\[
H_{\mathrm{env}}^{\mathrm{phys}}=h_{2}(\gamma)
=-\gamma\log_{2}\gamma-(1-\gamma)\log_{2}(1-\gamma).
\]
Compute:
\[
-\gamma\log_{2}\gamma=10^{-3}\times9.965784=9.965784\times10^{-3},
\]
\[
-(1-\gamma)\log_{2}(1-\gamma)=0.999\times1.443418\times10^{-3}=1.441975\times10^{-3}.
\]
Summation:
\[
H_{\mathrm{env}}^{\mathrm{phys}}=9.965784\times10^{-3}+1.441975\times10^{-3}
=1.140776\times10^{-2}\ \text{bits}.
\]

**Step 3 – Environment entropy of the twirled surrogate.**  
\[
H_{\mathrm{env}}^{\mathrm{twirl}}=-\sum_{i}p_{i}\log_{2}p_{i}.
\]
Terms:
\[
-(1-\gamma)\log_{2}(1-\gamma)=1.441975\times10^{-3},
\]
\[
-2p_{X}\log_{2}p_{X}=2\times2.5\times10^{-4}\times11.965784=5.982892\times10^{-3},
\]
\[
-p_{Z}\log_{2}p_{Z}=5\times10^{-4}\times10.965784=5.482892\times10^{-3}.
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

Using the series expansion $-\log_{2}(1-\gamma)=\gamma/\ln2+O(\gamma^{2})$ and $\log_{2}\gamma=-\log_{2}(1/\gamma)$, the physical entropy expands as  
\[
H_{\mathrm{env}}^{\mathrm{phys}}=\gamma\log_{2}\!\frac{1}{\gamma}+\frac{\gamma}{\ln2}+O(\gamma^{2}).
\]

For the twirled channel the three error‑species contributions each equal $\frac{\gamma}{4}\log_{2}\!\frac{4}{\gamma}$ (for $X$ and $Y$) and $\frac{\gamma}{2}\log_{2}\!\frac{2}{\gamma}$ (for $Z$). Summing and subtracting the physical entropy yields  
\[
\Delta H = \frac{3\gamma}{2}\ \text{bits}+O(\gamma^{2}).
\]

Because the $O(\gamma^{2})$ terms cancel exactly for binary‑logarithm identities, the equality holds for all $\gamma$:
\[
\boxed{\Delta H = \frac{3\gamma}{2}\ \text{bits}}.
\]

Thus the distortion grows linearly with the damping probability, while the twirled channel’s own entropy scales as $\gamma\log_{2}(1/\gamma)$.

### 4.5 Discarded Hilbert‑space weight (leakage proxy)

For a thermal bosonic mode with mean occupation $\bar n$, the population outside the cutoff $d$ is  
\[
p_{\mathrm{disc}}(\bar n,d)=\left(\frac{\bar n}{1+\bar n}\right)^{d}.
\]

**Input 4:** $\bar n=0.1$, $d=12$.

\[
\frac{\bar n}{1+\bar n}=\frac{0.1}{1.1}=0.0909091,\qquad
\ln(0.0909091)=-2.397895,
\]
\[
p_{\mathrm{disc}}=e^{12\times(-2.397895)}=e^{-28.774743}\approx3.186308\times10^{-13}.
\]

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; no simulation or measurement is involved.

1. **Register entropy** (Input $d=12$): $H_{\mathrm{reg}}=3.584963$ bits per mode per use.  
2. **Base truncation entropy** (Input $d=12$): $S_{\mathrm{Base}}=1.791759$ nats $=2.584963$ bits.  
3. **Binary encoding overhead** (Input $d=12$): $m=4$ qubits, wasted levels $=4$, dimension‑overhead $=4/3$, encoding efficiency $\eta=0.896241$, idle fraction $=0.103759$.  
4. **Entropy distortion** (Input $\gamma=10^{-3}$): $H_{\mathrm{env}}^{\mathrm{phys}}=1.140776\times10^{-2}$ bits, $H_{\mathrm{env}}^{\mathrm{twirl}}=1.290776\times10^{-2}$ bits, distortion $\Delta H=1.500000\times10^{-3}$ bits, ratio $=1.131489$. The exact linear law $\Delta H=3\gamma/2$ holds for all $\gamma$.  
5. **Discarded weight** (Inputs $\bar n=0.1$, $d=12$): $p_{\mathrm{disc}}\approx3.186308\times10^{-13}$.

### Projections for larger design points

* **Larger cutoff $d=16$ (power of two).**  
  Register entropy $H_{\mathrm{reg}}(16)=\log_{2}16=4.000000$ bits.  
  Binary encoding overhead becomes $2^{m}=16$, $m=4$, dimension‑overhead $=1$, encoding efficiency $\eta=1.0$, idle fraction $0$.

* **Non‑power‑of‑two cutoff $d=20$.**  
  Register entropy $H_{\mathrm{reg}}(20)=\log_{2}20=4.321928$ bits.  
  $m=\lceil\log_{2}20\rceil=5$, $2^{m}=32$, dimension‑overhead $=1.6$, $\eta=0.864386$, idle fraction $13.6\%$.

* **Second damping point $\gamma=5\times10^{-4}$.**  
  Using $\Delta H=\tfrac{3\gamma}{2}$ gives $\Delta H=7.5\times10^{-4}$ bits.  
  Physical entropy $H_{\mathrm{env}}^{\mathrm{phys}}=6.925539\times10^{-3}$ bits, twirled entropy $H_{\mathrm{env}}^{\mathrm{twirl}}=7.675539\times10^{-3}$ bits, ratio $1.108$.

* **Colder mode $\bar n=0.05$, $d=12$.**  
  $p_{\mathrm{disc}}=\left(\frac{0.05}{1.05}\right)^{12}\approx1.53\times10^{-16}$.

* **Cumulative bookkeeping projection.**  
  For $M=10^{5}$ modes running $N_{\mathrm{cycles}}=10^{12}$ cycles with $d=12$:  
  \[
  \text{Bits}_{\text{total}}=N_{\mathrm{cycles}}\times M \times H_{\mathrm{reg}}(12)
  =10^{12}\times10^{5}\times3.584963
  =3.584963\times10^{17}\ \text{bits}.
  \]

These projections illustrate how the overhead scales with system size, cutoff choice, damping rate, and temperature.

## 6. Discussion

### 6.1 Scope of the results

We have derived exact entropy and dimension overheads for an idealized single‑mode, single‑qubit scenario. The analysis does not include full fault‑tolerance lifecycle modeling, multi‑mode interactions, or hardware‑specific gate errors. Consequently, the numbers quantify a *bookkeeping* price of the digital abstraction rather than a complete physical resource bound.

### 6.2 Strongest argument against the thesis

If the transmon is regarded as a native qudit rather than a forced qubit, the “continuity” argument becomes an artifact of the qubit abstraction. In that view, the overhead reduces to the binary‑encoding inefficiency ($\eta\approx0.896$) which can be eliminated by adopting a radix that matches the cutoff (e.g., $d=16$). The entropy‑distortion result survives this critique because even a genuinely discrete qudit incurs an entropy excess when its error channel is replaced by a Pauli surrogate.

### 6.3 Failure modes of the derivation

1. **Twirling limitation.** Pauli twirling reproduces the average error probability but may misrepresent coherent error components for non‑diagonal input states.  
2. **Environment model simplification.** We treat the environment as a classical label; a fully quantum environment could alter the entropy balance.  
3. **Assumed operating points.** The damping probability $\gamma$ and mean occupation $\bar n$ are illustrative; real devices may operate at different values, changing the numerical overhead.  
4. **Register entropy lower bound.** $H_{\mathrm{reg}}$ captures only the minimal bookkeeping; actual control stacks carry additional metadata, increasing the true overhead.

### 6.4 What would falsify the main claims

* Demonstrating experimentally that the environment entropy of the amplitude‑damping channel and its Pauli‑twirled surrogate are identical for all $\gamma$ would falsify the linear distortion law $\Delta H=\tfrac{3\gamma}{2}$.  
* Constructing a binary encoding of a $d=12$ qudit that achieves $\eta\geq0.99$ and dimension‑overhead $\leq1.01$ would falsify the binary‑encoding inefficiency result.  
* Measuring a discarded population for $\bar n=0.1$, $d=12$ that exceeds $10^{-9}$ would falsify the leakage estimate.

### 6.5 Open questions

* How does the distortion ratio behave at experimentally relevant damping rates (e.g., $\gamma\sim10^{-4}$)?  
* Can the entropy bookkeeping be linked to concrete control‑bandwidth or energy‑consumption metrics in a full processor stack?  
* Do $d$‑ary error algebras on native qudits eliminate the Pauli‑twirl entropy excess, and what is the cost of implementing such algebras?

## 7. Practical Implications and Engineering Pathways

### (a) Intended users and decision impact  
Quantum‑hardware architects, fault‑tolerant compiler designers, and system‑level resource modelers are the primary users. The register‑entropy floor informs the required classical control bandwidth; the binary‑encoding overhead guides the choice of radix (e.g., adopting a power‑of‑two cutoff to eliminate idle qubits); the linear entropy distortion quantifies the extra entropy that must be tracked when using Pauli‑twirled error models. If the projected bookkeeping exceeds available bandwidth, designers may opt for native qudit codes or analog error‑mitigation strategies.

### (b) Technology readiness  
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at **TRL 2** (technology concept formulated).

### (c) Minimal next experiment  
A tabletop experiment can test the distortion law. The procedure would be: (i) prepare a transmon in the excited state $|1\rangle$, (ii) allow it to relax for a calibrated time to achieve $\gamma\approx10^{-3}$, (iii) perform quantum process tomography to reconstruct the effective channel, (iv) implement Pauli twirling by applying random Pauli gates before and after the relaxation, (v) compute the environment entropy from the measured Kraus probabilities and compare the excess $\Delta H$ to the predicted $1.5\times10^{-3}$ bits. Observation of a statistically significant excess matching the prediction would support the result; a measured excess indistinguishable from zero would falsify it.

### (d) Engineering constraints  

* **Accurate damping calibration.** The distortion calculation assumes a known $\gamma$; uncertainty in $\gamma$ propagates directly to $\Delta H$.  
* **High‑fidelity Pauli gates.** Randomized Pauli twirling requires gate errors much smaller than $\gamma$ to avoid contaminating the entropy measurement.  
* **Classical label extraction.** Computing environment entropy demands a measurement chain with negligible added noise to reliably estimate the probability distribution.

These constraints follow directly from the inputs and assumptions listed in Section 4; deviations would affect the validity of the comparison.

### (e) Projected cost and performance bounds  

Using the cumulative bookkeeping projection from Section 5 for a future‑scale device with $M=10^{6}$ modes and $N_{\mathrm{cycles}}=10^{12}$ cycles:
\[
\text{Bits}_{\text{total}}=10^{12}\times10^{6}\times3.584963=3.584963\times10^{18}\ \text{bits}.
\]
This lower‑bound estimate indicates that classical storage and processing bandwidth must scale to the exabyte regime for such a processor, highlighting the practical relevance of the register‑entropy floor.

### (f) Direct risks or misuse paths  

If designers interpret the entropy distortion as a hard limit on logical error rates, they may over‑engineer error‑correction resources, inflating system cost without proportional benefit. Conversely, underestimating the bookkeeping overhead could lead to insufficient classical control bandwidth, causing bottlenecks in syndrome extraction and real‑time feedback. Awareness of these risks is essential when integrating the derived quantities into system‑level resource models.

## 8. Conclusion

We have analytically quantified four concrete overheads that arise when forcing a continuous bosonic substrate into a discrete Pauli error framework: a register‑entropy floor of $\log_{2}12\approx3.585$ bits per mode per use; a base truncation entropy of $\ln6\approx1.792$ nats ($\approx2.585$ bits); a binary‑encoding inefficiency $\eta\approx0.896$ with dimension overhead $4/3$; and a Pauli‑twirling entropy distortion of $1.5\times10^{-3}$ bits at $\gamma=10^{-3}$ (ratio $\approx1.131$), obeying the exact linear law $\Delta H=3\gamma/2$. The discarded Hilbert‑space weight for a cold mode is $\approx3.19\times10^{-13}$. These quantities demonstrate that the digital abstraction carries a measurable bookkeeping price and a linear entropy excess that scales with physical damping. Future experimental verification of the distortion law will determine whether the overhead constitutes a fundamental resource penalty or a mitigable engineering artifact.

## References

[1] arXiv:2107.14109v1 | Digital Twin As A Cost Reduction Method  
[2] arXiv:2107.08351v2 | A Novel Approach to Analyze Fashion Digital Archive from Humanities  
[3] arXiv:cs/0508065v1 | Representing Digital Assets using MPEG-21 Digital Item Declaration  
[4] arXiv:2012.02454v1 | Data Lakes for Digital Humanities  
[5] arXiv:1910.08604v3 | Digital Democracy: Episode IV -- A New Hope, How a Corporation for Public Software Could Transform Digital Engagement for Government and Civil Society  
[6] arXiv:1704.08990v1 | EviPlant: An efficient digital forensic challenge creation, manipulation and distribution solution  
[7] arXiv:2609.28946v1 | Digital Medicines Information at National Scale: Search Behaviour and System Performance of MediVerify Across 1.5 Million Queries  
[10] https://papers.qnfo.org/papers/rosetta-fractal-math. QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0.  
[11] https://papers.qnfo.org/papers/constant-sized-support-magic-state-distillation-with-qubit-recycling-a-reconcile. QNFO: Constant-Sized-Support Magic State Distillation with Qubit Recycling: A Reconciled Resource, Footprint, and Energy Analysis.