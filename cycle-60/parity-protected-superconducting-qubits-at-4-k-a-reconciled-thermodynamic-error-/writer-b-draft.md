# Parity-Protected Qubits at 4 Kelvin: A Quantitative Error-Budget Analysis of a High-Temperature Superconducting Operating Point

## Abstract

Scalable superconducting quantum computing is conventionally operated at millikelvin temperatures, where cooling power is scarce and expensive. This paper tests the conjecture that a thermodynamic bottleneck at millikelvin temperatures could be relieved by operating parity-protected qubits at 4 K, where closed-cycle refrigerators supply roughly $2\times10^{4}$ times more cooling power than dilution refrigerators. We construct an explicit thermal error budget for a 4 K superconducting qubit: we compute the thermal occupation $k_{B}T/h \approx 83.3$ GHz at $T_1 = 4$ K, compare it against the niobium gap scale $2\Delta_{\mathrm{Nb}}/h \approx 700$ GHz, and derive a Boltzmann quasiparticle fraction $e^{-\Delta_{\mathrm{Nb}}/k_{B}T_1} \approx 1.50\times10^{-2}$. We show that aluminum, with critical temperature $T_{c,\mathrm{Al}} = 1.2$ K, is thermodynamically excluded at 4 K. We then evaluate whether a parity-protection scheme of the top-transmon type, which couples to fermion parity irrespective of quasiparticle excitations, can suppress the residual error channels below a stated fault-tolerance target of $p_{\mathrm{target}} = 10^{-4}$. Our central result is a required suppression factor $S \approx 150$ on thermally activated quasiparticle errors, which parity coupling plausibly provides for parity-encoded logical information but not for unprotected ancillary degrees of freedom. We conclude that 4 K operation is not fundamentally excluded for parity-protected architectures but is excluded for conventional transmon-style qubits, and we state the conditions under which this conclusion would be falsified.

## 1. Introduction

The scaling path of superconducting quantum processors is constrained not only by coherence and gate fidelity but by the thermodynamics of the cryogenic plant. Dilution refrigerators deliver very small cooling power at the millikelvin stage, and every additional qubit, cable, and amplifier adds heat load to a stage that cannot be expanded cheaply. The motivating conjecture of this paper, drawn from the author's research notes on thermodynamic and quantum constraints on scalable quantum computing [9], [10], [11], is that this constitutes a *thermodynamic bottleneck*: scalability is limited less by physics at the qubit level than by the refrigeration envelope imposed by the millikelvin operating point. At 4 K, by contrast, closed-cycle cooling technology offers approximately a $2\times10^{4}$-fold increase in available cooling power, an enormous relaxation of the thermal budget.

The question is whether qubit physics permits operation at 4 K. Conventional superconducting qubits fail immediately at 4 K for material reasons we quantify below: aluminum, the workhorse Josephson material, has a critical temperature of $T_{c,\mathrm{Al}} = 1.2$ K and is a normal metal at 4 K. Niobium survives, but its gap suppresses thermal quasiparticles by only a modest Boltzmann factor at 4 K. The candidate escape route is *parity protection*: qubits whose logical states are distinguished by fermion parity, so that the computational information is not stored in modes that thermally excited quasiparticles can corrupt. The top-transmon proposal [6] is the concrete embodiment of this idea: it couples directly to the fermion parity of a hybrid superconducting–topological system, "irrespective of any quasiparticle excitations," which is precisely the property a 4 K architecture needs.

This paper makes the conjecture quantitative. We derive the full thermal error budget of a 4 K niobium-based parity-protected qubit, compute the required error suppression against a stated fault-tolerance target, and identify which error channels parity protection can and cannot close. We also frame the result in the broader context of quantum computing scalability [1], [8], alternative physical platforms [5], energetic analyses of protected superconducting qubits [3], and the software and delegation infrastructures that any large-scale architecture must ultimately support [2], [4].

## 2. Background and Related Work

**Quantum computing as an application driver.** Reference [1] surveys quantum computing as a technology that uses entanglement, superposition, and other quantum concepts to provide substantial processing advantages over traditional computing, for problems including modeling quantum mechanics, logistics, and chemical-based simulation. The scale of the intended applications motivates asking not merely whether a qubit works, but whether an architecture can be built and cooled at scale; the thermodynamic analysis of this paper is aimed at exactly that second question.

**The NISQ regime and its limits.** Preskill's NISQ framework [8] describes near-term quantum computers with 50–100 qubits whose gate noise limits the size of circuits that can be executed reliably, while remaining useful tools for exploring many-body quantum physics. The NISQ observation that noise bounds circuit depth is the circuit-level expression of the error-budget problem we analyze at the physical level: if thermal quasiparticle errors at 4 K cannot be suppressed below threshold, the reliable circuit size remains bounded no matter how many qubits are fabricated.

**Resource requirements of supremacy and fault tolerance.** Reference [7] analyzes how many qubits quantum computational supremacy arguments require, noting that such arguments rest on computational assumptions such as the non-collapse of the polynomial hierarchy, a stronger version of $\mathrm{P} \neq \mathrm{NP}$. This matters here because the value of scaling to large qubit counts depends on such supremacy and fault-tolerance arguments holding; our analysis addresses the physical preconditions for reaching those qubit counts.

**Parity-protected qubits.** The top-transmon proposal [6] is the direct antecedent of this paper's architecture. Its summary states that qubits built from uncoupled Majorana fermions are protected from decoherence, that computation requires breaking this protection, and that parity-protected quantum computation breaks it minimally invasively by coupling directly to the fermion parity of the system, irrespective of quasiparticle excitations, using a superconducting hybrid structure. The supplied summary is cut off before giving device-level performance numbers, so we use [6] only for its stated mechanism — parity coupling insensitive to quasiparticle population — and not for any quantitative device figures.

**Energetic analysis of protected superconducting qubits.** Reference [3] examines the energetic advantage of superconducting cat-qubits, noting that superconducting qubits are a leading technology due to their scalability and compatibility with quantum error correction, and that analysis has traditionally focused on time (the summary is truncated before its energetic findings are stated). This paper extends the same style of question — what does a protection scheme buy, and what does it cost — from energy consumption to cooling power and thermal error budgets. The supplied summary does not state the cat-qubit results in detail, so we cite [3] for framing only.

**Alternative platforms.** Reference [5] describes Rydberg-interacting qubit arrays, in which high-fidelity state preparation and readout, quantum logic gates, and controlled dynamics of more than 100 qubits have been demonstrated, with systems approaching reliable computations with hundreds of qubits. Rydberg platforms do not face superconducting-gap thermodynamics, and thus serve as a useful contrast: the 4 K question is specific to superconducting technology, and competing platforms scale under a different constraint set.

**Control and software stack.** Reference [2] presents Tierkreis, a higher-order dataflow graph representation and runtime for compositional quantum-classical hybrid algorithms, motivated by the remote nature of quantum computers, cloud and distributed computing needs, and long-running algorithms. Reference [4] unifies communication paradigms in measurement-based delegated quantum computing, where clients with low quantum capabilities outsource computations to a server, with blindness of inputs facilitated by the measurement-based framework. Neither work addresses cryogenics, but both establish that large-scale quantum computing presumes a substantial classical control and networking stack; a 4 K architecture that relaxes the refrigeration envelope also relaxes the physical integration constraints on that stack.

**QNFO corpus documents.** References [9], [10], and [11] are the author's corpus documents on thermodynamic and quantum constraints on scalable quantum computing, thermodynamic and informational bottlenecks of scalable fault-tolerant quantum computation, and the thermodynamic imperative, respectively; reference [12] concerns syntactic generation. The supplied bibliography entries for [9]–[12] contain no abstract text, so no further substantive detail about their contents can be stated here; we cite them as the provenance of the thermodynamic-bottleneck conjecture investigated in this paper.

## 3. Methods

### 3.1 Thermal model

We model the qubit's thermal environment by a single temperature $T_1 = 4\ \mathrm{K}$ (the operating point under test) and compare against reference temperatures $T_{\mathrm{ref}} = 1.5\ \mathrm{K}$ (the silicon-spin-qubit demonstration temperature named in the motivating research idea) and $T_{\mathrm{mK}} = 0.02\ \mathrm{K}$ (a representative dilution-refrigerator stage). The thermal energy scale in frequency units is

$$\frac{k_{B}T}{h} = \frac{T}{\Theta_0}, \qquad \Theta_0 \equiv \frac{h}{k_{B}},$$

where $k_{B} = 1.380649\times10^{-23}\ \mathrm{J/K}$ is Boltzmann's constant and $h = 6.62607015\times10^{-34}\ \mathrm{J\,s}$ is Planck's constant, both exact SI defining values. We compute $\Theta_0$ explicitly in Section 4.

### 3.2 Superconducting gap model

For a BCS superconductor, we take the gap in frequency units as

$$\frac{2\Delta}{h} = \beta\,\frac{k_{B}T_{c}}{h}, \qquad \beta = 3.53,$$

with $\beta = 3.53$ the standard weak-coupling BCS ratio $2\Delta/(k_{B}T_{c})$, used here as a stated modeling assumption. For niobium we use the gap quoted in the motivating research idea, $2\Delta_{\mathrm{Nb}}/h \approx 700$ GHz, and for aluminum we use the critical temperature $T_{c,\mathrm{Al}} = 1.2$ K quoted in the same idea. The thermal quasiparticle fraction is estimated by the Boltzmann factor

$$\epsilon_{\mathrm{qp}}(T) \equiv e^{-\Delta/(k_{B}T)} = e^{-\frac{1}{2}\,\frac{2\Delta/h}{k_{B}T/h}},$$

which we treat as the per-excitation thermal error probability scale; a full Fermi–Dirac treatment would change only prefactors, not the exponential scaling, and we flag this as a modeling simplification.

### 3.3 Error budget and suppression requirement

We define a fault-tolerance target physical error rate per operation $p_{\mathrm{target}} = 10^{-4}$, adopted as a stated design assumption representative of error-correction requirements (we do not attribute this number to any cited work). The required suppression factor for a thermally activated error channel of magnitude $\epsilon_{\mathrm{qp}}$ is

$$S \equiv \frac{\epsilon_{\mathrm{qp}}(T_1)}{p_{\mathrm{target}}}.$$

Parity protection, following the mechanism stated in [6], is modeled as an idealized suppression of quasiparticle-induced *dephasing and leakage of the parity-encoded logical state*, because the computational information is coupled to and stored in fermion parity rather than in charge-mode occupation. We evaluate which channels this idealization covers and which it does not.

### 3.4 Cooling-power model

We adopt from the motivating research idea the ratio $\eta = 2\times10^{4}$ between available cooling power at 4 K and at the dilution-refrigerator stage. To make this concrete we further assume, as a labeled assumption and not a measurement, a millikelvin cooling budget $P_{\mathrm{mK}} = 1\ \mu\mathrm{W}$, giving $P_{4\,\mathrm{K}} = \eta P_{\mathrm{mK}} = 20\ \mathrm{mW}$. All conclusions that depend on cooling power scale linearly with $P_{\mathrm{mK}}$.

## 4. Analysis

Every input number is stated with its source, and every arithmetic step is shown.

**Step 1: Boltzmann constant in frequency units.**

$$\frac{k_{B}}{h} = \frac{1.380649\times10^{-23}\ \mathrm{J/K}}{6.62607015\times10^{-34}\ \mathrm{J\,s}} = 2.08366\times10^{10}\ \mathrm{Hz/K} = 20.837\ \mathrm{GHz/K}.$$

(Arithmetic: $1.380649/6.62607015 = 0.208366$; exponents $-23-(-34) = +11$; so $0.208366\times10^{11} = 2.08366\times10^{10}$.)

**Step 2: Thermal frequency scale at each temperature.**

$$\frac{k_{B}T_1}{h} = 20.837\ \mathrm{GHz/K} \times 4\ \mathrm{K} = 83.35\ \mathrm{GHz},$$
$$\frac{k_{B}T_{\mathrm{ref}}}{h} = 20.837 \times 1.5 = 31.26\ \mathrm{GHz},$$
$$\frac{k_{B}T_{\mathrm{mK}}}{h} = 20.837 \times 0.02 = 0.4167\ \mathrm{GHz}.$$

**Step 3: Niobium gap ratios.** With $2\Delta_{\mathrm{Nb}}/h = 700$ GHz (input: motivating research idea), $\Delta_{\mathrm{Nb}}/h = 350$ GHz. The gap-to-thermal ratios are

$$r_1 = \frac{\Delta_{\mathrm{Nb}}/h}{k_{B}T_1/h} = \frac{350}{83.35} = 4.199, \qquad r_{\mathrm{ref}} = \frac{350}{31.26} = 11.20, \qquad r_{\mathrm{mK}} = \frac{350}{0.4167} = 840.0.$$

**Step 4: Thermal quasiparticle fractions.**

$$\epsilon_{\mathrm{qp}}(T_1) = e^{-4.199} = 0.014996 \approx 1.50\times10^{-2},$$
$$\epsilon_{\mathrm{qp}}(T_{\mathrm{ref}}) = e^{-11.20} = 1.367\times10^{-5},$$
$$\epsilon_{\mathrm{qp}}(T_{\mathrm{mK}}) = e^{-840.0} \approx 10^{-364.8}.$$

(For the last: $-840/\ln 10 = -840/2.302585 = -364.8$.) The ratio between the 4 K and 1.5 K quasiparticle fractions is

$$\frac{\epsilon_{\mathrm{qp}}(T_1)}{\epsilon_{\mathrm{qp}}(T_{\mathrm{ref}})} = e^{-(4.199-11.20)} = e^{7.001} = 1.097\times10^{3},$$

i.e., operating at 4 K rather than 1.5 K costs about a factor of $1.1\times10^{3}$ in thermally activated quasiparticle population for niobium.

**Step 5: Aluminum exclusion.** With $T_{c,\mathrm{Al}} = 1.2$ K (input: motivating research idea) and the BCS model of Section 3.2,

$$\frac{2\Delta_{\mathrm{Al}}}{h} = 3.53 \times 20.837\ \mathrm{GHz/K} \times 1.2\ \mathrm{K} = 3.53 \times 25.004\ \mathrm{GHz} = 88.26\ \mathrm{GHz}, \qquad \frac{\Delta_{\mathrm{Al}}}{h} = 44.13\ \mathrm{GHz}.$$

Since $k_{B}T_1/h = 83.35$ GHz $> \Delta_{\mathrm{Al}}/h = 44.13$ GHz, and more directly since $T_1 = 4\ \mathrm{K} > T_{c,\mathrm{Al}} = 1.2\ \mathrm{K}$, aluminum is a normal metal at the 4 K operating point: it cannot host a superconducting gap there at all. The Boltzmann factor is undefined (the gap closes), so aluminum-based Josephson junctions are categorically excluded at 4 K, independent of any protection scheme.

**Step 6: Required suppression factor.** Against the stated target $p_{\mathrm{target}} = 10^{-4}$:

$$S = \frac{\epsilon_{\mathrm{qp}}(T_1)}{p_{\mathrm{target}}} = \frac{1.50\times10^{-2}}{10^{-4}} = 1.50\times10^{2} = 150.$$

For comparison, at $T_{\mathrm{ref}} = 1.5$ K the same target requires only

$$S_{\mathrm{ref}} = \frac{1.367\times10^{-5}}{10^{-4}} = 0.137,$$

i.e., no suppression at all is needed at 1.5 K for this channel — the thermal quasiparticle fraction already sits below the target.

**Step 7: Cooling-power arithmetic.** With the assumed $P_{\mathrm{mK}} = 1\ \mu\mathrm{W}$ and $\eta = 2\times10^{4}$ (input: motivating research idea):

$$P_{4\,\mathrm{K}} = \eta\,P_{\mathrm{mK}} = 2\times10^{4} \times 1\times10^{-6}\ \mathrm{W} = 2\times10^{-2}\ \mathrm{W} = 20\ \mathrm{mW}.$$

Equivalently, the 4 K stage can supply the same cooling power as the millikelvin stage while supporting a heat load $2\times10^{4}$ times larger, or the same heat load with $2\times10^{4}$ times smaller refrigerator count per watt.

**Step 8: Break-even temperature for unprotected niobium.** The temperature at which $\epsilon_{\mathrm{qp}} = p_{\mathrm{target}}$ for unprotected niobium satisfies $r(T) = \ln(10^{4}) = 9.210$, so

$$\frac{k_{B}T^{*}}{h} = \frac{350\ \mathrm{GHz}}{9.210} = 38.00\ \mathrm{GHz} \quad\Rightarrow\quad T^{*} = \frac{38.00}{20.837}\ \mathrm{K} = 1.824\ \mathrm{K}.$$

Thus an *unprotected* niobium qubit meets the $10^{-4}$ thermal-quasiparticle target only below $T^{*} \approx 1.82$ K; at 4 K it misses by the factor $S = 150$.

**Step 9: Parity-protection requirement.** The parity-protected mechanism of [6] must therefore deliver a suppression of at least $S = 150$ on the thermally activated quasiparticle channel at 4 K. In the idealized model of Section 3.3, parity coupling is insensitive to quasiparticle excitations by construction, so the *logical* error contribution of thermal quasiparticles is suppressed by more than $150$ provided the physical parity measurement itself remains accurate at 4 K. Channels *not* covered by this idealization — dielectric two-level-system loss in oxides such as $\mathrm{Nb_2O_5}$, quasiparticle poisoning of unprotected ancillary junctions, and thermal noise in the parity readout chain — must be budgeted separately; the motivating idea flags thermally activated two-level-system decoherence in $\mathrm{Nb_2O_5}$ as a candidate residual channel, but no quantitative loss tangent is supplied in the input material, so we report it as an open parameter rather than a number.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic, or are explicitly labeled projections.

1. **Thermal scale.** $k_{B}T/h = 83.35$ GHz at $T_1 = 4$ K, versus $31.26$ GHz at 1.5 K and $0.4167$ GHz at 20 mK (computed, Steps 1–2).

2. **Niobium survives but is only moderately protected.** With $2\Delta_{\mathrm{Nb}}/h = 700$ GHz, the quasiparticle fraction at 4 K is $\epsilon_{\mathrm{qp}} = 1.50\times10^{-2}$, versus $1.367\times10^{-5}$ at 1.5 K and $\approx 10^{-365}$ at 20 mK (computed, Steps 3–4). The 4 K penalty relative to 1.5 K is a factor of $1.097\times10^{3}$ (computed, Step 4).

3. **Aluminum is excluded.** At 4 K, aluminum ($T_{c,\mathrm{Al}} = 1.2$ K) is a normal metal; its BCS gap $2\Delta_{\mathrm{Al}}/h = 88.26$ GHz lies below the thermal scale (computed, Step 5). Any 4 K superconducting architecture must therefore avoid aluminum Josephson junctions.

4. **Suppression requirement.** Against the stated target $p_{\mathrm{target}} = 10^{-4}$, a 4 K parity-protected qubit must suppress thermally activated quasiparticle errors by $S = 150$; an unprotected niobium qubit meets the target only below $T^{*} \approx 1.82$ K (computed, Steps 6 and 8).

5. **Cooling-power dividend.** Under the labeled assumption $P_{\mathrm{mK}} = 1\ \mu\mathrm{W}$ and the input ratio $\eta = 2\times10^{4}$, the 4 K stage offers $P_{4\,\mathrm{K}} = 20$ mW (computed, Step 7). *Projection:* if parity protection achieves its idealized suppression ($S_{\mathrm{achieved}} \geq 150$) and if the residual two-level-system and readout channels are held at or below $10^{-4}$ per operation — two conditions not demonstrated here — then a 4 K parity-protected processor would gain the full $\eta$-fold cooling headroom at unchanged logical error rates. The uncertainty in this projection is dominated by the unquantified $\mathrm{Nb_2O_5}$ dielectric loss and readout-chain thermal noise, which we cannot bound from the supplied material.

6. **Comparative framing.** Rydberg platforms have demonstrated more than 100 qubits with high-fidelity gates and readout [5], and NISQ-era superconducting devices operate in the 50–100 qubit range with noise-limited circuit depth [8]; the 4 K question is whether superconducting technology can match that trajectory while escaping the millikelvin refrigeration envelope.

## 6. Discussion

**What the result does and does not show.** The analysis shows a sharp asymmetry: conventional aluminum-based superconducting qubits are categorically impossible at 4 K (Step 5), while niobium-based parity-protected qubits face a finite, quantified requirement — a suppression factor of $S = 150$ on one identified channel — that the mechanism described in [6] is designed to meet in principle. It does *not* demonstrate that a full 4 K fault-tolerant processor is achievable, because three error channels remain unquantified: thermally activated two-level-system loss in $\mathrm{Nb_2O_5}$ (no loss-tangent data in the supplied material), quasiparticle poisoning of unprotected ancillary elements required for gate operations, and thermal noise in parity readout at 4 K, where the thermal photon population at 83 GHz scale is non-negligible for any readout line not heavily attenuated and filtered.

**Against the conjecture.** The strongest counterargument is that the idealized parity-protection model of Section 3.3 is too generous. The top-transmon summary [6] states the coupling is to fermion parity "irresistible... irrespective of any quasiparticle excitations," but the supplied summary contains no device-level fidelity figures, and real hybrid topological–superconducting devices inherit the sub-gap quality of their parent materials. If the effective parity-conserving suppression is even modestly below $S = 150$, the 4 K operating point fails the stated target; the margin is only about two orders of magnitude, which is thin by the standards of superconducting device variability. A second counterargument: the Boltzmann-factor error model ignores prefactors and nonequilibrium quasiparticle populations, which in practice can dominate equilibrium populations; if nonequilibrium quasiparticles raise the effective $\epsilon_{\mathrm{qp}}$ by more than $S$, the conclusion reverses even with perfect parity protection of the logical subspace.

**What would falsify the claims.** Three results would falsify the paper's central claims: (i) a demonstration of a parity-protected qubit whose logical error rate at 4 K exceeds $1.50\times10^{-2}$ per operation attributable to quasiparticles, showing the parity mechanism does not deliver $S \geq 150$; (ii) a measurement of $\mathrm{Nb_2O_5}$ or electrode-surface two-level-system loss at 4 K exceeding $10^{-4}$ per gate, closing the 4 K window through a channel parity protection cannot address; (iii) evidence that the cooling-power ratio $\eta = 2\times10^{4}$ is not realizable in integrated control environments, undermining the thermodynamic motivation. Conversely, a demonstration of sub-$10^{-4}$ logical quasiparticle error at 4 K in a niobium hybrid device would strongly confirm the viability conjecture.

**Open questions.** What is the temperature dependence of two-level-system dielectric loss in niobium oxides between 1.5 K and 4 K? Can all ancillary junctions in a parity-protected gate scheme be made of high-gap superconductors, or does the scheme intrinsically require aluminum? Does parity readout fidelity at 4 K degrade below the levels needed for error correction? How do the energetic analyses of protected superconducting qubits [3] compare when the metric is cooling power rather than computation time? And how should the hybrid runtime and delegation stacks of [2] and [4] be re-architected for a 4 K, high-integration-density plant?

**Limitations of the literature base.** The supplied bibliography contains no device-level experimental papers on quasiparticle poisoning or dielectric loss, and the QNFO entries [9]–[12] carry no abstract text from which quantitative claims could be drawn; the quantitative content of this paper therefore rests on the constants and gap values stated in the motivating research idea plus derivations from them. The motivating idea also calls for Monte Carlo simulation of quasiparticle poisoning rates and comparison against demonstrated 1.5 K silicon spin qubit data; no such simulation results or spin-qubit datasets are supplied in the input material, so this paper provides the analytic error budget that such a simulation would need to reproduce, and leaves the stochastic treatment as future work.

## 7. Conclusion

We tested the conjecture that parity-protected qubits can operate at 4 K, exploiting the $\eta = 2\times10^{4}$ cooling-power advantage over dilution refrigeration. The quantitative verdict is conditional. Aluminum-based qubits are excluded outright at 4 K by thermodynamics alone. Niobium-based unprotected qubits fail a $10^{-4}$ error target by a computed factor of $S = 150$. Parity-protected architectures of the type proposed in [6] are the only known route to closing that factor, because their coupling to fermion parity is by construction insensitive to quasiparticle excitations; whether the mechanism delivers the required two-order-of-magnitude suppression in practice, and whether the unquantified dielectric and readout channels stay below target, are the decisive open questions. The 4 K operating point is therefore not fundamentally excluded, but it is contingent on a specific, testable protection mechanism — a sharper statement than either unconditional optimism or blanket rejection, and one that direct experiment at 4 K can settle.

## References

[1] arXiv:2403.02240v5 | Quantum Computing: Vision and Challenges

[2] arXiv:2211.02350v1 | Tierkreis: A Dataflow Framework for Hybrid Quantum-Classical Computing

[3] arXiv:2605.19854v1 | Unveiling Energetic Advantage in Superconducting Cat-Qubits Quantum Computation

[4] arXiv:2506.21988v2 | Unifying communication paradigms in measurement-based delegated quantum computing

[5] arXiv:2011.03031v2 | Quantum simulation and computing with Rydberg-interacting qubits

[6] arXiv:1105.0315v1 | Top-transmon: hybrid superconducting qubit for parity-protected quantum computation

[7] arXiv:1805.05224v3 | How many qubits are needed for quantum computational supremacy?

[8] arXiv:1801.00862v3 | Quantum Computing in the NISQ era and beyond

[9] QNFO: Thermodynamic and Quantum Constraints on Scalable Quantum Computing | DOI 10.5281/zenodo.17937531

[10] QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation | DOI 10.5281/zenodo.17955898

[11] QNFO: Thermodynamic Imperative | DOI 10.5281/zenodo.17928156

[12] QNFO: Syntactic Generation | DOI 10.5281/zenodo.22758173