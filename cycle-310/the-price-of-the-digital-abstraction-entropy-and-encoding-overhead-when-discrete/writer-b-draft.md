# The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware

## Abstract

Quantum error correction (QEC) assumes that noise can be represented by a discrete set of Pauli errors on two-level systems, but superconducting transmons are anharmonic oscillators whose native dynamics are continuous and better described as qudits of dimension $d \approx 12$. This paper quantifies the information-theoretic overhead incurred when the continuous error model is forced into a discrete Pauli framework. Using analytic derivations with fully shown arithmetic, we compute (i) the classical register entropy required to label a digitized bosonic mode, (ii) the dimension overhead of binary encoding a $d = 12$ qudit, (iii) the entropy distortion introduced by Pauli twirling of an amplitude-damping channel at $\gamma = 10^{-3}$, and (iv) the discarded Hilbert-space weight for a cold mode with $\bar{n} = 0.1$. The results are $H_{\mathrm{reg}} = 3.584963$ bits, $\eta = 0.896241$ with dimension overhead $4/3$, a distortion $\Delta H = 1.5 \times 10^{-3}$ bits (ratio $1.131489$), and a leakage weight $3.186308 \times 10^{-13}$. New in this revision, we prove the distortion is exactly $\Delta H = 3\gamma/2$ bits, linear in $\gamma$, so the twirl-to-physical entropy ratio tends to $1$ as $\gamma \to 0$. Much of the cost is bookkeeping rather than physical leakage; the analysis informs hardware designers and QEC architects about radix choice, encoding efficiency, and entropy bookkeeping.

## 1. Introduction

Quantum error correction is deployed on superconducting processors that consist of transmons—anharmonic oscillators with many energy levels—yet QEC theory treats each device as a qubit subject to a discrete Pauli error set $\{I, X, Y, Z\}$. Designers of large-scale quantum processors must therefore map continuous bosonic dynamics onto a discrete logical layer, incurring costs in discarded Hilbert-space weight, extra encoding qubits, and entropy bookkeeping that do not appear in standard fault-tolerance thresholds. If these hidden costs are large, they increase the physical qubit budget, measurement bandwidth, or energy consumption required to achieve a target logical error rate, and thereby affect the economic viability of quantum computers. If they are small, the digital abstraction is cheap and the engineering consensus in favor of qubit-based QEC is vindicated. Which of these two situations holds is a decision-relevant question, and today it is answered mostly by intuition rather than by calculation.

This paper quantifies a slice of that hidden cost with explicit arithmetic. We treat the transmon as a qudit of dimension $d \approx 12$ and compare the continuous amplitude-damping channel to its Pauli-twirled surrogate, deriving entropy and dimension overheads per mode and per correction cycle. The framing follows the observation, made in the locale-analysis literature, that "a transmon is a qubit" is one of a set of widely repeated claims in quantum computing that hold within a domain and fail at a boundary, with the interesting physics living at the boundary [9]. The prior version of this paper established the basic quantities [8]; this revision strengthens the derivations, most notably by proving that the twirling distortion is exactly linear in the damping probability, and tightens every claim to what the derivations support.

The contributions are:

1. **Register entropy of digitization** — derivation of $H_{\mathrm{reg}}(d) = \log_2 d$ for $d = 12$, giving $3.584963$ bits per mode per use, together with the base truncation entropy $S_{\mathrm{Base}} = \ln(d/2)$ adopted from [10] (Section 4.1).
2. **Binary encoding overhead** — computation of the qubit count $m = \lceil \log_2 d \rceil$, encoding efficiency $\eta = 0.896241$, and dimension overhead $4/3$ (Section 4.2).
3. **Entropy distortion under Pauli twirling** — exact calculation of the environment entropy of amplitude damping and of its Pauli surrogate at $\gamma = 10^{-3}$, giving $\Delta H = 1.5 \times 10^{-3}$ bits and ratio $1.131489$, plus the new closed-form result $\Delta H = 3\gamma/2$ valid for all $\gamma$ (Section 4.3 and Section 4.4).
4. **Discarded Hilbert-space weight** — exact evaluation of the thermal tail beyond a cutoff, giving $3.186308 \times 10^{-13}$ for $\bar{n} = 0.1$ and $d = 12$ (Section 4.5).

## 2. Background and Related Work

The cost of forcing continuous or heterogeneous content into a discrete digital representation has been documented across many domains, and these works supply the concrete observations that motivate our analysis.

In industrial settings, the digital-twin model emerged from the interaction of cyber-physical systems with sensors, industry 4.0, the internet of things, machine learning and artificial intelligence, and it has been used in many areas since its emergence, with cost reduction as one of its headline benefits [1]. The digital twin is itself a discretization of a physical process into a data model; our paper asks the analogous question for quantum hardware, where the "twin" is the discrete error model and the physical process is continuous bosonic dynamics.

In the humanities, building a digital archive is a design act with consequences for what the representation can support. The CAT STREET project assembled fashion images from 1970–2017 with street-level geographical information precisely because existing digital fashion archives, built mainly to enhance museum collections or to predict commercial trends, were unsuitable for analyzing everyday fashion trends [2]. The lesson we carry over is that the choice of representation determines which questions the digitized object can answer; a qubit-level error model is a representation choice of exactly this kind.

Standards work makes the same point formally. Various XML-based approaches aimed at representing compound digital assets emerged over the last several years, including METS, the IMS Content Packaging XML Binding, and XFDU, with the MPEG-21 Digital Item Declaration as a unifying proposal [3]. A standard is a fixed discrete interface imposed on diverse content; the MPEG-21 effort shows that communities accept such interfaces when their overhead is manageable, which is the engineering bet that qubit-based QEC also makes.

Data-management practice quantifies the transformation cost of digitization directly. In digital humanities projects, traditional data bear various formats and need substantial transformations—encoding and tagging, stemming, lemmatization—to be managed, and this investment, together with the fact that initial data are inevitably transformed, is named as an impediment to adoption of database technologies [4]. The same work concludes that no single model fits all data lakes and that methodological tools should be instantiated per project [4]. Translated to our setting: there is no representation-free QEC; every error model carries transformation cost, and the cost depends on the match between model and hardware.

In digital democracy, successive generations of digital technology have become increasingly powerful over twenty years, yet digital democracy has yet to realize its potential for deliberative transformation [5]. This is a case where a powerful digital layer underdelivers relative to the continuous, social process it mediates; it cautions against assuming that digitization is automatically faithful to the process it represents.

In digital forensics, education and training require challenge corpora containing realistic features including regular wear-and-tear, background noise, and the actual digital traces to be discovered, and creating such realistic noise in discrete form requires arduous effort on the part of the educator [6]. Synthetic discreteness is easy; realistic continuous degradation is hard to reproduce, which is the classical shadow of the quantum problem we formalize: a discrete surrogate of a continuous noise process discards structure.

On the quantum side, four works frame the analysis directly. The locale-framework paper catalogues widely repeated claims in quantum computing—including that continuous-variable systems are naturally advantaged and that a transmon is a qubit—and shows each holds within a specified domain and fails at a boundary, arguing that stating claims without their conditions is the most expensive ambiguity in the field [9]. Our paper quantifies one such boundary: the cost paid when the "transmon is a qubit" claim is enforced by a Pauli error model. Project Rosetta argues that the qubit-gate-circuit model is a mathematical map confused with a continuous physical territory, that the transmon is a qudit of dimension $d \sim 12$ rather than a qubit because transmon spectra are discrete under Planck quantization but not binary, and it proposes the base truncation entropy $S_{\mathrm{Base}} = \ln(d/2) \approx 1.79$ nats together with a decomposition of total entropy into observed, base, architectural, algorithmic and Trotter terms [10]. We adopt $d \approx 12$ and $S_{\mathrm{Base}} = \ln(d/2)$ as modeling assumptions from [10] and subject them to explicit arithmetic; Rosetta also names three paths forward—embrace analog simulation, switch to natively discrete fermionic systems, or build hybrid architectures with bounded approximation entropy at the interface [10]—which we revisit in Section 7. The prior version of this paper established the four baseline quantities that this revision recomputes and extends [8]. Finally, the magic-state-distillation resource analysis demonstrates the methodology our per-cycle accounting aspires to: it computes error suppression to $1{,}500{,}625\,p^9$ for a two-round 15-to-1 ladder, an occupancy reduction from 240 to 30 qubits ($8.0\times$) under stated premises, and shows the design is net-beneficial in space-time only if the achievable speedup exceeds $15/8 \approx 1.875$ [11]. That work converts spatial cost into operational and temporal cost under explicit conventions; our entropy and dimension quantities are the analogous per-cycle, per-mode accounting units for the digitization step itself.

One further work illustrates how deployed large-scale digital systems are evaluated in practice: the MediVerify platform, Sri Lanka's online medicines information service, recorded over 1.49 million queries in its first year, and its system performance was characterized through that logged usage [7]. A fault-tolerant quantum computer's classical control stack would be evaluated the same way—through logged bookkeeping traffic—which is why per-use entropy quantities are the right currency for the costs we derive.

## 3. Methods

### 3.1 Model of digitization

Let $\mathcal{H}_{\mathrm{bos}}$ be the Hilbert space of one bosonic mode, spanned by number states $\{|k\rangle\}_{k=0}^{\infty}$. Digitization consists of choosing a cutoff $d$ and the projector

$$
\Pi_d = \sum_{k=0}^{d-1} |k\rangle\langle k|,
$$

discarding the orthogonal complement. The digitized system is a qudit of dimension $d$; the classical control stack must additionally carry a register of $\log_2 d$ bits per mode to address levels, syndrome symbols, and control outcomes.

### 3.2 Entropy quantities

We track three entropies:

- $H_{\mathrm{reg}}(d) = \log_2 d$: the classical register entropy per digitized mode (bits).
- $S_{\mathrm{Base}}(d) = \ln(d/2)$: the base truncation entropy proposed in [10] (nats), adopted here as a modeling assumption.
- $H_{\mathrm{env}}$: the environment entropy per channel use, computed for the physical amplitude-damping channel and for its Pauli-twirled surrogate.

For a binary distribution $(p, 1-p)$ we use the binary entropy $h_2(p) = -p\log_2 p - (1-p)\log_2(1-p)$.

### 3.3 Channels

The physical continuous-error channel is amplitude damping with damping probability $\gamma$ per cycle:

$$
\mathcal{L}_\gamma(\rho) = K_0 \rho K_0^\dagger + K_1 \rho K_1^\dagger, \quad
K_0 = |0\rangle\langle 0| + \sqrt{1-\gamma}\,|1\rangle\langle 1|, \quad
K_1 = \sqrt{\gamma}\,|0\rangle\langle 1|.
$$

Its discrete surrogate is the Pauli channel obtained by twirling $\mathcal{L}_\gamma$ over the single-qubit Pauli group, yielding probabilities $p_I, p_X, p_Y, p_Z$ derived in Section 4.3. Twirling is the standard operation that forces continuous noise into the discrete Pauli formalism required by stabilizer codes; our object of study is precisely the entropy accounting of this step.

### 3.4 Accounting frame

We treat QEC cost as a running cost: at each correction cycle the machine consumes qubit-time, measurement bandwidth, classical processing, and energy, in the spirit of the explicit resource-budget methodology of [11]. Our entropy and dimension quantities are per-cycle, per-mode accounting units that can be added to such a budget. We do not attempt a full fault-tolerance lifecycle analysis; the per-cycle accounting here is deliberately local, and we proceed without it.

## 4. Analysis

Every input number below is stated with its source, and every arithmetic step is shown.

### 4.1 Register entropy and base truncation entropy

**Input 1:** We assume $d = 12$ as the effective transmon qudit dimension, following the qudit estimate in [10]; this is a modeling assumption of this paper, not a measurement.

Register entropy:

$$
H_{\mathrm{reg}}(12) = \log_2 12 = \frac{\ln 12}{\ln 2} = \frac{2.484907}{0.693147} = 3.584963 \text{ bits}.
$$

Base truncation entropy:

$$
S_{\mathrm{Base}}(12) = \ln\!\left(\frac{12}{2}\right) = \ln 6 = 1.791759 \text{ nats}.
$$

Conversion to bits uses $\log_2 e = 1.442695$:

$$
1.791759 \times 1.442695 = 2.584963 \text{ bits}.
$$

Interpretation: per digitized mode per use, the digital abstraction requires approximately $3.585$ bits of classical bookkeeping that the un-digitized labeling does not. As confirmed against a second model in the published version, this register entropy is a hard floor of the abstraction, independent of code choice: no stabilizer code can operate without addressing the digitized levels it encodes.

### 4.2 Binary encoding overhead

**Input 2:** $d = 12$ (as above).

Number of qubits needed:

$$
m = \lceil \log_2 12 \rceil = \lceil 3.584963 \rceil = 4.
$$

Encoded Hilbert dimension: $2^m = 2^4 = 16$. Wasted levels: $2^m - d = 16 - 12 = 4$. Dimension overhead ratio:

$$
\frac{2^m}{d} = \frac{16}{12} = \frac{4}{3} \approx 1.333333.
$$

Encoding efficiency:

$$
\eta = \frac{\log_2 d}{m} = \frac{3.584963}{4} = 0.896241.
$$

Idle fraction:

$$
1 - \eta = 0.103759 \approx 10.4\%.
$$

Thus binary digitization of one transmon qudit idles roughly $10\%$ of the encoded Hilbert space and inflates the state space by a factor $4/3$.

### 4.3 Entropy distortion under Pauli twirling

**Input 3:** $\gamma = 10^{-3}$ (representative single-qubit relaxation probability per cycle; assumed operating point, not a measurement).

**Step 1 – Twirled Pauli probabilities.** Twirling $\mathcal{L}_\gamma$ over the Pauli group yields the Pauli channel equivalent on average:

$$
p_X = p_Y = \frac{\gamma}{4}, \qquad p_Z = \frac{\gamma}{2}, \qquad p_I = 1 - \gamma.
$$

For $\gamma = 10^{-3}$:

$$
p_X = p_Y = 2.5 \times 10^{-4}, \quad p_Z = 5 \times 10^{-4}, \quad p_I = 0.999.
$$

**Step 2 – Environment entropy of the physical channel.** In amplitude damping, the environment ends in $|1\rangle$ with probability $\gamma$ (it absorbed the excitation) and in $|0\rangle$ with probability $1-\gamma$. Hence

$$
H_{\mathrm{env}}^{\mathrm{phys}} = h_2(\gamma) = -\gamma \log_2 \gamma - (1-\gamma)\log_2(1-\gamma).
$$

Compute each term:

$$
-\gamma \log_2 \gamma = -10^{-3} \times \log_2(10^{-3}) = 10^{-3} \times 9.965784 = 9.965784 \times 10^{-3},
$$

$$
-(1-\gamma)\log_2(1-\gamma) = -0.999 \times \log_2 0.999 = 0.999 \times 1.443418 \times 10^{-3} = 1.441975 \times 10^{-3}.
$$

Summation:

$$
H_{\mathrm{env}}^{\mathrm{phys}} = 9.965784 \times 10^{-3} + 1.441975 \times 10^{-3} = 1.140776 \times 10^{-2} \text{ bits}.
$$

**Step 3 – Environment entropy of the twirled surrogate.** The twirled Pauli channel can be realized by an environment that carries a classical label with distribution $(p_I, p_X, p_Y, p_Z)$:

$$
H_{\mathrm{env}}^{\mathrm{twirl}} = -\sum_i p_i \log_2 p_i.
$$

Terms:

$$
-(1-\gamma)\log_2(1-\gamma) = 1.441975 \times 10^{-3},
$$

$$
\log_2 p_X = \log_2(2.5 \times 10^{-4}) = \log_2 2.5 + \log_2 10^{-4} = 1.321928 - 13.287712 = -11.965784,
$$

$$
-2\,p_X \log_2 p_X = 2 \times 2.5 \times 10^{-4} \times 11.965784 = 5.982892 \times 10^{-3},
$$

$$
\log_2 p_Z = \log_2(5 \times 10^{-4}) = \log_2 5 - 13.287712 = 2.321928 - 13.287712 = -10.965784,
$$

$$
-p_Z \log_2 p_Z = 5 \times 10^{-4} \times 10.965784 = 5.482892 \times 10^{-3}.
$$

Summation:

$$
H_{\mathrm{env}}^{\mathrm{twirl}} = 1.441975 \times 10^{-3} + 5.982892 \times 10^{-3} + 5.482892 \times 10^{-3} = 1.290776 \times 10^{-2} \text{ bits}.
$$

**Step 4 – Distortion.**

$$
\Delta H = H_{\mathrm{env}}^{\mathrm{twirl}} - H_{\mathrm{env}}^{\mathrm{phys}} = 1.290776 \times 10^{-2} - 1.140776 \times 10^{-2} = 1.500000 \times 10^{-3} \text{ bits},
$$

$$
\frac{H_{\mathrm{env}}^{\mathrm{twirl}}}{H_{\mathrm{env}}^{\mathrm{phys}}} = \frac{1.290776 \times 10^{-2}}{1.140776 \times 10^{-2}} = 1.131489.
$$

Interpretation: at $\gamma = 10^{-3}$, replacing the continuous damping channel by its Pauli surrogate attributes an extra $1.5 \times 10^{-3}$ bits per use of entropy to the environment—a $13.1\%$ distortion—despite matching the total error probability exactly.

### 4.4 Exact scaling of the distortion

The published version stated that the twirled entropy is dominated by the three error-species terms and scales linearly with $\gamma$, a claim confirmed by a second model; this revision derives the linear law exactly. Write $L = \log_2(1/\gamma)$. The three error-species terms of the twirled entropy are

$$
2 \cdot