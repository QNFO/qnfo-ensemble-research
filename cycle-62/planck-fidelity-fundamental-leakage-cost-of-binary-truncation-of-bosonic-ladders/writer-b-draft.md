# Planck Fidelity: Fundamental Leakage Cost of Binary Truncation of Bosonic Ladders

## Abstract

A transmon is a bosonic oscillator whose spectrum is a discrete but unbounded ladder of levels; encoding it as a qubit, i.e., restricting computational states to $n \in \{0,1\}$, is a radix choice rather than a physical necessity. We formalize the conjecture that any finite-time gate on such an oscillator, driven through the raising operator $a^\dagger$, incurs a strictly nonzero "Planck Loss" $L_P = 1 - \mathrm{Tr}(P_{\mathrm{qubit}}\,|\psi\rangle\langle\psi|)$, a leakage floor independent of materials and control engineering. We derive an explicit perturbative expression for coherent leakage population in levels $n \geq 2$ under a resonant drive, showing that it scales as $r^2$ in the drive-to-anharmonicity ratio $r = \Omega/\alpha$ and vanishes only in the unphysical limits $\Omega \to 0$ or $\alpha \to \infty$. Under stated illustrative parameters ($f_\Omega = 20\,\mathrm{MHz}$, $f_\alpha = 200\,\mathrm{MHz}$), a single $\pi$ pulse carries a coherent leakage probability of $\approx 4.76 \times 10^{-4}$ and a time-averaged leakage of $\approx 9.80 \times 10^{-3}$. We further quantify the truncation entropy $S_{\mathrm{Base}} = \ln(d/2) \approx 1.7918$ nats for $d = 12$ resolvable levels, and show that qubit encoding of such an oscillator uses at most $27.9\%$ of its available Hilbert-space radix. We argue these results reframe leakage as evidence for base-$d$ qudit hardware, and state the conditions under which the conjecture would be falsified.

## 1. Introduction

The transmon — a capacitively shunted Josephson junction behaving, to leading order, as a weakly anharmonic bosonic oscillator — is routinely treated as a qubit. Its energy spectrum $E_n$ is discrete and unbounded in the idealized oscillator model, and the computational subspace $\{|0\rangle, |1\rangle\}$ is a two-element subset of a much larger ladder. The choice of radix $2$ is inherited from the broader digital-computing convention, not from the physics of the device: the oscillator itself does not "know" it is supposed to be a two-level system.

This paper develops a conjecture, stated in the source research idea, that we call the Planck Fidelity conjecture: for any finite-time gate driven by a raising operator $a^\dagger$ on a bosonic ladder truncated to two levels, the leakage

$$L_P = 1 - \mathrm{Tr}\!\left(P_{\mathrm{qubit}}\, |\psi\rangle\langle\psi|\right), \qquad P_{\mathrm{qubit}} = |0\rangle\langle 0| + |1\rangle\langle 1|,$$

is strictly positive, in a sense made precise below, and therefore constitutes a fundamental limit on qubit-encoded bosonic hardware that is independent of materials, fabrication, or control refinement. Truncating $d$ resolvable levels to $2$ additionally carries an information-theoretic cost, which the source material [9] names the base entropy $S_{\mathrm{Base}} = \ln(d/2)$.

Our contributions are: (i) a precise perturbative model in which the leakage population of levels $n \geq 2$ under a resonant drive can be computed in closed form, with every arithmetic step shown; (ii) an explicit numerical evaluation under clearly labeled illustrative parameters; (iii) a computation of the truncation entropy and radix-efficiency penalties for $d = 12$; and (iv) a candid discussion of what the conjecture does and does not claim, including the observation that in the idealized two-level-plus-one detuned model the instantaneous leakage can vanish at isolated revival times, so that the robust statement concerns time-averaged or generic-time leakage rather than pointwise positivity at every instant.

Throughout, "leakage" means population of states outside the computational subspace; "anharmonicity" means the detuning $\alpha$ between adjacent transition frequencies of the ladder; and "radix" means the number of distinguishable symbols per physical carrier.

## 2. Background and Related Work

The bibliography supplied for this paper is heterogeneous: eight entries concern the European Space Agency's Planck cosmic microwave background (CMB) mission, and three concern the QNFO "Project Rosetta" corpus from which the present research idea originates. We discuss each on the basis of its supplied summary only, and we are explicit where a summary is thin. The thematic link between the two groups is the word "Planck" and, more substantively, the notion of extracting essentially all of the information physically present in a system rather than a small commissioned fraction of it.

**The Planck CMB mission papers.** Reference [1], *The Scientific Programme of Planck*, states that for 40 years the CMB has been the most important source of information about the geometry and contents of the Universe, that only a small fraction of the available information had been extracted to date, and that Planck — the third space CMB mission after COBE and WMAP — is designed to extract essentially all of the information in the CMB temperature anisotropies. This is the analogy we invoke: a measurement program can be designed to exhaust the information content of its target, and the present paper asks whether quantum hardware design exhausts the information content of its carrier. Reference [2], *Planck Early Results: The Planck mission*, records that the satellite was launched on 14 May 2009 and has been surveying the sky stably and continuously since 13 August 2009, with performance in line with expectations; it supplies the operational-continuity framing within which the later catalogue and calibration papers sit. Reference [3] describes the Planck Catalogue of Compact Sources (PCCS), nine single-frequency catalogues of compact Galactic and extragalactic sources over the entire sky, covering $30$–$857\,\mathrm{GHz}$, with $90\%$ completeness at $180\,\mathrm{mJy}$ in the best channel; it is an example of a complete discrete census of resolvable "levels" (sources) of a physical field. Reference [4] describes the all-sky Sunyaev–Zeldovich cluster catalogue from the first 15.5 months of observations, containing 1227 entries — over six times the earlier ESZ sample — of which 861 are confirmed clusters; again, a census whose value lies in counting and classifying all resolvable objects rather than a privileged subset, the same move we advocate for transmon levels. Reference [5] exploits the Early Release Compact Source Catalogue to measure number counts $\mathrm{d}N/\mathrm{d}S$ of extragalactic radio sources at 30, 44, 70, 100, 143 and 217 GHz, noting that the full-sky nature of the catalogue extends the measurement to the rarest and brightest sources; counting the population of each rung of a brightness ladder is structurally the exercise we propose for occupation numbers $n$ of a bosonic ladder. Reference [6], on the HFI spectral response, states that the relative spectral response including out-of-band signal rejection of all HFI detectors was measured in ground-based cryogenic tests prior to launch. Out-of-band rejection is the direct observational analogue of computational-subspace leakage: signal arriving outside the designated band is indistinguishable, in its harmful effect, from population arriving outside $\{|0\rangle,|1\rangle\}$, and it must be characterized, not assumed away. Reference [7] presents the Second Planck Catalogue of Compact Sources, detected in single-frequency maps over the full mission duration and superseding previous versions; it illustrates that censuses are revised as instrument understanding improves, as level counts $d$ in a transmon are revised as coherence improves. Reference [8] describes the pipeline calibrating LFI timelines into thermodynamic temperatures over four years of operations, using the CMB dipole — spin-synchronous modulation as in 2013, now with the orbital component added — as the calibrator; it is a case study in absolute calibration against a known reference, the role that a leakage benchmark metric would play for gate sets.

**The QNFO corpus.** Reference [9], *Project Rosetta ... v2.0* (DOI 10.5281/zenodo.21486780), is the direct source of the framing used here: its v2.0 "Planck-Radix Correction" states that the transmon spectrum IS discrete (Planck quantization), that binary truncation is a radix error and not a physics error, that the transmon is a qudit with $d \sim 12$ rather than a qubit, and that the base entropy is $S_{\mathrm{Base}} = \ln(d/2) \sim 1.79$ nats; it is an 11-page PDF. We adopt the quantity $S_{\mathrm{Base}}$ and recompute it exactly in Section 4. Reference [10], *The Two-Level Lie: The Transmon Is Not a Qubit — And the Entire Field Knows It* (DOI 10.5281/zenodo.21484345), states that its v2.0 adds "Part II: The Approximation Entropy," described as a meta-mathematical framework quantifying the irreducible cost of translating continuous bosonic physics to discrete digital computation, and that it introduces a "Rosetta Constant," a "Trotter Wall," and a "Fractal Wall theorem" together with a falsifiable calorimetry experimental proposal. The supplied summary gives no further detail on these objects, so we do not use them quantitatively; we note only that the falsifiability orientation of [10] matches the falsification criteria we state in Section 6. Reference [11], *Thermodynamic Scaling of 4-Kelvin Topological Processors* (DOI 10.5281/zenodo.17899087), has an empty summary in the supplied bibliography; we therefore cannot state what it contains, and we relate it to our argument only through its title, which suggests a thermodynamic-scaling perspective on alternative hardware that would be the natural venue for an entropy-cost accounting such as $S_{\mathrm{Base}}$.

We emphasize for honesty: none of the eight Planck mission papers addresses superconducting qubits, and neither [9] nor [10] supplies the perturbative leakage derivation given below; the derivation in Section 4 is original to this paper, built on the conjecture's own premises.

## 3. Methods

### 3.1 Device model

We model the transmon as a weakly anharmonic bosonic oscillator with Hamiltonian ($\hbar = 1$)

$$H_0 = \omega\, a^\dagger a + \frac{\alpha}{2}\, a^\dagger a^\dagger a\, a,$$

where $a$, $a^\dagger$ are the ladder operators with $a^\dagger|n\rangle = \sqrt{n+1}\,|n+1\rangle$, $\omega$ is the $0 \to 1$ transition frequency, and $\alpha$ is the anharmonicity, i.e., the detuning of the $1 \to 2$ transition from $0 \to 1$. A classical resonant drive on the $0 \to 1$ transition adds

$$H_d(t) = \Omega \left( a + a^\dagger \right) \cos(\omega t),$$

with Rabi amplitude $\Omega$. In the rotating wave approximation and a frame rotating at $\omega$, the relevant three-level truncation $\{|0\rangle, |1\rangle, |2\rangle\}$ is

$$H_{\mathrm{eff}} = \frac{\alpha}{2}|2\rangle\langle 2| + \frac{\Omega}{2}\left(|0\rangle\langle 1| + |1\rangle\langle 0|\right) + \frac{\Omega\sqrt{2}}{2}\left(|1\rangle\langle 2| + |2\rangle\langle 1|\right).$$

The factor $\sqrt{2}$ is the matrix element $\langle 2|a^\dagger|1\rangle = \sqrt{2}$.

### 3.2 Leakage observable

The Planck Loss is $L_P = 1 - \mathrm{Tr}(P_{\mathrm{qubit}}\rho)$ for the evolved state $\rho$; in the three-level truncation with initial $|0\rangle$, $L_P = P_2$, the population of $|2\rangle$. We compute $P_2(t)$ exactly within this truncation (Section 4.1), which is a derivation, not an empirical claim; its parameters are labeled illustrative.

### 3.3 Entropy and radix accounting

Following [9], the base entropy of binary truncation of a $d$-level ladder is

$$S_{\mathrm{Base}}(d) = \ln\!\frac{d}{2},$$

in nats. The radix efficiency of qubit encoding is the ratio of the information carried per physical oscillator under binary encoding ($\log_2 2 = 1$ bit) to that under full base-$d$ encoding ($\log_2 d$ bits).

### 3.4 Assumption discipline

All numerical results in Section 4 derive from exactly three inputs: the level count $d = 12$ (from the source idea and [9]), and the illustrative drive parameters $f_\Omega = 20\,\mathrm{MHz}$ and $f_\alpha = 200\,\mathrm{MHz}$, which we introduce as stated assumptions for concreteness and do not attribute to any measurement. Ratios, entropies, and leakage probabilities are then computed with all steps shown.

## 4. Analysis

### 4.1 Exact coherent leakage in the three-level truncation

Within $\{|0\rangle,|1\rangle,|2\rangle\}$, the $|1\rangle \leftrightarrow |2\rangle$ pair is a driven two-level system with coupling $g$ and detuning $\delta$:

$$g = \frac{\Omega\sqrt{2}}{2} = \frac{\Omega}{\sqrt{2}}, \qquad \delta = \alpha.$$

For initial condition $c_1(0) = 1$, $c_2(0) = 0$, the standard detuned-Rabi solution gives the $|2\rangle$ population

$$P_2(t) = \frac{g^2}{g^2 + (\alpha/2)^2}\,\sin^2\!\left(\sqrt{g^2 + (\alpha/2)^2}\; t\right).$$

Substituting $g^2 = \Omega^2/2$:

$$P_2(t) = \frac{\Omega^2/2}{\Omega^2/2 + \alpha^2/4}\,\sin^2\!\left(\sqrt{\Omega^2/2 + \alpha^2/4}\; t\right) = \frac{2\Omega^2}{\alpha^2 + 2\Omega^2}\,\sin^2\!\left(\frac{\alpha}{2}\sqrt{1 + 2r^2}\; t\right),$$

where we define the dimensionless drive ratio

$$r = \frac{\Omega}{\alpha}.$$

Two exact consequences follow immediately.

**(a) Peak leakage.** The prefactor is the maximal leakage:

$$P_{2,\max} = \frac{2r^2}{1 + 2r^2}.$$

This is strictly positive for every $r > 0$ and tends to zero only as $r \to 0$ ($\Omega \to 0$, i.e., no gate) or $r \to \infty$ is excluded but $\alpha \to \infty$ (an exactly harmonic... in fact infinitely anharmonic) would be required to suppress it at fixed $\Omega$. This is the precise sense in which leakage is a *radix* artifact: it is controlled by the ratio of drive strength to level spacing structure, not by materials.

**(b) Time-averaged leakage.** Since $\langle \sin^2 \rangle = 1/2$ over a Rabi period,

$$\overline{P}_2 = \frac{r^2}{1 + 2r^2}.$$

**(c) Honesty about "strictly positive."** The instantaneous $P_2(t)$ vanishes at isolated times $t_k = k\pi / \left(\frac{\alpha}{2}\sqrt{1+2r^2}\right)$. The robust, defensible statement of the Planck Fidelity conjecture is therefore: for any gate of nonzero duration $t_g$ drawn from a continuous distribution of gate times or phases, $P_2(t_g) > 0$ except on a measure-zero set; and the time-averaged leakage $\overline{P}_2 > 0$ for every $r > 0$. We return to this in Section 6.

### 4.2 Numerical evaluation (illustrative parameters)

**Inputs.** $f_\Omega = 20\,\mathrm{MHz}$ (assumed), $f_\alpha = 200\,\mathrm{MHz}$ (assumed), so

$$r = \frac{f_\Omega}{f_\alpha} = \frac{20}{200} = 0.1, \qquad r^2 = 0.01.$$

**Peak leakage.**

$$P_{2,\max} = \frac{2 \times 0.01}{1 + 2 \times 0.01} = \frac{0.02}{1.02} = 0.019608 \approx 1.96 \times 10^{-2}.$$

**Time-averaged leakage.**

$$\overline{P}_2 = \frac{0.01}{1.02} = 0.009804 \approx 9.80 \times 10^{-3}.$$

**Leakage at the end of a $\pi$ pulse.** A resonant $\pi$ pulse on $0 \to 1$ has duration

$$t_\pi = \frac{\pi}{\Omega} = \frac{1}{2 f_\Omega} = \frac{1}{2 \times 20 \times 10^{6}\,\mathrm{s}^{-1}} = 2.5 \times 10^{-8}\,\mathrm{s} = 25\,\mathrm{ns}.$$

The Rabi phase argument at $t = t_\pi$ is

$$\theta = \frac{\alpha}{2}\sqrt{1 + 2r^2}\; t_\pi = \pi f_\alpha \sqrt{1.02}\; t_\pi.$$

Compute each factor: $\pi f_\alpha t_\pi = \pi \times 200 \times 10^{6} \times 2.5 \times 10^{-8} = \pi \times 5 = 15.70796\,\mathrm{rad}$; $\sqrt{1.02} = 1.0099505$; hence

$$\theta = 15.70796 \times 1.0099505 = 15.86445\,\mathrm{rad}.$$

Reduce modulo $2\pi$: $15.86445 - 4\pi = 15.86445 - 12.56637 = 3.29808\,\mathrm{rad}$; then $3.29808 - \pi = 0.15649\,\mathrm{rad}$, so $\sin\theta = -\sin(0.15649)$. Using $\sin x \approx x - x^3/6$ with $x = 0.15649$: $x^3 = 3.829 \times 10^{-3}$, $x^3/6 = 6.38 \times 10^{-4}$, so $\sin(0.15649) \approx 0.15585$, and

$$\sin^2\theta \approx (0.15585)^2 = 0.024288.$$

Therefore

$$P_2(t_\pi) = P_{2,\max} \times \sin^2\theta = 0.019608 \times 0.024288 = 4.76 \times 10^{-4}.$$

**Sequence-level survival.** If each of $N$ independent gates leaks probability $L = 4.76 \times 10^{-4}$ with no leakage recovery, the survival probability of the computational subspace is

$$S_N = (1 - L)^N \approx e^{-NL}.$$

For $N = 1000$: $NL = 1000 \times 4.7624 \times 10^{-4} = 0.47624$, so

$$S_{1000} \approx e^{-0.47624} = 0.6212.$$

That is, under these assumptions a 1000-gate qubit-encoded circuit retains population in the computational subspace only $\approx 62\%$ of the time absent active leakage return — the quantitative core of the "leakage crisis" framing.

### 4.3 Truncation entropy and radix efficiency for $d = 12$

**Inputs.** $d = 12$ resolvable levels (source idea; [9] states $d \sim 12$).

**Base entropy.**

$$S_{\mathrm{Base}} = \ln\frac{12}{2} = \ln 6 = 1.791759\,\mathrm{nats}.$$

In bits, dividing by $\ln 2 = 0.693147$:

$$S_{\mathrm{Base}} = \frac{1.791759}{0.693147} = 2.584963\,\mathrm{bits}.$$

This reproduces the $\sim 1.79$ nats quoted in [9] to the precision given there.

**Radix efficiency of qubit encoding.** Full use of the ladder carries $\log_2 12$ bits per oscillator:

$$\log_2 12 = \frac{\ln 12}{\ln 2} = \frac{2.484907}{0.693147} = 3.584963\,\mathrm{bits}.$$

Binary encoding carries $\log_2 2 = 1$ bit. Efficiency:

$$\eta = \frac{1}{3.584963} = 0.278942 \approx 27.9\%.$$

Equivalently, encoding one $d = 12$ oscillator faithfully requires $\lceil \log_2 12 \rceil = 4$ qubits, i.e., a fourfold physical-qubit overhead per logical oscillator merely to represent the radix — before any error-correction overhead.

### 4.4 Scaling summary

Collecting the closed forms, with $r = \Omega/\alpha$ and level count $d$:

$$P_{2,\max} = \frac{2r^2}{1+2r^2}, \qquad \overline{P}_2 = \frac{r^2}{1+2r^2}, \qquad S_{\mathrm{Base}} = \ln\frac{d}{2}, \qquad \eta = \frac{1}{\log_2 d}.$$

All four quantities are exact within the stated model; only the parameter values $r = 0.1$, $d = 12$ are assumptions.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; the drive parameters are explicitly illustrative assumptions, not measurements.

1. **Coherent leakage per $\pi$ pulse:** $P_2(t_\pi) = 4.76 \times 10^{-4}$ for $r = 0.1$ (assumed $f_\Omega = 20\,\mathrm{MHz}$, $f_\alpha = 200\,\mathrm{MHz}$), from the exact three-level detuned-Rabi solution.
2. **Peak and time-averaged leakage:** $P_{2,\max} = 1.96 \times 10^{-2}$; $\overline{P}_2 = 9.80 \times 10^{-3