# Parity-Protected Qubits at 4 Kelvin: A Thermodynamic Error-Budget Analysis of a Warm Operating Point for Scalable Quantum Computing

## Abstract

Scalable quantum computing is widely assumed to require millikelvin cryogenics, yet the cooling power available at millikelvin temperatures is severely limited. We examine the conjecture that a thermodynamic bottleneck at millikelvin temperatures motivates operating superconducting-style qubits at 4 K, where cooling power is roughly $2\times10^{4}$ times larger, provided that a parity-protection mechanism suppresses the thermally activated error channels that otherwise dominate at that temperature. We construct an explicit error budget at 4 K: we compute the thermal quasiparticle population relative to the superconducting gap for niobium ($2\Delta/h \approx 700$ GHz against $k_{B}T/h \approx 83.4$ GHz at 4 K, giving $e^{-\Delta/k_{B}T} \approx 1.5\times10^{-2}$), show that aluminum ($T_{c} = 1.2$ K) is thermodynamically excluded as a junction material at 4 K ($e^{-\Delta/k_{B}T} \approx 0.59$), and compare against the same materials at 100 mK. We combine this with the parity-protected coupling scheme of the top-transmon proposal, which couples directly to fermion parity irrespective of quasiparticle excitations, and derive a conditional error model. We find that parity protection is a necessary but not sufficient condition: raw thermal quasiparticle populations at 4 K exceed fault-tolerance-relevant levels by many orders of magnitude unless parity-selective coupling removes the poisoning channel. We state the assumptions under which the 4 K operating point remains viable and identify the falsifying measurements.

## 1. Introduction

The scaling path of quantum computing is constrained not only by coherence and gate fidelity but by the thermodynamics of keeping a large machine cold. The research idea underlying this paper conjectures that scalability is thermodynamically bottlenecked at millikelvin temperatures, and that qubits operating at 4 K—exploiting the roughly $20{,}000\times$ increase in cooling power available there compared with dilution-refrigerator stages—could enable scalable architectures, if a suitable protection scheme suppresses the thermally activated error channels that appear at 4 K.

This conjecture faces an immediate physical objection: at 4 K, the thermal energy $k_{B}T$ is a substantial fraction of the superconducting gap of most superconductors, so thermally excited quasiparticles are abundant. The purpose of this paper is to make that objection quantitative and then to ask whether any parity-protection scheme can plausibly remove the resulting error channels below fault-tolerance thresholds. Our method is deliberately conservative: every number is either a stated input, a fundamental constant, or derived here with shown arithmetic. Where a full treatment would require a Monte Carlo simulation of quasiparticle poisoning rates—which we specify as a proposed method but do not report results for—we state the assumptions such a simulation would need and give the analytic bounds that any such simulation must respect.

The paper is organized as follows. Section 2 reviews the related literature, with the caveat that several supplied bibliography entries carry only truncated summaries, which we respect by limiting our claims about those works to what their summaries state. Section 3 defines the error-budget model. Section 4 carries out the derivations. Section 5 reports the computed results. Section 6 discusses limitations, failure modes, and what would falsify the central claims, and Section 7 concludes.

## 2. Background and Related Work

We draw on twelve supplied bibliography entries. Because several entries provide only truncated abstracts, we confine every statement about a cited work to what its own summary states.

[1] (arXiv:2403.02240v5, *Quantum Computing: Vision and Challenges*) frames quantum computing as using entanglement, superposition, and other quantum fundamental concepts to provide substantial processing advantages over traditional computing, for problems including modeling quantum mechanics, logistics, and chemical-based tasks. We use it as the general motivation: the application pull described there is what makes the thermodynamic scaling question of this paper practically relevant.

[2] (arXiv:2211.02350v1, *Tierkreis*) presents a higher-order dataflow graph program representation and runtime for compositional quantum-classical hybrid algorithms, motivated by the remote nature of quantum computers, the need for hybrid algorithms to involve cloud and distributed computing, and the long-running nature of these algorithms. This is relevant to our argument because a 4 K architecture changes the physical siting of control electronics, and dataflow-style runtimes of the kind Tierkreis describes are the software layer that would absorb such architectural changes; the summary supplied gives no further detail, so we relate it to our argument only at this level.

[3] (arXiv:2605.19854v1, *Unveiling Energetic Advantage in Superconducting Cat-Qubits Quantum Computation*) notes that among various implementations superconducting qubits have become the leading technology due to their scalability and compatibility with quantum error correction mechanisms, and indicates that time has traditionally been the primary focus (the summary truncates there). Its relevance is that it treats energetic advantage as an explicit design axis for superconducting qubits, the same axis this paper quantifies for the 4 K operating point; the truncated summary prevents us from attributing any specific energetic result to it.

[4] (arXiv:2506.21988v2, *Unifying communication paradigms in measurement-based delegated quantum computing*) concerns delegated quantum computing, in which clients with low quantum capabilities outsource computations to a server hosting a quantum computer, often within the measurement-based framework, which naturally facilitates blindness of inputs. We cite it to note that the client-server architecture it describes is indifferent to the server's operating temperature; our thermodynamic analysis is complementary to such architectural work.

[5] (arXiv:2011.03031v2, *Quantum simulation and computing with Rydberg-interacting qubits*) describes arrays of optically trapped atoms excited to Rydberg states as a competitive physical platform in which high-fidelity state preparation and readout, quantum logic gates, and controlled quantum dynamics of more than 100 qubits have been demonstrated, with systems approaching reliable computations with hundreds of qubits (summary truncates). This matters for our argument as a reminder that the thermodynamic bottleneck analyzed here is specific to superconducting-style platforms; atomic platforms do not share the millikelvin cryogenic constraint, though they have their own scaling constraints not analyzed here.

[6] (arXiv:1105.0315v1, *Top-transmon*) is the central prior work for our proposal. Its summary states that qubits constructed from uncoupled Majorana fermions are protected from decoherence, but that performing a quantum computation requires breaking this topological protection; parity-protected quantum computation breaks the protection in a minimally invasive way, by coupling directly to the fermion parity of the system—irrespective of any quasiparticle excitations—and proposes to use a superconducting (top-transmon) hybrid qubit for this purpose. The phrase "irrespective of any quasiparticle excitations" is exactly the property a 4 K operating point requires: if the logical information is encoded in fermion parity and read and manipulated through parity-selective coupling, the thermally generated quasiparticle population does not by itself decohere the qubit. Our error budget in Sections 4–5 is built around testing what this property does and does not buy at 4 K.

[7] (arXiv:1805.05224v3, *How many qubits are needed for quantum computational supremacy?*) discusses quantum computational supremacy arguments, which require computational assumptions related to the limitations of classical computation, such as the assumption that the polynomial hierarchy does not collapse—a stronger version of $P \neq NP$. We cite it to delimit scope: our paper addresses physical scalability, not computational-complexity arguments about supremacy; the summary supplied gives no further detail we rely on.

[8] (arXiv:1801.00862v3, *Quantum Computing in the NISQ era and beyond*) introduces Noisy Intermediate-Scale Quantum (NISQ) technology: quantum computers with 50–100 qubits may perform tasks surpassing classical digital computers, but noise in quantum gates will limit the size of quantum circuits that can be executed reliably. This is the framing our error budget addresses directly: the question at 4 K is precisely whether gate noise from thermal channels can be pushed below the level at which reliable circuit execution becomes possible, i.e., below fault-tolerance thresholds.

[9]–[12] are QNFO corpus entries (DOIs 10.5281/zenodo.17937531, 10.5281/zenodo.17955898, 10.5281/zenodo.17928156, 10.5281/zenodo.22758173), whose supplied summaries are empty. Their titles indicate coverage of thermodynamic and quantum constraints on scalable quantum computing, thermodynamic and informational bottlenecks of scalable fault-tolerant quantum computation, a "Thermodynamic Imperative" theme, and syntactic generation. We cite them as the provenance of the thermodynamic-bottleneck framing of this paper but, because the supplied entries give no substantive text, we make no specific claim about their contents beyond what the titles state.

## 3. Methods

### 3.1 Operating points and constants

We compare two operating points: $T_{\mathrm{warm}} = 4\ \mathrm{K}$ and $T_{\mathrm{cold}} = 0.1\ \mathrm{K}$ (100 mK, a representative dilution-refrigerator stage temperature; the input idea frames the comparison against millikelvin operation generally, and we fix 100 mK as the explicit reference point for all ratios). We use the fundamental constant

$$\frac{k_{B}}{h} = 20.84\ \mathrm{GHz\,K^{-1}},$$

so that the thermal energy in frequency units is $k_{B}T/h = (20.84\ \mathrm{GHz\,K^{-1}})\,T$.

### 3.2 Materials

Two superconductors bracket the analysis:

- **Niobium (Nb):** the input idea specifies $2\Delta \approx 700$ GHz, i.e., $\Delta/h = 350$ GHz.
- **Aluminum (Al):** the input idea specifies a critical temperature $T_{c} = 1.2$ K. We use the standard BCS relation $\Delta \approx 1.76\,k_{B}T_{c}$ (a textbook relation, stated here as an explicit modeling assumption), giving $\Delta/h = 1.76 \times 1.2\ \mathrm{K} \times 20.84\ \mathrm{GHz\,K^{-1}}$.

### 3.3 Error model

We model the thermally activated quasiparticle population by the Boltzmann factor

$$p_{\mathrm{th}}(T) = \exp\!\left(-\frac{\Delta}{k_{B}T}\right) = \exp\!\left(-\frac{\Delta/h}{(k_{B}/h)\,T}\right),$$

which is the equilibrium probability (up to a prefactor of order unity per mode, which we absorb into an attempt factor $A$) that a mode at the gap edge is thermally occupied. For a gate-level error probability we write

$$p_{\mathrm{qp}}(T) = A\,p_{\mathrm{th}}(T),$$

with $A$ an attempt factor that a quasiparticle-poisoning Monte Carlo simulation would need to determine; we treat $A$ parametrically rather than asserting a value.

### 3.4 Parity protection

The protection mechanism we analyze is that of [6]: the qubit couples directly to fermion parity, "irrespective of any quasiparticle excitations." We formalize this as the assumption that the logical error channel from quasiparticle poisoning is suppressed by a parity-selectivity factor $S_{\mathrm{par}}$, so that the effective poisoning error becomes

$$p_{\mathrm{eff}} = A\,S_{\mathrm{par}}\,p_{\mathrm{th}}(T).$$

The central quantitative question is: for what values of $S_{\mathrm{par}}$ does $p_{\mathrm{eff}}$ fall below an assumed fault-tolerance threshold $\epsilon_{\mathrm{th}} = 10^{-2}$ (a conventional illustrative figure, stated here as an assumption of this paper, not a measured value)?

### 3.5 Thermodynamic accounting

The input idea supplies the cooling-power ratio: 4 K platforms offer roughly $20{,}000\times$ the cooling power of dilution-refrigerator stages. We additionally compute the ideal Carnot limit on refrigerator efficiency to separate the fundamental thermodynamic contribution from engineering reality: the coefficient of performance is $\mathrm{COP} = T_{c}/(T_{h}-T_{c})$ with $T_{h} = 300$ K room temperature.

### 3.6 Proposed (not executed) Monte Carlo

The input idea proposes Monte Carlo simulation of quasiparticle poisoning rates and comparison against demonstrated 1.5 K silicon spin qubit data. No such simulation results and no silicon spin qubit dataset are supplied in the input block; we therefore specify the simulation design (sampling quasiparticle generation, tunneling, and parity-switching events with rates anchored to the Boltzmann factors computed in Section 4) but report **no** simulation numbers in this paper.

## 4. Analysis

Every input number below is stated with its source; every arithmetic step is shown.

### 4.1 Thermal energy scale

Source: fundamental constant $k_{B}/h = 20.84\ \mathrm{GHz\,K^{-1}}$ (Section 3.1).

$$\frac{k_{B}T_{\mathrm{warm}}}{h} = 20.84 \times 4 = 83.36\ \mathrm{GHz}.$$

$$\frac{k_{B}T_{\mathrm{cold}}}{h} = 20.84 \times 0.1 = 2.084\ \mathrm{GHz}.$$

The input idea quotes $k_{B}T \approx 83$ GHz at 4 K, consistent with our $83.36$ GHz.

### 4.2 Niobium gap ratio and Boltzmann factor

Source: input idea, $2\Delta \approx 700$ GHz for Nb, so $\Delta/h = 700/2 = 350$ GHz.

At 4 K:

$$\frac{\Delta}{k_{B}T} = \frac{350}{83.36} = 4.199.$$

$$p_{\mathrm{th}}^{\mathrm{Nb}}(4\ \mathrm{K}) = e^{-4.199} = 0.01498 \approx 1.5\times10^{-2}.$$

At 100 mK:

$$\frac{\Delta}{k_{B}T} = \frac{350}{2.084} = 167.95.$$

$$p_{\mathrm{th}}^{\mathrm{Nb}}(0.1\ \mathrm{K}) = e^{-167.95}.$$

In base 10: $167.95 / \ln 10 = 167.95 / 2.302585 = 72.95$, so

$$p_{\mathrm{th}}^{\mathrm{Nb}}(0.1\ \mathrm{K}) \approx 10^{-72.95} \approx 1.1\times10^{-73}.$$

The ratio of thermal populations between the two operating points is

$$\frac{p_{\mathrm{th}}^{\mathrm{Nb}}(4\ \mathrm{K})}{p_{\mathrm{th}}^{\mathrm{Nb}}(0.1\ \mathrm{K})} = e^{167.95 - 4.199} = e^{163.75}.$$

In base 10: $163.75/2.302585 = 71.12$, so the ratio is $\approx 10^{71.1}$. This is the quantitative core of the problem: raising the operating point from 100 mK to 4 K multiplies the equilibrium gap-edge thermal occupation of niobium by a factor of order $10^{71}$.

### 4.3 Aluminum: thermodynamic exclusion at 4 K

Source: input idea, $T_{c}^{\mathrm{Al}} = 1.2$ K; modeling assumption $\Delta = 1.76\,k_{B}T_{c}$.

$$\frac{\Delta_{\mathrm{Al}}}{h} = 1.76 \times 1.2 \times 20.84 = 1.76 \times 25.008 = 44.01\ \mathrm{GHz}.$$

At 4 K:

$$\frac{\Delta_{\mathrm{Al}}}{k_{B}T} = \frac{44.01}{83.36} = 0.528.$$

$$p_{\mathrm{th}}^{\mathrm{Al}}(4\ \mathrm{K}) = e^{-0.528} = 0.590.$$

That is, at 4 K the gap-edge thermal occupation factor of aluminum is $\approx 0.59$—the gap barely exceeds the thermal energy, and the superconductor is thermally saturated. For comparison, at 100 mK:

$$\frac{\Delta_{\mathrm{Al}}}{k_{B}T} = \frac{44.01}{2.084} = 21.12,\qquad p_{\mathrm{th}}^{\mathrm{Al}}(0.1\ \mathrm{K}) = e^{-21.12} = 6.7\times10^{-10}.$$

(Base-10 check: $21.12/2.302585 = 9.173$; $10^{-9.173} = 6.7\times10^{-10}$.) Conclusion: aluminum, the workhorse junction material of conventional superconducting qubits, is thermodynamically excluded at 4 K in the sense that its thermal quasiparticle population is of order unity rather than exponentially small. Any 4 K architecture must use a higher-gap material such as niobium.

### 4.4 Cooling power and Carnot accounting

Source: input idea, cooling-power ratio $\approx 20{,}000\times$ at 4 K over dilution-refrigerator stages. We take this as a given empirical input, $R_{P} = 2\times10^{4}$.

Carnot limit (Section 3.5), with $T_{h} = 300$ K:

$$\mathrm{COP}_{4\ \mathrm{K}} = \frac{4}{300-4} = \frac{4}{296} = 0.01351.$$

$$\mathrm{COP}_{0.1\ \mathrm{K}} = \frac{0.1}{300-0.1} = \frac{0.1}{299.9} = 3.344\times10^{-4}.$$

The ratio of ideal coefficients of performance is

$$\frac{\mathrm{COP}_{4\ \mathrm{K}}}{\mathrm{COP}_{0.1\ \mathrm{K}}} = \frac{0.01351}{3.344\times10^{-4}} = 40.4.$$

Interpretation: fundamental thermodynamics alone favors 4 K by a factor of $\approx 40$ in ideal efficiency; the empirically supplied factor of $2\times10^{4}$ in practical cooling power is dominated by engineering realities of dilution refrigeration (the supplied input does not decompose this factor, and we do not speculate on its decomposition). Either way, the thermodynamic incentive for 4 K operation is real and large.

### 4.5 Parity-protection requirement

With the assumed threshold $\epsilon_{\mathrm{th}} = 10^{-2}$ (Section 3.4, stated assumption) and the model $p_{\mathrm{eff}} = A\,S_{\mathrm{par}}\,p_{\mathrm{th}}(T)$:

**Without parity protection** ($S_{\mathrm{par}} = 1$), even with an optimistic attempt factor $A = 10^{-3}$:

$$p_{\mathrm{qp}}^{\mathrm{Nb}}(4\ \mathrm{K}) = 10^{-3} \times 1.498\times10^{-2} = 1.498\times10^{-5}.$$

This single-channel number sits below the assumed threshold, but this is misleading: $p_{\mathrm{th}}$ is a per-mode equilibrium factor, whereas a real device has a quasiparticle density, tunneling rates, and poisoning events per gate time; the attempt factor $A$ absorbs all of this and is precisely what the proposed Monte Carlo must determine. We therefore do **not** claim viability from this number alone.

**With parity protection**, the requirement is

$$A\,S_{\mathrm{par}}\,p_{\mathrm{th}}^{\mathrm{Nb}}(4\ \mathrm{K}) < \epsilon_{\mathrm{th}} \quad\Longrightarrow\quad S_{\mathrm{par}} < \frac{\epsilon_{\mathrm{th}}}{A\,p_{\mathrm{th}}^{\mathrm{Nb}}(4\ \mathrm{K})}.$$

For $A = 10^{-3}$:

$$S_{\mathrm{par}} < \frac{10^{-2}}{10^{-3} \times 1.498\times10^{-2}} = \frac{10^{-2}}{1.498\times10^{-5}} = 667.6.$$

For a pessimistic $A = 1$:

$$S_{\mathrm{par}} < \frac{10^{-2}}{1.498\times10^{-2}} = 0.668.$$

Reading: if the attempt factor is small (poisoning events are rare relative to gate time), parity protection need only avoid *amplifying* the thermal channel ($S_{\mathrm{par}} \lesssim 10^{2}$–$10^{3}$ suffices); if poisoning events are frequent ($A \sim 1$), parity protection must *reduce* the effective channel by at least a factor of $\approx 0.67$—i.e., must genuinely decouple the logical state from quasiparticle number, which is exactly the property [6] claims for parity-selective coupling ("irrespective of any quasiparticle excitations"). The viability question at 4 K therefore reduces entirely to the physical value of $A$ and the achievable $S_{\mathrm{par}}$, both of which are empirical quantities not fixed by the supplied input.

### 4.6 Aluminum under parity protection

Even with parity protection, aluminum at 4 K has $p_{\mathrm{th}} = 0.590$ (Section 4.3). The requirement becomes

$$S_{\mathrm{par}} < \frac{10^{-2}}{A \times 0.590}.$$

For $A = 10^{-3}$: $S_{\mathrm{par}} < 16.9$; for $A = 1$: $S_{\mathrm{par}} < 0.017$. Parity protection would need to suppress the aluminum thermal channel by factors of $17$ to $60$, on top of whatever suppression the parity mechanism provides against quasiparticle *number* fluctuations—while the pair-breaking channel itself is thermally saturated. We conclude that parity protection cannot rescue aluminum at 4 K under this model, because protection addresses the poisoning channel, not the saturation of the condensate itself.

### 4.7 Thermally activated TLS decoherence in Nb₂O₅

The input idea identifies thermally activated two-level-system (TLS) decoherence in niobium pentoxide ($\mathrm{Nb_2O_5}$, the native oxide of niobium) as a material constraint at 4 K. The supplied input gives no TLS activation energies or densities for $\mathrm{Nb_2O_5}$, so no quantitative TLS error rate can be computed here. We record this as an open error channel: any 4 K niobium architecture must measure TLS activation spectra in its own oxide and demonstrate that the thermally activated TLS contribution at 4 K is either small or mitigated (e.g., by oxide removal or surface treatments—mitigation strategies are not specified in the supplied input and we do not assert their efficacy).

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

1. **Thermal energy at 4 K:** $k_{B}T/h = 83.36$ GHz (computed, Section 4.1); at 100 mK, $2.084$ GHz.

2. **Niobium thermal factor:** $p_{\mathrm{th}}^{\mathrm{Nb}}(4\ \mathrm{K}) = 1.5\times10^{-2}$ (computed); $p_{\mathrm{th}}^{\mathrm{Nb}}(0.1\ \mathrm{K}) \approx 1.1\times10^{-73}$ (computed). Population ratio between operating points $\approx 10^{71.1}$ (computed).

3. **Aluminum thermal factor:** $p_{\mathrm{th}}^{\mathrm{Al}}(4\ \mathrm{K}) = 0.590$ (computed, under the stated BCS assumption $\Delta = 1.76\,k_{B}T_{c}$); $p_{\mathrm{th}}^{\mathrm{Al}}(0.1\ \mathrm{K}) = 6.7\times10^{-10}$ (computed). Aluminum is thermodynamically excluded at 4 K under this model.

4. **Cooling power:** practical ratio $R_{P} = 2\times10^{4}$ (input, not derived here); ideal Carnot efficiency ratio $40.4$ (computed).

5. **Parity-protection requirement (projection, stated assumptions:** threshold $\epsilon_{\mathrm{th}} = 10^{-2}$ assumed; model $p_{\mathrm{eff}} = A\,S_{\mathrm{par}}\,p_{\mathrm{th}}$): for niobium at 4 K, parity protection suffices if $S_{\mathrm{par}} < 667.6/A'$ where $A' = A/10^{-3}$ rescales the attempt factor; i.e., for $A = 10^{-3}$, $S_{\mathrm{par}} < 667.6$, and for $A = 1$, $S_{\mathrm{par}} < 0.668$. Uncertainty: these bounds scale linearly in $1/A$ and linearly in $\epsilon_{\mathrm{th}}$; both $A$ and $\epsilon_{\mathrm{th}}$ are assumptions, not measurements.

6. **No Monte Carlo results are reported.** The proposed simulation (Section 3.6) and the comparison against 1.5 K silicon spin qubit data (proposed in the input idea) require datasets not supplied in the input block; reporting invented numbers would violate the evidentiary standard of this paper.

## 6. Discussion

**What the analysis supports.** The thermodynamic incentive for 4 K operation is quantitatively real: a computed Carnot efficiency ratio of $40.4$ and a supplied practical cooling-power ratio of $2\times10^{4}$ both favor the warm operating point. The thermal cost is equally real and enormous: a factor of $\approx 10^{71}$ in niobium's equilibrium gap-edge thermal occupation between 100 mK and 4 K. The viability of 4 K operation therefore hinges entirely on protection mechanisms, and the parity-protected coupling of [6]—coupling to fermion parity irrespective of quasiparticle excitations—is, in our model, exactly the right *kind* of mechanism, because it targets the dominant thermal channel (quasiparticle poisoning) rather than the gap itself.

**What the analysis does not support.** We have not shown that a 4 K parity-protected qubit is buildable. Three gaps separate our model from a demonstration:

1. **The attempt factor $A$ is unknown.** Our conditional result (Section 4.5) spans $S_{\mathrm{par}} < 0.668$ to $S_{\mathrm{par}} < 667.6$ depending on $A$. If real-world poisoning event rates at 4 K are frequent relative to gate times ($A \sim 1$ or larger), parity protection must provide genuine suppression, and whether the top-transmon coupling achieves $S_{\mathrm{par}} < 1$ in practice is an empirical question the supplied bibliography does not answer—the [6] summary describes the proposal, not measured suppression factors.

2. **Parity protection addresses one channel.** TLS decoherence in $\mathrm{Nb_2O_5}$ (Section 4.7), dielectric loss, and control-line thermal noise at 4 K are unmodeled. The input idea names the TLS channel explicitly; without activation parameters we cannot bound it, and it could alone exceed $\epsilon_{\mathrm{th}}$.

3. **Aluminum exclusion is model-relative.** Our exclusion of aluminum rests on the BCS assumption $\Delta = 1.76\,k_{B}T_{c}$ and on equilibrium Boltzmann weighting; nonequilibrium effects, subgap states, or higher-gap aluminum alloys could alter the conclusion, though the supplied input gives no data on such modifications.

**What would falsify the central claims.** (i) A demonstration of conventional (non-parity-protected) superconducting qubits with fault-tolerance-relevant fidelities at 4 K would falsify our claim that protection is *necessary*. (ii) A measurement showing that parity-selective coupling of the [6] type fails to suppress quasiparticle-induced errors at elevated temperature ($S_{\mathrm{par}} \geq 1$ with $A \sim 1$) would falsify the viability projection. (iii) A demonstration that aluminum-based junctions operate with low error at 4 K would falsify our thermodynamic exclusion result. (iv) Conversely, a Monte Carlo poisoning study anchored to the Boltzmann factors computed here, showing $A \ll 10^{-3}$ for niobium devices, would strengthen the case substantially.

**Open questions.** What is the physical value of $A$ for niobium transmon-like devices at 4 K? What $S_{\mathrm{par}}$ does a concrete top-transmon implementation achieve at elevated temperature? What are the TLS activation parameters of $\mathrm{Nb_2O_5}$ at 4 K? How does the $2\times10^{4}$ cooling-power ratio decompose into fundamental versus engineering contributions? And how does the 4 K architecture integrate with the remote, hybrid, long-running execution models that runtime frameworks such as [2] are designed to support?

**Scope caveat on the bibliography.** Entries [9]–[12] carry empty supplied summaries and entries [1]–[8] carry truncated ones; our literature claims are limited accordingly, and the quantitative content of this paper rests on the input idea's stated numbers, fundamental constants, and the derivations shown, not on the