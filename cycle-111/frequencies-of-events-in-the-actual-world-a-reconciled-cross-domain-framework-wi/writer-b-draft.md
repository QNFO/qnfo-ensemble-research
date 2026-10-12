# Event Frequencies in the Actual World: A Cross-Domain Framework for Observing, Counting, and Interpreting Real-World Events

## Abstract

Events — discrete, datable happenings — are counted in nearly every empirical discipline, yet the practice of measuring *event frequencies* is fragmented across fields that rarely compare methods. This paper proposes a cross-domain framework for event-frequency observation in the actual world, organized around three questions: what counts as an event, what sampling process generates the observed counts, and what the frequency of an event class tells us about the generating process. We formalize event observation as a point process with a detector function, distinguish Archimedean (log-spaced) from radix-locked (p-adic) frequency parameterizations, and derive detection thresholds for rare-event searches. As worked examples we compute radix-locked angular frequencies $\omega_p = 2\pi/\ln p$ for $p \in \{2,3,5,7\}$, yielding values from $\omega_2 \approx 9.06$ to $\omega_7 \approx 3.23$ rad; we analyze the frequency set $\{98, 120, 132, 160\}$ MHz of impulsive radio events recorded in the quiet solar corona by the Murchison Widefield Array, computing pairwise ratios and showing they are inconsistent with a single radix-locked ladder; and we derive Poisson zero-event probabilities that quantify how non-detection constrains event rates. We connect the framework to event causality inference in text, social-media event characterization, sound event localization, closed-loop world models, algorithmic-complexity tests of physical data, and super-resolution of real-world imagery. The framework's contribution is methodological: a shared vocabulary and explicit arithmetic for comparing event-frequency claims across otherwise disconnected literatures.

## 1. Introduction

The phrase "frequencies of events observed in this, actual world" names a deceptively simple object of study. Every empirical science counts events: radio astronomers count impulsive bursts, social-media researchers count posts during crises, computational linguists count causal event pairs in text, and physicists count annihilation candidates attributed to dark matter. But the *frequency* of an event is not a property of the world alone; it is a property of the joint system (world, detector, sampling protocol, and counting convention). A burst at 132 MHz exists only as an "event" relative to an instrument with a specific band, sensitivity, and trigger logic; a "real world event" in social media exists only relative to a keyword lexicon and a platform's data access.

This paper treats event-frequency observation as a unified methodological problem. Our motivating re-entry point is a prior record (10.5281/zenodo.17204355) posing the question of event frequencies in the actual world; here we develop that question into a framework with three components:

1. **Event individuation.** What rule carves a continuous flux into countable units? We model this with a detector function and show that different individuation rules (threshold crossing, template match, human annotation) yield different counts from the same underlying signal.
2. **Frequency parameterization.** Frequencies can be laid out on an Archimedean (linear or log-linear) axis or on a radix-locked, p-adic ladder. We compute the radix-locked angular frequencies $\omega_p = 2\pi/\ln p$ and give a concrete test — pairwise ratio consistency — for whether an observed frequency set supports a radix-locked structure.
3. **Rare-event inference.** When few or zero events are observed, what follows? We derive Poisson-based zero-event probabilities and upper-limit logic, and apply them to a worked example.

Our running physical example is the set of impulsive radio events in the quiet solar corona recorded by the Murchison Widefield Array (MWA) at frequencies 98, 120, 132, and 160 MHz, which one line of interpretation attributes to dark-matter annihilation events in the axion quark nugget (AQN) framework [6]. We do not adjudicate that physical interpretation; we use the frequency set as a well-specified case study in how event frequencies are reported, compared, and constrained.

The paper is organized as follows. Section 2 reviews related work across eight literatures. Section 3 formalizes the framework. Section 4 carries out all derivations with explicit arithmetic. Section 5 reports results. Section 6 discusses limitations and falsification conditions, and Section 7 concludes.

## 2. Background and Related Work

We draw on eight literatures, each contributing one facet of the event-frequency problem.

**Event causality in text.** The inference of fine-grained event causality from blogs and films is motivated by the observation that human understanding of narrative is mainly driven by reasoning about causal relations between events, making their recognition a key capability for computational language understanding; work in this area proceeds either by acquiring a knowledge base of common causal relations between events or by understanding a particular narrative's causal structure [1]. For our framework, this literature supplies the *semantic* individuation rule: an "event" in text is individuated by causal role, not by physical timestamp. Event frequencies computed over such corpora therefore count causal units, and comparing them with physically timestamped event counts requires an explicit mapping.

**Social media during real-world events.** Prior studies analyzed the role and dynamics of Twitter during real-world events, but comparatively little work has explored other social media services or compared content across two networks during the same events; the characterization of Facebook content during real-world events argues that platforms like Facebook also play a vital role in disseminating information during such events [2]. This literature contributes the *multi-detector* perspective: the same real-world event is observed by multiple platforms with different populations and affordances, so per-platform event frequencies are detector-dependent and must not be conflated with a world-side rate.

**Sound event localization and detection.** Sound event localization and detection (SELD) unifies sound event detection with direction-of-arrival estimation, and thereby inherits the challenges of both tasks — noise, reverberation, interference, polyphony, and non-stationarity of sound sources — plus the additional challenge of assigning correct correspondence between detections and sources; error analysis is used to identify what makes the task difficult [3]. SELD exemplifies the individuation problem in the acoustic domain: polyphony means that the count of detected events depends on how overlapping sources are segmented, so the observed event frequency is a joint property of scene and detector.

**Closed-loop evaluation of world models.** Generative world models can now simulate worlds with striking visual realism, raising the question of whether they endow embodied agents with predictive perception for decision making; progress has been limited by fragmented evaluation, since most benchmarks adopt open-loop protocols emphasizing visual quality in isolation, and the World-in-World benchmark addresses this by evaluating world models in a closed-loop world [4]. For event frequencies, closed-loop evaluation matters because an agent's *actions* change which events it subsequently observes: the effective event frequency experienced by an embodied agent is action-conditioned, a complication absent from passive counting.

**Algorithmic tests of physical data.** A test based on algorithmic complexity and an experimental evaluation of Levin's universal distribution was proposed to identify evidence for or against the claim that the world is algorithmic in nature, implemented as a statistical comparison of frequency distributions of data from physical sources on the one hand and repositories of information on the other [5]. This is the closest methodological antecedent to our question: it treats the *frequency distribution of observed data* as a diagnostic of the world's underlying structure. Our radix-locked versus Archimedean distinction (Section 3.2) plays an analogous role at the level of event frequencies rather than symbol frequencies.

**Radio impulsive events and dark matter.** The Murchison Widefield Array recorded impulsive radio events in the quiet solar corona at frequencies 98, 120, 132, and 160 MHz, and it has been proposed that these events are the direct manifestation of dark matter annihilation events within the axion quark nugget (AQN) framework, building on prior arguments about AQN annihilation events [6]. This is our primary worked example: a concrete, published event-frequency claim in which a small set of discrete observing frequencies carries the interpretive weight.

**Brane-world gravity.** In brane-world cosmology a 4-dimensional brane is embedded in a 5-dimensional bulk; applying the Arnowitt-Deser-Misner decomposition yields a 3+1+1 break-up, and the resulting canonical (Hamiltonian) theory of brane cosmology allows the study of physical phenomena in brane gravity [7]. We cite this as a structural analogy: just as the Hamiltonian formulation separates bulk from brane dynamics, our framework separates the world-side event-generating process (the "bulk") from the detector-side observation process (the "brane"), and insists that frequency claims specify which layer they refer to. The entry supplied gives no further detail on specific results, so we use it only at this structural level.

**Real-world super-resolution.** Most image super-resolution literature assumes paired low-resolution/high-resolution training data or a known degradation operator (usually bicubic downscaling); such methods perform well on benchmarks but often fail in real-world settings, and a frequency-separation approach has been proposed for the real-world case [8]. The analogy is direct: methods tuned to a synthetic observation model fail on real data, and the fix involves separating frequency bands. Our framework makes the same move for event counting — separating the world-side event process from the detector-side degradation before inferring rates.

**P-adic log-periodic searches.** A search for p-adic (ultrametric) log-periodic signatures in the cosmic microwave background bispectrum considered radix-locked oscillations with angular frequency $\omega_p = 2\pi/\ln p$ for $p \in \{2,3,5,7\}$, reporting upper bounds $\epsilon_p < 2.5$ at 95% confidence with no detection, within a single-modulation model [10]. This supplies our radix-locked frequency definition and an example of a rigorous non-detection bound. Two QNFO entries on mass-frequency context and on zitterbewegung as an adelic observable [9], [11], [12] motivate the p-adic program generally; the supplied summaries for [9] and [11] are empty, so we cite them only as context markers without attributing any specific claim, while [12] connects the Archimedean and 2-adic descriptions of the zitterbewegung frequency via a representation-theoretic underdetermination (the Silent Parameter Principle, with SU(2) and $\mathbb{Z}_2^x$ sharing identical fusion rules at matching levels), illustrating that the same observable can admit Archimedean and p-adic parameterizations — exactly the duality our event-frequency framework formalizes.

## 3. Methods

### 3.1 Events as a detected point process

Let the world generate an event process with unobserved rate $\lambda_w$ (events per unit time in some class $c$). A detector $D$ with sensitivity window $W_D$ and threshold $\theta_D$ produces detections. We model the detected count in observation time $T_{\text{obs}}$ as a Poisson random variable:

$$N_D \sim \text{Poisson}(\lambda_D T_{\text{obs}}), \qquad \lambda_D = \eta_D(\theta_D, W_D)\,\lambda_w,$$

where $\eta_D \in [0,1]$ is the detector efficiency. The central methodological rule of this paper is that any reported event frequency is $\lambda_D$, not $\lambda_w$, unless $\eta_D$ is known and corrected for. The probability of observing zero events despite a nonzero rate is

$$P(N_D = 0) = e^{-\lambda_D T_{\text{obs}}}.$$

This gives the standard rare-event logic: if zero events are seen in time $T_{\text{obs}}$ at confidence level $1-\alpha$, then any rate $\lambda_D$ with $e^{-\lambda_D T_{\text{obs}}} > \alpha$ is not excluded, so the 95% upper limit (per unit time) satisfies

$$\lambda_D^{\text{UL}} = \frac{-\ln 0.05}{T_{\text{obs}}} = \frac{2.996}{T_{\text{obs}}}.$$

### 3.2 Archimedean versus radix-locked frequency parameterizations

Let an observed set of characteristic frequencies be $F = \{f_1, \dots, f_k\}$. Two structural hypotheses are:

- **Archimedean:** the $f_i$ are independently placed (e.g., instrumental band centers), with no constraint on ratios $r_{ij} = f_j / f_i$.
- **Radix-locked (p-adic):** structure appears in log-space at angular frequencies $\omega_p = 2\pi/\ln p$, so that a log-periodic modulation of period $\ln p$ in some underlying variable produces ratios that are powers of $p$ (or of a fixed base). The p-adic program tests exactly this structure in cosmological data [10].

A minimal consistency test for a radix-locked ladder with base $p$ is that all pairwise ratios $r_{ij}$ be near integer powers of $p$: define the residual

$$\delta_{ij}(p) = \left| \log_p r_{ij} - \operatorname{round}\!\left(\log_p r_{ij}\right) \right|,$$

and declare the set consistent with base $p$ if $\max_{i,j} \delta_{ij}(p) < \epsilon$ for a pre-declared tolerance $\epsilon$. We use $\epsilon = 0.15$ (roughly a half-width of one bin if frequencies are quoted to two significant figures, since $120$ MHz quoted as such has a relative precision of order $10^{-2}$, and $\ln(1.05) \approx 0.049$; we take a conservative $\epsilon$ and state it as a convention, not a derived constant).

### 3.3 Multi-detector event counting

Following the multi-platform lesson of social-media event research [2] and the polyphony lesson of SELD [3], we define the observed frequency of event class $c$ on detector $d$ as

$$\hat{\lambda}_{c,d} = \frac{N_{c,d}}{T_{\text{obs},d}},$$

and require that cross-detector comparison be made through the efficiency-corrected quantity $\hat{\lambda}_{c,d}/\hat{\eta}_{c,d}$, with $\hat{\eta}_{c,d}$ estimated from a shared calibration subset. Where no calibration subset exists, cross-detector comparisons are reported as detector-conditional and not aggregated.

### 3.4 Action-conditioned observation

In closed-loop settings [4], the observation time itself depends on agent behavior. We model this by making $T_{\text{obs}}$ a stopping time $\tau_A$ determined by policy $A$, so the experienced event rate is $\lambda_D^{(A)} = E[N_D]/E[\tau_A]$. Passive benchmarks (open-loop) cannot estimate this quantity; only closed-loop protocols can.

## 4. Analysis

All inputs below are stated with their sources; all arithmetic is shown step by step.

**Input 1 (from [10]):** the radix-locked angular frequencies are $\omega_p = 2\pi/\ln p$ for $p \in \{2,3,5,7\}$.

Compute each (using $\pi \approx 3.14159265$, $\ln 2 \approx 0.693147$, $\ln 3 \approx 1.098612$, $\ln 5 \approx 1.609438$, $\ln 7 \approx 1.945910$):

$$\omega_2 = \frac{2\pi}{\ln 2} = \frac{6.283185307}{0.693147} \approx 9.064720 \ \text{rad}.$$

$$\omega_3 = \frac{6.283185307}{1.098612} \approx 5.719100 \ \text{rad}.$$

$$\omega_5 = \frac{6.283185307}{1.609438} \approx 3.903440 \ \text{rad}.$$

$$\omega_7 = \frac{6.283185307}{1.945910} \approx 3.229440 \ \text{rad}.$$

Check: $\omega_2/\omega_3 = 9.064720/5.719100 \approx 1.585$, and indeed $\ln 3/\ln 2 = 1.098612/0.693147 \approx 1.58496$, whose reciprocal is $0.693147/1.098612 \approx 0.63093$; consistency holds since $\omega_2/\omega_3 = \ln 3/\ln 2$ by construction.

**Input 2 (from [6]):** the MWA impulsive-event frequencies $f \in \{98, 120, 132, 160\}$ MHz.

Compute all pairwise ratios $r_{ij} = f_j/f_i$ with $f_j > f_i$:

- $r_{1} = 120/98 \approx 1.224490$
- $r_{2} = 132/98 \approx 1.346939$
- $r_{3} = 160/98 \approx 1.632653$
- $r_{4} = 132/120 = 1.100000$
- $r_{5} = 160/120 \approx 1.333333$
- $r_{6} = 160/132 \approx 1.212121$

Test base $p=2$: $\log_2 r$ for each ratio. Since $\log_2 r = \ln r / \ln 2$:

- $\ln(1.224490) \approx 0.202441$; $\log_2 = 0.202441/0.693147 \approx 0.29206$; distance to nearest integer: $|0.29206 - 0| = 0.29206$.
- $\ln(1.346939) \approx 0.297877$; $\log_2 \approx 0.42960$; distance $0.42960$.
- $\ln(1.632653) \approx 0.490261$; $\log_2 \approx 0.70733$; distance to nearest integer ($1$): $|0.70733 - 1| = 0.29267$.
- $\ln(1.100000) \approx 0.095310$; $\log_2 \approx 0.13751$; distance $0.13751$.
- $\ln(1.333333) \approx 0.287682$; $\log_2 \approx 0.41504$; distance $0.41504$.
- $\ln(1.212121) \approx 0.192372$; $\log_2 \approx 0.27756$; distance $0.27756$.

Maximum residual: $\max \delta_{ij}(2) \approx 0.42960 > \epsilon = 0.15$.

Test base $p=3$: $\log_3 r = \ln r / 1.098612$:

- $0.202441/1.098612 \approx 0.18426$; distance $0.18426$.
- $0.297877/1.098612 \approx 0.27114$; distance $0.27114$.
- $0.490261/1.098612 \approx 0.44625$; distance $0.44625$.
- $0.095310/1.098612 \approx 0.08675$; distance $0.08675$.
- $0.287682/1.098612 \approx 0.26184$; distance $0.26184$.
- $0.192372/1.098612 \approx 0.17508$; distance $0.17508$.

Maximum residual: $\max \delta_{ij}(3) \approx 0.44625 > 0.15$.

Test base $p=5$: $\log_5 r = \ln r / 1.609438$:

- $0.202441/1.609438 \approx 0.12578$; distance $0.12578$.
- $0.297877/1.609438 \approx 0.18508$; distance $0.18508$.
- $0.490261/1.609438 \approx 0.30461$; distance $0.30461$.
- $0.095310/1.609438 \approx 0.05922$; distance $0.05922$.
- $0.287682/1.609438 \approx 0.17875$; distance $0.17875$.
- $0.192372/1.609438 \approx 0.11953$; distance $0.11953$.

Maximum residual: $\max \delta_{ij}(5) \approx 0.30461 > 0.15$.

Test base $p=7$: $\log_7 r = \ln r / 1.945910$:

- $0.202441/1.945910 \approx 0.10404$; distance $0.10404$.
- $0.297877/1.945910 \approx 0.15308$; distance $0.15308$.
- $0.490261/1.945910 \approx 0.25195$; distance $0.25195$.
- $0.095310/1.945910 \approx 0.04898$; distance $0.04898$.
- $0.287682/1.945910 \approx 0.14784$; distance $0.14784$.
- $0.192372/1.945910 \approx 0.09886$; distance $0.09886$.

Maximum residual: $\max \delta_{ij}(7) \approx 0.25195 > 0.15$.

**Conclusion of the ratio test:** no single radix-locked base in $\{2,3,5,7\}$ brings all six pairwise ratios within tolerance $\epsilon = 0.15$ of integer powers. The MWA frequency set is therefore consistent with the Archimedean hypothesis (independent instrumental band placement) and not, on frequency-ratio structure alone, with a radix-locked ladder. This does not refute the AQN interpretation of the events themselves [6]; it only establishes that the *observing frequencies* do not carry p-adic log-periodic structure.

**Input 3 (derived, Poisson zero-event logic from Section 3.1):** zero-event upper limits.

For $T_{\text{obs}} = 1$ year $= 365.25 \times 24 \times 3600 = 31{,}557{,}600$ s:

$$\lambda^{\text{UL}} = \frac{2.996}{31{,}557{,}600} \approx 9.493 \times 10^{-8} \ \text{s}^{-1}.$$

Converting to per year: $2.996$ events per year, i.e., observing zero events in one year excludes (at 95% CL) rates above $\approx 3.0$ yr$^{-1}$.

For a hypothetical detection of $N = 4$ events in $T_{\text{obs}} = 1$ yr, the Poisson 95% upper limit on the mean is the standard one-sided value $\mu^{\text{UL}}_{95} \approx 9.15$ (the classic $N + 1.96\sqrt{N+1}$-type approximation gives $4 + 1.96\sqrt{5} \approx 4 + 1.96 \times 2.23607 \approx 4 + 4.38270 \approx 8.38$; the exact one-sided Poisson limit for $N=4$ is $\mu$ such that $P(N' \le 4 \mid \mu) = 0.05$, which numerically is $\mu \approx 9.154$; we quote the exact value as a standard tabulated quantity and note the Gaussian approximation $8.38$ as a lower bound on it). The corresponding rate limit is $\lambda^{\text{UL}} \approx 9.154$ yr$^{-1}$.

**Input 4 (from [10]):** the reported upper bounds $\epsilon_p < 2.5$ at 95% CL on the single-modulation amplitude, with no detection. We use these only as a demonstration of the reporting convention: a non-detection is reported as a bound on a model parameter, not as a frequency; this is the same logic as our $\lambda^{\text{UL}}$ derivation, applied to an amplitude rather than a rate.

## 5. Results

**R1. Radix-locked angular frequencies.** For $p \in \{2,3,5,7\}$ [10]: $\omega_2 \approx 9.0647$, $\omega_3 \approx 5.7191$, $\omega_5 \approx 3.9034$, $\omega_7 \approx 3.2294$ (rad). These are exact evaluations of the stated formula, with arithmetic shown in Section 4.

**R2. MWA frequency-set structure.** For the MWA set $\{98, 120, 132, 160\}$ MHz [6], the maximum ratio residuals are $\max \delta_{ij}(2) \approx 0.430$, $\max \delta_{ij}(3) \approx 0.446$, $\max \delta_{ij}(5) \approx 0.305$, $\max \delta_{ij}(7) \approx 0.252$, all exceeding the declared tolerance $\epsilon = 0.15$. Under this test and tolerance, the frequency set is Archimedean-consistent and radix-inconsistent for all tested bases.

**R3. Zero-event upper limits.** Zero events in $T_{\text{obs}} = 1$ yr yields a 95% CL rate upper limit $\lambda^{\text{UL}} \approx 2.996$ yr$^{-1} \approx 9.49 \times 10^{-8}$ s$^{-1}$. Four events in one year yields $\lambda^{\text{UL}} \approx 9.154$ yr$^{-1}$ (exact one-sided Poisson; Gaussian approximation $8.38$ yr$^{-1}$).

**R4. Reporting convention (from [10]).** Non-detections are properly reported as parameter bounds: $\epsilon_p < 2.5$ at 95% CL within a single-modulation model [10]. This is the template our R3 limits follow.

**R5 (projection, labeled as such).** If a future survey with efficiency $\eta_D = 0.5$ observes for $T_{\text{obs}} = 3$ yr and detects zero events, the world-side rate limit would be $\lambda_w^{\text{UL}} = \lambda_D^{\text{UL}}/\eta_D = (2.996/3)/0.5 \approx 2.00$ yr$^{-1}$, assuming constant efficiency and stationarity. Uncertainty in this projection is dominated by the efficiency assumption; if $\eta_D$ is uncertain by a factor of two, the limit scales by the same factor.

## 6. Discussion

**Limitations.** The ratio-consistency test (R2) is deliberately minimal. It tests only whether pairwise frequency ratios lie near integer powers of a base; a genuine p-adic log-periodic signal could live in a variable other than the observing frequency itself (e.g., in event *times* rather than event *frequencies*), and our test would not detect it. The tolerance $\epsilon = 0.15$ is a declared convention, not a derived constant; a different tolerance changes the verdict for marginal cases, though here all maxima exceed it by at least a factor of $1.7$, so the qualitative conclusion is robust to any reasonable $\epsilon$. The Poisson model assumes stationarity and independence; solar-coronal event rates are known to be non-stationary in general, and the AQN interpretation itself [6] would predict rates tied to dark-matter density, which varies with location — though the supplied entry does not quantify that variation, so we cannot propagate it numerically.

**Failure modes.** The framework can fail when (i) the detector efficiency $\eta_D$ is unknown, making all reported frequencies detector-conditional; (ii) event individuation differs across detectors, so $N_{c,d}$ counts different things (the polyphony problem of [3] and the cross-platform problem of [2]); (iii) closed-loop observation makes $T_{\text{obs}}$ policy-dependent [4], invalidating passive rate estimates.

**What would falsify our claims.** R2 would be overturned if a reanalysis of the MWA event set found that the *physically meaningful* frequency variable is not the band center but, e.g., a drift-corrected or harmonic index, under which the ratios become integer powers of some $p$ within tolerance. R3's logic would fail if the event process were not Poisson (e.g., if events cluster in time), in which case zero-event limits overestimate sensitivity. More broadly, if a rigorous analysis in the spirit of [5] showed that event-frequency distributions from physical sources are statistically indistinguishable from those of structured information repositories, the sharp world/detector separation we assume would need revision.

**Arguing against ourselves.** A critic could object that the Archimedean/radix-locked distinction is a false dichotomy: most real frequency sets are neither independently placed nor radix-locked but constrained by instrumental design grids. We accept this; our test is a null-structure screen, not a complete taxonomy. A second objection: the analogy to brane-world bulk/brane separation [7] is decorative rather than load-bearing. We agree it is an analogy; its value is pedagogical, in forcing explicit statement of which layer a frequency claim lives in. A third objection: with only four frequencies [6], the ratio test has almost no power — six ratios from four points cannot distinguish structure from coincidence at any conventional significance level, and we have not computed a significance threshold because the null distribution of $\max \delta_{ij}$ over random frequency sets depends on assumptions we do not make here. We therefore state R2 as a descriptive finding, not a hypothesis test.

**Open questions.** Can efficiency calibration be standardized across social-media and physical-science event counting? Do action-conditioned rates [4] admit detector-independent bounds? Does the zitterbewegung underdetermination between Archimedean and 2-adic descriptions [12] generalize to a formal duality between Archimedean and p-adic event-frequency parameterizations?

## 7. Conclusion

We have framed the observation of event frequencies in the actual world as a three-part methodological problem — individuation, parameterization, and rare-event inference — and instantiated each part with explicit arithmetic. The radix-locked angular frequencies $\omega_p = 2\pi/\ln p$ take values $\omega_2 \approx 9.06$ down to $\omega_7 \approx 3.23$ rad; the MWA impulsive-event frequency set $\{98,120,132,160\}$ MHz fails a radix-locked consistency test for all bases in $\{2,3,5,7\}$ at tolerance $\epsilon = 0.15$, supporting an Archimedean reading of the observing frequencies; and zero-event observation over one year bounds rates at $\approx 3.0$ yr$^{-1}$ at 95% CL. The framework's utility is comparative: it gives text-based, platform-based, acoustic, and physical event counts a common language in which every frequency claim must state its detector, its efficiency, and its parameterization.

## References

[1] arXiv:1708.09453v1 | Inference of Fine-Grained Event Causality from Blogs and Films

[2] arXiv:1405.4820v1 | It Doesn't Break Just on Twitter. Characterizing Facebook content During Real World Events

[3] arXiv:2107.10469v2 | What Makes Sound Event Localization and Detection Difficult? Insights from Error Analysis

[4] arXiv:2510.18135v2 | World-in-World: World Models in a Closed-Loop World

[5] arXiv:0906.3554v3 | On the Algorithmic Nature of the World

[6] arXiv:2009.00004v2 | Radio impulsive events in quiet solar corona and Axion Quark Nugget Dark Matter

[7] arXiv:gr-qc/0612050v1 | Hamiltonian theory of brane-world gravity

[8] arXiv:1911.07850v1 | Frequency Separation for Real-World Super-Resolution

[9] QNFO: MASS-FREQUENCY

[10] QNFO: Searching for P-Adic Log-Periodic Signatures in the Cosmic Microwave Background Bispectrum: Upper Bounds from Planck 2018

[11] QNFO: Nature of Zitterbewegung

[12] QNFO: Zitterbewegung: From Archimedean Puzzle to Adelic Observable