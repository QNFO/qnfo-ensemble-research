# Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis

## Abstract

Photosynthetic antennae transfer excitation energy with near‑unity efficiency on sub‑picosecond timescales, and modelers of these systems must decide whether to pay for a non‑Markovian boson‑mediated framework that retains bath memory or to use a Markovian dephasing master equation that discards it. Earlier applicability tests for this decision used a coupling range wider than the experimentally reported values, a dimensionally inconsistent transfer‑time expression, and memory‑ratio windows that do not follow from the stated inputs. This revision adopts the experimentally reported excitonic coupling magnitude $V\in[50,75]\;\mathrm{cm^{-1}}$ and site‑energy difference $\Delta\in[110,180]\;\mathrm{cm^{-1}}$ for the FMO bacteriochlorophyll 3–4 pair, replaces the transfer‑time expression with the dimensionally consistent $\tau_{T}=\Delta/(2\pi cV^{2})$, and replaces the defective dephasing dissipator with the standard pure‑dephasing Lindblad term. The corrected derivations give a transfer‑time interval $\tau_{T}\in[0.1038,0.3822]\;\mathrm{ps}$, an optimal hopping rate $k^{*}=V^{2}/\Delta\in[13.89,51.14]\;\mathrm{cm^{-1}}$, a single‑hop trapping efficiency $\eta=0.999001$, and memory ratios $R_{\mathrm{fast}}\in[0.26,0.96]$ for an assumed fast bath ($\tau_{B}=0.1\;\mathrm{ps}$) and $R_{\mathrm{slow}}\in[2.6,9.6]$ for an assumed slow bath ($\tau_{B}=1\;\mathrm{ps}$). Every realistic slow‑mode scenario therefore lies in the non‑Markovian sector, while fast solvent‑like baths straddle the transitional threshold. The memory‑ratio rule thus gives modelers a computable, falsifiable criterion for allocating computational effort in excitation‑energy‑transfer modeling.

## 1. Introduction

Designers of bio‑inspired photovoltaic devices and researchers interpreting ultrafast spectroscopic data face a concrete methodological choice: allocate high‑performance‑computing resources to a non‑Markovian boson‑mediated description that retains bath memory, or adopt a Markovian dephasing master equation that discards memory at negligible cost. The non‑Markovian route for a seven‑site FMO simulation is assumed here to require on the order of $10^{4}$ CPU‑hours, while a Markovian master equation runs on a laptop in minutes; both figures are assumptions of this paper, not measurements. An incorrect choice either wastes computational budget or yields quantitatively wrong transfer rates and optimal dephasing conditions, which propagates into sub‑optimal device designs or misinterpreted observables. A decision rule that predicts when memory effects are essential would reduce unnecessary computation and improve the reliability of modeling outcomes.

The physical backdrop is well established. Dephasing‑assisted transport (DAT) — the use of pure dephasing noise to raise excitation‑energy‑transfer (EET) efficiency — has been demonstrated to push efficiencies well above $90\%$ across the Fenna–Matthews–Olson (FMO) complex within a fully Markovian treatment [2], and the underlying mechanisms have been isolated in exactly solvable fully connected networks, where the sink population without noise is only $p_{\mathrm{sink}}(\infty)=1/(N-1)$ [8]. What remains contested is not whether noise helps, but when the cheaper Markovian noise model is quantitatively sufficient. The boson‑mediated framework proposes that structured phonon fields act as directed signals rather than disruptive noise, reporting simulated transfer efficiencies above $95\%$ under that reading [10]; a timescale‑based test of when that framework must replace the Markovian description is the subject of this paper.

Timescale‑based model selection has precedent outside quantum biology: in transient thermal grating analysis, quantitative interpretation of the measured response requires a forward model that consistently connects energy deposition, subsequent transport, and the detected temporal response [1], and the applicable transport regime is selected by comparing the experimental timescales against the model's assumptions. The present work transfers the same logic to EET: compare the bath memory time $\tau_{B}$ against the intrinsic transfer time $\tau_{T}$, and let the ratio decide the modeling framework.

This revision corrects specific defects of the published version [9]. The published text presented $V\in[20,75]\;\mathrm{cm^{-1}}$ as the full experimentally reported coupling range, whereas the cited vibronic‑dimer study reports couplings between $-50$ and $-75\;\mathrm{cm^{-1}}$ for the BChl 3–4 pair [4]; it used a transfer‑time expression $\tau_{T}=\hbar\Delta/(2\pi cV^{2})$ whose units are $\mathrm{J\,s^{2}}$, not time; it quoted memory‑ratio spans ($R=0.17$–$1.70$) that do not follow from its own inputs; it cited an urban‑transportation multiplex‑network study as mirroring the memory‑ratio sensitivity, although that study concerns the extraction of multimodal profiles from city transport networks and makes no claim about quantum transport [3]; and it wrote a dephasing Lindblad term that, because $\sigma_{z}^{2}=\mathbb{1}$, reduces to a multiple of the identity and generates no dephasing at all. Each correction is derived explicitly below.

**Contributions.**

1. Derivation of the optimal dephasing rate $\Gamma^{*}=\Delta$ and optimal hopping rate $k^{*}=V^{2}/\Delta$ for the two‑site Haken–Strobl model, with the differentiation shown step by step and corner‑by‑corner numerical evaluation over the experimental box (Section 4.1).
2. Dimensional verification of the corrected transfer‑time formula $\tau_{T}=\Delta/(2\pi cV^{2})$, an explicit demonstration that the previously published expression $\hbar\Delta/(2\pi cV^{2})$ carries units of $\mathrm{J\,s^{2}}$, and evaluation of $\tau_{T}$ at all four corners of the experimental box, giving $\tau_{T}\in[0.1038,0.3822]\;\mathrm{ps}$ (Section 4.2).
3. Computation of the single‑hop trapping‑limited efficiency $\eta=0.999001$ under trap and recombination rates stated as explicit assumptions (Section 4.3).
4. Exhaustive calculation of the memory ratio $R=\tau_{B}/\tau_{T}$ over the full experimental box, giving $R_{\mathrm{fast}}\in[0.26,0.96]$ and $R_{\mathrm{slow}}\in[2.6,9.6]$, replacing the published span $R=0.17$–$1.70$ (Section 4.4).
5. Replacement of the defective dephasing dissipator $-(\Gamma/2)(1-\sigma_{z}^{2}/2)$ — which vanishes into a term proportional to the identity — with the standard pure‑dephasing Lindblad generator, and verification that it reproduces the hopping rate used in the optimality derivation (Section 3.1 and Section 4.1).
6. Removal of the claim that an urban transportation multiplex‑network study mirrors the memory‑ratio sensitivity, with the actual content of that study stated (Section 2 and Section 6).
7. A falsifiable projection that the non‑Markovian correction to the optimal dephasing rate scales as $\delta\Gamma^{*}/\Gamma^{*}\sim R$, contrasted with the sub‑twofold rate effects reported for nuclear quantum effects in vibrational motion (Sections 5 and 6).

## 2. Background and Related Work

**Noise‑assisted transport in FMO.** The dephasing‑assisted transport study develops physically intuitive mechanisms for the effect of noise on EET and, using a hybrid basis of excitons and sites, shows how noise enables transfer with efficiencies well above $90\%$ across the FMO complex [2]. Its conclusion section states that the identification of transport‑suppressing pathways is made without reference to the noise model, so any noise model that enhances transport must carry out the strategy of suppressing inefficient paths and enhancing direct relaxation channels [2]. This matters here because it licenses a Markovian pure‑dephasing model as the physically meaningful baseline against which non‑Markovian corrections must be measured: if all enhancing noise models act through the same pathway logic, the Markovian baseline captures the mechanism, and the open question is quantitative accuracy, not qualitative possibility.

**Fundamental mechanisms in exactly solvable networks.** The fully connected network analysis derives an exact analytical solution for the density matrix of arbitrarily large uniform networks and shows that with no dissipation and no dephasing the total transfer to the sink is $p_{\mathrm{sink}}(\infty)=1/(N-1)$, a strikingly poor result for large $N$ [8]. Its concluding remarks identify the suppression of destructive interference by dephasing noise, static disorder, and path‑speed differences, together with dephasing‑broadened site overlap, as the key mechanisms of noise‑assisted transport [8]. The two‑site Haken–Strobl optimality condition derived in Section 4.1, $\Gamma^{*}=\Delta$, is the two‑site shadow of the dephasing‑broadened‑overlap mechanism: dephasing must broaden the site lines to the detuning scale before hopping becomes efficient.

**Experimentally grounded excitonic parameters.** The vibronic exciton dimer study states that for the FMO complex there is general agreement that BChl 3 and 4 have the lowest site energies, that the transition energy difference is proposed to be from about $110$ to $180\;\mathrm{cm^{-1}}$, and that the excitonic coupling between these two molecules is negative with values from about $-50$ to $-75\;\mathrm{cm^{-1}}$ [4]. These are the numbers that define the parameter box of this paper; the published claim that the full experimentally reported range extended down to $V=20\;\mathrm{cm^{-1}}$ has no support in this source and is withdrawn. The same study reports a total Huang–Rhys factor of $0.03$ for vibrational modes near $180\;\mathrm{cm^{-1}}$ in the lowest‑energy BChl, and finds that Huang–Rhys factors obtained from fluorescence spectroscopy of strongly coupled complexes need corrections that can reach $100\%$ [4] — a caution that the vibrational side of the parameter box carries non‑negligible experimental uncertainty.

**Atomistic energy funneling.** The atomistic study of green sulfur bacteria constructs a model of $3988$ pigments spanning chlorosome, baseplate, and FMO, solves a quantum master equation including coherent, dephasing, and relaxation processes, and finds that the energy‑funneling results converge within the overall timescale of $10\;\mathrm{ps}$ regardless of initiating conditions [5]. The $10\;\mathrm{ps}$ convergence timescale is the relevant sanity check for this paper's transfer times: the dimer transfer times derived here ($0.1$–$0.4\;\mathrm{ps}$) are an order of magnitude shorter, consistent with the dimer being one fast hop inside a slower multi‑stage funnel. The trap rate and exciton lifetime used in Section 4.3 are not quoted in this source's supplied text; they are stated below as explicit assumptions.

**Ultrafast single‑complex spectroscopy.** The single‑molecule pump–probe (SM2P) study demonstrates that ultrafast energy relaxation can be observed in individual light‑harvesting complexes, with the fastest processes in the sub‑100 fs range, using $200$–$250\;\mathrm{fs}$ pulses from a $76\;\mathrm{MHz}$ Ti:Sapphire laser and showing that the relaxation‑time distribution changes with excitation wavelength in a way explained by energetic disorder of the LH2 pigments [7]. This establishes empirically that sub‑picosecond, indeed sub‑100 fs, relaxation channels exist in antenna complexes; it supports — but does not fix — the choice of a fast bath correlation time $\tau_{B}=0.1\;\mathrm{ps}$ used below, which is therefore labeled an assumption.

**Nuclear quantum effects on rates.** The mixed quantum–classical study compares classical and quantum treatments of vibrational motion in LH2, FMO, and LHCII at $300\;\mathrm{K}$ and concludes that the main difference is not the direction of energy flow but the rate: the classical treatment generally overestimates the transfer rate, the quantum effect on the rate is benign (less than a factor $2$) for biologically relevant parameter regimes, and vibrational‑dipole renormalization provides a simple correction [6]. This bounds the size of one class of non‑Markovian‑adjacent corrections and thereby calibrates the falsifiability threshold of the projection in Section 5: a memory‑scaled shift of order $R$ must exceed this sub‑twofold rate background to be attributable to bath memory alone.

**Urban multiplex networks — a corrected citation.** The multiplex‑network study proposes the overlap census method, which extracts a multimodal profile from a city's multiplex transportation network, applies it to $15$ cities, and finds six k‑means clusters explaining more than $90\%$ of the variance, ranging from bicycle‑dominated Amsterdam to car‑centric clusters containing Los Angeles, Bogota, Mexico City, Beihai, and Jakarta [3]. The published version of the present paper cited this work as mirroring the memory‑ratio sensitivity result; that claim is retracted. The overlap census is a method for reducing a layered infrastructure network to a descriptive profile; it contains no timescale ratio, no quantum dynamics, and no result that parallels $R=\tau_{B}/\tau_{T}$. The citation is retained only to document what the work actually does, so that the retraction is on the record.

**Timescale‑based forward modeling in another transport domain.** The transient thermal grating analysis argues that quantitative interpretation of TTG measurements requires a forward model that consistently connects energy deposition, subsequent heat transport, and the detected temporal response, across transport regimes [1]. This is the methodological template for the present paper: a forward model's validity domain is set by timescale comparisons, and the model‑selection rule must be derived from the model's own parameters rather than assumed.

**The framework under test and its predecessor.** The boson‑mediated framework proposes that bosonic fields (phonons) act as structured control signals directing fermionic excitons through the energy landscape, reports simulated efficiencies above $95\%$ under this reading, and frames the protein environment as actively directing rather than merely perturbing the dynamics [10]. The predecessor of the present paper formulated the timescale‑based re‑entry test for that framework and stated the corrected parameter box, transfer‑time formula, and memory‑ratio windows in its results section [9]. The present revision completes that correction at the level of the abstract, the dissipator, and the cross‑domain citation, and shows every arithmetic step that the corrected numbers rest on.

## 3. Methods

### 3.1 Toy model and corrected dephasing dissipator

We consider the two‑site Haken–Strobl model in the single‑excitation manifold,

$$
H_{S}=\frac{\Delta}{2}\,\sigma_{z}+V\,\sigma_{x},
$$

where $\sigma_{x},\sigma_{z}$ are Pauli matrices on the two‑site basis, $\Delta$ is the site‑energy difference, and $V$ is the excitonic coupling. Site 2 carries a trap with rate $\kappa$.

The published version wrote the dephasing Lindblad term as

$$
-\frac{\Gamma}{2}\Bigl(1-\frac{\sigma_{z}^{2}}{2}\Bigr).
$$

This term is defective. Since $\sigma_{z}^{2}=\mathbb{1}$, the operator $1-\sigma_{z}^{2}/2=\mathbb{1}/2$, so the whole expression equals $-(\Gamma/4)\,\mathbb{1}$: a term proportional to the identity superoperator, which generates no evolution of any density‑matrix element and in particular no dephasing. The correct pure‑dephasing Lindblad generator with jump operator $\sigma_{z}$ is

$$
\mathcal{L}_{\phi}[\rho]=-\frac{\Gamma}{2}\,[\sigma_{z},[\sigma_{z},\rho]],
$$

which leaves populations invariant and damps the coherence $\rho_{12}$ as $\dot{\rho}_{12}=-2\Gamma\,\rho_{12}$ in the energy eigenbasis convention used here; the hopping‑rate expression derived in Section 4.1 fixes the convention so that $\Gamma$ is the dephasing rate entering the linewidth. All subsequent derivations use this corrected generator. The correction does not change the optimality result $\Gamma^{*}=\Delta$, which follows from the standard Haken–Strobl hopping rate; it changes only the written form of the dynamics, which in the published version could not produce dephasing at all.

### 3.2 Re‑entry criterion

The memory ratio is

$$
R=\frac{\tau_{B}}{\tau_{T}},
$$

with $\tau_{B}$ the bath correlation time and $\tau_{T}$ the intrinsic single‑hop transfer time derived in Section 4.2. The thresholds are conventions chosen to render the criterion falsifiable:

- $R\lesssim 0.1$: Markovian reduction suffices.
- $0.1<R<0.5$: transitional regime; error estimation against a non‑Markovian benchmark required.
- $R\gtrsim 0.5$: non‑Markovian framework required.

The thresholds are not derived from first principles here; they are stated as the decision boundaries whose empirical adequacy the projection in Section 5 is designed to test.

### 3.3 Input parameters

| Symbol | Value | Status |
|--------|-------|--------|
| $V$ | $[50,75]\;\mathrm{cm^{-1}}$ (magnitudes of the reported $-50$ to $-75\;\mathrm{cm^{-1}}$) | reported in [4] |
| $\Delta$ | $[110,180]\;\mathrm{cm^{-1}}$ | reported in [4] |
| $\kappa$ | $1\;\mathrm{ps^{-1}}$ | assumption of this paper |
| $\tau_{e}$ | $1\;\mathrm{ns}$ | assumption of this paper |
| $\tau_{B}$ | $0.1\;\mathrm{ps}$ (fast) and $1\;\mathrm{ps}$ (slow) | assumptions; the fast value is motivated by the sub‑100 fs relaxation resolved in [7], the slow value represents intramolecular modes of order the $180\;\mathrm{cm^{-1}}$ scale discussed in [4] |
| $c$ | $2.9979\times10^{10}\;\mathrm{cm\,s^{-1}}$ | defined constant for unit conversion |

Every parameter is either taken from the cited literature with the specific value stated in the source, or labeled an assumption. The trap rate $\kappa$ and exciton lifetime $\tau_{e}$ were previously attributed to the atomistic study [5]; that attribution is withdrawn and both values are carried as assumptions.

## 4. Analysis

### 4.1 Optimal dephasing rate and hopping rate

In the strong‑disorder limit $V\ll\Delta$, adiabatic elimination of the coherences in the Haken–Strobl master equation with the corrected pure‑dephasing generator of Section 3.1 gives the hopping rate

$$
k(\Gamma)=\frac{2V^{2}\,\Gamma}{\Gamma^{2}+\Delta^{2}}.
$$

Differentiating with respect to $\Gamma$:

$$
\frac{\mathrm{d}k}{\mathrm{d}\Gamma}
=2V^{2}\,\frac{(\Gamma^{2}+\Delta^{2})-\Gamma\cdot 2\Gamma}{(\Gamma^{2}+\Delta^{2})^{2}}
=2V^{2}\,\frac{\Delta^{2}-\Gamma^{2}}{(\Gamma^{2}+\Delta