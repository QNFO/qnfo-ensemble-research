# Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis

## Abstract

Photosynthetic antennae transfer excitation energy with near‑unity efficiency on sub‑picosecond timescales, and every modeler of this process must decide whether the computationally expensive non‑Markovian boson‑mediated framework is required or a cheaper Markovian dephasing master equation suffices. Earlier applicability tests used a coupling range wider than the experimentally reported values and a transfer‑time formula carrying a spurious factor of $\hbar$. We adopt the experimentally reported coupling and site‑energy‑difference ranges for the FMO BChl 3–4 dimer ($V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$) and use the dimensionally consistent expression $\tau_{T}=\Delta/(2\pi c V^{2})$. At the representative point $(V,\Delta)=(50,110)\ \mathrm{cm^{-1}}$ the transfer time is $\tau_{T}=0.2336\ \mathrm{ps}$ and the single‑hop trapping efficiency is $\eta=0.999001$. The memory ratio $R=\tau_{B}/\tau_{T}$ spans $R_{\mathrm{fast}}\in[0.26,0.96]$ for fast baths ($\tau_{B}=0.1\ \mathrm{ps}$) and $R_{\mathrm{slow}}\in[2.6,9.6]$ for slow baths ($\tau_{B}=1\ \mathrm{ps}$, an assumption), so every slow‑mode scenario in the reported box lies in the non‑Markovian sector while fast baths remain transitional. We formulate a falsifiable hypothesis that the optimal dephasing rate shifts by $\delta\Gamma^{*}/\Gamma^{*}\sim R$ when $R\gtrsim0.5$. The corrected memory‑ratio rule gives modelers an analytically derived guideline for allocating computational effort in excitation‑energy‑transfer modelling.

## 1. Introduction

Photosynthetic organisms convert sunlight into chemical free energy after funnelling excitation through pigment networks with efficiencies exceeding $95\%$ on sub‑picosecond to picosecond excitation‑energy‑transfer (EET) timescales [2], [8]. Every computational study of this process faces a concrete methodological decision with real costs on both sides: implement the full non‑Markovian boson‑mediated framework, which retains bath memory at the price of time‑nonlocal kernels and large numerical effort, or use a Markovian dephasing master equation, which is cheap but discards physics exactly when bath correlation times approach the transfer time. Choosing wrongly either wastes high‑performance‑computing allocations or produces transfer rates and optimal dephasing conditions that are quantitatively wrong, which in turn misguides design parameters for bio‑inspired light‑harvesting devices and the interpretation of ultrafast spectra. A validated, analytically derived decision rule would let a modeler allocate compute where memory effects matter and skip them where they do not.

Several strands of prior work frame this decision. Markovian master equations remain the standard initial test‑bed for exciton transport, and a careful treatment of the Bloch‑Redfield equations shows that a complete understanding of coherence and spectral response in molecular aggregates requires the inclusion of non‑Markovian effects, while Markovian equations still provide powerful insight when their approximations are applied consistently [9]. Simulations of the FMO complex find that quantum correlations contribute a significant fraction of the total correlation during the first picosecond of dynamics [7], and entanglement in FMO persists on picosecond timescales, essentially until the excitation is trapped [3]. On the experimental side, single‑molecule pump–probe spectroscopy resolves sub‑100 fs energy relaxation in individual light‑harvesting complexes [6], so fast bath components with correlation times of order $0.1\ \mathrm{ps}$ are measured, not inferred. The target framework whose applicability we assess is the non‑Markovian boson‑mediated description, in which structured phonon fields are proposed to direct exciton transport with efficiencies above $95\%$ [13]. A previous applicability analysis of that framework proposed a memory‑ratio test, but it rested on a coupling range wider than the experimentally reported values, on a transfer‑time formula carrying a spurious factor of $\hbar$, and on an analogy to urban transportation networks that does not survive scrutiny [12]. This paper corrects those errors and re‑derives the criterion.

**Contributions.**
1. Derivation of the optimal dephasing rate $\Gamma^{*}=\Delta$ and optimal hopping rate $k^{*}=V^{2}/\Delta$ for the two‑site Haken–Strobl model, with the derivative shown explicitly (Section 4.1).
2. Correction of the transfer‑time formula to $\tau_{T}=\Delta/(2\pi c V^{2})$, with a dimensional check, and its evaluation over the experimentally reported box, giving $\tau_{T}\in[0.1039,0.3823]\ \mathrm{ps}$ (Section 4.2).
3. Computation of the single‑hop trapping‑limited efficiency $\eta=0.999001$ under stated assumptions for the trap and recombination rates (Section 4.3).
4. Recomputation of the memory ratios over the experimentally reported box $V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$, giving $R_{\mathrm{fast}}\in[0.26,0.96]$ and $R_{\mathrm{slow}}\in[2.6,9.6]$, with a corner‑extremality argument (Section 4.4).
5. A corrected regime classification: within the reported box no bath in the range $\tau_{B}\in[0.1,1]\ \mathrm{ps}$ falls in the Markovian sector, and slow baths are non‑Markovian everywhere (Section 5).
6. A falsifiable projection that the non‑Markovian correction to the optimal dephasing rate scales as $\delta\Gamma^{*}/\Gamma^{*}\sim R$, together with an explicit statement of the convention dependence introduced by the $2\pi$ factor in $\tau_{T}$ (Sections 5 and 6).

## 2. Background and Related Work

**Incoherent rate‑equation models of antenna rings.** Reference [1] models incoherent energy transfer in light‑harvesting antenna systems with a two‑parameter, two‑dimensional set of 17 coupled linear rate equations for the excited bacteriochlorophyll dimers of a ring, and reports that when a BChl molecule is excited, the energy can reach equilibrium within about $10\ \mathrm{ps}$. That work demonstrates that rate‑equation (fully incoherent) descriptions are already competitive for antenna‑scale dynamics on $10\ \mathrm{ps}$ timescales, which sharpens the question of when the more expensive non‑Markovian treatment is actually needed at the dimer scale studied here.

**Superradiance transition and trapping in FMO.** Reference [2] analyzes energy transport in the seven‑site FMO complex with an effective non‑Hermitian Hamiltonian and shows that a superradiance transition occurs at approximately the same coupling to the reaction center for which energy transport efficiency is maximal; the maximal efficiency depends only weakly on temperature and the effect survives the presence of the thermal bath. This establishes that trapping‑induced level broadening, not only dephasing, controls efficiency, and it motivates our inclusion of an explicit trap rate $\kappa$ in the toy model.

**Entanglement and dimer structure in FMO.** Reference [3] shows, using the well‑characterized Chlorobium tepidum site energies and couplings, that pairs of chromophores in FMO are moderately strongly coupled and effectively form dimers whose Frenkel excitons are primarily delocalized across the dimer, with entanglement persisting on picosecond timescales until trapping. The two‑site dimer used in Section 3 is therefore not merely a convenience: it is the dynamically relevant unit identified in that work. Reference [5] reviews dimeric spin‑boson studies in which the bath frequency cutoff, and hence the timescale of the bath response, directly controls the persistence of bipartite entanglement, and reports that entanglement in FMO and LHCII is remarkably robust when the environmental dynamics are included on their natural timescales. This is the closest qualitative precedent for a timescale‑based criterion: bath response time relative to system time controls the quantum character of the dynamics.

**Delocalized excitons as the generic regime.** Reference [4] surveys natural light‑harvesting complexes and concludes that the majority of excitons residing in pigment molecules are well described by Frenkel exciton theory, typically delocalized over a few to tens of pigments, and that determining how fast excitons move between regions in the presence of disorder and fluctuations requires reliable energetic and dynamic data. We take this as the justification for working with a Frenkel‑exciton two‑level dimer Hamiltonian rather than a Wannier‑exciton or continuum model.

**Ultrafast single‑molecule spectroscopy.** Reference [6] applies a single‑molecule pump–probe (SM2P) technique to individual LH2 complexes and demonstrates that ultrafast energy relaxation, in the sub‑100 fs range, can be observed in individual light‑harvesting complexes; the observed relaxation‑time distribution is explained by the energetic disorder of the LH2 pigments at the values commonly used in bulk spectroscopy modelling. This provides the empirical anchor for our fast‑bath correlation time $\tau_{B}=0.1\ \mathrm{ps}$.

**Quantum correlations in the first picosecond.** Reference [7] simulates the FMO complex at cryogenic and physiological temperatures and finds that the single‑excitation relative entropy of entanglement equals the quantum discord in all simulated cases, with quantum correlations contributing a significant fraction of the total correlation during the first picosecond of dynamics. A memory ratio $R\gtrsim0.5$ corresponds, in the language of that work, to bath memory persisting over a large fraction of the transfer process, which is precisely the regime where such correlations are observed.

**Dimerization‑assisted transport and overall efficiency.** Reference [8] models LH2 as two coupled bacteriochlorophyll rings with an open‑quantum‑system master equation and shows that dimerization of the B850 ring can enhance transfer efficiency and shorten the average transfer time; the same work states that photosynthetic energy capture and transport to the reaction center completes within about $100\ \mathrm{ps}$ with more than $95\%$ efficiency. These system‑level numbers bound the trap and recombination rates used in Section 4.3.

**Markovian master equations and their limits.** Reference [9] challenges the view that Bloch‑Redfield equations are inferior to phenomenological Lindblad equations, shows that non‑positivity and loss of coherent oscillations are not inherent to the Bloch‑Redfield formalism when a consistent physical model underpins it, and states that a complete understanding of coherence and spectral response requires the inclusion of non‑Markovian effects. Our criterion complements that work: it tells the modeler when the Markovian equations that [9] treats carefully must nevertheless be abandoned for a non‑Markovian description.

**Experimentally reported dimer parameters.** Reference [10] studies a vibronic exciton heterodimer with parameters chosen to mimic the FMO complex and reports that the transition energy difference between BChl 3 and 4 is proposed to be from about $110$ to $180\ \mathrm{cm^{-1}}$, that the excitonic coupling between these two molecules is negative with values from about $-50$ to $-75\ \mathrm{cm^{-1}}$, and that fluorescence line narrowing spectroscopy reveals vibrational modes near $180\ \mathrm{cm^{-1}}$ with a total Huang–Rhys factor of $0.03$. These are the experimentally reported ranges adopted throughout this paper, and they correct the wider coupling box used in the previous version of this analysis [12].

**Single‑photon absorption with non‑Markovian phonon coupling.** Reference [11] combines a continuous‑mode quantum optical master equation with a hierarchy of equations of motion for excitonic dynamics in the presence of non‑Markovian phonon coupling, producing simulations of photon absorption under realistic pigment–protein conditions that cover the full range of timescales from femtoseconds to nanoseconds. That work shows concretely what the expensive branch of our decision rule costs and what it buys: a unified treatment of absorption and transfer across four orders of magnitude in time.

**The target framework and the analysis under revision.** Reference [13] proposes the boson–fermion signaling framework, in which structured phonon fields act as signals that direct excitons through the energy landscape, and reports simulations in which this phonon guidance sustains transfer efficiencies above $95\%$. Reference [12] is the previous applicability analysis of that framework, which introduced the memory ratio $R=\tau_{B}/\tau_{T}$ but suffered from the parameter‑range, formula, and analogy errors corrected here. We retain its criterion structure and re‑derive every number.

## 3. Methods

### 3.1 Toy model

We adopt a two‑site Frenkel‑exciton Hamiltonian in the single‑excitation manifold, following the dimer structure identified in FMO [3] and the parameterization of [10]:

$$
H_{S}= \frac{\Delta}{2}\,\sigma_{z}+V\,\sigma_{x},
$$

where $\Delta$ is the site‑energy difference, $V$ the excitonic coupling magnitude, and $\sigma_{x},\sigma_{z}$ are Pauli operators in the site basis. The system is subject to pure dephasing at rate $\Gamma$ and a trap on site 2 with rate $\kappa$. The dephasing dissipator is the standard Lindblad form with jump operator $\sigma_{z}$,

$$
\frac{\mathrm{d}\rho}{\mathrm{d}t}\Big|_{\mathrm{deph}} = -\frac{\Gamma}{2}\,[\sigma_{z},[\sigma_{z},\rho]],
$$

which in the site basis damps the off‑diagonal element $\rho_{12}$ at rate $\Gamma$ while leaving populations unchanged. (The previous version of this analysis wrote the dephasing term as $-\frac{\Gamma}{2}(1-\sigma_{z}^{2}/2)$; since $\sigma_{z}^{2}=\mathbb{I}$, that expression is a multiple of the identity, generates no dynamics, and is incorrect as a dissipator [12].)

### 3.2 Re‑entry criterion

We define the memory ratio

$$
R=\frac{\tau_{B}}{\tau_{T}},
$$

with $\tau_{B}$ the bath correlation time and $\tau_{T}$ the transfer time derived in Section 4.2. Thresholds are set as

- $R\lesssim0.1$: Markovian reduction suffices.
- $0.1<R<0.5$: Transitional regime; error estimation required.
- $R\gtrsim0.5$: Non‑Markovian framework required.

These thresholds are conventions that render the criterion falsifiable; the qualitative conclusion below (slow baths are non‑Markovian everywhere in the reported box) is insensitive to threshold shifts of order unity, as shown in Section 4.4.

### 3.3 Input parameters

| Symbol | Value | Status and rationale |
|--------|-------|-----------|
| $V$ | $[50,75]\ \mathrm{cm^{-1}}$ | Experimentally reported: excitonic coupling of the FMO BChl 3–4 pair is from about $-50$ to $-75\ \mathrm{cm^{-1}}$ [10]; we use the magnitude |
| $\Delta$ | $[110,180]\ \mathrm{cm^{-1}}$ | Experimentally reported transition‑energy difference for BChl 3–4 [10] |
| $\kappa$ | $1\ \mathrm{ps^{-1}}$ | Assumption, chosen so that a multi‑hop path completes within the $\sim100\ \mathrm{ps}$ system‑level transfer time reported for photosynthetic antennae [8] |
| $\tau_{e}$ | $1\ \mathrm{ns}$ | Assumption for the exciton lifetime, consistent with near‑unity internal quantum efficiency of light harvesting [11] |
| $\tau_{B}$ | $[0.1,\,1]\ \mathrm{ps}$ | Fast bound from observed sub‑100 fs relaxation processes in single complexes [6]; slow bound $\tau_{B}=1\ \mathrm{ps}$ is an assumption for slow intramolecular modes |
| $c$ | $2.9979\times10^{10}\ \mathrm{cm\,s^{-1}}$ | Speed of light for wavenumber‑to‑frequency conversion |

All parameters are either taken from the cited literature or stated as explicit assumptions. The vibrational modes near $180\ \mathrm{cm^{-1}}$ with total Huang–Rhys factor $0.03$ reported for the FMO lowest‑energy BChl [10] have periods $T=1/(c\,\tilde\nu)=1/(2.9979\times10^{10}\times180)\ \mathrm{s}=1.86\times10^{-13}\ \mathrm{s}=0.186\ \mathrm{ps}$, which is of the same order as $\tau_{T}$; this is the physical reason a timescale comparison is decisive for this dimer.

## 4. Analysis

### 4.1 Optimal dephasing rate

In the strong‑disorder limit $V\ll\Delta$, the Haken–Strobl hopping rate under pure dephasing $\Gamma$ is

$$
k(\Gamma)=\frac{2V^{2}\,\Gamma}{\Gamma^{2}+\Delta^{2}}.
$$

Setting $\frac{\mathrm{d}k}{\mathrm{d}\Gamma}=0$ yields

$$
\frac{\mathrm{d}}{\mathrm{d}\Gamma}\!\left(\frac{2V^{2}\Gamma}{\Gamma^{2}+\Delta^{2}}\right)
=2V^{2}\,\frac{(\Gamma^{2}+\Delta^{2})-\Gamma\cdot 2\Gamma}{(\Gamma^{2}+\Delta^{2})^{2}}
=2V^{2}\,\frac{\Delta^{2}-\Gamma^{2}}{(\Gamma^{2}+\Delta^{2})^{2}}=0
\;\Longrightarrow\;
\Gamma^{*}=\Delta.
$$

Thus the optimal dephasing rate equals the energetic disorder:

$$
\Gamma^{*}= \Delta.
$$

This recovers, in the dimer limit, the noise‑assisted‑transport mechanism studied at the network level: dephasing tuned to the system's energy scales opens transport pathways [7], [9].

### 4.2 Transfer time

Substituting $\Gamma^{*}$ into $k(\Gamma)$ gives the optimal hopping rate

$$
k^{*}=k(\Gamma^{*})=\frac{2V^{2}\Delta}{2\Delta^{2}}=\frac{V^{2}}{\Delta}.
$$

The rate $k^{*}$ is expressed in $\mathrm{cm^{-1}}$; multiplying by the speed of light $c$ converts it to a frequency in $\mathrm{s^{-1}}$, and the factor $2\pi$ converts that frequency to an angular frequency:

$$
\omega^{*} = 2\pi\,c\,\frac{V^{2}}{\Delta}.
$$

The transfer time is the inverse of $\omega^{*}$:

$$
\tau_{T}= \frac{1}{\omega^{*}} = \frac{\Delta}{2\pi c V^{2}}.
$$

Dimensional check: $V^{2}/\Delta$ has units $\mathrm{cm^{-1}}$; $c\,V^{2}/\Delta$ has units $\mathrm{cm\,s^{-1}\,cm^{-1}}=\mathrm{s^{-1}}$; $2\pi c\,V^{2}/\Delta$ has units $\mathrm{s^{-1}}$; its inverse has units $\mathrm{s}$. The formula is dimensionally consistent. (The previous version wrote $\tau_{T}=\hbar\Delta/(2\pi c V^{2})$ [12]; since $\hbar$ carries units of action $\mathrm{J\,s}$, that expression has units $\mathrm{J\,s^{2}}$, which is not a time. The factor of $\hbar$ is spurious and is removed.)

Using the representative point $(V,\Delta)=(50,110)\ \mathrm{cm^{-1}}$:

$$
\begin{aligned}
V^{2} &= 50^{2}=2500\ \mathrm{(cm^{-1})^{2}},\\
2\pi c V^{2} &= 2\pi \times 2.9979\times10^{10}\times 2500 = 4.7091\times10^{14}\ \mathrm{s^{-1}},\\
\tau_{T} &= \frac{110}{4.7091\times10^{14}}
= 2.336\times10^{-13}\ \mathrm{s}
= 0.2336\ \mathrm{ps}.
\end{aligned}
$$

The longest transfer time occurs at the smallest coupling and largest energy gap ($V=50\ \mathrm{cm^{-1}}$, $\Delta=180\ \mathrm{cm^{-1}}$):

$$
\tau_{T}^{\mathrm{max}} = \frac{180}{4.7091\times10^{14}}
= 3.822\times10^{-13}\ \mathrm{s}
= 0.3823\ \mathrm{ps}.
$$

The shortest transfer time occurs at the largest coupling and smallest energy gap ($V=75\ \mathrm{cm^{-1}}$, $\Delta=110\ \mathrm{cm^{-1}}$):

$$
\begin{aligned}
2\pi c V^{2} &= 2\pi \times 2.9979\times10^{10}\times 5625 = 1.0595\times10^{15}\ \mathrm{s^{-1}},\\
\tau_{T}^{\mathrm{min}} &= \frac{110}{1.0595\times10^{15}}
= 1.038\times10^{-13}\ \mathrm{s}
= 0.1039\ \mathrm{ps}.
\end{aligned}
$$

Because $\tau_{T}=\Delta/(2\pi c V^{2})$ is monotone increasing in $\Delta$ and decreasing in $V$, these corner values are the extrema over the whole box; no interior point can exceed them (corner‑extremality argument, used again in Section 4.4).

### 4.3 Trapping‑limited efficiency

With the assumed exciton lifetime $\tau_{e}=1\ \mathrm{ns}$, the recombination rate is $\gamma_{\mathrm{rec}}=1/\tau_{e}=10^{-3}\ \mathrm{ps^{-1}}$. The single‑hop trapping efficiency, i.e. the probability that the excitation is trapped at site 2 before recombination once it arrives, is

$$
\eta = \frac{\kappa}{\kappa+\gamma_{\mathrm{rec}}}= \frac{1}{1+10^{-3}} = 0.999001.
$$

This is an upper bound for the full complex: it neglects recombination during the multi‑hop journey and losses to other pathways, consistent with the system‑level picture in which the full antenna‑to‑reaction‑center transfer completes within about $100\ \mathrm{ps}$ at more than $95\%$ efficiency [8] and with the near‑unity internal quantum efficiency discussed in [11].

### 4.4 Memory ratio and regime classification

Using the bounds $\tau_{T}^{\mathrm{max}}=0.3823\ \mathrm{ps}$ and $\tau_{T}^{\mathrm{min}}=0.1039\ \mathrm{ps}$, the memory ratio for a given bath correlation time $\tau_{B}$ satisfies

$$
R_{\mathrm{fast}} = \frac{0.1\ \mathrm{ps}}{\tau_{T}} \in \left[\frac{0.1}{0.3823},\frac{0.1}{0.1039}\right]=[0.262,0.962],
$$

$$
R_{\mathrm{slow}} = \frac{1\ \mathrm{ps}}{\tau_{T}} \in \left[\frac{1}{0.3823},\frac{1}{0.1039}\right]=[2.616,9.625].
$$

Rounded to two significant figures,

$$
R_{\mathrm{fast}}\in[0.26,0.96],\qquad
R_{\mathrm{slow}}\in[2.6,9.6].
$$

The extrema are attained at the corners of the box because $R=\tau_{B}\,2\pi c V^{2}/\Delta$ is monotone increasing in $V$ and decreasing in $\Delta$; the corner‑extremality argument of Section 4.2 therefore carries over directly, and no interior scan is needed. All slow‑bath values exceed the $0.5$ threshold, placing every slow‑mode scenario in the non‑Markovian sector. Fast baths fall below $0.5$ only when $V<\sqrt{0.5\,\Delta/(2\pi c\,\tau_{B})}$ evaluated in consistent units, i.e. only for the smallest couplings in the box; otherwise they remain transitional. Specifically, $R_{\mathrm{fast}}=0.5$ requires $\tau_{T}=0.