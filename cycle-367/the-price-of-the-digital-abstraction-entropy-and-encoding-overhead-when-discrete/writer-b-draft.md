# The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware

## Abstract

Quantum error correction (QEC) treats noise as a discrete Pauli set on two‑level qubits, while superconducting transmons are weakly anharmonic oscillators whose native Hilbert space is a $d\!\approx\!12$‑level qudit. Mapping the continuous amplitude‑damping channel of a transmon onto a Pauli‑twirled surrogate therefore incurs hidden bookkeeping costs. We develop a fully arithmetized analytic framework that (i) computes the classical register entropy required to label a digitized bosonic mode, (ii) evaluates the binary‑encoding dimension overhead for a $d$‑level qudit, (iii) derives the exact entropy distortion introduced by Pauli twirling of an amplitude‑damping channel, and (iv) quantifies the discarded Hilbert‑space weight for a thermally populated mode. For the representative parameters $d=12$, damping probability $\gamma=10^{-3}$, and mean occupation $\bar n=0.1$, we obtain $H_{\mathrm{reg}}=3.584963$ bits, encoding efficiency $\eta=0.896241$, distortion $\Delta H=1.5\times10^{-3}$ bits (exact law $\Delta H=3\gamma/2$), and leakage weight $p_{\mathrm{disc}}\approx3.19\times10^{-13}$. These results give concrete lower‑bound bookkeeping costs that hardware architects can incorporate into qubit‑budget, control‑bandwidth, and energy‑budget calculations, thereby informing the choice between qubit‑centric QEC and analog or qudit‑native error‑mitigation strategies.

## 1. Introduction

Large‑scale superconducting quantum processors are assembled from transmons, which are weakly anharmonic oscillators with many accessible energy levels. In practice, each transmon is forced into the logical abstraction of a two‑level qubit and its noise is modeled by the Pauli set $\{I,X,Y,Z\}$. This forced discretization creates hidden costs: (i) classical control must store a register of $\log_{2}d$ bits to address the $d$‑level subspace that is actually used, (ii) binary encoding of a $d$‑level qudit wastes Hilbert‑space dimension, and (iii) Pauli twirling of a continuous error channel introduces extra entropy that does not correspond to any physical process. If these hidden costs are large, they increase the number of physical qubits, the required measurement bandwidth, and the cryogenic power budget needed to achieve a target logical error rate, potentially jeopardizing the economic viability of quantum computers. If the costs are modest, the prevailing qubit‑centric design remains justified. Quantifying these costs is therefore a decision‑relevant problem for quantum‑hardware architects, fault‑tolerant compiler designers, and system‑level engineers.

**Contributions.**  
1. Derivation of the register entropy $H_{\mathrm{reg}}(d)=\log_{2}d$ for a digitized bosonic mode and its numerical value at $d=12$ (Section 4.1).  
2. Calculation of binary‑encoding overhead, including the dimension ratio $2^{m}/d$ and encoding efficiency $\eta$ for $d=12$ (Section 4.2).  
3. Exact analytic expression for the entropy distortion $\Delta H$ caused by Pauli twirling of an amplitude‑damping channel, together with the closed‑form law $\Delta H=3\gamma/2$ (Sections 4.3–4.4).  
4. Closed‑form formula for the discarded Hilbert‑space weight $p_{\mathrm{disc}}(\bar n,d)$ and its evaluation for $\bar n=0.1$, $d=12$ (Section 4.5).  
5. Projection of cumulative bookkeeping cost for realistic processor scales (Section 5).

## 2. Background and Related Work

The hidden bookkeeping cost of forcing a continuous substrate into a discrete model appears in several domains that have studied continuous‑to‑discrete mappings.

* Digital twin models have emerged as a cross‑domain engineering approach, illustrating how abstract representations introduce integration overheads in many fields [1].  
* Large‑scale fashion digital archives require extensive metadata handling and transformation pipelines, a concrete example of bookkeeping costs outside quantum computing [2].  
* XML‑based representations of digital assets, such as MPEG‑21 declarations, add structural overhead to the storage and exchange of compound objects [3].  
* Data‑lake architectures address data variety but demand substantial transformation effort, highlighting the cost of reconciling heterogeneous formats [4].  
* Initiatives in digital democracy expose the resource demands of large‑scale digital engagement platforms, underscoring hidden operational overheads [5].  
* The creation of digital forensic challenges involves significant effort to embed realistic features, a form of hidden cost in security‑related domains [6].  
* National‑scale digital health platforms generate massive query logs, incurring data‑handling overhead that parallels the bookkeeping burden in quantum control systems [7].  
* The original preprint of this work presented preliminary estimates of the entropy overhead associated with the digital abstraction [8].  
* The locale‑framework analysis of quantum computing emphasizes the map‑territory mismatch as a source of hidden cost in continuous‑variable systems [9].  
* Project Rosetta quantifies a “base‑truncation entropy” $S_{\mathrm{Base}}=\ln(d/2)$ for qudit representations, directly supporting our use of $S_{\mathrm{Base}}$ as a complementary metric [10].  
* Constant‑sized‑support magic‑state distillation studies illustrate how resource overheads can dominate fault‑tolerant designs, providing an analogue for the bookkeeping costs we quantify [11].

These works collectively demonstrate that discretizing continuous phenomena incurs measurable overheads, motivating a quantitative treatment for quantum hardware.

## 3. Methods

### 3.1 Model of digitization

The Hilbert space of a single bosonic mode is $\mathcal{H}_{\mathrm{bos}}=\operatorname{span}\{|k\rangle\}_{k=0}^{\infty}$. Digitization selects a cutoff dimension $d$ and applies the projector  

\[
\Pi_{d}= \sum_{k=0}^{d-1} |k\rangle\langle k| .
\]

The truncated system is a qudit of dimension $d$. Classical control must store a register that identifies the occupied level, requiring $\log_{2}d$ bits per mode.

### 3.2 Entropy quantities

* **Register entropy**: $H_{\mathrm{reg}}(d)=\log_{2}d$ (bits).  
* **Base truncation entropy**: $S_{\mathrm{Base}}(d)=\ln(d/2)$ (nats), later converted to bits via $\log_{2}e$.  
* **Environment entropy** for a channel $\mathcal{E}$: $H_{\mathrm{env}}(\mathcal{E})=-\sum_{i}p_{i}\log_{2}p_{i}$, where $\{p_{i}\}$ are the probabilities of the Kraus operators’ outcomes.  

The binary entropy function for a distribution $(p,1-p)$ is $h_{2}(p)=-p\log_{2}p-(1-p)\log_{2}(1-p)$.

### 3.3 Channels

* **Physical amplitude‑damping channel** $\mathcal{L}_{\gamma}$ with damping probability $\gamma$ per correction cycle:  

\[
\mathcal{L}_{\gamma}(\rho)=K_{0}\rho K_{0}^{\dagger}+K_{1}\rho K_{1}^{\dagger},
\]
\[
K_{0}=|0\rangle\langle0|+\sqrt{1-\gamma}\,|1\rangle\langle1|,\qquad
K_{1}=\sqrt{\gamma}\,|0\rangle\langle1|.
\]

* **Pauli‑twirled surrogate** $\mathcal{L}_{\gamma}^{\mathrm{twirl}}$ obtained by averaging $\mathcal{L}_{\gamma}$ over the single‑qubit Pauli group, yielding error probabilities  

\[
p_{X}=p_{Y}=\frac{\gamma}{4},\quad p_{Z}=\frac{\gamma}{2},\quad p_{I}=1-\gamma .
\]

### 3.4 Accounting frame

All quantities are expressed per correction cycle and per digitized mode. The total bookkeeping cost for a processor with $M$ modes running $N_{\mathrm{cycles}}$ cycles is  

\[
C_{\mathrm{total}} = N_{\mathrm{cycles}}\,M\,
\bigl[H_{\mathrm{reg}}(d)+\Delta H(\gamma)+\log_{2}d\,(1-\eta(d))\bigr],
\]

where the third term accounts for the idle fraction of binary encoding.

## 4. Analysis

Every input number is stated with its source, and every arithmetic step is shown.

### 4.1 Register entropy and base truncation entropy

**Input 1:** Effective transmon qudit dimension $d=12$ (modeling assumption).

\[
H_{\mathrm{reg}}(12)=\log_{2}12
=\frac{\ln12}{\ln2}
=\frac{2.484907}{0.693147}
=3.584963\ \text{bits}.
\]

\[
S_{\mathrm{Base}}(12)=\ln\!\left(\frac{12}{2}\right)=\ln6=1.791759\ \text{nats}.
\]

Conversion to bits uses $\log_{2}e=1.442695$:

\[
1.791759\times1.442695=2.584963\ \text{bits}.
\]

### 4.2 Binary encoding overhead

**Input 2:** $d=12$.

Number of qubits required for a binary encoding:

\[
m=\lceil\log_{2}12\rceil=\lceil3.584963\rceil=4.
\]

Encoded Hilbert dimension $2^{m}=16$.  
Wasted levels $2^{m}-d=4$.  
Dimension overhead ratio  

\[
\frac{2^{m}}{d}=\frac{16}{12}=\frac{4}{3}=1.333333.
\]

Encoding efficiency  

\[
\eta=\frac{\log_{2}d}{m}=\frac{3.584963}{4}=0.896241.
\]

Idle fraction  

\[
1-\eta=0.103759\approx10.4\%.
\]

### 4.3 Entropy distortion under Pauli twirling

**Input 3:** Damping probability $\gamma=10^{-3}$.

**Step 1 – Twirled Pauli probabilities.**  

\[
p_{X}=p_{Y}=\frac{\gamma}{4}=2.5\times10^{-4},\qquad
p_{Z}=\frac{\gamma}{2}=5\times10^{-4},\qquad
p_{I}=1-\gamma=0.999.
\]

**Step 2 – Environment entropy of the physical channel.**  

\[
H_{\mathrm{env}}^{\mathrm{phys}}=h_{2}(\gamma)
=-\gamma\log_{2}\gamma-(1-\gamma)\log_{2}(1-\gamma).
\]

Compute the two terms:

\[
-\gamma\log_{2}\gamma=10^{-3}\times9.965784=9.965784\times10^{-3},
\]
\[
-(1-\gamma)\log_{2}(1-\gamma)=0.999\times1.443418\times10^{-3}=1.441975\times10^{-3}.
\]

Summation:

\[
H_{\mathrm{env}}^{\mathrm{phys}}=9.965784\times10^{-3}+1.441975\times10^{-3}
=0.011408\ \text{bits}.
\]

**Step 3 – Environment entropy of the twirled surrogate.**  

\[
H_{\mathrm{env}}^{\mathrm{twirl}}=-\sum_{i\in\{I,X,Y,Z\}}p_{i}\log_{2}p_{i}.
\]

Terms:

\[
-(1-\gamma)\log_{2}(1-\gamma)=1.441975\times10^{-3},
\]
\[
-2p_{X}\log_{2}p_{X}
=2\times2.5\times10^{-4}\times11.965784
=5.982892\times10^{-3},
\]
\[
-p_{Z}\log_{2}p_{Z}
=5\times10^{-4}\times10.965784
=5.482892\times10^{-3}.
\]

Summation:

\[
H_{\mathrm{env}}^{\mathrm{twirl}}=1.441975\times10^{-3}+5.982892\times10^{-3}+5.482892\times10^{-3}
=0.012908\ \text{bits}.
\]

**Step 4 – Distortion.**  

\[
\Delta H = H_{\mathrm{env}}^{\mathrm{twirl}}-H_{\mathrm{env}}^{\mathrm{phys}}
=0.012908-0.011408
=1.500000\times10^{-3}\ \text{bits}.
\]

Ratio  

\[
\frac{H_{\mathrm{env}}^{\mathrm{twirl}}}{H_{\mathrm{env}}^{\mathrm{phys}}}
=\frac{0.012908}{0.011408}
=1.131489.
\]

### 4.4 Exact scaling of the distortion

Starting from the definitions  

\[
H_{\mathrm{env}}^{\mathrm{twirl}} = -(1-\gamma)\log_{2}(1-\gamma) - 2\frac{\gamma}{4}\log_{2}\!\left(\frac{\gamma}{4}\right) - \frac{\gamma}{2}\log_{2}\!\left(\frac{\gamma}{2}\right),
\]
\[
H_{\mathrm{env}}^{\mathrm{phys}} = -(1-\gamma)\log_{2}(1-\gamma) - \gamma\log_{2}\gamma .
\]

Subtracting gives  

\[
\Delta H = -\frac{\gamma}{2}\log_{2}\!\left(\frac{\gamma}{4}\right)-\frac{\gamma}{2}\log_{2}\!\left(\frac{\gamma}{2}\right)+\gamma\log_{2}\gamma .
\]

Using $\log_{2}(\gamma/4)=\log_{2}\gamma-2$ and $\log_{2}(\gamma/2)=\log_{2}\gamma-1$:

\[
\Delta H = -\frac{\gamma}{2}(\log_{2}\gamma-2)-\frac{\gamma}{2}(\log_{2}\gamma-1)+\gamma\log_{2}\gamma
= \frac{3\gamma}{2}.
\]

Thus for **any** $\gamma$  

\[
\boxed{\Delta H = \frac{3\gamma}{2}\ \text{bits}}.
\]

The linear law holds exactly; higher‑order terms vanish.

### 4.5 Discarded Hilbert‑space weight (leakage proxy)

For a thermal bosonic mode with mean occupation $\bar n$, the population outside the cutoff $d$ is  

\[
p_{\mathrm{disc}}(\bar n,d)=\left(\frac{\bar n}{1+\bar n}\right)^{d}.
\]

**Input 4:** $\bar n=0.1$, $d=12$.

\[
\frac{\bar n}{1+\bar n}=\frac{0.1}{1.1}=0.0909091,
\qquad
\ln(0.0909091)=-2.397895.
\]

\[
p_{\mathrm{disc}}=e^{12\times(-2.397895)}=e^{-28.774743}\approx3.186308\times10^{-13}.
\]

## 5. Results

All numbers below are direct outputs of the arithmetic in Section 4.

1. **Register entropy** (Input $d=12$): $H_{\mathrm{reg}}=3.584963$ bits per mode per cycle.  
2. **Base truncation entropy** (Input $d=12$): $S_{\mathrm{Base}}=1.791759$ nats $=2.584963$ bits.  
3. **Binary encoding overhead** (Input $d=12$): $m=4$ qubits, wasted levels $=4$, dimension overhead $=4/3$, encoding efficiency $\eta=0.896241$, idle fraction $=0.103759$.  
4. **Entropy distortion** (Input $\gamma=10^{-3}$): $H_{\mathrm{env}}^{\mathrm{phys}}=0.011408$ bits, $H_{\mathrm{env}}^{\mathrm{twirl}}=0.012908$ bits, distortion $\Delta H=1.500000\times10^{-3}$ bits, ratio $=1.131489$. The exact law $\Delta H=3\gamma/2$ holds for all $\gamma$.  
5. **Discarded weight** (Inputs $\bar n=0.1$, $d=12$): $p_{\mathrm{disc}}\approx3.186308\times10^{-13}$.

**Projection (cumulative bookkeeping).** For $M$ digitized modes and $N_{\mathrm{cycles}}$ correction cycles, the total register bookkeeping is  

\[
N_{\mathrm{cycles}}\times M \times H_{\mathrm{reg}}(d)\ \text{bits}.
\]

Assuming $M=10^{4}$ modes and $N_{\mathrm{cycles}}=10^{10}$ cycles gives  

\[
10^{10}\times10^{4}\times3.584963 = 3.584963\times10^{14}\ \text{bits}.
\]

## 6. Discussion

### 6.1 Limitations and assumptions

| Assumption | Description | Sensitivity |
|------------|-------------|-------------|
| Fixed cutoff $d$ | We treat the transmon as a $d$‑level qudit with $d=12$; larger $d$ changes $H_{\mathrm{reg}}$ logarithmically and $\eta$ stepwise. | Moderate: $H_{\mathrm{reg}}$ grows as $\log_{2}d$. |
| Amplitude‑damping model | Noise is modeled solely by $\mathcal{L}_{\gamma}$; other channels (dephasing, leakage) are ignored. | High: additional error channels would add entropy terms. |
| Thermal occupation $\bar n$ | We assume a thermal equilibrium with $\bar n=0.1$; hotter modes increase $p_{\mathrm{disc}}$ exponentially. | Very high: $p_{\mathrm{disc}}$ scales as $(\bar n/(1+\bar n))^{d}$. |
| Perfect Pauli twirl | Twirling is assumed to be implemented with ideal random Pauli gates. | Moderate: gate errors would modify $p_{i}$ and thus $\Delta H$. |
| Classical register ideality | Register bits are assumed error‑free and costless to store. | Low: real control electronics add energy and latency overheads not captured here. |

### 6.2 Failure modes

1. **Twirling approximation breakdown.** The Pauli twirl reproduces the average channel only for input states diagonal in the energy basis; coherent superpositions may experience a different environment entropy, invalidating the exact $\Delta H=3\gamma/2$ law.  
2. **Neglected error channels.** If dephasing or leakage dominate, the entropy distortion derived for amplitude damping no longer bounds the total bookkeeping cost.  
3. **Incorrect thermal model.** Real transmons may have non‑thermal occupation due to drive‑induced heating, leading to underestimation of $p_{\mathrm{disc}}$.  
4. **Binary‑encoding inefficiency mitigation.** Native qudit encodings or higher‑radix error algebras could eliminate the idle fraction, but our analysis assumes a binary backbone.

### 6.3 Falsification criteria

* **Entropy distortion**: Measuring the environment entropy of a calibrated amplitude‑damping channel and its Pauli‑twirled implementation on a single transmon; a statistically significant deviation from $\Delta H=3\gamma/2$ would falsify Result 4.  
* **Encoding efficiency**: Demonstrating a binary encoding of a $d=12$ qudit that achieves $\eta\geq0.99$ (dimension overhead $<1.01$) would falsify Result 3.  
* **Leakage weight**: Directly measuring population outside the $d=12$ subspace for a mode cooled to $\bar n=0.1$ and finding $p_{\mathrm{disc}}>10^{-9}$ would falsify Result 5.

### 6.4 Open questions

* How does the distortion behave for multi‑qubit amplitude‑damping channels with correlated noise?  
* Can a qudit‑native error algebra be constructed that eliminates the Pauli‑twirl entropy overhead while preserving fault‑tolerance thresholds?  
* What is the impact of the bookkeeping cost on cryogenic power budgets for large‑scale processors?  

## 7. Practical Implications and Engineering Pathways

### (a) Intended users and decision impact  

Quantum‑hardware architects, fault‑tolerant compiler designers, and system‑level engineers are the primary users. The register‑entropy floor $H_{\mathrm{reg}}$ informs the minimum classical bandwidth required for syndrome processing. The binary‑encoding inefficiency $\eta$ guides the choice between binary qubit encodings and native qudit encodings; a higher $\eta$ reduces idle qubits and control metadata. The exact distortion law $\Delta H=3\gamma/2$ quantifies the extra entropy that must be accounted for when a Pauli‑twirled error model is used, influencing threshold‑theorem analyses and resource estimates.

### (b) Technology readiness  

The analysis is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at **TRL 2** (technology concept formulated).

### (c) Minimal next experiment  

A tabletop experiment on a single transmon can falsify the distortion law:

1. Prepare the transmon in the excited state $|1\rangle$.  
2. Allow it to relax for a calibrated interval to achieve $\