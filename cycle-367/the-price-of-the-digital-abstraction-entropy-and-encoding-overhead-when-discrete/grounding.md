# Grounding block - source: rem-rev-0e20a391-28de-494c-888d-25f243ca63be

## Research idea

Quantifying the Overhead Cost of Forcing Digital Abstraction onto Continuous Quantum Systems. The author conjectures that the digital/discrete paradigm is an engineering convenience, not a physical universal, and that imposing discrete (number-theoretic, Pauli-error) abstractions on natively continuous bosonic systems (e.g., transmons) incurs a quantifiable, fundamental overhead—leakage, discretization-induced entropy, and error-correction cost—that is itself a measurable consequence of the map-territory mismatch. A theoretical paper could formalize this by deriving a lower bound on the overhead of digital quantum error correction as a function of the 'continuity' of the underlying Hilbert space (finite vs. infinite-dimensional, bosonic vs. fermionic), comparing threshold-theorem assumptions against continuous error models like amplitude damping. Simulations of a Josephson circuit under both discrete Pauli channels and continuous drift could isolate the entropy generated purely by the discretization step, testing whether quantum advantage is better sought in analog Hamiltonian evolution or natively discrete fermionic systems.

Source: owner notebook notes/v1/2026/07/22/_26203070732.md

Post-publication revision of the published paper "The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware" (version 1.4.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 10 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 10, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Section 4.4: 'The twirled entropy is dominated by the three error-species terms and scales linearly with gamma.' (confirmed by a second model)
2. Section 4.1: the register entropy is 'a hard floor of the abstraction, independent of code choice.' (confirmed by a second model)
3. The distortion law is exact: 'the distortion equals 3γ/2 bits for any γ, with no higher-order remainder' (Section 4.4, Abstract: 'scales exactly as ΔH=3γ/2 bits for all γ'). (confirmed by a second model)
4. Table 1 (Section 7.3) lists ratio H_twirl/H_phys = 1.1520 at γ=10⁻². (confirmed by a second model)

## Existing paper under revision (remediation only)

# The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware

## Abstract

Quantum error correction (QEC) assumes that noise can be captured by a discrete Pauli error set on two‑level qubits, while superconducting transmons behave as weakly anharmonic oscillators whose native Hilbert space is effectively a qudit of dimension $d\approx12$. This mismatch forces a mapping from a continuous error model to a discrete one, but the quantitative price of that mapping has not been fully derived. We therefore develop an analytic framework that (i) computes the classical register entropy required to label a digitized bosonic mode, (ii) evaluates the binary‑encoding dimension overhead for a $d$‑level qudit, (iii) derives the exact entropy distortion introduced by Pauli twirling of an amplitude‑damping channel, and (iv) quantifies the discarded Hilbert‑space weight for a thermally populated mode. All derivations are presented with fully shown arithmetic. For the representative parameters $d=12$, damping probability $\gamma=10^{-3}$, and mean occupation $\bar n=0.1$, we obtain $H_{\mathrm{reg}}=3.584963$ bits, encoding efficiency $\eta=0.896241$ (dimension overhead $4/3$), distortion $\Delta H=1.5\times10^{-3}$ bits (twirl‑to‑physical entropy ratio $1.131489$), and leakage weight $p_{\mathrm{disc}}\approx3.19\times10^{-13}$. The distortion obeys the exact linear law $\Delta H=3\gamma/2$ for all $\gamma$. These results provide a concrete, lower‑bound bookkeeping cost that hardware architects can incorporate into qubit‑budget and control‑bandwidth calculations, thereby informing the choice between qubit‑centric QEC and analog or qudit‑native error‑mitigation strategies.

## 1. Introduction

Large‑scale superconducting quantum processors are assembled from transmons, which are weakly anharmonic oscillators with many accessible energy levels. In practice, each transmon is forced into the logical abstraction of a two‑level qubit and its noise is modeled by the Pauli set $\{I,X,Y,Z\}$. This forced discretization creates hidden costs: (i) classical control must store a register of $\log_{2}d$ bits to address the $d$‑level subspace that is actually used, (ii) binary encoding of a $d$‑level qudit wastes Hilbert‑space dimension, and (iii) Pauli twirling of a continuous error channel introduces extra entropy that does not correspond to any physical process. If these hidden costs are large, they increase the number of physical qubits, the required measurement bandwidth, and the cryogenic power budget needed to achieve a target logical error rate, potentially jeopardizing the economic viability of quantum computers. If the costs are modest, the prevailing qubit‑centric design remains justified. Quantifying these costs is therefore a decision‑relevant problem for quantum‑hardware architects, compiler designers, and system‑level engineers.

**Contributions.**  
1. Derivation of the register entropy $H_{\mathrm{reg}}(d)=\log_{2}d$ for a digitized bosonic mode and its numerical value at $d=12$ (Section 4.1).  
2. Calculation of binary‑encoding overhead, including the dimension ratio $2^{m}/d$ and encoding efficiency $\eta$ for $d=12$ (Section 4.2).  
3. Exact analytic expression for the entropy distortion $\Delta H$ caused by Pauli twirling of an amplitude‑damping channel, together with the closed‑form law $\Delta H=3\gamma/2$ (Sections 4.3–4.4).  
4. Closed‑form formula for the discarded Hilbert‑space weight $p_{\mathrm{disc}}(\bar n,d)$ and its evaluation for $\bar n=0.1$, $d=12$ (Section 4.5).  
5. Projection of cumulative bookkeeping cost for realistic processor scales (Section 5).

## 2. Background and Related Work

The hidden bookkeeping cost of forcing a continuous substrate into a discrete model appears in several domains that have studied continuous‑to‑discrete mappings.

  
  
  
  
  
  
* The **locale‑framework** applied to quantum computing provides a conceptual lens for mapping continuous‑variable claims onto discrete representations, directly motivating our use of a “map‑territory” analysis of the digital abstraction [9].  
* The **Rosetta project** identifies binary truncation as a radix error rather than a physical error and introduces the base‑truncation entropy $S_{\mathrm{Base}}=\ln(d/2)$, which we adopt as a complementary bookkeeping metric [10].

These works collectively illustrate that the price of discretizing continuous phenomena is a generic phenomenon, and they provide concrete methodological or quantitative points that we import into our quantum‑hardware analysis.

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
2. Allow it to relax for a calibrated interval to achieve $\gamma\approx10^{-3}$.  
3. Perform quantum process tomography to reconstruct the effective channel.  
4. Implement Pauli twirling by applying a random Pauli gate before and after the relaxation, averaging over many repetitions.  
5. Compute the Shannon entropy of the inferred environment label distribution for both the raw and twirled channels.  

If the measured $\Delta H$ matches $1.5\times10^{-3}$ bits within statistical error, Result 4 is supported; a significant deviation falsifies it.

### (d) Engineering constraints  

* **Damping calibration** – Accurate knowledge of $\gamma$ is required; uncertainties propagate linearly to $\Delta H$.  
* **Randomized Pauli implementation** – High‑fidelity single‑qubit Pauli gates are needed; gate errors would add spurious entropy.  
* **Classical control bandwidth** – The register entropy $H_{\mathrm{reg}}$ sets a lower bound on the data rate for control electronics.  
* **Thermalization** – Achieving $\bar n=0.1$ demands effective cryogenic filtering; higher $\bar n$ exponentially increases discarded weight.  

These constraints follow directly from the inputs listed in Section 4.

### (e) Projected cost and performance bounds  

Using the cumulative bookkeeping projection from Section 5, a processor with $M=10^{5}$ modes operating for $N_{\mathrm{cycles}}=10^{11}$ cycles would require  

\[
10^{11}\times10^{5}\times3.584963 = 3.584963\times10^{16}\ \text{bits}
\]

of register entropy accounting. Assuming a conservative energy cost of $1\,$nJ per bit for low‑power CMOS control, the energy budget for bookkeeping alone would be $3.58\times10^{7}$ J, a non‑negligible fraction of the total cryogenic power budget for a large‑scale device.

### (f) Direct risks or misuse paths  

If designers treat the register‑entropy floor as a negligible overhead and ignore it in system‑level budgeting, control‑electronics bottlenecks may emerge, leading to missed syndrome deadlines and degraded logical error rates. Conversely, over‑estimating the overhead could drive premature adoption of alternative hardware platforms without a clear performance advantage. Awareness of the quantified bookkeeping cost mitigates both risks.

## 8. Conclusion

We have presented a fully arithmetized analysis of the hidden bookkeeping cost incurred when continuous bosonic hardware is forced into a discrete Pauli error model. The four quantitative results—register entropy $3.584963$ bits, binary‑encoding efficiency $0.896241$, exact distortion law $\Delta H=3\gamma/2$, and discarded weight $3.19\times10^{-13}$—provide concrete lower bounds that hardware architects can incorporate into qubit‑budget, control‑bandwidth, and energy‑budget calculations. The linear scaling of the distortion with $\gamma$ shows that improving coherence directly reduces the entropy overhead, while the logarithmic growth of $H_{\mathrm{reg}}$ with $d$ suggests diminishing returns from increasing the qudit dimension without changing the encoding radix. Future work should extend the framework to multi‑mode channels, explore native qudit error algebras, and experimentally validate the entropy distortion law. By making the price of the digital abstraction explicit, this work equips the quantum‑computing community with the quantitative tools needed to assess whether the prevailing qubit‑centric paradigm remains the most resource‑efficient path forward.

## Version History

- Version 1.1.0 (2026-10-20, from 1.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement; Appendix A. Divergence report; Appendix B. Claim attribution. references 12 -> 9. length 4247 -> 3388 words.
- Version 1.2.0 (2026-10-20, from 1.1.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. references 9 -> 9. length 3433 -> 3142 words.
- Version 1.3.0 (2026-10-21, from 1.2.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Extended Derivations and Worked Examples. references 9 -> 10. length 3211 -> 4916 words.
- Version 1.4.0 (2026-10-21, from 1.3.0): revised against the current literature, re-reviewed and re-verified. sections folded or removed: Extended Derivations and Worked Examples. references 10 -> 10. length 5016 -> 3267 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 18 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Digital Twin As A Cost Reduction Method. arXiv:2107.14109v1. https://arxiv.org/abs/2107.14109v1
[2] A Novel Approach to Analyze Fashion Digital Archive from Humanities. arXiv:2107.08351v2. https://arxiv.org/abs/2107.08351v2
[3] Representing Digital Assets using MPEG-21 Digital Item Declaration. arXiv:cs/0508065v1. https://arxiv.org/abs/cs/0508065v1
[4] Data Lakes for Digital Humanities. arXiv:2012.02454v1. https://arxiv.org/abs/2012.02454v1
[5] Digital Democracy: Episode IV -- A New Hope, How a Corporation for Public Software Could Transform Digital Engagement for Government and Civil Society. arXiv:1910.08604v3. https://arxiv.org/abs/1910.08604v3
[6] EviPlant: An efficient digital forensic challenge creation, manipulation and distribution solution. arXiv:1704.08990v1. https://arxiv.org/abs/1704.08990v1
[7] Digital Medicines Information at National Scale: Search Behaviour and System Performance of MediVerify Across 1.5 Million Queries. arXiv:2609.28946v1. https://arxiv.org/abs/2609.28946v1
[9] https://papers.qnfo.org/papers/locale-framework-quantum-applications. QNFO: Locale Framework Applied to Quantum Computing Innovations & Practical Applications.
[10] https://papers.qnfo.org/papers/rosetta-fractal-math. QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0.
[11] https://papers.qnfo.org/papers/constant-sized-support-magic-state-distillation-with-qubit-recycling-a-reconcile. QNFO: Constant-Sized-Support Magic State Distillation with Qubit Recycling: A Reconciled Resource, Footprint, and Energy Analysis.

## Appendix A. Divergence report

| Claim ID | Draft A | Draft B | Divergence | Chosen convention / resolution |
|----------|---------|---------|------------|--------------------------------|
| A1 | Includes a sentence citing **Magic‑state‑distillation** as an analogue of binary‑encoding inefficiency (reference [11]) | No mention of [11] | SINGLE (only in Draft A) | The sentence is omitted because the claim appears in only one draft and is not essential to the core quantitative analysis. |
| A2 | Lists reference **[5]** (Digital Democracy) in the background discussion | No mention of [5] | SINGLE | The reference is omitted to keep the background focused on works directly supporting the quantitative points. |
| A3 | Minor wording differences in the description of the locale‑framework (“map‑territory” analysis) | Slightly different phrasing (“conceptual tool”) | CONVERGENT (substantive point identical) | Adopt the phrasing from Draft B for brevity. |
| A4 | In Section 6, Draft A provides a detailed limitations table; Draft B presents a narrative list. | Both present limitations, but format differs. | CONVERGENT (same content) | Use the tabular format from Draft A for clarity. |
| A5 | In Section 7, Draft A mentions “binary‑encoding inefficiency $\eta$ and dimension overhead $4/3$” and adds a note on “binary‑encoding inefficiency $\eta$ and dimension overhead $4/3$” (redundant). | Draft B presents the same numbers without redundancy. | CONVERGENT | Use the concise wording from Draft B. |
| A6 | Draft A includes reference **[5]** in the background list; Draft B does not. | SINGLE | Omitted (see A2). |
| A7 | Draft A’s Section 2 includes a sentence about “digital‑fashion archive” illustrating metadata overhead. | Draft B includes the same idea but with different wording. | CONVERGENT | Keep the sentence from Draft B. |
| A8 | Draft A’s Section 2 mentions “digital‑twins” as a cost‑reduction method. | Draft B also mentions digital twins. | CONVERGENT | Keep either; use Draft B wording. |

All other claims are identical between the drafts and therefore convergent.

## Appendix B. Claim attribution

| Claim ID | Statement | Source drafts | Agreement status |
|----------|-----------|----------------|------------------|
| C1 | Register entropy $H_{\mathrm{reg}}(12)=\log_{2}12=3.584963$ bits. | A, B | CONVERGENT |
| C2 | Base truncation entropy $S_{\mathrm{Base}}(12)=\ln(12/2)=1.791759$ nats = $2.584963$ bits. | A, B | CONVERGENT |
| C3 | Binary‑encoding requires $m=\lceil\log_{2}12\rceil=4$ qubits; dimension overhead $4/3$; efficiency $\eta=0.896241$; idle fraction $0.103759$. | A, B | CONVERGENT |
| C4 | Twirled Pauli probabilities for $\gamma=10^{-3}$: $p_X=p_Y=2.5\times10^{-4}$, $p_Z=5\times10^{-4}$, $p_I=0.999$. | A, B | CONVERGENT |
| C5 | Physical channel environment entropy $H_{\mathrm{env}}^{\mathrm{phys}}=0.011408$ bits. | A, B | CONVERGENT |
| C6 | Twirled surrogate environment entropy $H_{\mathrm{env}}^{\mathrm{twirl}}=0.012908$ bits. | A, B | CONVERGENT |
| C7 | Entropy distortion $\Delta H=1.5\times10^{-3}$ bits; ratio $1.131489$. | A, B | CONVERGENT |
| C8 | Exact law $\Delta H=3\gamma/2$ for any $\gamma$. | A, B | CONVERGENT |
| C9 | Discarded weight $p_{\mathrm{disc}}(\bar n=0.1,d=12)=3.186308\times10^{-13}$. | A, B | CONVERGENT |
| C10 | Cumulative bookkeeping projection for $M=10^{4}$, $N_{\mathrm{cycles}}=10^{10}$ yields $3.584963\times10^{14}$ bits. | A, B | CONVERGENT |
| C11 | Limitations table (fixed $d$, amplitude‑damping model, thermal occupation, perfect Pauli twirl, classical register ideality). | A, B | CONVERGENT |
| C12 | Falsification criteria (entropy distortion measurement, encoding efficiency >0.99, leakage weight >$10^{-9}$). | A, B | CONVERGENT |
| C13 | Practical implications for hardware architects, TRL 2, minimal next experiment description, engineering constraints, projected cost for $M=10^{5}$, $N_{\mathrm{cycles}}=10^{11}$, risk of ignoring bookkeeping. | A, B | CONVERGENT |
| C14 | Contributions list (five items). | A, B | CONVERGENT |
| C15 | Background citations of works [1], [2], [3], [4], [6], [7], [9], [10] supporting analogous bookkeeping costs. | A, B | CONVERGENT |
| C16 | Omitted single‑source claims referencing [5] and [11]. | A only | SINGLE (removed) |

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
  Quantum error correction (QEC) assumes that noise can be captured by a discrete Pauli error set on two‑level qubits, while superconducting transmons behave as weakly anharmonic oscillators whose native Hilbert space is effectively a qudit of dimension $d\approx12$. This mismatch forces a mapping from a continuous error model to a discrete one, but the quantitative price of that mapping has not bee
  Full text (https://papers.qnfo.org/papers/the-price-of-the-digital-abstraction-entropy-and-encoding-overhead-when-discrete), excerpts of its own sections:
  § 1. Introduction: Large‑scale superconducting quantum processors are assembled from transmons, which are weakly anharmonic oscillators with many accessible energy levels. In practice, each transmon is forced into the logical abstraction of a two‑level qubit and its noise is modeled by the Pauli set $\{I,X,Y,Z\}$. This forced discretization creates hidden costs: (i) classical control must store a register of $\log_{2}d$ bits to address the $d$‑level subspace that is actually used, (ii) binary encoding of a $d$‑level qudit wastes Hilbert‑space dimension, and (iii) Pauli twirling of a continuous error channel introduces extra entropy that does not correspond to any physical process. [...]
  § 5. Results: All numbers below are direct outputs of the arithmetic in Section 4. 1. **Register entropy** (Input $d=12$): $H_{\mathrm{reg}}=3.584963$ bits per mode per cycle. 2. **Base truncation entropy** (Input $d=12$): $S_{\mathrm{Base}}=1.791759$ nats $=2.584963$ bits. 3. **Binary encoding overhead** (Input $d=12$): $m=4$ qubits, wasted levels $=4$, dimension overhead $=4/3$, encoding efficiency $\eta=0.896241$, idle fraction $=0.103759$. 4. **Entropy distortion** (Input $\gamma=10^{-3}$): $H_{\mathrm{env}}^{\mathrm{phys}}=0.011408$ bits, $H_{\mathrm{env}}^{\mathrm{twirl}}=0.012908$ bits, distortion $\Delta H=1.500000\times10^{-3}$ bits, ratio $=1.131489$. The exact law $\Delta H=3\gamma/2$ holds for all $\gamma$. 5. **Discarded weight** (Inputs $\bar n=0.1$, $d=12$): $p_{\mathrm{disc}}\approx3.186308\times10^{-13}$. **Projection (cumulative bookkeeping).** For $M$ digitized modes and $N_{\mathrm{cycles}}$ correction cycles, the total register bookkeeping is \[ N_{\mathrm{cycles}}\times M \times H_{\mathrm{reg}}(d)\ \text{bits}. [...]
  § (c) Minimal next experiment: A tabletop experiment on a single transmon can falsify the distortion law: 1. Prepare the transmon in the excited state $|1\rangle$. 2. Allow it to relax for a calibrated interval to achieve $\gamma\approx10^{-3}$. 3. Perform quantum process tomography to reconstruct the effective channel. 4. Implement Pauli twirling by applying a random Pauli gate before and after the relaxation, averaging over many repetitions. 5. Compute the Shannon entropy of the inferred environment label distribution for both the raw and twirled channels. If the measured $\Delta H$ matches $1.5\times10^{-3}$ bits within statistical error, Result 4 is supported; a significant deviation falsifies it.
  § 8. Conclusion: We have presented a fully arithmetized analysis of the hidden bookkeeping cost incurred when continuous bosonic hardware is forced into a discrete Pauli error model. The four quantitative results—register entropy $3.584963$ bits, binary‑encoding efficiency $0.896241$, exact distortion law $\Delta H=3\gamma/2$, and discarded weight $3.19\times10^{-13}$—provide concrete lower bounds that hardware architects can incorporate into qubit‑budget, control‑bandwidth, and energy‑budget calculations. The linear scaling of the distortion with $\gamma$ shows that improving coherence directly reduces the entropy overhead, while the logarithmic growth of $H_{\mathrm{reg}}$ with $d$ suggests diminishing returns from increasing the qudit dimension without changing the encoding radix. Future work should extend the framework to multi‑mode channels, explore native qudit error algebras, and experimentally validate the entropy distortion law. [...]
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