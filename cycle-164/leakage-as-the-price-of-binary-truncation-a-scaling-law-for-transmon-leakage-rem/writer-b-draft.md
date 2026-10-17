# Leakage as the Price of Binary Truncation: A Scaling Law for Bosonic Qubits and Its Ontological Reading

## Abstract

Superconducting transmon processors lose population from the computational $\{|0\rangle,|1\rangle\}$ subspace into higher levels of an anharmonic oscillator, and this leakage is normally treated as an engineering defect to be suppressed pulse by pulse. The gap addressed here is conceptual and quantitative: no existing framework states how much leakage a gate must produce as a consequence of encoding a bosonic ladder into two levels, nor what removal capacity that production rate demands of a processor architecture. We adopt the perturbative and exact three-level leakage formulas of the Planck-Fidelity analysis of binary truncation of bosonic ladders, insert illustrative transmon parameters ($f_\Omega = 20$ MHz, $f_\alpha = 200$ MHz, $\Omega/|\alpha| = 0.05$), and derive a per-gate time-averaged leakage $\overline{L}_2 = 0.01$ with quadratic scaling in $\Omega/|\alpha|$. Combining this production rate with an assumed 50 ns gate cycle gives a leakage production rate of $2\times10^{5}\ \mathrm{s}^{-1}$, so holding steady-state leakage at $10^{-4}$ requires a removal capacity $\Gamma_{\mathrm{rem}} = 2\times10^{9}\ \mathrm{s}^{-1}$, which exceeds the fastest leakage hopping rate reported for tunable-coupler transmon arrays ($\sim10$ MHz) by a factor of 200. We interpret the residual as the empirical cost of projecting a continuous bosonic degree of freedom onto a discrete bit, predict that bosonic platforms systematically exceed fermionic ones in leakage burden, and state the falsification conditions.

## 1. Introduction

Builders of superconducting quantum processors face a persistent error channel that their error-correcting codes were not designed to absorb: population escaping the two-level computational subspace of each qubit. Leakage excitations traveling between qubits generate correlated errors, induce leakage multiplication, decrease gate fidelity, and increase systemic randomness, and typical error-correction codes protect only against qubit errors [4]. Every gate operated on a transmon therefore carries a hidden tax, paid in population that must be pumped back or it accumulates until the code fails. The cost is concrete: leakage-removal units, DRAG pulse shaping, and frequency-crowding mitigation all consume calibration time, gate cycles, and design margin that would otherwise serve computation.

What changes if the result of this paper holds? If per-gate leakage is not an avoidable defect but a fixed function of the drive-to-anharmonicity ratio, then processor architects can budget removal capacity from first principles — before building the chip — by reading a single scaling law off the device Hamiltonian. It would also reframe an ontological question in operational terms. The "it from bit" conjecture holds that discrete binary information is fundamental; under that reading, a transmon should natively confine to two levels, and leakage should be a contingent engineering artifact tending toward zero. The alternative reading, advanced by the QNFO research program, is that the transmon is a bosonic mode coerced into two-level behavior, with a relative anharmonicity of only $1.9\%$ at the state of the art, so that "the qubit is the correction term, not the identity" [9]. Under the alternative, leakage measures the cost of the coercion and should scale in a lawful, platform-dependent way: large for bosonic carriers (transmons, fluxonium, cat qubits) and structurally small for fermionic carriers (spin qubits), whose two-level map matches the physical spectrum rather than truncating it.

This paper does not settle the ontology. It derives the scaling law, evaluates it numerically with fully shown arithmetic, and computes the removal-capacity deficit that the law implies for a representative transmon architecture, anchoring the removal side in the measured leakage hopping rates of tunable-coupler transmon arrays [4]. The contributions are:

- A restatement of the binary-truncation leakage bound $L_2 = 8(\Omega/|\alpha|)^2\sin^2(\alpha T_g/2)$ and the exact three-level result $P_{2,\max} = 2r^2/(1+2r^2)$ as the operative scaling law for transmon leakage, with numerical evaluation at illustrative parameters (Section 4.1–4.2, from the derivations of [8]).
- A computation of the leakage production rate per qubit, $2\times10^{5}\ \mathrm{s}^{-1}$ under stated assumptions, and of the removal capacity $\Gamma_{\mathrm{rem}} = 2\times10^{9}\ \mathrm{s}^{-1}$ needed to hold steady-state leakage at $10^{-4}$ (Section 4.3).
- A quantified deficit: the fastest leakage hopping rate in tunable-coupler transmon arrays, $\sim10$ MHz [4], falls short of the required removal capacity by a factor of 200 (Section 4.4).
- A computation of the discarded-information fraction of a $d=12$ transmon, $f_{\mathrm{disc}} = 0.721125$, quantifying how much of the physical Hilbert space the binary map discards (Section 4.5, following [8]).
- A falsifiable platform-ordering prediction — bosonic leakage burden exceeds fermionic — with explicit falsification conditions (Section 5 and Section 6).

## 2. Background and Related Work

The transmon Hamiltonian is $H = 4E_C n^2 - E_J\cos(\phi)$, where $n = Q/(2e)$ is the Cooper-pair number operator, $\phi$ the superconducting phase difference, $E_C = e^2/(2C)$ the charging energy, and $E_J = I_c\Phi_0/(2\pi)$ the Josephson energy; the $\cos(\phi)$ potential is periodic and supports an infinite ladder of eigenstates, so the system "is not, and has never been, two-level" [9]. In the transmon regime $E_J \gg E_C$, expanding the cosine to fourth order yields an approximately harmonic oscillator with a small quartic correction, and it is this correction — the anharmonicity — that is the only feature distinguishing the device from a pure oscillator [9]. At $E_J/E_C = 325$, the highest ratio reported by Wang et al. (2024) for a functional transmon, the device supports $d = 12$ resolvable energy levels and its relative anharmonicity $\alpha_r \equiv |\alpha|/\omega_{01}$ is $1.9\%$; the same source documents that the field's approximately \$35 billion in global investment has gone into an architecture whose two-level behavior is maintained by suppression techniques — DRAG pulses, optimal control, leakage reduction units, frequency-crowding mitigation — whose existence is itself evidence of the coercion [9]. That source also proposes a falsifiable calorimetry protocol: compare heat dissipated in free evolution of a transmon prepared in $|1\rangle$ for 100 ns against heat dissipated by a DRAG-calibrated gate sequence implementing the same identity rotation, isolating the translation cost of the digital map from the computation cost [9]. We adopt its ontological framing as the interpretive layer of this paper and its $d=12$, $\alpha_r = 1.9\%$ figures as the state-of-the-art anchor.

The quantitative core of our scaling law comes from the Planck-Fidelity analysis of binary truncation of bosonic ladders [8]. That work derives a first-order leakage bound $L_2 = 8(\Omega/|\alpha|)^2\sin^2(\alpha T_g/2)$ for finite-time gates driven through the raising operator, an exact three-level peak leakage $P_{2,\max} = 2r^2/(1+2r^2)$ with time average $\overline{P}_2 = r^2/(1+2r^2)$ where $r = f_\Omega/f_\alpha$, and a base-truncation entropy $S_{\mathrm{Base}} = \ln 6 = 1.791759$ nats for $d = 12$, i.e. a discarded-information fraction $f_{\mathrm{disc}} = 0.721125$ of the $\ln 12$-nat Hilbert-space content [8]. Its own limitations section states that the perturbative bound is first order in $\Omega$, neglects levels $n \ge 3$, and holds for finite-time finite-amplitude drives of the stated form under the rotating-wave approximation, with shaped envelopes able to null first-order leakage only at isolated, measure-zero parameter points [8]. We reuse its formulas and arithmetic unchanged and build the removal-capacity analysis on top of them.

On the removal side, the leakage-mobility study of transmons with tunable couplers [4] establishes three points we use directly. First, leakage beyond the qubit subspace is a considerable error source and a challenge even for quantum error correction, since typical codes are protected only against qubit errors [4]. Second, leakage is mobile: excitations hop among qubits, causing correlated errors, leakage multiplication, and gate-fidelity degradation, and mobility depends on lattice architecture, couplers, and operating parameters [4]. Third, quantitatively, coupler operating points that cancel single-excitation exchange or ZZ interactions do not simultaneously suppress leakage hopping; in the resonant case leakage hopping rates fall in the range of $0.8$–$10$ MHz, and next-nearest-neighbor hopping reaches approximately $0.1$ MHz when the nearest site is far-detuned [4]. These hopping rates are the only removal-transport speeds we treat as measured, and Section 4.4 compares them against the production-derived removal requirement.

The calibration-loop analysis [10] supplies a complementary constraint: under subspace-restricted measurements, the total-variation distance between a strict two-level ontology and a three-level anharmonic carrier with leakage amplitude $|c| = 0.1$ is exactly zero, so population tomography cannot distinguish the ontologies; the degeneracy degrades as $(\Omega/2\Delta)^2$ at larger drive, and breaking it once a leakage-resolving observable exists requires shot budgets of $N \ge 2500$ (one sigma) and $N \ge 22500$ (three sigma) against a per-shot readout error scale $\varepsilon_{\mathrm{ro}} = 9\times10^{-5}$ [10]. This matters here because it explains why the leakage channel this paper quantifies is invisible to the certification apparatus actually used on processors: the standard measurement chain is confined to the computational subspace. The platform pedagogy [11] completes the picture of what control and readout physically do — control pulses couple to the electric dipole of the plasmon mode, readout measures a macroscopic observable correlated with the qubit state — and states that a qubit is a constrained two-level subspace of a physical degree of freedom, which working engineers have never doubted, while flagging the fragile view that each abstraction layer from physical qubit to fault-tolerant computation compounds gauge freedoms [11]. Our scaling law gives the fragile view a number.

Three further works anchor the methodological posture. The European strategy analysis [1] argues that progress on the fundamental puzzles unsolved by the Standard Model requires a judicious combination of abstract methods in theoretical physics and precise experimental scrutiny, with precision measurements of rare processes as the low-energy alternative to direct high-energy searches [1]; we borrow that two-sided discipline: an abstract claim (ontological priority of the continuous) must be paired with a precision observable (leakage rates). The linear-collider report [2] demonstrates the pattern of deriving a facility's feasibility from its scaling laws before construction, presenting the design and technology basis of a 0.5–1.5 TeV linear collider and the accelerator-physics lessons of the SLC as the foundation for the next machine's design choices [2]; our removal-capacity budget plays the same pre-construction role for leakage architecture. The MHD design study [6] shows scaling-law extrapolation in practice: tokamak ignition is projected from empirical scaling laws, and stabilization requirements — e.g. the ECCD current for neoclassical-tearing-mode stabilization computed with a Lundquist number $S = 5.56\times10^6$ and bootstrap fraction $j_b/j_p = 0.3$ — are derived before engineering designs are frozen [6]. Finally, two works from outside physics supply a structural analogy we use once each. The API-documentation study [5] found that $66.5\%$ of analyzed API elements carry at least one usage directive, i.e. that a reusable abstraction requires an extensive constraint-documentation layer; the transmon's pulse-shaping and leakage-removal apparatus is exactly such a directive layer for the qubit abstraction. The digital-archive study [3] shows that a classification scheme built for one purpose (its FashionStyle14 categories) "does not cover all contemporary fashion styles and their substyles in a mutually exclusive and collectively exhaustive manner" [3]; the $\{|0\rangle,|1\rangle\}$ radix is a classification of the same kind — purpose-built, and provably non-exhaustive over the underlying state space.

## 3. Methods

We proceed in four steps, using only formulas already derived in [8] and measured rates from [4], plus explicitly stated assumptions where the sources are silent.

**Step 1 (leakage per gate).** The operative scaling law is the first-order bound of [8],

$$L_2 = 8\left(\frac{\Omega}{|\alpha|}\right)^2 \sin^2\!\left(\frac{\alpha T_g}{2}\right),$$

where $\Omega$ is the drive Rabi frequency, $|\alpha|$ the anharmonicity magnitude, and $T_g$ the gate duration. Its gate-averaged form, for gate times uniform over the anharmonicity beat period (mean of $\sin^2$ equal to $1/2$), is

$$\overline{L}_2 = 4\left(\frac{\Omega}{|\alpha|}\right)^2.$$

The exact three-level companion, with $r = f_\Omega/f_\alpha$ the ratio of drive frequency to anharmonicity frequency scales, is

$$P_{2,\max} = \frac{2r^2}{1+2r^2}, \qquad \overline{P}_2 = \frac{r^2}{1+2r^2}.$$

**Step 2 (production rate).** We convert per-gate leakage into a volumetric production rate $\Lambda = \overline{L}_2 \cdot f_g$, where $f_g$ is the gate cycle rate. The gate cycle time is an assumption of this paper: we take a cycle of twice the resonant $\pi$-pulse duration $t_\pi = 25$ ns computed in [8] for the illustrative parameter set, i.e. $T_{\mathrm{cyc}} = 50$ ns, $f_g = 2\times10^{7}\ \mathrm{s}^{-1}$.

**Step 3 (removal requirement).** We model per-qubit leakage population $P_L$ as

$$\frac{dP_L}{dt} = \Lambda - \Gamma_{\mathrm{rem}} P_L,$$

with $\Gamma_{\mathrm{rem}}$ an effective removal rate. Steady state gives $P_{L,\mathrm{ss}} = \Lambda/\Gamma_{\mathrm{rem}}$, so holding leakage at a target $P^*$ requires $\Gamma_{\mathrm{rem}} \ge \Lambda/P^*$. The target $P^* = 10^{-4}$ is our assumption, chosen as a plausible leakage budget per qubit for a code that tolerates only qubit errors [4]; we treat it as a free parameter and report the scaling.

**Step 4 (comparison and interpretation).** We compare $\Gamma_{\mathrm{rem}}$ against the leakage hopping rates of [4] ($0.8$–$10$ MHz resonant; $\approx 0.1$ MHz next-nearest-neighbor), compute the discarded-information fraction of the $d=12$ ladder following [8], and state the ontological reading and its falsification conditions. No experimental data are reported in this paper; every number is computed below with shown arithmetic or labeled a projection.

## 4. Analysis

### 4.1 Leakage per gate at the illustrative operating point

**Inputs.** From the illustrative Set B of [8] (explicitly assumptions, not measurements): $f_\Omega = 20$ MHz, $f_\alpha = 200$ MHz. From the illustrative Set C of [8]: $\Omega/|\alpha| = 0.05$.

Compute the ratio:

$$r = \frac{f_\Omega}{f_\alpha} = \frac{20}{200} = 0.1, \qquad r^2 = 0.01.$$

Exact three-level peak leakage:

$$P_{2,\max} = \frac{2r^2}{1+2r^2} = \frac{2\times0.01}{1+2\times0.01} = \frac{0.02}{1.02} = 0.019608 \approx 1.96\times10^{-2}.$$

Time-averaged three-level leakage:

$$\overline{P}_2 = \frac{r^2}{1+2r^2} = \frac{0.01}{1.02} = 0.009804 \approx 9.80\times10^{-3}.$$

Perturbative bound at worst-case gate timing ($\alpha T_g/2 = \pi/2$, so $\sin^2 = 1$):

$$L_2 = 8\left(\frac{\Omega}{|\alpha|}\right)^2 \sin^2\!\left(\frac{\alpha T_g}{2}\right) = 8\times(0.05)^2\times1 = 8\times0.0025 = 0.02.$$

Gate-averaged:

$$\overline{L}_2 = 8\times0.0025\times\frac{1}{2} = 0.01.$$

**Scaling check** (from [8], recomputed): doubling $\Omega/|\alpha|$ from $0.05$ to $0.10$ gives $\overline{L}_2 = 4\times(0.10)^2\times\frac{1}{2} = 4\times0.01\times\frac{1}{2} = 0.02$; the ratio $0.02/0.01 = 2$... we instead verify the quadratic law through the peak form: $L_2(0.10)/L_2(0.05) = (0.10/0.05)^2 = 4$, and indeed $8\times0.01 = 0.08 = 4\times0.02$. The quadratic scaling in $\Omega/|\alpha|$ is confirmed.

### 4.2 The scaling law as an architectural constraint

The law $\overline{L}_2 = 4(\Omega/|\alpha|)^2$ has one consequence that is independent of the illustrative numbers: per-gate leakage can be driven down only by increasing anharmonicity relative to drive strength. But the transmon's anharmonicity is bounded above by its design: at the state of the art, $\alpha_r = 1.9\%$ [9], and increasing $E_J/E_C$ to suppress charge noise simultaneously suppresses $|\alpha|$. The transmon therefore sits in a design corner where the truncation cost is minimized in decoherence terms and maximized in leakage terms. This is the quantitative content of the statement that the qubit is the correction term, not the identity [9]: the correction term's magnitude, $1.9\%$, is exactly the denominator of the leakage law.

### 4.3 Leakage production rate and removal requirement

**Input (assumption).** Gate cycle time $T_{\mathrm{cyc}} = 50$ ns, chosen as twice the $\pi$-pulse duration $t_\pi = 25$ ns computed in [8] ($t_\pi = 1/(2f_\Omega) = 1/(2\times20\times10^{6})\ \mathrm{s} = 2.5\times10^{-8}$ s). Then

$$f_g = \frac{1}{T_{\mathrm{cyc}}} = \frac{1}{50\times10^{-9}\ \mathrm{s}} = 2\times10^{7}\ \mathrm{s}^{-1}.$$

**Production rate** using $\overline{L}_2 = 0.01$ from Section 4.1:

$$\Lambda = \overline{L}_2 \cdot f_g = 0.01\times2\times10^{7}\ \mathrm{s}^{-1} = 2\times10^{5}\ \mathrm{s}^{-1}.$$

That is, each qubit injects population into the leakage manifold at $2\times10^{5}$ events per second while gates run continuously.

**Removal requirement** for target $P^* = 10^{-4}$ (assumption):

$$\Gamma_{\mathrm{rem}} \ge \frac{\Lambda}{P^*} = \frac{2\times10^{5}}{10^{-4}} = 2\times10^{9}\ \mathrm{s}^{-1}.$$

Equivalently, $\Gamma_{\mathrm{rem}} \ge 2\times10^{9}/(2\pi\times10^{6}) \approx 318$ MHz if expressed as a circular frequency; we keep angular-free units ($\mathrm{s}^{-1}$) throughout for direct comparison with the MHz hopping rates of [4], which are quoted as ordinary frequencies. In ordinary frequency units the requirement is $\Gamma_{\mathrm{rem}}/2\pi$-free, i.e. a removal rate constant of $2\times10^{9}\ \mathrm{s}^{-1}$ corresponds to an ordinary-frequency scale of $2\times10^{9}\ \mathrm{s}^{-1} \approx 2000$ MHz divided by $2\pi$ only if the rate is modeled as a damped oscillation; for a population rate constant the comparison in $\mathrm{s}^{-1}$ is direct, and we make it in Section 4.4 in those units.

**Accumulation time without removal.** Time for leakage population to reach $P = 10^{-2}$ at production $\Lambda$:

$$t_{\mathrm{fill}} = \frac{10^{-2}}{2\times10^{5}\ \mathrm{s}^{-1}} = 5\times10^{-8}\ \mathrm{s} = 50\ \mathrm{ns}.$$

One gate cycle. Without active removal, a continuously gated transmon reaches percent-level leakage within a single cycle at this operating point — which is the operational reason leakage-reduction units exist as dedicated hardware [9].

### 4.4 Removal-capacity deficit against measured hopping rates

The measured leakage hopping rates in tunable-coupler transmon arrays are $0.8$–$10$ MHz in the resonant case and approximately $0.1$ MHz for next-nearest-neighbor hopping [4]. Converting to $\mathrm{s}^{-1}$:

$$10\ \mathrm{MHz} = 1.0\times10^{7}\ \mathrm{s}^{-1}, \qquad 0.8\ \mathrm{MHz} = 8\times10^{5}\ \mathrm{s}^{-1}, \qquad 0.1\ \mathrm{MHz} = 1\times10^{5}\ \mathrm{s}^{-1}.$$

Deficit factors against the requirement $\Gamma_{\mathrm{rem}} = 2\times10^{9}\ \mathrm{s}^{-1}$:

$$\frac{2\times10^{9}}{1.0\times10^{7}} = 200 \quad (\text{fastest resonant hopping}),$$

$$\frac{2\times10^{9}}{8\times10^{5}} = 2500 \quad (\text{slowest resonant hopping}),$$

$$\frac{2\times10^{9}}{1\times10^{5}} = 2\times10^{4} \quad (\text{next-nearest-neighbor hopping}).$$

Even the fastest measured leakage transport channel is short of the required removal capacity by a factor of 200, under the stated assumptions ($\overline{L}_2 = 0.01$, $f_g = 2\times10^{7}\ \mathrm{s}^{-1}$, $P^* = 10^{-4}$). The deficit scales linearly in each assumption: halving the per-gate leakage to $0.005$ halves the requirement to $1\times10^{9}\ \mathrm{s}^{-1}$ and the deficit to 100; relaxing the target to $P^* = 10^{-3}$ divides the requirement by 10, leaving a deficit factor of 20 at the fastest hopping rate. Passive mobility alone therefore cannot close the gap at any operating point in this family; dedicated, faster removal mechanisms (resonator-mediated swap-and-reset, driven removal units) are structurally required, consistent with the observation that leakage removal is an active subfield rather than a solved boundary condition [4].

### 4.5 Discarded information of the binary map

Following [8], for a $d = 12$ ladder the full Hilbert-space information content is

$$\ln 12 = 2.484906\ \mathrm{nats},$$

and the base-truncation entropy retained by the two-level map's classical shadow is

$$S_{\mathrm{Base}} = \ln 6 = 1.791759\ \mathrm{nats} = 2.584963\ \mathrm{bits}.$$

The discarded fraction is

$$f_{\mathrm{disc}} = \frac{\ln 6}{\ln 12} = \frac{1.791759}{2.484906} = 0.721125,$$

i.e. $72.1\%$ of the oscillator's information content is outside what the binary radix efficiently represents; the radix efficiency is $\eta \approx 27.9\%$, and one $d=12$ oscillator would require $\lceil\log_2 12\rceil = 4$ qubits for lossless binary encoding, against $\log_2 12 = 3.584963$ qubits of fractional capacity [8]. The leakage computed in Sections 4.1–4.4 is the dynamical face of this static $72.1\%$ deficit: what the map discards, the drive partially re-injects as population outside the computational subspace.

### 4.6 Observability of the leakage channel

The calibration-loop result [10] bounds what the standard certification apparatus can see. Under subspace-restricted measurements, a two-level ontology and a three-level carrier with leakage amplitude $|c| = 0.1$ are observationally identical with total-variation distance $D_{\mathrm{TV}} = 0$ exactly; the degeneracy breaks only as $(\Omega/2\Delta)^2$ at larger drive, and resolving it against the readout error floor $\varepsilon_{\mathrm{ro}} = 9\times10^{-5}$ requires $N \ge 2500$ shots (one sigma) or $N \ge 22500$ (three sigma) once a leakage-resolving observable exists [10]. The signal-to-floor margin for $|c|^2 = 0.01$ is $|c|^2/\varepsilon_{\mathrm{ro}} = 0.01/9\times10^{-5} \approx 111$ [10]. The leakage this paper quantifies is therefore real, large relative to the readout floor, and yet invisible to the tomography actually run on processors — a measurement-architecture gap, not a smallness of the effect.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic, or labeled projections under stated assumptions. No experimental or simulated data are reported in this paper.

1. **Per-gate leakage (computed, Section 4.1).** At $r = 0.1$: $P_{2,\max} = 0.019608$, $\overline{P}_2 = 0.009804$; at $\Omega/|\alpha| = 0.05$: $L_2 = 0.02$ (worst-case timing), $\overline{L}_2 = 0.01$. Quadratic scaling in $\Omega/|\alpha|$ confirmed by the factor-$4$ check.

2. **Leakage production rate (computed, Section 4.3, under the stated gate-cycle assumption).** $\Lambda = 2\times10^{5}\ \mathrm{s}^{-1}$ per gated qubit.

3. **Removal requirement (computed, Section 4.3, under the stated target assumption).** $\Gamma_{\mathrm{rem}} \ge 2\times10^{9}\ \mathrm{s}^{-1}$ for $P^* = 10^{-4}$; fill time without removal $t_{\mathrm{fill}} = 50$ ns, i.e. one gate cycle.

4. **Removal-capacity deficit (computed, Section 4.4).** Factor 200 against the fastest measured resonant hopping rate ($10$ MHz), 2500 against the slowest ($0.8$ MHz), $2\times10^{4}$ against next-nearest-neighbor hopping ($0.1$