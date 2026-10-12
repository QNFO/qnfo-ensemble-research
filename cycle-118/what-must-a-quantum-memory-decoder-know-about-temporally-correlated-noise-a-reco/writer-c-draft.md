# What Must a Quantum-Memory Decoder Know About Temporally Correlated Noise? An Expository and Quantitative Reconstruction

## Abstract

Temporal correlations in quantum-memory noise create a calibration problem that is invisible to syndrome statistics alone. We reconstruct, in expository form, the central results of a recent study of fixed stabilizer memory experiments with known system-environment interactions [1],[2]. The study's main example uses weak coherent $X$ rotations in a class of CSS codes including Shor, Steane, and odd-distance rotated surface codes, in which all physical qubits share a sign that is either fixed throughout a run or independently redrawn each interval. The two noise models have identical syndrome statistics and the same spatiotemporal Pauli process, yet require different logical corrections at suitable storage times. We give explicit derivations of the mechanism behind the worst-case fidelity loss approaching $1/2$ for a model-agnostic decoder with full syndrome access, and of the calibration-cost scalings: a number of noise intervals proportional to the inverse rotation angle raised to the code's $X$ distance for complete quantum error-correction cycles, reduced to inverse-square scaling when two uninterrupted intervals precede one extraction. We work numerical examples for representative parameters and discuss what these results imply for decoder design, the role of Pauli twirling, and the information-theoretic cost of noise calibration in quantum memories.

## 1. Introduction

A quantum memory is only as good as its decoder, and a decoder is only as good as its noise model. When the noise acting on a stabilizer code is independent and identically distributed in time, the syndrome record carries essentially all relevant information, and standard decoding heuristics suffice. When the noise is temporally correlated — for example, when a coherent error rotates every physical qubit in the same direction over many consecutive intervals — the syndrome statistics can remain identical to those of an uncorrelated model while the optimal logical correction changes completely. This is the problem addressed in the work under study [1],[2]: for fixed stabilizer memory experiments with known system-environment interactions, what must a decoder know about temporally correlated noise, and what does it cost to learn?

The question matters practically. Quantum error-correction overhead is a dominant cost in any realistic architecture; the QNFO analysis of physical limits on computation emphasizes that overheads of $10^{2}$–$10^{3}$ physical operations per logical operation multiply the thermodynamic cost of the whole machine [13]. If calibration of temporal noise structure adds a further overhead scaling badly with code distance and inverse noise strength, this must be counted in any honest investment assessment of quantum-memory architectures [10]. Conversely, auditing claims of near-term advantage requires knowing which noise parameters a demonstrated system actually calibrated and which it assumed [12].

This paper is a reconstruction and analysis, not a new proof. All structural claims about the two noise models, the fidelity-loss bound, and the calibration scalings are taken from the abstract of the source work [1],[2]; our contribution is to (i) state the mechanism in elementary terms, (ii) derive the stated bounds from explicit assumptions with all arithmetic shown, and (iii) compute illustrative numerical examples so that the scalings become concrete. Section 2 situates the work in the supplied literature. Section 3 sets up the models. Section 4 contains the derivations. Section 5 reports only computed numbers. Section 6 discusses limitations and failure modes.

## 2. Background and Related Work

We discuss each supplied bibliography entry in turn, restricting every statement to what the entry itself supports.

**[1] and [2] (the source work).** Entries [1] and [2] refer to the same preprint, arXiv:2610.03545v1, "What Must a Quantum-Memory Decoder Know About Temporally Correlated Noise?" The supplied abstract states the full result set that this paper reconstructs: calibration formulated in terms of the fidelity differences that select a Pauli recovery; a main example of weak coherent $X$ rotations in a class of CSS codes including Shor, Steane, and odd-distance rotated surface codes; two sign models (fixed throughout a run versus independently redrawn each interval) with identical syndrome statistics and the same spatiotemporal Pauli process (SPP) obtained by Pauli-twirling every noise interval; different required logical corrections at suitable storage times; a worst-case fidelity loss approaching $1/2$ without model information despite full syndrome access; matching calibration bounds at fixed code and fixed positive target loss below $1/2$; interval counts scaling as the inverse rotation angle to the code's $X$ distance for complete QEC cycles, reduced to inverse-square scaling with two uninterrupted intervals before one extraction; and the observations that physical Pauli twirling changes both recovery performance and information requirements, that discarding the record of applied random Pauli operations makes the SPP sufficient for optimal recovery, and that keeping the record can improve attainable fidelity but may require additional noise information. Entry [2]'s summary is truncated relative to entry [1]; we rely on entry [1] for the complete statement of results.

**[3] arXiv:1008.0667v2, "Noise and Bell's inequality".** This entry discusses the concept of reality from the EPR paradox onward and the Bell inequality, noting that considerable evidence exists that the inequality can be violated even by classical systems, so that experiments showing quantum behavior may be open to alternative interpretation. The relevance to our topic is thematic rather than technical: the source work's two noise models are observationally equivalent at the level of syndrome statistics, exactly the kind of situation in which empirical data alone underdetermine the underlying model. The entry supplies no further technical detail, and we use it only for this conceptual connection.

**[4] arXiv:1310.1481v1, "Strongly correlated superconductivity".** These lecture notes concern the failure of band theory and BCS theory in high-temperature and layered organic superconductors, emphasizing that low-energy properties of a phase of matter are generally emergent. The connection to our problem is the general lesson that effective descriptions can hide the microscopic degrees of freedom that determine behavior in a different regime; the supplied summary gives no quantum-information content, and we draw no technical claim from it.

**[5] arXiv:1612.01464v2, "Finite blocklength and moderate deviation analysis of hypothesis testing of correlated quantum states and application to classical-quantum channels with memory".** This work applies martingale concentration inequalities — described as a powerful tool across probability, statistics, information theory, and machine learning — to quantum hypothesis testing, the problem of discriminating quantum states belonging to two different sequences $\{\rho_n\}$. This is the closest methodological relative of the source work in the supplied bibliography: calibrating between the fixed-sign and redrawn-sign noise models is precisely a hypothesis-testing problem between two correlated quantum state sequences, and the finite-blocklength perspective matches the source work's question of how many noise intervals calibration requires. The entry's summary is truncated and gives no specific bounds, so we cite it for the methodological framing only.

**[6] arXiv:1601.00157v1, "Theory of noise suppression in $\Lambda$-type quantum memories by means of a cavity".** This entry concerns quantum memories storing single photons or other quantum states of light for on-demand retrieval, based on far-off-resonant Raman absorption in ensembles of $\Lambda$-type atoms, and identifies unwanted four-wave mixing at room temperature as prohibitive for application. It is a concrete instance of a physically correlated noise process (four-wave mixing) degrading a quantum memory, motivating the abstract study of how decoders must handle correlated noise. The summary is truncated; no further detail is available from it.

**[7] arXiv:1612.03430v1, "Quantum and Classical Frontiers of Noise".** This is an introduction to a special issue of eleven works, using weather and its butterfly effect as the typical example of phenomena not predictable with certainty, and defining noise in classical or quantum phenomena as the difference between the empirical output of an experiment and its statistical description. This definition is directly apt: the source work's central observation is that two noise models with the same statistical description of the empirical output (the syndrome record) can nonetheless demand different actions from the decoder.

**[8] arXiv:2311.17794v1, "Noise Dynamics in the Quantum Regime".** This experimental work shows that a time-dependent bias voltage on a tunnel junction modulates current fluctuations, generating correlations between current fluctuating at any frequency $f$ and at frequency $\pm\tilde{f}-f$, measured in the fully quantum regime. It demonstrates that engineered temporal correlations in noise are real, controllable, and measurable — the physical premise on which the source work's calibration question rests. The summary is truncated beyond this result.

**[9] arXiv:1605.07838v1, "Decoherence and noise in open quantum system dynamics".** This entry treats quantum noise within the Copenhagen interpretation applied to a composite system-environment setting, where averaging over environmental degrees of freedom leads to stochastic quantum dynamics complying with the statistical structure of quantum mechanics. This is the standard formal backdrop for the source work's "known system-environment interactions": the environment is explicit, and the noise model is a stochastic process over intervals. The summary is truncated and supplies no specific equations.

**[10] QNFO: The Problem-Substrate Mapping.** This QNFO work translates a critique of computational claims into an investment portfolio matching problem classes (optimization, linear algebra, probabilistic inference, quantum simulation, cryptography, general-purpose) to physical substrates. It frames our significance argument: calibration overheads belong in the cost accounting of any substrate proposed for quantum memory. The summary is truncated.

**[11] QNFO: Spectral Benchmarking of Holographic Quantum Simulations.** The supplied entry has an empty summary; it provides no content we can use, and we note this explicitly as a limitation of the supplied corpus.

**[12] QNFO: Auditing the BQNN.** This QNFO work audits a tunable quantum neural network implemented on three quantum computing platforms, through a research pipeline including due diligence, an external literature search across 32 papers, and a nine-stage process. It exemplifies the audit culture in which the source work's calibration-cost results should be deployed: a decoder's noise assumptions are an auditable design choice.

**[13] QNFO: The Physics of Computation.** This QNFO work examines fundamental physical limits (Landauer bound, Margolus-Levitin theorem, Bremermann limit, Bekenstein bound) and shows that quantum error-correction overhead of $10^{2}$–$10^{3}$ physical operations per logical operation multiplies thermodynamic cost. This gives the quantitative backdrop against which any additional calibration overhead must be judged.

## 3. Methods

### 3.1 The two noise models

Following [1], consider a fixed stabilizer memory experiment using a CSS code with $X$ distance $d_X$ (the minimum weight of a logical $X$-type operator; $d_X = d$ for Shor, Steane, and odd-distance rotated surface codes in the class considered). Time is divided into noise intervals. In each interval, every physical qubit undergoes a weak coherent $X$ rotation by angle $\theta$ (per interval, per qubit), with a sign $s_i \in \{+1,-1\}$ shared by all physical qubits in that interval. Two models:

- $M_{\mathrm{fix}}$: the shared sign is fixed throughout the run, $s_i = s$ for all intervals $i$.
- $M_{\mathrm{red}}$: the shared sign is independently redrawn each interval, $s_i \overset{\text{iid}}{\sim} \mathrm{Unif}\{+1,-1\}$.

Both models are assumed known in structure (the system-environment interaction is known); the calibration question is which model obtains and what information suffices to decode optimally.

### 3.2 Observational equivalence

By Pauli-twirling every noise interval (replacing each coherent rotation by a random Pauli drawn to match its averaged channel), both models yield the same spatiotemporal Pauli process (SPP), and the two models have identical syndrome statistics. Hence any decoder whose input is only the syndrome record — even the full record — cannot distinguish the models from a single run's statistics, yet the models require different logical corrections at suitable storage times.

### 3.3 Decoder classes

We consider three decoder classes, mirroring the structure of [1]:

1. $\mathcal{D}_{\mathrm{noise\text{-}aware}}$: knows which model obtains and decodes optimally for it.
2. $\mathcal{D}_{\mathrm{SPP}}$: knows only the SPP (the Pauli-twirled process), not the sign realization or record.
3. $\mathcal{D}_{\mathrm{agnostic}}$: knows only the syndrome record and nothing about which model obtains.

### 3.4 Fidelity accounting

For a Pauli recovery $R$ and noise model $M$, let $F_R(M)$ denote the resulting storage fidelity. Calibration in [1] is formulated in terms of the fidelity differences $\Delta F = F_{R_1}(M) - F_{R_2}(M)$ that select a Pauli recovery. The fidelity loss of a decoder $D$ relative to the noise-aware optimum is

$$L(D) = \max_{M \in \{M_{\mathrm{fix}}, M_{\mathrm{red}}\}} \left[ F^*(M) - F_D(M) \right],$$

where $F^*(M)$ is the optimum under model $M$.

## 4. Analysis

Every input number below is either (a) quoted from the abstract of [1], with the quote identified, or (b) an assumption of our illustrative parameter set, explicitly labeled. All arithmetic is shown.

### 4.1 Derivation of the worst-case fidelity loss approaching $1/2$

**Input (from [1]):** "Without model information, even the best final recovery has a worst-case fidelity loss approaching $1/2$ relative to the noise-aware optimum, despite access to the full syndrome record."

**Derivation.** Suppose the storage time $T$ is in the regime where the two models' optimal logical corrections disagree. Concretely, assume (Assumption A1, an idealization of the regime described in [1]):

- (i) The noise-aware optima achieve $F^*(M_{\mathrm{fix}}) = F^*(M_{\mathrm{red}}) = F^*$, with $F^* \approx 1$ (the abstract states each model is "almost perfectly correctable when known" in the weak-noise limit).
- (ii) The optimal corrections under the two models apply opposite logical $X$-type corrections on a set $S$ of syndrome records, and the record lies in $S$ with probability $q(T)$.
- (iii) The decoder has no information distinguishing the models beyond the syndrome record, which is identically distributed under both; so any decoder's output is a fixed function of the record and applies the same correction under both models.

On records in $S$, a decoder applying the correction optimal for $M_{\mathrm{fix}}$ is wrong for $M_{\mathrm{red}}$ and vice versa. A decoder that commits to one model's correction is optimal for one model and pays the full disagreement on the other; a decoder that randomizes 50/50 pays half the disagreement on both. In all cases, on records in $S$ the decoder's fidelity is at most the average of the two model-conditional optima minus a disagreement penalty. Under the symmetric idealization where a wrong logical correction takes the fidelity from $F^*$ to approximately $1 - F^*$ (logical error with probability near $1$ on the affected branch), the fidelity on a record in $S$ for the mismatched model is $\approx 1 - F^*$, and the loss for that model is

$$F^* - (1 - F^*) = 2F^* - 1.$$

With $F^* \to 1$, this loss tends to $2(1) - 1 = 1$ on the affected branch; averaged over the two models with equal prior weight $1/2$ each, the worst-case loss is

$$L_{\mathrm{worst}} = \frac{1}{2}\left(2F^* - 1\right) \xrightarrow{F^* \to 1} \frac{1}{2}\left(2 - 1\right) = \frac{1}{2}.$$

$$\boxed{L_{\mathrm{worst}} \to \frac{1}{2}}$$

This reproduces the stated bound of [1] as the $q(T) \to 1$, $F^* \to 1$ limit of the symmetric disagreement mechanism. The bound is a worst case over the two models; the abstract's phrasing "approaching $1/2$" matches the limit just computed.

**Numerical instance.** Take $F^* = 0.98$ (Assumption A2, illustrative weak-noise value) and full disagreement $q = 1$. Then

$$L_{\mathrm{worst}} = \frac{1}{2}\left(2 \times 0.98 - 1\right) = \frac{1}{2}\left(1.96 - 1\right) = \frac{1}{2}(0.96) = 0.48.$$

So with $F^* = 0.98$, the model-agnostic decoder loses $0.48$ in worst-case fidelity against the noise-aware optimum — close to the asymptotic $1/2 = 0.5$.

### 4.2 Calibration cost: complete QEC cycles

**Input (from [1]):** "With logical preparation and final readout, complete QEC cycles require a number of noise intervals scaling as the inverse rotation angle raised to the code's $X$ distance."

**Derivation of the scaling form.** Let $N_{\mathrm{cyc}}(d_X, \theta)$ be the number of noise intervals needed for calibration to a fixed positive target loss $\ell < 1/2$ at fixed code. The stated scaling is

$$N_{\mathrm{cyc}}(d_X, \theta) \propto \theta^{-d_X}.$$

The mechanism (reconstructed): the distinguishing signal between $M_{\mathrm{fix}}$ and $M_{\mathrm{red}}$ accumulates coherently over intervals, while the discriminating statistic must overcome fluctuations whose size grows with the number of ways a distance-$d_X$ logical operator can be affected; resolving the sign structure to logical-operator precision costs one factor of $\theta^{-1}$ per order of the code's $X$ distance. We take the scaling as given by [1] and compute its consequences.

**Numerical instance (Assumption A3, illustrative parameters):** $\theta = 0.05$ rad per interval, $d_X = 3$ (e.g., a distance-3 Steane-type code in the class). Then, in units of the unknown proportionality constant $C$:

$$N_{\mathrm{cyc}} = C \cdot \theta^{-d_X} = C \cdot (0.05)^{-3}.$$

Compute $(0.05)^{-3}$: $0.05 = 5 \times 10^{-2}$, so $(0.05)^{-3} = (5 \times 10^{-2})^{-3} = 5^{-3} \times 10^{6} = \frac{1}{125} \times 10^{6} = 8000$.

$$N_{\mathrm{cyc}} = 8000\,C \text{ intervals}.$$

If instead $\theta = 0.1$ rad: $(0.1)^{-3} = 10^{3} = 1000$, so $N_{\mathrm{cyc}} = 1000\,C$ — a factor $8000/1000 = 8$ reduction, consistent with the $\theta^{-3}$ scaling since $(0.1/0.05)^{3} = 2^{3} = 8$.

### 4.3 Calibration cost: two uninterrupted intervals before one extraction

**Input (from [1]):** "Allowing two uninterrupted intervals before one extraction reduces the optimal cost to inverse-square scaling."

**Derivation.** The improved scheme has

$$N_{2}(d_X, \theta) \propto \theta^{-2},$$

independent of $d_X$ in the exponent. For the same parameters ($\theta = 0.05$, $d_X = 3$):

$$N_{2} = C' \cdot (0.05)^{-2} = C' \cdot \frac{1}{0.0025} = 400\,C' \text{ intervals}.$$

The improvement factor, taking $C' \approx C$ (Assumption A4, same prefactor — an assumption, since [1] states only the exponent change), is

$$\frac{N_{\mathrm{cyc}}}{N_{2}} = \frac{8000\,C}{400\,C'} = 20 \cdot \frac{C}{C'} \approx 20.$$

Equivalently, the ratio of scalings is $\theta^{-d_X}/\theta^{-2} = \theta^{-(d_X - 2)} = (0.05)^{-1} = 20$, confirming the arithmetic.

### 4.4 Effect of Pauli twirling and record-keeping

**Inputs (from [1]):** "Physical Pauli twirling of every noise interval changes both recovery performance and its information requirements. Discarding the record of applied random Pauli operations makes the SPP sufficient for optimal recovery. Keeping this record can improve the attainable fidelity, but reaching that optimum may require additional noise information."

No further arithmetic is derivable from the supplied text for this point beyond the qualitative statement; we report it as a structural result of [1] without invented numbers.

### 4.5 Storage-time projection (labeled projection)

**Projection with stated assumptions.** If each noise interval has duration $\Delta t$ and the fixed-sign model accumulates a net coherent rotation $N\theta$ after $N$ intervals, the storage time at which the two models' optimal corrections maximally disagree (net rotation of order $\pi/2$ per the coherent-accumulation picture) is, as a rough order-of-magnitude projection,

$$N_{\mathrm{dis}} \approx \frac{\pi/2}{\theta} = \frac{\pi}{2\theta}.$$

With $\theta = 0.05$: $N_{\mathrm{dis}} \approx \frac{\pi}{2 \times 0.05} = \frac{\pi}{0.1} = 10\pi \approx 31.4$ intervals, i.e., $N_{\mathrm{dis}} \approx 31$ intervals (rounding down, since the disagreement regime begins before exact alignment). With $\Delta t = 1\ \mu\mathrm{s}$ (Assumption A5, illustrative), this is $T_{\mathrm{dis}} \approx 31\ \mu\mathrm{s}$. **This is a projection from a coherent-accumulation heuristic, not a result of [1]; the abstract states only that the models "require different logical corrections" "at suitable storage times," without specifying the time.** Uncertainty: the proportionality constant and the exact alignment angle are not given in [1], so this projection carries at least an order-one multiplicative uncertainty.

## 5. Results

We report only quantities computed in Section 4, each with its derivation reference.

**R1 (derived, Section 4.1).** Under the symmetric disagreement mechanism with idealized assumptions A1, the worst-case fidelity loss of a model-agnostic decoder with full syndrome access tends to $L_{\mathrm{worst}} = 1/2 = 0.5$ as $F^* \to 1$, reproducing the bound stated in [1].

**R2 (computed, Section 4.1).** For the illustrative weak-noise value $F^* = 0.98$ (Assumption A2) and full disagreement, $L_{\mathrm{worst}} = 0.48$.

**R3 (computed, Section 4.2).** With the scaling $N_{\mathrm{cyc}} \propto \theta^{-d_X}$ from [1] and illustrative parameters $\theta = 0.05$, $d_X = 3$: $N_{\mathrm{cyc}} = 8000\,C$ intervals, where $C$ is the unstated proportionality constant. At $\theta = 0.1$: $N_{\mathrm{cyc}} = 1000\,C$, an $8$-fold reduction.

**R4 (computed, Section 4.3).** With the inverse-square scaling from [1] and the same parameters: $N_{2} = 400\,C'$ intervals; improvement factor $\approx 20$ relative to R3 under Assumption A4 ($C' = C$).

**R5 (projection, Section 4.5).** Under the coherent-accumulation heuristic with $\theta = 0.05$ and $\Delta t = 1\ \mu\mathrm{s}$, the disagreement regime begins at $N_{\mathrm{dis}} \approx 31$ intervals, i.e., $T_{\mathrm{dis}} \approx 31\ \mu\mathrm{s}$. This is a projection with order-one uncertainty in the prefactor and alignment angle; it is not a result of [1].

No experimental or simulated data are reported in this paper; all numbers above are either arithmetic consequences of scalings stated in [1] under labeled assumptions, or explicitly labeled projections.

## 6. Discussion

**Limitations of the reconstruction.** Our derivation of the $1/2$ bound (Section 4.1) uses an idealized symmetric disagreement model (Assumption A1) that we constructed to reproduce the abstract's stated limit; the actual proof in [1] may proceed differently, and the finite-$F^*$ correction term ($L = F^* - 1/2$ at full disagreement under our model, giving $0.48$ at $F^* = 0.98$) is our model's prediction, not a result of [1]. Similarly, the proportionality constants $C$ and $C'$ in the calibration scalings are not given in the supplied abstract, so all interval counts in R3 and R4 are stated in units of an unknown constant; only the ratios (8-fold from doubling $\theta$, 20-fold from the two-interval scheme under A4) are constant-free. Assumption A4 (equal prefactors) is ours and could be wrong in either direction.

**Failure modes of the claims.** If the two models' optimal corrections disagree only on a small-probability set $S$ at the storage times of practical interest, the worst-case loss is scaled down by $q(T)$ and the $1/2$ bound is loose; the abstract's "at suitable storage times" phrasing suggests exactly this storage-time dependence, which our reconstruction does not quantify. If the code class behaves differently for small $d_X$ (e.g., $d_X = 3$), the $\theta^{-d_X}$ calibration scaling may have large prefactors that dominate at realistic $\theta$. Our projection R5 assumes coherent accumulation up to $\pi/2$; dephasing or interval-to-interval variation would invalidate it.

**What would falsify the claims.** The reconstructed claims would be falsified if (i) a decoder using only the syndrome record could achieve fidelity loss substantially below $1/2$ in the worst case for this model pair — this would contradict the observational equivalence premise, since identical syndrome statistics force identical decoder output distributions; (ii) the calibration interval count scaled better than $\theta^{-d_X}$ for complete QEC cycles in this code class; or (iii) physical Pauli twirling left recovery performance and information requirements unchanged, contradicting the stated structural result of [1].

**Open questions.** The supplied abstract does not state: the constants $C, C'$; the exact storage-time window of maximal disagreement; whether the matching calibration bounds extend beyond the specific CSS class; how the bounds interpolate between the fixed-sign and redrawn-sign models for partial side information; and the quantitative fidelity gain from keeping the record of applied random Pauli operations. Each is a concrete target for follow-up work.

**Corpus limitation.** The supplied bibliography contains only the source work's abstract plus thematically adjacent entries with truncated summaries, and one entry ([11]) with no summary at all; a full related-work treatment of decoder calibration and correlated noise would require a broader corpus, which we flag as a limitation rather than fill from memory.

## 7. Conclusion

We reconstructed the central results of the study of temporally correlated noise in quantum-memory decoding [1],[2] with explicit derivations and computed examples. The core finding is an information-theoretic gap: two noise models with identical syndrome statistics and identical Pauli-twirled processes can demand different logical corrections, and a decoder lacking model information suffers a worst-case fidelity loss approaching $1/2$ relative to the noise-aware optimum, even with full syndrome access. Calibration is not free: complete QEC cycles cost a number of noise intervals scaling as $\theta^{-d_X}$, reduced to $\theta^{-2}$ by a two-uninterrupted-intervals scheme — a factor $\approx 20$ at our illustrative parameters. Physical Pauli twirling is not a free simplification: it changes both recovery performance and information requirements. These results quantify a calibration overhead that must appear in any honest accounting of quantum-memory architectures, complementing the physical-limits overhead analyses of [13] and the audit methodology of [12].

## References

[1] arXiv Query: search_query=&id_list=2610.03545&start=0&max_results=1 — "What Must a Quantum-Memory Decoder Know About Temporally Correlated Noise?" (abstract of arXiv:2610.03545v1).

[2] arXiv:2610.03545v1 | What Must a Quantum-Memory Decoder Know About Temporally Correlated Noise?

[3] arXiv:1008.0667v2 | Noise and Bell's inequality

[4] arXiv:1310.1481v1 | Strongly correlated superconductivity

[5] arXiv:1612.01464v2 | Finite blocklength and moderate deviation analysis of hypothesis testing of correlated quantum states and application to classical-quantum channels with memory

[6] arXiv:1601.00157v1 | Theory of noise suppression in $\Lambda$-type quantum memories by means of a cavity

[7] arXiv:1612.03430v1 | Quantum and Classical Frontiers of Noise

[8] arXiv:2311.17794v1 | Noise Dynamics in the Quantum Regime

[9] arXiv:1605.07838v1 | Decoherence and noise in open quantum system dynamics

[10] QNFO: The Problem-Substrate Mapping: A Framework for Honest Computational Investment

[11] QNFO: Spectral Benchmarking of Holographic Quantum Simulations

[12] QNFO: Auditing the BQNN: Does a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware Demonstrate a Route to Near-Term Quantum Advantage?

[13] QNFO: The Physics of Computation: Fundamental Limits and the Honest Boundaries of Post-Classical Computing