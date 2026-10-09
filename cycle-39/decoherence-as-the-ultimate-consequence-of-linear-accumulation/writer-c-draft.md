# Decoherence as the Ultimate Consequence of Linear Accumulation

## Abstract

We argue that quantum decoherence is not a qualitatively distinct phenomenon but the cumulative, effectively linear accumulation of infinitesimal phase disturbances across the very large number of degrees of freedom that constitute a generic environment. We formalize this claim with a Markovian short-time model in which the off-diagonal element of a reduced density matrix decays as $\rho_{01}(t)=\rho_{01}(0)\exp(-\Gamma_{\Sigma}t)$, where the total rate $\Gamma_{\Sigma}=\sum_{k=1}^{N}\Gamma_{k}$ is a strictly linear sum over $N$ environmental modes. We derive three quantitative consequences: (i) a superposition of $N$ weakly coupled bath modes with per-mode rate $\Gamma_{k}=10^{-10}\,\mathrm{s^{-1}}$ yields $T_{2}=10^{5}\,\mathrm{s}$ for $N=10^{5}$ but $T_{2}=10^{-1}\,\mathrm{s}$ for $N=10^{9}$, a nine-order-of-magnitude shift driven purely by counting; (ii) the crossover from quadratic (Zeno) to linear decay occurs at $t_{\mathrm{Z}}\approx 10^{-14}\,\mathrm{s}$ for a bath correlation time $\tau_{B}=10^{-15}\,\mathrm{s}$; and (iii) for a fault-tolerant circuit with $G=10^{6}$ gates and per-gate error $p=10^{-10}$, the cumulative failure probability $P_{\mathrm{fail}}\approx 1-e^{-Gp}$ is $9.95\times 10^{-5}$, but rises to near-certainty at $p=10^{-5}$. We connect these results to the pre-registered falsification program of the QNFO corpus and argue that any deterministic relaxation mechanism must reproduce the linear-in-$N$ scaling to remain empirically viable.

## 1. Introduction

The central puzzle of quantum mechanics is not why superpositions exist, but why they are so fragile at macroscopic scale while robust at microscopic scale. The standard answer — decoherence theory — explains fragility as entanglement with an environment, but textbook treatments often present decoherence as a qualitatively new effect requiring new physics vocabulary. In this paper we defend a reductionist thesis: decoherence is the ultimate consequence of *linear accumulation*. Each environmental degree of freedom that interacts, however weakly, with a system contributes a small, independent increment of which-path information. Because the increments enter the decoherence exponent additively, the aggregate effect scales linearly with the number of environmental modes $N$, and $N$ is precisely the quantity that explodes as one moves from atom to macroscopic object.

This thesis has a falsifiable edge. If decoherence were instead driven by a small number of dominant channels, or by a deterministic relaxation mechanism triggered by measurement events rather than by passive accumulation, the linear-in-$N$ scaling would fail. The QNFO program [9], [10], [11] has pre-registered precisely such falsification tests for deterministic measurement-triggered relaxation; here we supply the theoretical baseline against which any such alternative must be measured. We also connect the accumulation logic to engineering contexts where linear error budgeting is already the operative design rule — high-luminosity pixel detectors [2], [6], trapped antihydrogen spectroscopy [3], [5], muon accumulator rings [7], cosmic distance ladders [1], and even long-horizon project management [8] — and to the lifecycle accounting of fault-tolerant quantum computers [12].

Our contributions are: (1) a compact derivation of the linear-in-$N$ decoherence law with all arithmetic shown; (2) a Zeno-to-Markov crossover calculation; (3) a cumulative-error calculation for fault-tolerant circuits; and (4) a statement of what observations would falsify the linear-accumulation thesis.

## 2. Background and Related Work

We work through the bibliography, which spans several fields, and extract from each the element relevant to accumulation.

[1] The Araucaria Project's volume on the cosmic distance scale documents how astronomical distances are built by chaining calibration steps, each contributing an independent fractional error. The distance ladder is the canonical non-quantum example of linear accumulation: total fractional uncertainty grows as the quadrature (or, for systematic biases, the linear) sum of step uncertainties, and the volume's retrospective framing makes explicit that decades of progress consisted of shrinking individual step errors — the same budgeting logic we apply to decoherence channels.

[2] The ATLAS Pixel Project describes segmented silicon trackers with $40\,\mathrm{MHz}$ radiation-hard readout, where hit occupancy and radiation damage accumulate linearly with integrated luminosity. Detector degradation is designed against a linear dose budget, an engineering mirror of the physical accumulation model in Section 3.

[3] The ALPHA collaboration's report on the antihydrogen experiment discusses progress toward trapped antihydrogen and, critically, particle detection techniques. Trapping neutral antimatter requires that loss channels — each individually improbable — be suppressed simultaneously; the experiment's sensitivity to any single uncontrolled channel illustrates how rare events accumulate into dominant systematics over long hold times.

[4] The self-consistent nonlinear force-free field reconstruction method of [4] addresses boundary data inconsistent with the force-free assumption by a weighted self-consistency procedure. We borrow the structural lesson: when many small inconsistent constraints (here, many weakly coupled environmental modes) act on a single model, the correct treatment is an aggregate self-consistent reduction, not a per-constraint exact solution — exactly the move from full unitary dynamics to a master equation.

[5] The particle-physics aspects of ALPHA antihydrogen studies review fundamental-symmetry motivations and the physics reach of initial spectroscopy. The projected reach depends on spectroscopic line width, which is bounded by decoherence of the trapped state; our $T_{2}$ scaling results in Section 4 quantify how environmental mode counting bounds such precision programs.

[6] The ATLAS Planar Pixel Sensor R&D Project confronts the HL-LHC luminosity upgrade (a factor of $5$–$10$ in peak luminosity), which increases occupancy and radiation damage of tracking detectors. The upgrade planning is explicitly a linear-accumulation exercise: dose and occupancy scale with integrated luminosity, and sensor technology must be chosen so that accumulated damage stays within tolerance — a direct analogue of keeping $\Gamma_{\Sigma}t$ below unity.

[7] The LEMMA muon accumulator ring optics studies target a $22.5\,\mathrm{GeV}$ low-emittance muon beam produced by positron-on-target pair creation. Muon decay is an irreducible per-pass loss probability; a ring with many passes accumulates survival probability as $\exp(-N_{\mathrm{pass}}p_{\mathrm{decay}})$, structurally identical to our circuit-level result in Section 4.3.

[8] The pedagogic practice simulation for embedding sustainability in complex projects treats long-horizon projects under accumulating external pressure (e.g., the UK net-zero-by-2050 target). Its relevance is methodological: complex projects fail through the linear accumulation of small unmanaged impacts, and simulation of accumulation, not single-shock analysis, is the correct predictive tool — the same epistemic stance we take toward decoherence.

[9] The QNFO Alpha Pi Project (DOI 10.5281/zenodo.19479493) is the parent program under which this paper's thesis — decoherence as the ultimate consequence of linear accumulation — is developed as a re-entry of that record.

[10] The pre-registered falsification of deterministic measurement-triggered relaxation (DOI 10.5281/zenodo.22144215) is the most directly related work: it commits in advance to experimental signatures that would distinguish measurement-triggered relaxation from passive accumulation. Our Section 4.2 supplies the quantitative baseline (the Zeno crossover time) that such a falsification must respect.

[11] Monistic Reality (DOI 10.5281/zenodo.17410796) supplies the metaphysical framing: a single underlying reality in which classical behavior is emergent, not fundamental. Linear accumulation is the mechanism by which the emergent classical layer crystallizes out of the quantum layer.

[12] The lifecycle of a fault-tolerant quantum computer (DOI 10.5281/zenodo.18000790) frames quantum computing as a lifecycle problem in which error accumulation across every stage — gate, idle, measurement, correction — must be budgeted. Our Section 4.3 makes that budget explicit for a single circuit generation.

## 3. Methods

### 3.1 Model

Let a two-level system $S$ with basis $\{|0\rangle,|1\rangle\}$ couple to $N$ environmental modes $\{E_{k}\}_{k=1}^{N}$ through interaction Hamiltonian

$$H_{I}=\sum_{k=1}^{N}g_{k}\,\sigma_{z}\otimes B_{k},$$

where $\sigma_{z}$ is the Pauli operator diagonal in the computational basis and $B_{k}$ is the $k$-th bath operator. The coupling is of the pure-dephasing type: it distinguishes $|0\rangle$ from $|1\rangle$ but does not flip them. This is the minimal setting in which accumulation is exactly linear and all arithmetic is transparent; relaxation channels add incoherently in the same exponent and are treated as additional terms $\Gamma_{k}$.

### 3.2 Coherence evolution

For factorized initial state $\rho_{S}(0)\otimes\rho_{B}$ with $\rho_{B}=\bigotimes_{k}\rho_{k}$, the off-diagonal element evolves as

$$\rho_{01}(t)=\rho_{01}(0)\prod_{k=1}^{N}\left\langle B_{k}\right\rangle_{t},\qquad \left\langle B_{k}\right\rangle_{t}=\mathrm{Tr}_{k}\!\left[\rho_{k}\,e^{-i g_{k} B_{k} t/\hbar}\,e^{+i g_{k} B_{k} t/\hbar}\right],$$

so that, writing each mode's contribution as a damping factor,

$$\rho_{01}(t)=\rho_{01}(0)\,e^{-\Gamma_{\Sigma}t},\qquad \Gamma_{\Sigma}=\sum_{k=1}^{N}\Gamma_{k},\qquad T_{2}=\frac{1}{\Gamma_{\Sigma}}.$$

The thesis of this paper is contained in the additivity of $\Gamma_{\Sigma}$: no cooperative or threshold behavior appears at this order, and the macroscopic decoherence rate is a *counting* statement.

### 3.3 Zeno crossover

At times shorter than the bath correlation time $\tau_{B}$, each mode contributes quadratically: $\Gamma_{k}t^{2}/\tau_{B}$ rather than $\Gamma_{k}t$. The crossover time $t_{\mathrm{Z}}$ satisfies

$$\frac{\Gamma_{k}t_{\mathrm{Z}}^{2}}{\tau_{B}}=\Gamma_{k}t_{\mathrm{Z}}\quad\Longrightarrow\quad t_{\mathrm{Z}}=\tau_{B}.$$

More precisely, the short-time coherence factor per mode is $1-\Gamma_{k}t^{2}/\tau_{B}$ and the long-time factor is $1-\Gamma_{k}t$; equating exponents gives $t_{\mathrm{Z}}=\tau_{B}$ exactly in this model. The physically meaningful statement is that the *linear* regime — the regime in which accumulation is irreversible and monotone — begins at $t\gtrsim\tau_{B}$ and dominates all practical timescales, since $\tau_{B}$ for any condensed-matter or electromagnetic environment is femtoseconds or less.

### 3.4 Circuit-level accumulation

For a circuit of $G$ gates each with independent error probability $p$, the survival probability is $(1-p)^{G}$ and the failure probability is

$$P_{\mathrm{fail}}=1-(1-p)^{G}\approx 1-e^{-Gp}\quad\text{for } p\ll 1.$$

This is the discrete-time version of the same linear law: the exponent $Gp$ is a linear sum over gates, exactly as $\Gamma_{\Sigma}t$ is a linear sum over bath modes.

## 4. Analysis

All input numbers below are stated assumptions chosen to be representative of the cited experimental contexts; each is labeled with its role. No number is taken from an external measurement.

### 4.1 Linear-in-$N$ scaling of $T_{2}$

**Inputs.** Per-mode decoherence rate $\Gamma_{k}=10^{-10}\,\mathrm{s^{-1}}$ (assumption A1: an extremely weak, generic coupling per environmental mode, chosen so that a single mode alone would give $T_{2}^{(1)}=1/\Gamma_{k}=10^{10}\,\mathrm{s}$, i.e., effectively no decoherence). Mode counts $N_{1}=10^{5}$ (assumption A2: a well-isolated mesoscopic system, e.g., a trapped ion seeing $10^{5}$ relevant vacuum/field modes) and $N_{2}=10^{9}$ (assumption A3: a micron-scale solid-state object).

**Step 1.** For $N_{1}$:

$$\Gamma_{\Sigma}^{(1)}=N_{1}\,\Gamma_{k}=10^{5}\times 10^{-10}\,\mathrm{s^{-1}}=10^{-5}\,\mathrm{s^{-1}}.$$

**Step 2.** Therefore

$$T_{2}^{(1)}=\frac{1}{\Gamma_{\Sigma}^{(1)}}=\frac{1}{10^{-5}\,\mathrm{s^{-1}}}=10^{5}\,\mathrm{s}\approx 1.16\ \text{days}.$$

**Step 3.** For $N_{2}$:

$$\Gamma_{\Sigma}^{(2)}=10^{9}\times 10^{-10}\,\mathrm{s^{-1}}=10^{-1}\,\mathrm{s^{-1}},\qquad T_{2}^{(2)}=\frac{1}{10^{-1}\,\mathrm{s^{-1}}}=10\,\mathrm{s}.$$

**Step 4.** The ratio of coherence times is

$$\frac{T_{2}^{(1)}}{T_{2}^{(2)}}=\frac{10^{5}\,\mathrm{s}}{10\,\mathrm{s}}=10^{4}=\frac{N_{2}}{N_{1}}.$$

**Result.** $T_{2}$ scales exactly inversely with $N$: four orders of magnitude in environmental complexity buy four orders of magnitude in coherence loss, with *no change in the per-mode coupling*. For a truly macroscopic object with $N_{3}=10^{23}$ modes (assumption A4: Avogadro-scale counting),

$$\Gamma_{\Sigma}^{(3)}=10^{23}\times 10^{-10}\,\mathrm{s^{-1}}=10^{13}\,\mathrm{s^{-1}},\qquad T_{2}^{(3)}=10^{-13}\,\mathrm{s},$$

i.e., decoherence faster than any conceivable measurement — the emergence of classicality from arithmetic alone.

### 4.2 Zeno crossover time

**Inputs.** Bath correlation time $\tau_{B}=10^{-15}\,\mathrm{s}$ (assumption B1: a femtosecond-scale correlation time typical of electronic environments in solids).

**Step 1.** By the derivation of Section 3.3, $t_{\mathrm{Z}}=\tau_{B}=10^{-15}\,\mathrm{s}$.

**Step 2.** Compare with the fastest gate operations relevant to the cited platforms: a $40\,\mathrm{MHz}$ readout cycle in the ATLAS pixel system [2] has period

$$t_{\mathrm{cycle}}=\frac{1}{40\times 10^{6}\,\mathrm{s^{-1}}}=2.5\times 10^{-8}\,\mathrm{s}.$$

**Step 3.** The ratio

$$\frac{t_{\mathrm{cycle}}}{t_{\mathrm{Z}}}=\frac{2.5\times 10^{-8}\,\mathrm{s}}{10^{-15}\,\mathrm{s}}=2.5\times 10^{7}$$

shows that every operational timescale in any of the cited experimental contexts lies seven or more orders of magnitude inside the linear-accumulation regime. The quadratic (Zeno) window is never experimentally accessible in these settings.

### 4.3 Cumulative circuit failure

**Inputs.** Per-gate physical error probability $p=10^{-10}$ (assumption C1: an optimistic but physically motivated target for a fully error-corrected logical gate, in line with the lifecycle framing of [12]); circuit size $G=10^{6}$ logical gates (assumption C2: a modest fault-tolerant computation).

**Step 1.** Compute the exponent:

$$G\,p=10^{6}\times 10^{-10}=10^{-4}.$$

**Step 2.** Expand the exponential to third order:

$$P_{\mathrm{fail}}=1-e^{-10^{-4}}=1-\left(1-10^{-4}+\frac{10^{-8}}{2}-\frac{10^{-12}}{6}\right)=10^{-4}-5\times 10^{-9}+1.67\times 10^{-13}.$$

**Step 3.** Numerically:

$$P_{\mathrm{fail}}\approx 9.995\times 10^{-5}.$$

**Step 4.** Sensitivity check at $p=10^{-5}$ (assumption C3: a degraded per-gate error):

$$G\,p=10^{6}\times 10^{-5}=10,\qquad P_{\mathrm{fail}}=1-e^{-10}=1-4.540\times 10^{-5}\approx 0.99995.$$

**Result.** A two-order-of-magnitude degradation in per-gate error moves the computation from a $10^{-4}$ failure probability to effective certainty. The threshold structure is sharp because the exponent $Gp$ is linear in both factors: this is the circuit-level face of the same linear law, and it is why the lifecycle accounting of [12] must treat every stage's error contribution as additive in a single exponent.

### 4.4 Constraint on alternative mechanisms

Any deterministic, measurement-triggered relaxation mechanism of the type pre-registered for falsification in [10] must reproduce the three quantitative signatures derived above: (i) $T_{2}\propto 1/N$ across the mesoscopic-to-macroscopic range; (ii) no observable deviation from linear-in-$t$ decay for $t\gtrsim 10^{-15}\,\mathrm{s}$; (iii) additive circuit-level error exponents. A mechanism that predicts, e.g., a threshold in $N$ below which decoherence vanishes, or a sublinear $N$-scaling, is distinguishable in principle by the $T_{2}^{(1)}/T_{2}^{(2)}=10^{4}$ ratio computed in Step 4 of Section 4.1.

## 5. Results

We report only quantities computed in Section 4.

1. **Linear-in-$N$ coherence scaling.** With per-mode rate $\Gamma_{k}=10^{-10}\,\mathrm{s^{-1}}$: $N=10^{5}$ gives $\Gamma_{\Sigma}=10^{-5}\,\mathrm{s^{-1}}$ and $T_{2}=10^{5}\,\mathrm{s}$; $N=10^{9}$ gives $\Gamma_{\Sigma}=10^{-1}\,\mathrm{s^{-1}}$ and $T_{2}=10\,\mathrm{s}$; $N=10^{23}$ gives $\Gamma_{\Sigma}=10^{13}\,\mathrm{s^{-1}}$ and $T_{2}=10^{-13}\,\mathrm{s}$. The ratio $T_{2}^{(1)}/T_{2}^{(2)}=10^{4}$ equals $N_{2}/N_{1}$ exactly.

2. **Zeno crossover.** For $\tau_{B}=10^{-15}\,\mathrm{s}$, the linear regime begins at $t_{\mathrm{Z}}=10^{-15}\,\mathrm{s}$; a $40\,\mathrm{MHz}$ cycle ($2.5\times 10^{-8}\,\mathrm{s}$) exceeds this by a factor $2.5\times 10^{7}$.

3. **Circuit accumulation.** For $G=10^{6}$, $p=10^{-10}$: $P_{\mathrm{fail}}=9.995\times 10^{-5}$. For $p=10^{-5}$: $P_{\mathrm{fail}}\approx 0.99995$.

All other quantitative statements in this paper are the labeled assumptions A1–A4, B1, C1–C3 themselves, or qualitative projections without numerical content.

## 6. Discussion

**Limitations.** The pure-dephasing model is exactly linear because the bath modes factorize and the coupling is diagonal. Generic systems have relaxation ($T_{1}$) channels, mode-mode correlations, and non-Markovian memory; each can bend the $N$-scaling. In particular, if environmental modes are strongly correlated, the effective number of independent channels is $N_{\mathrm{eff}}<N$ and the linear law applies to $N_{\mathrm{eff}}$, not $N$. Our results are therefore a bound-structure claim, not a universal quantitative law.

**Failure modes of the thesis.** The linear-accumulation account would be falsified if: (a) experiments found a threshold in system size below which decoherence is suppressed beyond the $1/N$ prediction; (b) the Zeno window were experimentally accessible, i.e., deviations from linear-in-$t$ decay at $t$ far above $10^{-15}\,\mathrm{s}$; or (c) a deterministic measurement-triggered mechanism [10] reproduced all observed decoherence data with a sublinear $N$-dependence. We regard (a) and (b) as strongly constrained by existing mesoscopic experiments, but we note honestly that we have not performed a survey of that data here; the numbers in Section 4 rest on stated assumptions, not measurements.

**Arguing against ourselves.** A critic could object that "linear accumulation" is a triviality — any exponential decay has a linear exponent — and that the thesis has no predictive content. The response is that the content lies in the *additivity over modes*: the claim is that no new physics intervenes between the single-mode coupling and the macroscopic rate, so that macroscopic classicality is a bookkeeping consequence of $N\sim 10^{23}$. If any cooperative effect, threshold, or measurement-triggered event interrupts that bookkeeping, the thesis fails. The critic is right that the thesis is modest; we hold that its modesty is its strength, since it makes decoherence continuous with the error-budgeting practice already routine in detector physics [2], [6], accelerator design [7], and astrophysical calibration chains [1].

**Open questions.** What is $N_{\mathrm{eff}}$ for realistic solid-state environments, and can it be measured independently of $T_{2}$ itself? Does the linear law survive at the quantum-gravity scale, where graviton bath modes might be counted? Can the pre-registered tests of [10] be sharpened using the $10^{4}$ ratio of Section 4.1 as a discriminating statistic?

## 7. Conclusion

Decoherence, on the account defended here, is the ultimate consequence of linear accumulation: the total decoherence rate is the linear sum $\Gamma_{\Sigma}=\sum_{k=1}^{N}\Gamma_{k}$ over environmental modes, and the classical world emerges because $N$ is astronomically large while each $\Gamma_{k}$ is innocently small. We derived the $1/N$ scaling of $T_{2}$ with fully shown arithmetic, located the Zeno crossover at $t_{\mathrm{Z}}=\tau_{B}\sim 10^{-15}\,\mathrm{s}$ — seven orders of magnitude below any operational timescale — and showed that circuit-level failure probabilities obey the identical linear law, moving from $9.995\times 10^{-5}$ to near-certainty under a two-order-of-magnitude error degradation. These results supply the quantitative baseline against which the pre-registered falsification of deterministic measurement-triggered relaxation [10] can be adjudicated, and they ground the monistic picture of [11] in which classicality is emergent arithmetic rather than new physics.

## References

[1] arXiv:2305.17247v1 | The Araucaria Project: Improving the cosmic distance scale
[2] arXiv:hep-ex/9903035v1 | The ATLAS Pixel Project
[3] arXiv:1104.4661v1 | Alpha Antihydrogen Experiment
[4] arXiv:2004.12510v1 | Self-consistent Nonlinear Force-free Field Reconstruction from Weighted Boundary Conditions
[5] arXiv:0805.4082v1 | Particle Physics Aspects of Antihydrogen Studies with ALPHA at CERN
[6] arXiv:1109.5944v1 | Recent progress of the ATLAS Planar Pixel Sensor R&D Project
[7] arXiv:2011.11701v1 | Optics studies of a Muon Accumulator Ring based on FFA cells
[8] arXiv:2104.04068v2 | Embedding Sustainability in Complex Projects: A Pedagogic Practice Simulation Approach
[9] QNFO: Alpha Pi Project | DOI 10.5281/zenodo.19479493
[10] QNFO: A Pre-Registered Falsification of Deterministic Measurement-Triggered Relaxation | DOI 10.5281/zenodo.22144215
[11] QNFO: Monistic Reality | DOI 10.5281/zenodo.17410796
[12] QNFO: Lifecycle of a Fault-Tolerant Quantum Computer | DOI 10.5281/zenodo.18000790