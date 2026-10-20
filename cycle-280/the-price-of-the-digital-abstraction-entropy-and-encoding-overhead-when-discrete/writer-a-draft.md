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

* **[1]** reports that digital‑twin models are employed as cost‑reduction methods in cyber‑physical systems, illustrating that a discrete surrogate can lower operational expenses but also introduces abstraction overhead.  
* **[2]** shows that digitizing fashion archives requires selection and encoding choices, an analogue of truncating a bosonic mode to a finite $d$.  
* **[3]** describes XML‑based standards (METS, IMS, XFDU) for representing compound digital assets, demonstrating that the choice of discrete representation format is consequential enough to be standardized.  
* **[4]** notes that integrating AI and machine learning into digital forensics is transformative yet nascent, highlighting that new discrete toolchains can reshape existing continuous investigative processes.  
* **[5]** proposes data‑lake architectures to overcome data‑siloing and variety problems, emphasizing that consolidating heterogeneous continuous data into a discrete storage layer incurs engineering effort.  
* **[6]** argues that digital democracy has not yet realized its potential for deliberative transformation, a case where a digital abstraction underdelivers relative to the underlying social process.  
* **[7]** points out that realistic digital‑forensic challenges must embed wear‑and‑tear, background noise, and actual digital traces, illustrating the difficulty of synthesizing realistic discrete noise.  
* **[8]** records that the MediVerify platform handled over 1.49 million queries in its first year, showing that large‑scale digital services must manage massive discrete request streams.  

Quantum‑specific framing is drawn from the QNFO corpus:

* **[9]** enumerates recurring claims in quantum computing, including the belief that continuous‑variable systems enjoy a natural advantage, which our work interrogates from the opposite direction.  
* **[10]** states that a transmon is better modeled as a qudit with $d\approx12$ and defines the base truncation entropy $S_{\mathrm{Base}}=\ln(d/2)\approx1.79$ nats, providing the key parameters for our digitization analysis.  
* **[12]** demonstrates that active QEC continuously consumes physical resources (qubits, measurement bandwidth, classical processing, energy), establishing the resource‑axis perspective that we complement with an information‑axis analysis.

## 3. Methods

### 3.1 Model of digitization

Let $\mathcal{H}_{\mathrm{bos}}$ be the Hilbert space of a single bosonic mode, spanned by number states $\{|k\rangle\}_{k=0}^{\infty}$. Digitization selects a cutoff $d$ and applies the projector  

$$
\Pi_d = \sum_{k=0}^{d-1} |k\rangle\langle k|,
$$  

discarding the orthogonal complement. The resulting system is a $d$‑dimensional qudit. Classical control must store a register of $\log_2 d$ bits per mode to address the retained levels.

### 3.2 Entropy quantities

We define three entropies:

* $H_{\mathrm{reg}}(d)=\log_2 d$ (bits) – classical register entropy per digitized mode.  
* $S_{\mathrm{Base}}(d)=\ln(d/2)$ (nats) – base truncation entropy as proposed in [10].  
* $H_{\mathrm{env}}$ – environment entropy per channel use, computed for the physical amplitude‑damping channel and for its Pauli‑twirled surrogate.

For a binary distribution $(p,1-p)$ we use the binary entropy $h_2(p)=-p\log_2 p-(1-p)\log_2(1-p)$.

### 3.3 Channels

The physical continuous‑error channel is amplitude damping with rate $\gamma$:

$$
\mathcal{L}_\gamma(\rho)=K_0\rho K_0^\dagger+K_1\rho K_1^\dagger,\qquad
K_0=|0\rangle\langle0|+\sqrt{1-\gamma}\,|1\rangle\langle1|,\qquad
K_1=\sqrt{\gamma}\,|0\rangle\langle1|.
$$

Pauli twirling $\mathcal{L}_\gamma$ over the single‑qubit Pauli group yields a Pauli channel with probabilities $p_I, p_X, p_Y, p_Z$ derived in Section 4.3.

### 3.4 Accounting frame

Following [12] we treat QEC cost as a per‑cycle running cost. Entropy and dimension quantities are expressed per‑cycle, per‑mode, and can be added to a broader resource budget. No full fault‑tolerance lifecycle analysis is attempted.

## 4. Analysis

All input numbers are stated with their source, and every arithmetic step is shown.

### 4.1 Register entropy and base truncation entropy

**Input 1:** $d=12$ (from [10]).

Register entropy:

$$
H_{\mathrm{reg}}(12)=\log_2 12=\frac{\ln 12}{\ln 2}
=\frac{2.484907}{0.693147}=3.584963\ \text{bits}.
$$

Base truncation entropy (definition from [10]):

$$
S_{\mathrm{Base}}(12)=\ln\!\left(\frac{12}{2}\right)=\ln 6=1.791759\ \text{nats}.
$$

Conversion to bits: $1.791759\times\log_2 e=1.791759\times1.442695=2.584963$ bits, consistent with $\log_2 6$.

### 4.2 Binary encoding overhead

**Input 2:** $d=12$ (from [10]).

Number of qubits required:

$$
m=\lceil\log_2 12\rceil=\lceil3.584963\rceil=4.
$$

Encoded Hilbert dimension: $2^m=16$. Wasted levels: $2^m-d=4$. Dimension overhead ratio:

$$
\frac{2^m}{d}=\frac{16}{12}=\frac{4}{3}=1.333333.
$$

Encoding efficiency:

$$
\eta=\frac{\log_2 d}{m}=\frac{3.584963}{4}=0.896241.
$$

Idle fraction $=1-\eta=0.103759$ (≈10.4 %).

### 4.3 Entropy distortion under Pauli twirling

**Input 3:** $\gamma=10^{-3}$ (assumed operating point).

**Step 1 – Twirled Pauli probabilities.** Twirling yields  

$$
p_X=p_Y=\frac{\gamma}{4}=2.5\times10^{-4},\qquad
p_Z=\frac{\gamma}{2}=5\times10^{-4},\qquad
p_I=1-\gamma=0.999.
$$

**Step 2 – Environment entropy of the physical channel.**  

$$
H_{\mathrm{env}}^{\mathrm{phys}}=h_2(\gamma)
=-\gamma\log_2\gamma-(1-\gamma)\log_2(1-\gamma).
$$

Compute:

\[
-\gamma\log_2\gamma= -10^{-3}\times\log_2(10^{-3})
=10^{-3}\times9.965784=9.965784\times10^{-3},
\]

\[
-(1-\gamma)\log_2(1-\gamma)= -0.999\times\log_2 0.999
=0.999\times1.443418\times10^{-3}=1.441975\times10^{-3}.
\]

Thus  

$$
H_{\mathrm{env}}^{\mathrm{phys}}=9.965784\times10^{-3}+1.441975\times10^{-3}
=1.140776\times10^{-2}\ \text{bits}.
$$

**Step 3 – Environment entropy of the twirled surrogate.**  

$$
H_{\mathrm{env}}^{\mathrm{twirl}}=-\sum_{i}p_i\log_2 p_i.
$$

Terms:

\[
-(1-\gamma)\log_2(1-\gamma)=1.441975\times10^{-3},
\]

\[
-2p_X\log_2 p_X=2\times2.5\times10^{-4}\times11.965784=5.982892\times10^{-3},
\]

\[
-p_Z\log_2 p_Z=5\times10^{-4}\times10.965784=5.482892\times10^{-3}.
\]

Summing:

$$
H_{\mathrm{env}}^{\mathrm{twirl}}=1.441975\times10^{-3}+5.982892\times10^{-3}+5.482892\times10^{-3}
=1.290776\times10^{-2}\ \text{bits}.
$$

**Distortion:**  

$$
\Delta H=H_{\mathrm{env}}^{\mathrm{twirl}}-H_{\mathrm{env}}^{\mathrm{phys}}
=1.290776\times10^{-2}-1.140776\times10^{-2}=1.500000\times10^{-3}\ \text{bits},
$$

$$
\frac{H_{\mathrm{env}}^{\mathrm{twirl}}}{H_{\mathrm{env}}^{\mathrm{phys}}}
=\frac{1.290776\times10^{-2}}{1.140776\times10^{-2}}=1.131489.
$$

Thus the Pauli surrogate overstates environment entropy by $13.1\%$ while matching total error probability $\gamma$.

### 4.4 Scaling of the distortion

For small $\gamma$, $h_2(\gamma)\approx\gamma\log_2(1/\gamma)+\gamma/\ln2$. The twirled entropy contains additional terms proportional to $\gamma\log_2(1/\gamma)$ from the three error species. The ratio $H_{\mathrm{env}}^{\mathrm{twirl}}/H_{\mathrm{env}}^{\mathrm{phys}}$ is a function of $\gamma$ alone; at $\gamma=10^{-3}$ it equals $1.131489$. The behavior as $\gamma\to0$ is left as an open question (see Section 6).

### 4.5 Discarded Hilbert‑space weight (leakage proxy)

For a thermal bosonic mode with mean occupation $\bar n$ the population beyond cutoff $d$ is  

$$
p_{\mathrm{disc}}(\bar n,d)=\left(\frac{\bar n}{1+\bar n}\right)^{d}.
$$

**Input 4:** $\bar n=0.1$ (assumed), $d=12$ (from [10]).

\[
\frac{\bar n}{1+\bar n}=\frac{0.1}{1.1}=0.0909091,\qquad
\ln(0.0909091)=-2.397895.
\]

\[
p_{\mathrm{disc}}=e^{12\times(-2.397895)}=e^{-28.774743}\approx3.20\times10^{-13}.
$$

The discarded weight is negligible at this operating point.

## 5. Results

All quantities below are derived in Section 4.

1. **Register entropy** $H_{\mathrm{reg}}(12)=3.584963$ bits per mode per use.  
2. **Base truncation entropy** $S_{\mathrm{Base}}(12)=1.791759$ nats $=2.584963$ bits.  
3. **Binary encoding overhead**: $m=4$ qubits, wasted levels $=4$, dimension overhead $=1.333333$, efficiency $\eta=0.896241$, idle fraction $=0.103759$.  
4. **Entropy distortion**: $H_{\mathrm{env}}^{\mathrm{phys}}=1.140776\times10^{-2}$ bits, $H_{\mathrm{env}}^{\mathrm{twirl}}=1.290776\times10^{-2}$ bits, $\Delta H=1.5\times10^{-3}$ bits, ratio $=1.131489$.  
5. **Discarded weight** $p_{\mathrm{disc}}\approx3.20\times10^{-13}$.

**Projection (cumulative bookkeeping).** For $M$ digitized modes operated over $N_{\mathrm{cycles}}$ correction cycles, the total register entropy is  

$$
H_{\mathrm{total}}=N_{\mathrm{cycles}}\times M\times H_{\mathrm{reg}}(12).
$$

Assuming $M=1000$ and $N_{\mathrm{cycles}}=10^{9}$ (illustrative values),  

$$
H_{\mathrm{total}}=10^{9}\times1000\times3.584963=3.584963\times10^{12}\ \text{bits}.
$$

This projection follows from the derived $H_{\mathrm{reg}}$ and the assumed $M$, $N_{\mathrm{cycles}}$.

## 6. Discussion

### What we have shown

We derived exact entropy and dimension overheads for idealized single‑mode and single‑qubit channels. The analysis isolates bookkeeping costs that arise solely from imposing a discrete Pauli algebra on continuous dynamics.

### Strongest counter‑argument

Entry [10] corrects the premise that the transmon spectrum is continuous: it is intrinsically discrete (a qudit with $d\approx12$), and binary truncation is a radix error rather than a physics error. Consequently, the “continuity” cost we quantify partly reflects an inefficient radix choice. A $d$‑ary error algebra could eliminate the binary‑encoding inefficiency ($\eta\to1$, overhead $\to1$). Nonetheless, the entropy‑distortion result (Result 4) persists because it stems from the mismatch between the physical amplitude‑damping process and any *binary* Pauli algebra, not from the discreteness of the spectrum itself.

### Failure modes of the derivation

1. **Twirling equivalence** holds only for input states diagonal in the energy basis; coherent superpositions may experience additional discrepancies.  
2. **Environment model** assumes a classical label for the Pauli surrogate; a fully quantum environment could yield different entropy.  
3. **Assumed parameters** ($\gamma=10^{-3}$, $\bar n=0.1$) are illustrative; real devices may operate at different values, altering the distortion ratio.  
4. **Register entropy** is a lower bound; actual control stacks may store additional metadata, increasing the true bookkeeping load.

### Falsifiability

*If* a quantum‑process‑tomography experiment demonstrated that the environment entropy of the physical amplitude‑damping channel equals that of its Pauli‑twirled surrogate (within experimental uncertainty), then Result 4 would be falsified.  
*If* a binary encoding of a $d=12$ qudit achieved $\eta\ge0.99$ without discarding levels, Result 3 would be falsified.  
*If* measurements of a cold transmon mode revealed a discarded population $>10^{-9}$, Result 5 would be falsified.

### Open questions

* How does the distortion ratio behave for experimentally measured damping rates (e.g., $\gamma\sim10^{-4}$)?  
* Can a $d$‑ary Pauli‑like error algebra be constructed that preserves environment entropy?  
* Does the cumulative register entropy translate into measurable overheads in measurement bandwidth or classical processing power, linking the information‑axis view to the resource‑axis analysis of [12]?

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.** Quantum hardware architects and QEC code designers can use the derived overheads to evaluate whether a binary qubit‑centric stack is optimal for a given transmon platform. If the cumulative register entropy or binary‑encoding inefficiency dominates the resource budget, designers may opt for native qudit encodings or $d$‑ary error models, thereby reducing the number of physical qubits and control bandwidth required.

**(b) Technology readiness.** The present work is a purely analytical study that has not undergone peer review; according to NASA’s scale it resides at TRL 2 (concept formulation).

**(c) Minimal de‑risking experiment.** A feasible next step is a quantum‑process‑tomography experiment on a single transmon: (i) prepare the transmon in the ground state, (ii) apply a calibrated amplitude‑damping channel with known $\gamma$, (iii) perform Pauli twirling by random Pauli pre‑ and post‑rotations, and (iv) reconstruct the environment’s classical label distribution to compute $H_{\mathrm{env}}^{\mathrm{twirl}}$. Observation that $H_{\mathrm{env}}^{\mathrm{twirl}}$ exceeds $H_{\mathrm{env}}^{\mathrm{phys}}$ by the predicted $1.5\times10^{-3}$ bits would confirm the analysis; a match within experimental error would falsify Result 4.

**(d) Engineering constraints.** The experiment requires (i) high‑fidelity single‑qubit gates for Pauli randomization, (ii) accurate calibration of $\gamma$, (iii) sufficient measurement repetitions to resolve entropy differences at the $10^{-3}$‑bit level, and (iv) low‑temperature cryogenic infrastructure to maintain $\bar n\approx0.1$. These constraints are intrinsic to any precise QEC benchmarking effort.

**(e) Projected cost/performance bounds (projection).** Assuming a processor with $M=10^4$ transmon qudits operating at $N_{\mathrm{cycles}}=10^{8}$ error‑correction cycles, the cumulative register entropy projection is  

$$
H_{\mathrm{total}}=10^{8}\times10^{4}\times3.584963=3.584963\times10^{12}\ \text{bits}.
$$  

If each bit of classical bookkeeping consumes $10^{-12}$ J of control energy (a conservative estimate based on typical digital control electronics), the projected energy overhead is $3.6$ J over the full runtime.

**(f) Risks and misuse.** Over‑interpreting the bookkeeping entropy as a direct physical energy cost could lead to over‑design of hardware, inflating system size without commensurate benefit. Conversely, neglecting the entropy distortion when selecting error models may cause underestimation of required syndrome‑processing bandwidth, potentially compromising fault‑tolerance margins.

## 8. Conclusion

We have quantified, with fully shown arithmetic, four faces of the cost of imposing a digital abstraction on bosonic quantum hardware: (i) a register‑entropy floor of $3.584963$ bits per digitized mode per use, (ii) a base truncation entropy of $1.791759$ nats ($2.584963$ bits) as defined in [10], (iii) a binary‑encoding inefficiency $\eta=0.896241$ with dimension overhead $4/3$, and (iv) a Pauli‑twirling entropy distortion of $1.5\times10^{-3}$ bits per use (ratio $1.131489$) at $\gamma=10^{-3}$. A negative result bounds discarded leakage weight at $\approx3.20\times10^{-13}$ for cold modes. These quantities support the conjecture that the digital abstraction carries a measurable, computable price. The Rosetta correction in [10] tempers the claim by showing that much of the overhead stems from a radix mismatch rather than a fundamental clash with physics. Distinguishing these interpretations motivates the experimental test outlined in Section 7.

## References

[1] arXiv:2107.14109v1 | Digital Twin As A Cost Reduction Method  
[2] arXiv:2107.08351v2 | A Novel Approach to Analyze Fashion Digital Archive from Humanities  
[3] arXiv:cs/0508065v1 | Representing Digital Assets using MPEG-21 Digital Item Declaration  
[4] arXiv:2012.02454v1 | Data Lakes for Digital Humanities  
[5] arXiv:1910.08604v3 | Digital Democracy: Episode IV -- A New Hope, How a Corporation for Public Software Could Transform Digital Engagement for Government and Civil Society  
[6] arXiv:1704.08990v1 | EviPlant: An efficient digital forensic challenge creation, manipulation and distribution solution  
[7] arXiv:2609.28946v1 | Digital Medicines Information at National Scale: Search Behaviour and System Performance of MediVerify Across 1.5 Million Queries  
[8] QNFO: The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware  
[9] QNFO: Locale Framework Applied to Quantum Computing Innovations & Practical Applications  
[10] QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0  
[11] QNFO: Lifecycle of a Fault-Tolerant Quantum Computer  
[12] QNFO: The Resource Burden of Active Quantum Error Correction: A Scaling Analysis of Qubit, Bandwidth, and Energy Overheads