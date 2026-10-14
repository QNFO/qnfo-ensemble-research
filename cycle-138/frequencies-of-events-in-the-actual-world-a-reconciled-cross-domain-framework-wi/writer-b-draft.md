# Frequencies of Events in the Actual World: A Reconciled Cross-Domain Framework with Explicit Arithmetic

## Abstract

Every empirical discipline counts events, but the practice of measuring event frequencies is fragmented across fields that rarely compare methods. This paper develops a cross-domain framework for event-frequency observation in the actual world, organized around three questions: what counts as an event, what sampling process generates the observed counts, and what a claimed frequency structure requires as evidence. We formalize event observation as a detected point process, distinguish Archimedean (freely placed) from radix‑locked ($p$‑adic) frequency parameterizations, and impose a single statistical discipline: Poisson count modeling with explicit sample‑size requirements. As worked examples we compute the radix‑locked angular frequencies $\omega_p = 2\pi/\ln(p)$ for $p \in \{2,3,5,7\}$, obtaining $\omega_2 = 9.064722$ through $\omega_7 = 3.228919$; we convert the impulsive radio‑event frequencies $\{98, 120, 132, 160\}$ MHz recorded in the quiet solar corona to angular frequencies, averaging $\overline{\Omega} = 8.01\times10^{8}\ \mathrm{rad\,s^{-1}}$; we show by two complementary tests that this frequency set carries no radix‑locked structure; and we derive Poisson zero‑event upper limits and the sample‑size rule $N \gtrsim 1/\epsilon^{2}$. The framework converts an open question about event frequencies in the actual world into falsifiable, arithmetically explicit tests, and its contribution is methodological rather than empirical.

## 1. Introduction

The question *what frequencies of events are observed in this, the actual world?* is deliberately ambiguous. It can be read metaphysically — is there a lawful distribution of event frequencies in the actual world? — or empirically: given the events we actually observe, across instruments and domains, what frequencies do they exhibit, and what structure, if any, do those frequencies carry? This paper takes the empirical reading seriously while refusing to overclaim on the metaphysical reading.

Every empirical science counts events: radio astronomers count impulsive bursts, social‑media researchers count posts during crises, computational linguists count causal event pairs in text, and physicists count annihilation candidates attributed to dark matter. But the *frequency* of an event is not a property of the world alone; it is a property of the joint system of world, detector, sampling protocol, and counting convention. A burst at 132 MHz exists as an “event” only relative to an instrument with a specific band, sensitivity, and trigger logic; a “real‑world event” in social media exists only relative to a keyword lexicon and a platform’s data access.

Our strategy is to define a minimal formal object — an event‑count process with a rate parameter $\lambda$ — and to ask three questions of any concrete event stream: (i) what is the observed rate and its uncertainty; (ii) is the stream consistent with a memoryless Poisson process, or does it show log‑periodic structure; (iii) if structure is claimed, what sample size would be required to establish it at a stated confidence? The radix‑locked (p‑adic) family of log‑periodic structures, searched for in the cosmic microwave background bispectrum with published non‑detection bounds [10], supplies our parametric example of such structure.

The paper's contributions are: (1) a unified event‑frequency formalism applicable to linguistic, social, acoustic, simulated, and physical event streams (Section 3); (2) explicit arithmetic for the radix‑locked angular frequencies, their ratios, Poisson probabilities, zero‑event upper limits, and the sample‑size requirement $N \gtrsim 1/\epsilon^{2}$ (Section 4); (3) a worked radix‑locking test on the four quiet‑corona radio‑impulsive frequencies recorded by the Murchison Widefield Array at 98, 120, 132, and 160 MHz [6], showing that the channel set is not radix‑locked (Section 4); and (4) a discussion of failure modes and falsification conditions (Section 6). Throughout, we distinguish sharply between numbers computed here with shown arithmetic, numbers quoted from the supplied literature entries, and projections carrying stated assumptions.

## 2. Background and Related Work

The relevant literature spans natural language processing, social computing, audio machine learning, embodied agents, fundamental physics, and the QNFO corpus. We survey it in bibliography order.

**Event causality in language [1].** The work on inference of fine‑grained event causality from blogs and films starts from the observation that human understanding of narrative is mainly driven by reasoning about causal relations between events, making their recognition a key capability for computational language understanding; it notes two routes — acquiring a knowledge base of common causal relations between events, or understanding a particular narrative's causal structure. This fixes the linguistic end of the event spectrum: an “event” in text is individuated by causal role, not by physical timestamp, so event frequencies over such corpora count causal units and require an explicit mapping before comparison with physically timestamped counts. The entry reports no frequency statistics, so we use it only to motivate the event ontology.

**Social media during real‑world events [2].** The study of Facebook content during real‑world events observes that prior studies analyzed the role and dynamics of Twitter during real‑world events, but little work had explored other social media services or compared content across two networks during the same events, and argues that platforms like Facebook also play a vital role in disseminating information during such events. This supplies the multi‑detector perspective: the same real‑world event is observed by multiple platforms with different populations, so per‑platform event frequencies are detector‑dependent and must not be conflated with a world‑side rate. The entry states no quantitative rates.

**Sound event localization and detection [3].** Sound event localization and detection (SELD) unifies sound event detection with direction‑of‑arrival estimation, inheriting the challenges of both tasks — noise, reverberation, interference, polyphony, and non‑stationarity of sound sources — plus the additional challenge of assigning correct correspondence between detections and sources; error analysis identifies what makes the task difficult. Polyphony and non‑stationarity are precisely the conditions under which naive Poisson rate estimates for acoustic events fail, and the correspondence problem is an event‑identity ambiguity that our counting formalism must treat as a systematic uncertainty.

**Closed‑loop evaluation of world models [4].** Generative world models can now simulate worlds with striking visual realism, raising the question of whether they endow embodied agents with predictive perception for decision making; progress has been limited by fragmented evaluation, since most benchmarks adopt open‑loop protocols emphasizing visual quality in isolation, and the World‑in‑World benchmark evaluates world models in a closed‑loop world. For event frequencies, closed‑loop evaluation matters because an agent’s actions change which events it subsequently observes: the effective event rate experienced by an embodied agent is action‑conditioned, and simulated worlds are a controlled laboratory where event counts are exactly known by construction. The entry reports no event‑rate statistics.

**Algorithmicity of the world [5].** A test based on algorithmic complexity theory and an experimental evaluation of Levin’s universal distribution was proposed to identify evidence for or against the claim that the world is algorithmic in nature, implemented as a statistical comparison of the frequency distributions of data from physical sources on the one hand and repositories of information on the other. This is the closest methodological antecedent to our question: it treats the frequency distribution of observed data as a diagnostic of the world’s underlying structure. Our radix‑locking tests are a narrower, parametric cousin: where [5] compares whole frequency distributions against a universal prior, we test a specific one‑parameter family of log‑periodic structures.

**Radio impulsive events and dark matter [6].** The Murchison Widefield Array recorded impulsive radio events in the quiet solar corona at frequencies 98, 120, 132, and 160 MHz, and it has been proposed that these events are the direct manifestation of dark matter annihilation events within the axion quark nugget (AQN) framework, building on prior arguments about AQN annihilation events. This is the only entry with concrete observed event frequencies in a physical channel, and we use it as our worked example. Note carefully what the entry supports: the four frequency values, the instrument, the quiet‑corona setting, and the AQN interpretation as a proposal. It does not supply event counts or rates, so our test concerns the frequency *values* as a candidate radix‑locked set, not the temporal statistics of the impulses.

**Brane‑world gravity [7].** The Hamiltonian theory of brane‑world gravity presents a canonical formulation in which a four‑dimensional brane is embedded in a five‑dimensional bulk, enabling the study of physical phenomena via Hamiltonian equations. We cite this as a structural analogy: just as the Hamiltonian formulation separates bulk from brane dynamics, our framework separates the world‑side event‑generating process (the “bulk”) from the detector‑side observation process (the “brane”), and insists that frequency claims specify which layer they refer to. The entry gives no further detail, so we use it only at this structural level.

**Frequency separation for real‑world super‑resolution [8].** Most super‑resolution methods assume paired low‑resolution/high‑resolution images or a known down‑scaling operator; while effective on benchmarks, they often fail to produce convincing results in real‑world settings, and a frequency‑separation approach has been proposed for the real‑world case. The analogy is direct: methods calibrated on idealized observation models fail on actual‑world streams whose degradation operator is unknown, and the fix involves separating frequency bands — the same move we make by separating the world‑side event process from detector‑side degradation before inferring rates.

**QNFO corpus entries [9]–[12].** The QNFO MASS‑FREQUENCY entry [9] and the “Nature of Zitterbewegung” entry [11] carry no summary text; we note only their title‑level role and state explicitly that no further detail is available from the material. The $p$‑adic CMB bispectrum search [10] supplies the quantitative anchor: radix‑locked oscillations with angular frequency $\omega_p = 2\pi/\ln(p)$ for $p \in \{2,3,5,7\}$, upper bounds $\epsilon_p < 2.5$ at 95 % confidence, no detection, within a single‑modulation model. Finally, the “Zitterbewegung: From Archimedean Puzzle to Adelic Observable” entry [12] supplies substantive content: the structural underdetermination of the position operator in relativistic quantum mechanics arises from a single representation‑theoretic origin (the Silent Parameter Principle, with SU(2) and $\mathbb{Z}_2^x$ sharing identical fusion rules at matching levels), and the 2‑adic Zitterbewegung frequency deviates from the Archimedean value. Entry [12] is a concrete case where an Archimedean frequency and a $p$‑adic frequency diverge — exactly the discrimination our framework is designed to test in event streams.

## 3. Methods

### 3.1 Events as a detected point process

Let the world generate an event process with unobserved rate $\lambda_w$ (events per unit time in some class $c$). A detector $D$ with sensitivity window $W_D$ and threshold $\theta_D$ produces detections. We model the detected count in observation time $T_{\text{obs}}$ as Poisson:

$$
N_D \sim \text{Poisson}(\lambda_D T_{\text{obs}}), \qquad 
\lambda_D = \eta_D(\theta_D, W_D)\,\lambda_w,
$$

where $\eta_D \in [0,1]$ is the detector efficiency. The central methodological rule of this paper is that any reported event frequency is $\lambda_D$, not $\lambda_w$, unless $\eta_D$ is known and corrected for. The probability of observing zero events despite a nonzero rate is

$$
P(N_D = 0) = e^{-\lambda_D T_{\text{obs}}}.
$$

If zero events are seen in time $T_{\text{obs}}$ at confidence level $1-\alpha$, any rate $\lambda_D$ with $e^{-\lambda_D T_{\text{obs}}} > \alpha$ is not excluded, so the 95 % upper limit satisfies

$$
\lambda_D^{\text{UL}} = \frac{-\ln 0.05}{T_{\text{obs}}} = \frac{2.996}{T_{\text{obs}}}.
$$

The structural alternative to the homogeneous null $\lambda_t = \lambda_0$ is a log‑periodic modulation of the rate,

$$
\lambda_t = \lambda_0 \left[1 + \epsilon_p \cos\!\left(\omega_p \ln \frac{t}{t_0}\right)\right], \qquad 
\omega_p = \frac{2\pi}{\ln p},
$$

with $|\epsilon_p| < 1$ required for positivity of the rate. This is the single‑modulation form consistent with the parametric family searched in the CMB bispectrum analysis [10], transplanted from angular bispectrum amplitude to event rate.

### 3.2 Archimedean versus radix‑locked parameterizations

Let an observed set of characteristic frequencies be $F = \{f_1, \dots, f_k\}$. Two structural hypotheses are:

- **Archimedean:** the $f_i$ are independently placed (e.g., instrumental band centers), with no constraint on ratios $r_{ij} = f_j/f_i$.
- **Radix‑locked ($p$‑adic):** structure appears in log‑space at angular frequencies $\omega_p = 2\pi/\ln p$, so a log‑periodic modulation of period $\ln p$ produces ratios that are powers of $p$.

We apply two complementary tests. **Test 1 (pairwise‑ratio residual, base $p$):** define

$$
\delta_{ij}(p) = \left| \log_p r_{ij} - \operatorname{round}\!\left(\log_p r_{ij}\right) \right|,
$$

and declare the set consistent with base $p$ if $\max_{i,j} \delta_{ij}(p) < \epsilon$ for a pre‑declared tolerance. We use $\epsilon = 0.15$, stated as a convention, not a derived constant. **Test 2 (consecutive log‑spacing):** the radix‑locking hypothesis for prime $p$ asserts that consecutive log‑spacings equal $\ln(p)$:

$$
\Delta_i = \ln\frac{f_{i+1}}{f_i} \stackrel{?}{=} \ln(p).
$$

Test 2 is deliberately conservative: it asks whether the frequency values themselves carry the radix structure, independent of any temporal modulation.

### 3.3 Sample‑size requirement

To resolve a fractional modulation of amplitude $\epsilon$ in a mean event count, the statistical precision of the estimated mean over $N$ events scales as $1/\sqrt{N}$ (standard error of a Poisson mean). Requiring the precision to be at least as fine as the modulation gives

$$
\frac{1}{\sqrt{N}} \lesssim \epsilon \quad \Longrightarrow \quad N \gtrsim \frac{1}{\epsilon^{2}}.
$$

### 3.4 Domain mapping

Each domain contributes an event stream under this formalism: causal‑event mentions in narrative text [1]; platform‑content bursts during real‑world incidents [2]; polyphonic acoustic detections with correspondence ambiguity [3]; exactly‑known event counts in closed‑loop simulated worlds [4]; physical‑source frequency distributions compared against universal expectations [5]; radio impulses in the quiet corona [6]; and, as a theoretical caution, the case where the 2‑adic Zitterbewegung frequency deviates from the Archimedean value [12]. Cross‑detector comparisons are reported as detector‑conditional unless an efficiency correction $\hat{\lambda}_{c,d}/\hat{\eta}_{c,d}$ is available.

## 4. Analysis

All inputs are stated with their sources; all arithmetic is shown step by step.

### 4.1 Radix‑locked angular frequencies

**Input (from [10]):** $\omega_p = 2\pi/\ln(p)$, $p \in \{2,3,5,7\}$. Constants: $2\pi = 6.283185$; $\ln 2 = 0.693147$; $\ln 3 = 1.098612$; $\ln 5 = 1.609438$; $\ln 7 = 1.945910$.

$$
\omega_2 = \frac{6.283185}{0.693147} = 9.064722, \qquad 
\text{check: } 0.693147 \times 9.064722 = 6.283185.
$$

$$
\omega_3 = \frac{6.283185}{1.098612} = 5.719203, \qquad 
\text{check: } 1.098612 \times 5.719203 = 6.283185.
$$

$$
\omega_5 = \frac{6.283185}{1.609438} = 3.903962, \qquad 
\text{check: } 1.609438 \times 3.903962 = 6.283185.
$$

$$
\omega_7 = \frac{6.283185}{1.945910} = 3.228919, \qquad 
\text{check: } 1.945910 \times 3.228919 = 6.283185.
$$

**Ratios.** Because $\omega_p = 2\pi/\ln(p)$, ratios of $\omega$’s are inverse log ratios:

$$
\frac{\omega_2}{\omega_3} = \frac{\ln 3}{\ln 2} = \frac{1.098612}{0.693147} = 1.584962 = \log_2 3,
$$

$$
\frac{\omega_2}{\omega_5} = \frac{1.609438}{0.693147} = 2.321929 = \log_2 5, \qquad 
\frac{\omega_3}{\omega_5} = \frac{1.609438}{1.098612} = 1.464974 = \log_3 5.
$$

These irrational logarithm‑ratio values are the signature of radix‑locking: a radix‑locked spectrum is *not* harmonically spaced, since $\omega_2/\omega_3 = \log_2 3 \approx 1.584962$ is not a ratio of small integers.

**Arithmetic mean of the $\omega_p$ (computed for completeness):**

$$
\overline{\omega} = \frac{9.064722 + 5.719203 + 3.903962 + 3.228919}{4}
= \frac{21.916806}{4} = 5.479201 \approx 5.48.
$$

We emphasize (see Section 6) that this mean has no physical significance: the $\omega_p$ are angular frequencies per log‑unit of a dimensionless argument, not temporal frequencies.

### 4.2 Conversion of the MWA radio frequencies to angular frequencies

**Input (from [6]):** $f \in \{98, 120, 132, 160\}$ MHz. Convert to hertz via $f_{\text{Hz}} = f_{\text{MHz}} \times 10^{6}$, then $\Omega = 2\pi f$:

$$
\Omega_1 = 6.283185 \times 98 \times 10^{6}
= 6.157521\times10^{8}\ \mathrm{rad\,s^{-1}},
$$

$$
\Omega_2 = 6.283185 \times 120 \times 10^{6}
= 7.539822\times10^{8}\ \mathrm{rad\,s^{-1}},
$$

$$
\Omega_3 = 6.283185 \times 132 \times 10^{6}
= 8.293804\times10^{8}\ \mathrm{rad\,s^{-1}},
$$

$$
\Omega_4 = 6.283185 \times 160 \times 10^{6}
= 1.005310\times10^{9}\ \mathrm{rad\,s^{-1}}.
$$

Mean:

$$
\overline{\Omega} = \frac{(6.157521 + 7.539822 + 8.293804 + 10.053096)\times10^{8}}{4}
= \frac{32.044243\times10^{8}}{4}
= 8.011061\times10^{8}\ \mathrm{rad\,s^{-1}}
\approx 8.01\times10^{8}\ \mathrm{rad\,s^{-1}}.
$$

### 4.3 Radix‑locking tests on the MWA frequency set

Natural logarithms: $\ln 98 = 4.584967$; $\ln 120 = 4.787492$; $\ln 132 = 4.882802$; $\ln 160 = 5.075174$.

**Test 2 (consecutive log‑spacings):**

$$
\Delta_1 = \ln\frac{120}{98} = 4.787492 - 4.584967 = 0.202525,
$$

$$
\Delta_2 = \ln\frac{132}{120} = 4.882802 - 4.787492 = 0.095310,
$$

$$
\Delta_3 = \ln\frac{160}{132} = 5.075174 - 4.882802 = 0.192372.
$$

Comparison against $\ln 2 = 0.693147$, $\ln 3 = 1.098612$, $\ln 5 = 1.609438$, $\ln 7 = 1.945910$: none of $\Delta_1, \Delta_2, \Delta_3$ is close to any $\ln(p)$; the smallest absolute deviation is $|\Delta_2 - \ln 2| = |0.095310 - 0.693147| = 0.597837$, and no spacing comes within a factor of $3$ of any $\ln(p)$.

**Test 1 (pairwise ratios).** All pairwise ratios $r_{ij} = f_j/f_i$ with $f_j > f_i$:

$$
r_{1} = \frac{120}{98} = 1.224490, \quad
r_{2} = \frac{132}{98} = 1.346939, \quad
r_{3} = \frac{160}{98} = 1.632653,
$$

$$
r_{4} = \frac{132}{120} = 1.100000, \quad
r_{5} = \frac{160}{120} = 1.333333, \quad
r_{6} = \frac{160}{132} = 1.212121.
$$

Their natural logarithms: $\ln r_1 = 0.202525$, $\ln r_2 = 0.297835$, $\ln r_3 = 0.490207$, $\ln r_4 = 0.095310$, $\ln r_5 = 0.287682$, $\ln r_6 = 0.192372$. Dividing by $\ln p$ and taking distance to the nearest integer:

- Base $p=2$ ($\ln 2 = 0.693147$): residuals $0.29220$, $0.42973$, $0.29278$, $0.13751$, $0.41504$, $0.27756$; maximum $\max \delta_{ij}(2) = 0.42973$.
- Base $p=3$ ($\ln 3 = 1.098612$): residuals $0.18435$, $0.27112$, $0.44621$, $0.08675$, $0.26184$, $0.17508$; maximum $\max \delta_{ij}(3) = 0.44621$.
- Base $p=5$ ($\ln 5 = 1.609438$): residuals $0.12584$, $0.18506$, $0.30460$, $0.05922$, $0.17875$, $0.11953$; maximum $\max \delta_{ij}(5) = 0.30460$.
- Base $p=7$ ($\ln 7 = 1.945910$): residuals $0.10406$, $0.15307$, $0.25191$, $0.04898$, $0.14784$, $0.09886$; maximum $\max \delta_{ij}(7) = 0.25191$.

All four maxima exceed the declared tolerance $\epsilon = 0.15$, by at least a factor of $0.25191/0.15 \approx 1.68$. **Conclusion:** no single radix‑locked base in $\{2,3,5,7\}$ brings the MWA frequency set within tolerance of integer powers. The set is Archimedean‑consistent and radix‑inconsistent under both tests. This does not refute the AQN interpretation of the events themselves [6]; it establishes only that the *observing frequencies* do not carry $p$‑adic log‑periodic structure.

## 5. Results

All numbers below are those computed with shown arithmetic in Section 4; no new measurements are introduced.

**R1 (radix‑locked angular frequencies, from [10]).** $\omega_2 = 9.064722$, $\omega_3 = 5.719203$, $\omega_5 = 3.903962$, $\omega_7 = 3.228919$; each verified by $\ln(p)\,\omega_p = 6.283185 = 2\pi$. Their ratios equal the corresponding logarithm ratios, e.g. $\omega_2/\omega_3 = \log_2 3 = 1.584962$, $\omega_2/\omega_5 = \log_2 5 = 2.321929$, $\omega_3/\omega_5 = \log_3 5 = 1.464974$. The arithmetic mean $\overline{\omega} = 5.479201$ is reported for completeness only and carries no physical significance (Section 6).

**R2 (angular conversion of the MWA frequencies, from [6]).** For $f \in \{98, 120, 132, 160\}$ MHz: $\Omega_1 = 6.157521\times10^{8}$, $\Omega_2 = 7.539822\times10^{8}$, $\Omega_3 = 8.293804\times10^{8}$, $\Omega_4 = 1.005310\times10^{9}\ \mathrm{rad\,s^{-1}}$, with mean $\overline{\Omega} = 8.011061\times10^{8} \approx 8.01\times10^{8}\ \mathrm{rad\,s^{-1}}$.

**R3 (radix‑locking tests on the MWA set).** Consecutive log‑spacings $\Delta_1 = 0.202525$, $\Delta_2 = 0.095310$, $\Delta_3 = 0.192372$; none is close to any $\ln(p)$, the smallest absolute deviation being $|\Delta_2 - \ln 2| = 0.597837$. Pairwise‑ratio residuals give maxima $\max \delta_{ij}(2) = 0.42973$, $\max \delta_{ij}(3) = 0.44621$, $\max \delta_{ij}(5) = 0.30460$, $\max \delta_{ij}(7) = 0.25191$, all exceeding the declared tolerance $\epsilon = 0.15$ (smallest excess factor $0.25191/0.15 \approx 1.68$). The MWA frequency set is therefore Archim