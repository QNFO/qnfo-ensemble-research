# Frequencies of Events in the Actual World: A Bounded Framework for Radix-Locked Event-Count Analysis

## Abstract

We address the question posed by the re-entry record 10.5281/zenodo.17204355: what frequencies of events are observed in this, the actual world, and how should a computational framework be constructed so that claims about those frequencies remain honest under sparse, heterogeneous evidence? We assemble a cross-domain framework that treats "event" generically — linguistic causal events, social-media events during real-world incidents, acoustic events, simulated world events, and physical annihilation or radio-impulsive events — and we impose a single statistical discipline on all of them: event counts are modeled as Poisson-distributed realizations, and any claimed structure in the frequencies (for example, radix-locked log-periodic modulation of the kind searched for in the cosmic microwave background bispectrum, where published upper bounds give $\epsilon_p < 2.5$ at 95% confidence with no detection) must be accompanied by an explicit sample-size requirement. We derive the angular frequencies $\omega_p = 2\pi/\ln(p)$ for $p \in \{2,3,5,7\}$, show that their ratios are exactly logarithm ratios such as $\omega_2/\omega_3 = \log_2 3 \approx 1.58496$, compute Poisson tail probabilities for a reference event rate, derive the sample-size scaling $N \gtrsim 1/\epsilon^2$ for resolving a fractional modulation of amplitude $\epsilon$, and test the four recorded quiet-Sun radio-impulsive frequencies (98, 120, 132, 160 MHz) for radix-locking, finding none. The framework's significance is methodological: it converts an open metaphysical question about event frequencies into a set of falsifiable, arithmetically explicit tests.

## 1. Introduction

The re-entry record 10.5281/zenodo.17204355 asks, in compressed form: *frequencies of events observed in this, actual world?* The question is deliberately ambiguous. It can be read metaphysically — is there a lawful distribution of event frequencies in the actual world, as opposed to merely possible worlds? — or empirically: given the events we actually observe, across instruments and domains, what frequencies do they exhibit, and what structure, if any, do those frequencies carry?

This paper takes the empirical reading seriously while refusing to overclaim on the metaphysical reading. Our strategy is to define a minimal formal object — an event-count process with a rate parameter $\lambda$ — and to ask three questions of any concrete event stream: (i) what is the observed rate and its uncertainty; (ii) is the stream consistent with a memoryless Poisson process, or does it show periodic or log-periodic structure; (iii) if structure is claimed, what sample size would be required to establish it at a stated confidence?

The motivation for imposing this discipline comes from two directions. First, the literature on algorithmic and statistical structure in physical data has proposed exactly this kind of test: a statistical comparison of frequency distributions from physical sources against repositories of information, using Levin's universal distribution, to find evidence for or against the claim that the world is algorithmic in nature [5]. Second, the QNFO corpus has developed concrete instantiations of radix-locked frequency searches, most notably a search for $p$-adic log-periodic signatures in the cosmic microwave background (CMB) bispectrum, which reported upper bounds $\epsilon_p < 2.5$ at 95% confidence and no detection [10]. A framework for "frequencies of events in the actual world" must be able to absorb both positive structural claims and null results without embarrassment.

The paper's contributions are:

1. A unified event-frequency formalism (Section 3) applicable to linguistic, social, acoustic, simulated, and physical event streams, drawing on the heterogeneous event literatures surveyed in Section 2.
2. Explicit arithmetic for the radix-locked angular frequencies $\omega_p = 2\pi/\ln(p)$, their mutual ratios, Poisson probabilities for a reference rate, and the sample-size requirement $N \gtrsim 1/\epsilon^2$ (Section 4).
3. A worked radix-locking test on the four quiet-Solar radio-impulsive frequencies recorded by the Murchison Widefield Array at 98, 120, 132, and 160 MHz [6], showing that their logarithmic spacings do not coincide with $\ln(p)$ for any single small prime, i.e., the channel set is not radix-locked (Section 4).
4. A discussion of failure modes, falsification conditions, and the limits of what event-frequency analysis can say about the "actual world" as such (Section 6).

Throughout, we distinguish sharply between numbers we compute here with shown arithmetic, numbers taken from the supplied literature entries, and projections that carry stated assumptions.

## 2. Background and Related Work

The relevant literature is scattered across natural language processing, social computing, audio machine learning, embodied agents, fundamental physics, and the QNFO corpus. We survey it in the bibliography's order.

**Event causality in language.** The work on inference of fine-grained event causality from blogs and films [1] starts from the observation that human understanding of narrative is mainly driven by reasoning about causal relations between events, so that recognizing such relations is a key capability for computational models of language understanding; it notes that computational work has approached this via two routes — acquiring a knowledge base of common causal relations between events, or attempting to understand a particular narrative's causal structure. For our purposes, this fixes the linguistic end of the event spectrum: an "event" in text is a causally connected node, and the frequency of such events in a corpus is a measurable quantity. The supplied summary of [1] does not report specific frequency statistics, so we use it only to motivate the event ontology, not as a source of numbers.

**Social-media events during real-world incidents.** The study of Facebook content during real-world events [2] observes that multiple prior studies analyzed the role and dynamics of the Twitter social network during real-world events, but little work had explored the content of other social media services or compared content across two networks during real-world events, and argues that platforms like Facebook also play a vital role in disseminating information during real-world events. This supplies the social end of the spectrum: bursts of platform content are observable proxies for real-world event occurrence, and their temporal density is an event-frequency signal. Again, the supplied summary states no quantitative rates; we cite it for the measurement setting.

**Acoustic event detection and its error structure.** Sound event localization and detection (SELD) unifies sound event detection with direction-of-arrival estimation, and thereby inherits the challenges of both tasks — noise, reverberation, interference, polyphony, and non-stationarity of sound sources — plus the additional challenge of assigning correct correspondence between detection and localization outputs [3]. This is directly relevant to our framework's error model: polyphony and non-stationarity are precisely the conditions under which naive Poisson rate estimates for acoustic events fail, and the correspondence-assignment problem is an event-identity ambiguity that our counting formalism must acknowledge as a systematic uncertainty.

**Closed-loop evaluation of world models.** The World-in-World benchmark [4] addresses generative world models, which can now simulate worlds with striking visual realism, and asks whether they endow embodied agents with predictive perception for decision making; it argues that progress has been limited by fragmented evaluation, since most existing benchmarks adopt open-loop protocols emphasizing visual quality in isolation, leaving the core issue unresolved. For us, simulated worlds are a controlled laboratory for event-frequency questions: in a closed-loop simulated world, event rates are exactly known by construction, providing the calibration limit that real-world streams never reach. The supplied summary of [4] does not report event-rate statistics, so we use it only to establish the closed-loop/open-loop distinction.

**Algorithmicity of the world.** The proposal in [5] is the closest methodological ancestor of this paper: a test based on algorithmic complexity theory and an experimental evaluation of Levin's universal distribution, designed to identify evidence in support of or in contravention of the claim that the world is algorithmic in nature, implemented as a statistical comparison of the frequency distributions of data from physical sources on the one hand and repositories of information on the other. Our radix-locking tests are a narrower, parametric cousin of this program: where [5] compares whole frequency distributions against a universal prior, we test for a specific, one-parameter family of log-periodic structures.

**Physical event candidates: AQN radio impulses.** The Murchison Widefield Array (MWA) recorded impulsive radio events in the quiet solar corona at frequencies 98, 120, 132, and 160 MHz, and it has been proposed that these radio events are the direct manifestation of dark matter annihilation events within the axion quark nugget (AQN) framework, building on arguments that AQN annihilation events produce such signatures [6]. This is the only entry in our bibliography that supplies concrete observed event frequencies in a physical channel, and we therefore use it as our worked example in Section 4. Note carefully what the entry supports: the four frequency values, the instrument, the quiet-corona setting, and the AQN interpretation as a proposal. It does not supply event counts or rates, so our test concerns the frequency *values* (as a candidate radix-locked set), not the temporal statistics of the impulses.

**Brane-world gravity as a modeling frame.** The Hamiltonian (canonical) treatment of brane-world gravity applies the Arnowitt–Deser–Misner decomposition to a 4-dimensional brane embedded in a 5-dimensional bulk, yielding a 3+1+1 break-up, and presents a canonical theory of brane cosmology whose Hamiltonian equations allow the study of physical phenomena in brane gravity [7]. We cite this as an example of a framework in which "events" in the actual world would be embedded in a higher-dimensional ontology; the supplied summary states no event-frequency content, and we draw no numbers from it.

**Frequency separation under real-world degradation.** The super-resolution literature [8] observes that most recent image super-resolution methods assume paired low-resolution and high-resolution training data or knowledge of the downgrading operator (usually bicubic downscaling), and that while such methods perform well on standard benchmarks they often fail to produce convincing results in real-world settings — the gap being attributed (in the supplied summary) to this mismatch. The analogy to our problem is exact: methods calibrated on idealized event streams (closed-loop, paired, stationary) fail on actual-world streams whose degradation operator is unknown. We adopt "frequency separation" as a design principle: separate the physical carrier frequency of an event stream from the modulation structure before testing for radix-locking.

**QNFO corpus results.** The QNFO MASS-FREQUENCY entry [9] carries no supplied summary text; we therefore note only its title-level role as a corpus node connecting mass and frequency, and state explicitly that no further detail is available from the supplied material. The $p$-adic CMB bispectrum search [10] supplies the quantitative anchor of the corpus: radix-locked oscillations with angular frequency $\omega_p = 2\pi/\ln(p)$ for $p \in \{2,3,5,7\}$, with Planck 2018 upper bounds $\epsilon_p < 2.5$ at 95% confidence, no detection, and (per the truncated summary) a statement about what the bound implies within a single-modulation model. The two Zitterbewegung entries differ: [11] ("Nature of Zitterbewegung") has no supplied summary, while [12] ("Zitterbewegung: From Archimedean Puzzle to Adelic Observable") supplies substantive content — the structural underdetermination of the position operator in relativistic quantum mechanics arises from a single representation-theoretic origin, the Silent Parameter Principle; SU(2) and $\mathbb{Z}_2^x$ share identical fusion rules at matching levels; and the 2-adic Zitterbewegung frequency deviates from the Archimedean value (the summary truncates at this point). Entry [12] is relevant because it is a concrete case where an Archimedean frequency and a $p$-adic frequency diverge — exactly the discrimination our framework is designed to test in event streams.

In summary: the literature supplies (a) event ontologies from language and social media [1,2], (b) error models for event detection [3], (c) a closed-loop calibration limit [4], (d) a distribution-comparison methodology [5], (e) one concrete physical frequency set [6], a higher-dimensional embedding frame [7], a real-world degradation caution [8], and (f) the radix-locked parametric family with published bounds [10,12]. Entries [9] and [11] are title-only in the supplied material.

## 3. Methods

### 3.1 Event-count process

Let $N_t$ denote the number of events of a specified type observed in window $t$. We model $N_t$ as Poisson with rate $\lambda_t$:

$$
P(N_t = k) = \frac{(\lambda_t T)^k e^{-\lambda_t T}}{k!},
$$

where $T$ is the window duration. The homogeneous null hypothesis is $\lambda_t = \lambda_0$ for all $t$. The structural alternative we consider is a log-periodic modulation of the rate,

$$
\lambda_t = \lambda_0 \left[1 + \epsilon_p \cos\left(\omega_p \ln \frac{t}{t_0}\right)\right],
$$

with $\omega_p = 2\pi/\ln(p)$ and $|\epsilon_p| < 1$ required for positivity of the rate. This is the single-modulation form consistent with the parametric family searched in the CMB bispectrum analysis [10], transplanted from angular bispectrum amplitude to event rate.

### 3.2 Radix-locking test for a frequency set

Given a set of observed carrier frequencies $\{f_i\}$ (e.g., the MWA channels), the radix-locking hypothesis for prime $p$ asserts that consecutive log-spacings equal $\ln(p)$:

$$
\Delta_i = \ln\frac{f_{i+1}}{f_i} \stackrel{?}{=} \ln(p).
$$

We compute each $\Delta_i$ and compare against $\ln(2), \ln(3), \ln(5), \ln(7)$. A set is radix-locked to $p$ only if all consecutive spacings match $\ln(p)$ to within the relevant tolerance. This is a deliberately conservative test: it asks whether the *frequency values themselves* carry the radix structure, independent of any temporal modulation.

### 3.3 Sample-size requirement

To resolve a fractional modulation of amplitude $\epsilon$ in a mean event count, the statistical precision of the estimated mean over $N$ events scales as $1/\sqrt{N}$ (standard error of a Poisson mean). Requiring the precision to be at least as fine as the modulation gives

$$
\frac{1}{\sqrt{N}} \lesssim \epsilon \quad \Longrightarrow \quad N \gtrsim \frac{1}{\epsilon^2}.
$$

This is the design rule we apply to all domains: linguistic, social, acoustic, and physical.

### 3.4 Domain mapping

Each domain contributes an event stream under this formalism: causal-event mentions in narrative text [1]; platform-content bursts during real-world incidents [2]; polyphonic acoustic detections with correspondence ambiguity [3]; exactly-known event counts in closed-loop simulated worlds [4]; physical-source frequency distributions compared against universal expectations [5]; radio impulses in the quiet corona [6]; and, as a theoretical caution, the case where the 2-adic Zitterbewegung frequency deviates from the Archimedean value [12], reminding us that the "same" observable can carry different frequency content depending on the number-theoretic lens applied.

## 4. Analysis

All arithmetic below is shown step by step. Inputs are labeled with their sources.

### 4.1 Radix-locked angular frequencies

**Input:** $\omega_p = 2\pi/\ln(p)$, $p \in \{2,3,5,7\}$, from the QNFO CMB bispectrum search [10]. Constants: $2\pi = 6.283185$; $\ln 2 = 0.693147$; $\ln 3 = 1.098612$; $\ln 5 = 1.609438$; $\ln 7 = 1.945910$.

$$
\omega_2 = \frac{6.283185}{0.693147} = 9.064720 \ \text{rad},
$$

(check: $0.693147 \times 9.064720 = 6.283185$.)

$$
\omega_3 = \frac{6.283185}{1.098612} = 5.719202 \ \text{rad},
$$

(check: $1.098612 \times 5.719202 = 6.283185$.)

$$
\omega_5 = \frac{6.283185}{1.609438} = 3.903962 \ \text{rad},
$$

(check: $1.609438 \times 3.903962 = 6.283185$.)

$$
\omega_7 = \frac{6.283185}{1.945910} = 3.228909 \ \text{rad},
$$

(check: $1.945910 \times 3.228909 = 6.283185$.)

**Ratios.** Because $\omega_p = 2\pi/\ln(p)$, ratios of $\omega$'s are inverse log ratios:

$$
\frac{\omega_2}{\omega_3} = \frac{\ln 3}{\ln 2} = \frac{1.098612}{0.693147} = 1.584963 = \log_2 3,
$$

$$
\frac{\omega_2}{\omega_5} = \frac{1.609438}{0.693147} = 2.321928 = \log_2 5,
$$

$$
\frac{\omega_3}{\omega_5} = \frac{1.609438}{1.098612} = 1.465025 = \log_3 5.
$$

Each check: $0.693147 \times 1.584963 = 1.098612$; $0.693147 \times 2.321928 = 1.609438$; $1.098612 \times 1.465025 = 1.609438$. These irrational, logarithm-ratio values are the signature of radix-locking: a radix-locked spectrum is *not* harmonically spaced, since $\omega_2/\omega_3 = \log_2 3 \approx 1.584963$ is not a ratio of small integers.

### 4.2 Poisson reference probabilities

**Input (stated assumption of this paper, not from any cited work):** a reference event rate $\lambda_0 = 4 \ \text{yr}^{-1}$, window $T = 1 \ \text{yr}$, so the mean count is $\lambda_0 T = 4$.

$$
P(N = 0) = e^{-4} = 0.018316,
$$

$$
P(N = 1) = 4 e^{-4} = 4 \times 0.018316 = 0.073263,
$$

$$
P(N \leq 1) = 0.018316 + 0.073263 = 0.091579.
$$

Thus, at four events per year, a year with zero or one observed events has probability $\approx 0.0916$ under the homogeneous null — about one year in eleven. This calibrates how rare a "quiet year" must be before it is surprising.

### 4.3 Sample-size requirement

**Formula:** $N \gtrsim 1/\epsilon^2$ (Section 3.3). Computed values:

- $\epsilon = 0.1$: $N = 1/(0.1)^2 = 1/0.01 = 100$ events.
- $\epsilon = 0.05$: $N = 1/(0.05)^2 = 1/0.0025 = 400$ events.
- $\epsilon = 0.01$: $N = 1/(0.01)^2 = 1/0.0001 = 10{,}000$ events.

**Connection to the published bound [10]:** the Planck 2018 analysis gives $\epsilon_p < 2.5$ at 95% confidence with no detection. Note that this bound exceeds the positivity limit $|\epsilon_p| < 1$ required by our rate-modulation form of Section 3.1; within the single-modulation model referenced (in truncated form) in [10], the bound therefore does not constrain a rate-level modulation of the kind we model here to below unity amplitude — it is a bound on a bispectrum amplitude parameter, not directly on an event-rate modulation. We flag this as a domain-translation caveat rather than silently equating the two $\epsilon$'s. For a *hypothetical* rate modulation at the detection threshold $\epsilon = 0.05$, the requirement is $N = 400$ events per modulation period, which we report as a projection conditional on the stated Poisson model.

### 4.4 Radix-locking test on the MWA frequency set

**Input:** the four recorded quiet-corona radio-impulsive frequencies 98, 120, 132, 160 MHz [6]. Natural logarithms: $\ln 98 = 4.584967$; $\ln 120 = 4.787492$; $\ln 132 = 4.882802$; $\ln 160 = 5.075174$.

Consecutive log-spacings:

$$
\Delta_1 = \ln\frac{120}{98} = 4.787492 - 4.584967 = 0.202525,
$$

$$
\Delta_2 = \ln\frac{132}{120} = 4.882802 - 4.787492 = 0.095310,
$$

$$
\Delta_3 = \ln\frac{160}{132} = 5.075174 - 4.882802 = 0.192372.
$$

Comparison against $\ln(p)$: $\ln 2 = 0.693147$, $\ln 3 = 1.098612$, $\ln 5 = 1.609438$, $\ln 7 = 1.945910$. None of $\Delta_1, \Delta_2, \Delta_3$ is close to any $\ln(p)$; the smallest absolute deviation is $|\Delta_2 - \ln 2| = |0.095310 - 0.693147| = 0.597837$, and no spacing comes within a factor of $3$ of any $\ln(p)$. Equivalently, the frequency ratios themselves are not radix-locked: $120/98 = 1.224490$, $132/120 = 1.100000$, $160/132 = 1.212121$, whereas radix-locking to $p$ would require each ratio to equal $p$ (or $p^{1/m}$ for integer $m$; even allowing $m = 6$, $2^{1/6} = 1.122462$, which matches none of the three ratios to better than $0.09$ in absolute value: $|1.224490 - 1.122462| = 0.102028$, $|1.100000 - 1.122462| = 0.022462$, $|1.212121 - 1.122462| = 0.089659$).

**Conclusion of the test:** the MWA channel set $\{98, 120, 132, 160\}$ MHz is not radix-locked to any single small prime. This is a statement about the *instrumental channel selection*, not evidence against the AQN interpretation of the impulses [6]; the AQN proposal concerns the occurrence of the events, not the carrier frequencies of the observing channels. The test's value is methodological: it demonstrates the full arithmetic pipeline that any candidate radix-locked event-frequency set must pass.

### 4.5 Cross-domain rate comparison (illustrative, stated assumptions)

To make the framework concrete across domains, we tabulate illustrative rates under explicitly stated assumptions. These are *projections for design purposes*, not measurements: linguistic causal-event density in narrative text [1], social-media burst rates during real-world events [2], and acoustic polyphonic event rates [3] are all domains where the supplied literature entries state no numbers; we therefore assume, solely for illustration, a common design target of $\lambda_0 = 4 \ \text{yr}^{-1}$ per stream and apply the Section 4.2–4.3 arithmetic uniformly. The only domain where the closed-loop limit applies is simulation [4], where event counts are exactly known by construction and the Poisson standard error $1/\sqrt{N}$ is the *only* uncertainty.

## 5. Results

We report only numbers computed in Section 4 or explicitly labeled projections.

**R1 (computed).** The radix-locked angular frequencies are $\omega_2 = 9.064720$, $\omega_3 = 5.719202$, $\omega_5 = 3.903962$, $\omega_7 = 3.228909$ (dimensionless radians per log-unit of the argument). Their ratios are exact logarithm ratios: $\omega_2/\omega_3 = \log_2 3 = 1.584963$, $\omega_2/\omega_5 = \log_2 5 = 2.321928$, $\omega_3/\omega_5 = \log_3 5 = 1.465025$.

**R2 (computed).** For a reference Poisson stream with $\lambda_0 = 4 \ \text{yr}^{-1}$: $P(N=0) = 0.018316$, $P(N=1) = 0.073263$, $P(N \leq 1) = 0.091579$ per year.

**R3 (computed).** Sample-size requirements for resolving a fractional rate modulation: $N = 100$ events at $\epsilon = 0.1$; $N = 400$ at $\epsilon = 0.05$; $N = 10{,}000$ at $\epsilon = 0.01$.

**R4 (computed).** The MWA quiet-corona frequency set $\{98, 120, 132, 160\}$ MHz has consecutive log-spacings $\Delta_1 = 0.202525$, $\Delta_2 = 0.095310$, $\Delta_3 = 0.192372$, none of which matches any of $\ln 2, \ln 3, \ln 5, \ln 7$; the set is not radix-locked to any single small prime.

**R5 (from the literature, not computed here).** The CMB bispectrum search reports upper bounds $\epsilon_p < 2.5$ at 95% confidence, with no detection, for the radix-locked family [10]. This number is quoted from the supplied entry, not derived in this paper.

**R6 (projection, stated assumptions).** If a real event stream (linguistic, social, or acoustic) were hypothesized to carry a rate-level log-periodic modulation with $\epsilon = 0.05$ at $\omega_2$, detection would require $