# Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis

## Abstract

Photosynthetic antennae transfer excitation energy with near‑unity efficiency on sub‑picosecond timescales, and modelers of these systems must decide whether to spend high‑performance‑computing resources on a non‑Markovian boson‑mediated description or to accept an inexpensive Markovian dephasing master equation. Earlier applicability tests for this decision used coupling ranges broader than the experimentally reported values, a dimensionally inconsistent transfer‑time expression, a defective dephasing dissipator, and an unsupportable analogy to multiplex transportation networks. This revision adopts the experimentally reported excitonic coupling $V\in[50,75]\;\mathrm{cm^{-1}}$ and site‑energy difference $\Delta\in[110,180]\;\mathrm{cm^{-1}}$ for the FMO BChl 3–4 dimer [4], the dimensionally consistent transfer time $\tau_{T}=\Delta/(2\pi cV^{2})$, and the correct pure‑dephasing Lindblad generator $-\frac{\Gamma}{2}[\sigma_{z},[\sigma_{z},\rho]]$. The corrected arithmetic gives $\tau_{T}\in[0.1038,0.3822]\;\mathrm{ps}$, a single‑hop trapping efficiency $\eta=0.999001$, and memory ratios $R_{\mathrm{fast}}\in[0.26,0.96]$ for $\tau_{B}=0.1\;\mathrm{ps}$ and $R_{\mathrm{slow}}\in[2.6,9.6]$ for $\tau_{B}=1\;\mathrm{ps}$. Every realistic slow‑mode scenario therefore lies in the non‑Markovian sector, while fast solvent‑like baths sit in a transitional window that requires error estimation rather than automatic dismissal of the Markovian limit. A falsifiable projection, $\delta\Gamma^{*}/\Gamma^{*}\approx R$ for the shift of the optimal dephasing rate when $R\gtrsim0.5$, turns the rule into a testable guideline for allocating computational effort in excitation‑energy‑transfer modelling.

## 1. Introduction

Designers of bio‑inspired photovoltaic devices and researchers interpreting ultrafast spectroscopic data face a concrete methodological choice: allocate high‑performance‑computing resources to a non‑Markovian boson‑mediated description that retains bath memory, or adopt a Markovian dephasing master equation that discards memory at negligible cost. The former can require on the order of $10^{4}$ CPU‑hours (order‑of‑magnitude estimate) for a seven‑site FMO simulation, while the latter runs on a laptop in minutes [9]. An incorrect choice either wastes computational budget or yields quantitatively inaccurate transfer rates and optimal dephasing conditions, which can propagate into sub‑optimal device designs or misinterpreted observables. A decision rule that predicts when memory effects are essential would reduce unnecessary computation and improve the reliability of modelling outcomes.

The published version of this analysis [9] contained errors that materially affect its conclusions, and each is corrected here after checking it against the paper's own derivations and its sources. First, the sensitivity box $V\in[20,75]\;\mathrm{cm^{-1}}$ was described as "the full experimentally reported range"; the vibronic dimer study actually reports excitonic couplings between $-50$ and $-75\;\mathrm{cm^{-1}}$ for the BChl 3–4 pair [4], so the lower bound $20\;\mathrm{cm^{-1}}$ has no experimental support and the correct box is $V\in[50,75]\;\mathrm{cm^{-1}}$. Second, Section 4.5 of the published version stated $\tau_{T}=\hbar\Delta/(2\pi cV^{2})$; the factor $\hbar$ carries units of action ($\mathrm{J\,s}$), so that expression is dimensionally inconsistent, and the correct transfer time is $\tau_{T}=\Delta/(2\pi cV^{2})$. Third, the published abstract reported a memory‑ratio span of $0.17$–$1.70$ and placed fast baths in a "transitional window" without qualification; the corrected arithmetic over the experimental box gives $R_{\mathrm{fast}}\in[0.26,0.96]$, so fast baths straddle the transitional regime rather than sitting wholly inside it. Fourth, Section 6.2 of the published version cited the urban‑transportation multiplex‑network study [3] as mirroring the memory‑ratio sensitivity result; that work applies an overlap census to transportation layers in 15 cities and makes no claim about quantum transport or any memory‑ratio metric, so the analogy is retracted. Fifth, the abstract's memory‑ratio windows are restated here with the corrected transfer‑time bounds. Sixth, the dephasing term $-(\Gamma/2)(1-\sigma_{z}^{2}/2)$ reduces to a multiple of the identity and generates no dephasing; the correct pure‑dephasing Lindblad generator with jump operator $\sigma_{z}$ is used instead.

Two decades of theory establish that environmental dephasing can assist transport, raising excitation‑energy‑transfer (EET) efficiencies above $90\%$ in the FMO complex within a fully Markovian treatment [2]. Single‑molecule pump–probe spectroscopy resolves energy relaxation on sub‑100 fs timescales in individual light‑harvesting complexes, supporting the assignment of fast solvent‑like bath correlation times $\tau_{B}=0.1\;\mathrm{ps}$ [7]. Atomistic and vibronic studies supply the excitonic couplings and site‑energy differences that define the realistic parameter box [4], and atomistic simulations of the full green‑sulfur‑bacterial antenna show that energy‑funnelling results converge within an overall $10\;\mathrm{ps}$ timescale [5]. These grounded ranges are narrower than the ranges used in the earlier applicability analysis [9], and the correction matters: with $V\in[50,75]\;\mathrm{cm^{-1}}$ instead of $[20,75]\;\mathrm{cm^{-1}}$, the smallest transfer time is shorter and the largest memory ratio is larger, strengthening the conclusion that slow baths demand a non‑Markovian treatment.

**Contributions.**
1. Derivation of the optimal dephasing rate $\Gamma^{*}=\Delta$ and optimal hopping rate $k^{*}=V^{2}/\Delta$ for the two‑site Haken–Strobl model with the corrected dissipator (Section 4.1).
2. Correction of the transfer‑time formula to $\tau_{T}=\Delta/(2\pi cV^{2})$, a dimensional verification, and evaluation at the four corners of the experimental box, yielding $\tau_{T}\in[0.1038,0.3822]\;\mathrm{ps}$ (Section 4.2).
3. Computation of the single‑hop trapping‑limited efficiency $\eta=0.999001$ from the assumed trap and recombination rates (Section 4.3).
4. Exhaustive calculation of memory ratios over the full experimental box, giving $R_{\mathrm{fast}}\in[0.26,0.96]$ and $R_{\mathrm{slow}}\in[2.6,9.6]$ (Section 4.4).
5. A revised regime classification in which all realistic slow‑mode baths fall in the non‑Markovian sector and fast baths occupy a transitional window (Section 5).
6. A falsifiable projection that the non‑Markovian correction to the optimal dephasing rate scales as $\delta\Gamma^{*}/\Gamma^{*}\approx R$ when $R\gtrsim0.5$ (Sections 5 and 6).

## 2. Background and Related Work

**Noise‑assisted transport in FMO.** The dephasing‑assisted transport (DAT) study [2] develops physically intuitive mechanisms for the effect of noise on EET and shows, in a hybrid basis of excitons and sites, how dephasing enables energy transfer with efficiencies well above $90\%$ across the FMO complex. Its conclusion section states that the identification of transport‑suppressing pathways is made without reference to the noise model, so any noise model that enhances transport must suppress the inefficient paths and enhance the direct relaxation channels. This establishes the practical relevance of dephasing‑assisted transport within a fully Markovian treatment and defines the baseline against which any non‑Markovian framework must demonstrate added value.

**Fundamental mechanisms of DAT.** The fully connected network (FCN) analysis [8] obtains an exact analytical solution for uniform networks and shows that with no dissipation and no dephasing the total transferred population approaches $p_{\mathrm{sink}}(\infty)=1/(N-1)$, a destructive‑interference limit that dephasing overcomes. Its concluding remarks identify the suppression of destructive interference and the dephasing‑broadened overlap between site lines as the key mechanisms of noise‑assisted transport. The optimal dephasing condition $\Gamma^{*}=\Delta$ derived in Section 4.1 of this paper is the two‑site instance of that mechanism.

**Excitonic coupling magnitudes and site energies.** The vibronic dimer study [4] states that for the FMO BChl 3 and 4 pair the transition energy difference is proposed to be from about $110$ to $180\;\mathrm{cm^{-1}}$ and the excitonic coupling is negative with values from about $-50$ to $-75\;\mathrm{cm^{-1}}$. These two ranges define the experimental parameter box used throughout this work, and they also report a fluorescence‑line‑narrowing Huang–Rhys factor of $0.03$ for modes near $180\;\mathrm{cm^{-1}}$, with corrections to Huang–Rhys factors of up to $100\%$ when excitonic coupling is significant. The same study finds that for negative coupling most oscillator strength resides in a transition of essentially electronic character, which supports treating the dimer's electronic parameters as the dominant transport quantities.

**Atomistic energy funnelling.** The atomistic study of the green‑sulfur‑bacterial antenna [5] builds a model of $3988$ pigments spanning chlorosome, baseplate, and six FMO trimers, solves a quantum master equation including coherent, dephasing and relaxation processes, and finds that results converge within the overall $10\;\mathrm{ps}$ timescale regardless of initiating conditions. That $10\;\mathrm{ps}$ funnel timescale is an order of magnitude longer than the single‑hop times derived here, which is consistent with the single‑hop time being one element of a multi‑hop chain.

**Ultrafast spectroscopy of bath and relaxation dynamics.** The single‑molecule study [7] employs a pump–probe type single‑molecule technique (SM2P) with $200$–$250\;\mathrm{fs}$ pulses to observe ultrafast energy relaxation in individual LH2 complexes, resolving relaxation‑time distributions that shift with excitation wavelength. The fastest processes in light‑harvesting complexes lie in the sub‑100 fs range, which motivates the fast bath correlation time $\tau_{B}=0.1\;\mathrm{ps}$ used here as an assumption anchored to that spectroscopic scale.

**Nuclear quantum effects on rates.** The mixed quantum–classical study [6] compares classical and quantum treatments of vibrational motion in LH2, FMO and LHCII at $300\;\mathrm{K}$ and concludes that the main difference is not the direction of energy flow but the rate: classical vibrational treatment generally overestimates the transfer rate, the quantum effect on the rate is benign (less than a factor $2$) for biologically relevant parameters, and vibrational‑Hamiltonian renormalization accounts for it. This bounds how much a quantum vibrational treatment can shift rates and supports the weak‑coupling assumption used in the Haken–Strobl rate formula of Section 4.1.

**Dimensional consistency in transport modelling.** The transient thermal grating (TTG) study [1] probes heat‑transport dynamics at small spatiotemporal scales and emphasizes that quantitative interpretation of the measured transient requires a forward model that consistently connects energy deposition, subsequent transport, and the detected signal. The same discipline of a dimensionally consistent forward model motivates the correction of the transfer‑time formula in Section 4.2: a wavenumber‑based rate must be converted to a time through $2\pi c$, not through an unconverted ratio.

**Multiplex‑network analysis.** The urban transportation study [3] proposes the overlap census method, applies it to $15$ cities, and identifies six clusters of cities with similar multimodal profiles that explain more than $90\%$ of the variance. Its subject is layered transportation infrastructure; it contains no claim about quantum transport and no memory‑ratio metric. The published version of this paper cited it as mirroring the memory‑ratio sensitivity result; that citation is retracted here, and the work is retained only as a documented example of a timescale‑free network analysis that offers no quantitative mapping to exciton–phonon dynamics.

**The boson‑mediated non‑Markovian framework.** The framework under test [10] proposes that bosonic fields (phonons) act as structured signals that direct fermionic excitons through the energy landscape, formulated as a non‑Markovian Hamiltonian dynamics intended to resolve the coexistence of near‑unity transfer efficiency with thermal disorder. Its summary reports simulated efficiencies above $95\%$ and maps the same principle to driven bosonic fields in condensed matter. This paper does not evaluate that framework's internal claims; it derives the timescale condition under which such a framework must be used instead of a Markovian reduction.

**The prior applicability analysis.** The published version of this work [9] formulated the memory‑ratio criterion $R=\tau_{B}/\tau_{T}$ and the projection $\delta\Gamma^{*}/\Gamma^{*}\approx R$, but with the defective parameter box, transfer‑time formula, dissipator and analogy listed in Section 1. The present revision keeps the criterion and the projection, which survive the corrections, and replaces every erroneous element.

Collectively, these works define the experimentally realistic parameter regime [4], the Markovian DAT baseline [2, 8], the spectroscopic and atomistic context for bath timescales [5, 7], the size of quantum‑vibrational corrections [6], the modelling discipline of dimensional consistency [1], and the framework whose applicability is being tested [10].

## 3. Methods

### 3.1 Toy model and corrected dephasing dissipator

We consider the two‑site Haken–Strobl Hamiltonian in the single‑excitation manifold,

$$
H_{S}= \frac{\Delta}{2}\,\sigma_{z}+V\,\sigma_{x},
$$

where $\sigma_{x},\sigma_{z}$ are Pauli matrices on the two‑site basis, $\Delta$ is the site‑energy difference, and $V$ is the excitonic coupling. Site 2 carries a trap with rate $\kappa$.

The correct pure‑dephasing Lindblad generator with jump operator $\sigma_{z}$ is

$$
\mathcal{L}_{\phi}[\rho]=-\frac{\Gamma}{2}\,[\sigma_{z},[\sigma_{z},\rho]],
$$

which leaves populations invariant and damps the coherence as $\dot{\rho}_{12}=-2\Gamma\,\rho_{12}$. This form replaces the defective term $-(\Gamma/2)(1-\sigma_{z}^{2}/2)$ of the published version: since $\sigma_{z}^{2}=\mathbb{1}$, that expression equals $-(\Gamma/4)\,\mathbb{1}$ up to constants, a multiple of the identity that generates no dephasing at all. Any optimality analysis built on it is void, and the corrected generator is used for every derivation below.

### 3.2 Re‑entry criterion

The memory ratio is defined as

$$
R=\frac{\tau_{B}}{\tau_{T}},
$$

with $\tau_{B}$ the bath correlation time and $\tau_{T}$ the intrinsic single‑hop transfer time (Section 4.2). Thresholds are conventions chosen to render the criterion falsifiable:

- $R\lesssim0.1$: Markovian reduction suffices.
- $0.1<R<0.5$: transitional regime; error estimation required before discarding memory.
- $R\gtrsim0.5$: non‑Markovian framework required.

### 3.3 Input parameters

| Symbol | Value | Source / status |
|--------|-------|-----------------|
| $V$ | $[50,75]\;\mathrm{cm^{-1}}$ | Reported in [4] (magnitudes of $-50$ to $-75$) |
| $\Delta$ | $[110,180]\;\mathrm{cm^{-1}}$ | Reported in [4] |
| $\kappa$ | $1\;\mathrm{ps^{-1}}$ | Assumption of this paper |
| $\tau_{e}$ | $1\;\mathrm{ns}$ | Assumption of this paper |
| $\tau_{B}$ | $0.1\;\mathrm{ps}$ (fast) and $1\;\mathrm{ps}$ (slow) | Assumptions; fast value motivated by the sub‑100 fs relaxation scale of [7] |
| $c$ | $2.9979\times10^{10}\;\mathrm{cm\,s^{-1}}$ | Defined constant for unit conversion |

All parameters are either taken directly from the cited literature or explicitly labelled as assumptions. The lower coupling bound is $50\;\mathrm{cm^{-1}}$, not the $20\;\mathrm{cm^{-1}}$ of the published sensitivity box, because [4] reports couplings between $-50$ and $-75\;\mathrm{cm^{-1}}$ and no source in this paper's bibliography reports a coupling as small as $20\;\mathrm{cm^{-1}}$ for the BChl 3–4 pair.

## 4. Analysis

### 4.1 Optimal dephasing rate and hopping rate

In the strong‑disorder limit $V\ll\Delta$, adiabatic elimination of the coherences in the Haken–Strobl master equation with the corrected pure‑dephasing generator yields the hopping rate

$$
k(\Gamma)=\frac{2V^{2}\,\Gamma}{\Gamma^{2}+\Delta^{2}}.
$$

Differentiating with respect to $\Gamma$:

$$
\frac{\mathrm{d}k}{\mathrm{d}\Gamma}=2V^{2}\,\frac{(\Gamma^{2}+\Delta^{2})-2\Gamma^{2}}{(\Gamma^{2}+\Delta^{2})^{2}}
=2V^{2}\,\frac{\Delta^{2}-\Gamma^{2}}{(\Gamma^{2}+\Delta^{2})^{2}}.
$$

Setting the derivative to zero gives $\Delta^{2}-\Gamma^{2}=0$, i.e.

$$
\Gamma^{*}=\Delta.
$$

Substituting $\Gamma^{*}$ back into $k(\Gamma)$:

$$
k^{*}=k(\Gamma^{*})=\frac{2V^{2}\Delta}{\Delta^{2}+\Delta^{2}}=\frac{V^{2}}{\Delta}.
$$

#### Numerical range of $k^{*}$

Evaluating $k^{*}=V^{2}/\Delta$ at the four corners of the experimental box:

| Corner | $V$ ($\mathrm{cm^{-1}}$) | $\Delta$ ($\mathrm{cm^{-1}}$) | $k^{*}=V^{2}/\Delta$ ($\mathrm{cm^{-1}}$) |
|--------|--------------------------|-------------------------------|--------------------------------------------|
| 1 (min $V$, max $\Delta$) | $50$ | $180$ | $2500/180=13.8889$ |
| 2 (min $V$, min $\Delta$) | $50$ | $110$ | $2500/110=22.7273$ |
| 3 (max $V$, max $\Delta$) | $75$ | $180$ | $5625/180=31.2500$ |
| 4 (max $V$, min $\Delta$) | $75$ | $110$ | $5625/110=51.1364$ |

Thus

$$
k^{*}\in[13.89,\,51.14]\;\mathrm{cm^{-1}}.
$$

### 4.2 Transfer time $\tau_{T}$

The optimal hopping rate $k^{*}$ has units of wavenumber ($\mathrm{cm^{-1}}$). A wavenumber $\tilde{\nu}$ corresponds to an angular frequency $\omega=2\pi c\,\tilde{\nu}$, so

$$
\omega^{*}=2\pi c\,k^{*}=2\pi c\,\frac{V^{2}}{\Delta}.
$$

The transfer time is the inverse of $\omega^{*}$:

$$
\tau_{T}= \frac{1}{\omega^{*}} = \frac{\Delta}{2\pi c V^{2}}.
$$

**Dimensional check.** $V^{2}$ has units $\mathrm{cm^{-2}}$; multiplying by $c$ ($\mathrm{cm\,s^{-1}}$) gives $\mathrm{cm^{-1}\,s^{-1}}$; dividing $\Delta$ ($\mathrm{cm^{-1}}$) by this gives seconds. The published expression $\hbar\Delta/(2\pi cV^{2})$ instead carries an extra factor of action ($\mathrm{J\,s}$) and is dimensionally inconsistent; it is discarded.

#### Extremal transfer times

With $2\pi c = 2\pi\times2.9979\times10^{10}\;\mathrm{s^{-1}} = 1.8836361\times10^{11}\;\mathrm{s^{-1}}$ per unit wavenumber:

*Maximum* $\tau_{T}$ (smallest $V$, largest $\Delta$): $V=50$, $\Delta=180$,

$$
\begin{aligned}
\tau_{T}^{\mathrm{max}} &= \frac{180}{2\pi c \times 50^{2}}
= \frac{180}{1.8836361\times10^{11}\times2500}
= \frac{180}{4.7090903\times10^{14}}\\
&= 3.8224\times10^{-13}\;\mathrm{s}
= 0.3822\;\mathrm{ps}.
\end{aligned}
$$

*Minimum* $\tau_{T}$ (largest $V$, smallest $\Delta$): $V=75$, $\Delta=110$,

$$
\begin{aligned}
\tau_{T}^{\mathrm{min}} &= \frac{110}{2\pi c \times 75^{2}}
= \frac{110}{1.8836361\times10^{11}\times5625}
= \frac{110}{1.0595453\times10^{15}}\\
&= 1.0382\times10^{-13}\;\mathrm{s}
= 0.1038\;\mathrm{ps}.
\end{aligned}
$$

Hence

$$
\tau_{T}\in[0.1038,\,0.3822]\;\mathrm{ps}.
$$

These bounds supersede both the dimensionally inconsistent values of the published version and the rounding $[0.1039,0.3823]\;\mathrm{ps}$ carried in its arithmetic; recomputation with $2\pi c=1.8836361\times10^{11}$ gives $0.38224$ and $0.10382\;\mathrm{ps}$, which round to $0.3822$ and $0.1038$.

### 4.3 Trapping‑limited efficiency $\eta$

The recombination rate follows from the assumed exciton lifetime $\tau_{e}=1\;\mathrm{ns}$:

$$
\gamma_{\mathrm{rec}} = \frac{1}{\tau_{e}} = \frac{1}{1\;\mathrm{ns}} = 10^{-3}\;\mathrm{ps^{-1}}.
$$

The single‑hop trapping efficiency for a trap rate $\kappa$ and recombination $\gamma_{\mathrm{rec}}$ is

$$
\eta = \frac{\kappa}{\kappa+\gamma_{\mathrm{rec}}}
= \frac{1}{1+10^{-3}}
= \frac{1}{1.001}
= 0.999001.
$$

This is a ceiling: it assumes the excitation has already reached the trap‑bearing site, and multi‑site networks add competing loss channels.

### 4.4 Memory ratio $R$ and regime classification

Using the bounds for $\tau_{T}$ from Section 4.2:

$$
R_{\mathrm{fast}} = \frac{0.1\;\mathrm{ps}}{\tau_{T}} \in \left[\frac{0.1}{0.3822},\,\frac{0.1}{0.1038}\right].
$$

Computing each endpoint:

$$
