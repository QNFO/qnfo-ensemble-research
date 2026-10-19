# Cross-Modal Temporal Binding Asynchronies as a Falsifiable Signature of Rendered Sensory Streams: A Statistical Framework

## Abstract

If the physical world is a computation, the first detectable artifacts may not appear in fundamental physics but at the mind-world interface, where visual and auditory streams are plausibly produced by separate rendering subroutines with independent clock rates. No existing framework converts this conjecture into a quantitative psychophysical test that distinguishes renderer artifacts from ordinary neural variability. We develop such a framework. We model audiovisual synchrony judgments as Gaussian biological noise convolved with deterministic quantization from a discrete render clock, derive the resulting latency distributions, and compute discriminable signatures: at a 60 Hz render clock the quantization contribution is $\sigma_q = 4.81$ ms on a biological baseline of $\sigma_{bio} = 50$ ms, producing a Kolmogorov-Smirnov distance of $D \approx 0.057$ from the purely neural distribution, detectable with $n \approx 566$ trials per condition at $\alpha = 0.05$. A mean asynchrony offset of 10 ms requires $n = 392$ per condition; a 10% widening of the temporal binding window under cognitive load requires $n \approx 433$. We specify the 40 Hz flicker-plus-click EEG paradigm, the null hypotheses, and the falsification conditions. The framework turns a philosophical claim into a bounded experiment whose outcome either constrains simulation hypotheses or establishes new psychophysical methodology for measuring cross-modal timing.

## 1. Introduction

Audiovisual synchrony perception is load-bearing in everyday technology and in clinical practice. Broadcast engineers, dubbing studios, video-conference providers, and hearing-aid and cochlear-implant fitting protocols all must keep audio and video aligned within the window over which human observers judge them as simultaneous; outside that window, users report lip-sync errors, reduced speech intelligibility, and impaired avatars' social presence. The same window is a clinical measurement in perceptual disorders. All of these applications rest on the assumption that the measured window reflects only the observer's neurophysiology and the display chain. If that assumption is incomplete—if an additional, non-physiological timing process contributes systematic structure to cross-modal latency—then every calibration standard built on synchrony judgments is measuring a composite quantity, and the composite is itself a scientific object worth characterizing.

The simulation hypothesis makes this precise. If reality is simulated, the visual and auditory channels are plausibly produced by separate rendering subroutines, and separate subroutines need not share a clock. The first detectable inconsistency would then lie not in particle physics but at the mind-world interface: cross-modal timing offsets that vary with scene complexity or cognitive load in ways no known neural mechanism predicts, or inter-hemispheric delays inconsistent with known corpus callosum conduction. Today this conjecture is untestable in any quantitative sense: no published analysis states what latency distribution a discrete render clock would imprint on synchrony judgments, how large a sample would distinguish that distribution from biological noise, or what observation would falsify the claim. A person deciding whether to fund, run, or publish such a psychophysical test currently has no effect-size estimate, no power calculation, and no falsification criterion to consult. If the framework developed here holds, those decisions become calculable: the experiment acquires a defined sample size, a defined test statistic, and a defined outcome that would count against the hypothesis.

This paper supplies that framework. We treat the simulation hypothesis as an engineering hypothesis about the timing of sensory delivery and derive its statistical consequences using only standard signal-processing and psychophysical tools. Our contributions are:

- A quantization-noise model of render-clock artifacts in cross-modal latency, yielding $\sigma_q = \Delta/\sqrt{12}$ for clock period $\Delta$, evaluated at 60 Hz and 120 Hz (Section 4.1).
- A computed Kolmogorov-Smirnov distance $D \approx 0.0572$ between the quantized-mixture distribution and the purely biological Gaussian, with the required sample size $n \approx 566$ per condition (Section 4.2).
- Power calculations for mean-offset detection ($n = 392$ per condition for a 10 ms offset) and for cognitive-load modulation of the binding window ($n \approx 433$ for a 10% width increase) (Section 4.3).
- An analysis of the inter-hemispheric prediction, showing that a single-frame artifact of 16.7 ms is not discriminative against callosal transfer times taken as 5-25 ms, and what structure would be (Section 4.4).
- A falsification criterion stated as an explicit statistical decision rule, and the experimental design that implements it (Sections 5 and 6).

## 2. Background and Related Work

The temporal-glitch literature in machine perception provides the closest existing taxonomy for our problem. TempGlitch [8] distinguishes spatial glitches, visible in a single frame, from temporal glitches, which "require reasoning over ordered visual evidence," and evaluates twelve vision-language models on gameplay videos containing both types. Its central empirical finding is that all studied models perform close to chance accuracy on temporal glitch detection, with failures driven by prediction bias, and that denser frame sampling, raw-video input, and model scale do not help. This result matters for our framework in two ways. First, it establishes that "temporal glitch" is an operational category with a working evaluation protocol—paired glitchy and glitch-free videos, binary classification, accuracy and F1 as headline metrics—which we adapt to the psychophysical setting by pairing simulated-render and pure-neural latency distributions. Second, its negative result shows that even large learned systems fail to detect temporal anomalies without dedicated temporal reasoning, supporting our choice of an explicit parametric statistical test rather than an exploratory or learned detector for the human-data setting.

Cross-modal temporal alignment is also an active engineering problem in audio-visual machine perception. The AVSR work of [6] strengthens video features by learning temporal dynamics—the context order between random audio and video frames, the playback direction, and the playback speed—through a cross-modal attention structure inserted between feature extractors and a pretrained encoder, and reports N-WER of 5.7% and 4.9% on LRS3 across noise types, surpassing AV-HuBERT and outperforming MIR-GAN and UniVPM by 5.4%/4.6% N-WER for clean/noisy pretraining types. The design premise of [6] is that audio and video streams carry independently extractable temporal structure that must be actively correlated; our hypothesis asks the analogous question about the streams delivered to a human observer, and its experimental paradigm (ordered-frame and speed judgments) is a machine analogue of the order-judgment tasks we specify for humans.

On the representation-learning side, CMAL [2] embeds visual and textual features into separate semantic spaces to learn intra-modal features before a unified encoder learns inter-modal features, and introduces an associative mapping task as a self-supervised pre-training objective; its experiments on four downstream vision-and-language tasks show competitive performance with a smaller pre-training corpus and lower computational cost. The architectural lesson—that cross-modal structure is learned most cleanly when each modality is first modeled on its own terms—motivates our decision to model the visual and auditory latency distributions separately before forming the cross-modal difference distribution. SemanticMap [3] makes a complementary methodological point: pairwise evaluation measures such as R@K "do not leverage semantic relationships rather strictly follow the manually marked image text query pairs," so systems score well on benchmark pairs while generalizing poorly to unseen data. Transposed into our setting, this warns against validating a synchrony-judgment model only on the stimulus pairs used to train or calibrate it; the falsification test in Section 6 therefore uses held-out stimulus conditions (varied scene complexity) that the null model was not fitted to.

The debiasing work of [7] is relevant through its causal treatment of paired cross-modal data. Because a recipe and its cooked dish are related as cause and effect, treating the recipe as a plain text description of the image creates bias; [7] models ingredients as a confounder and shows by simulation that near-perfect retrieval is attainable under this causal model, with the proposed module boosting three state-of-the-art models to the highest reported medR and recall on Recipe1M (medR = 1.4 for image-to-recipe and 1.0 for recipe-to-image on the 10K search set, versus R1 = 24.0% for RDE-GAN against 50.2% for VLPCook+Debiasing). The transferable point is that an unmodeled common cause can dominate a cross-modal similarity judgment; in our framework, cognitive load and scene complexity are candidate confounders of measured asynchrony, and Section 4.3 treats them explicitly rather than marginalizing them.

Cross-modal knowledge transfer between measurement modalities of the same underlying system is demonstrated by [5], which distills spatial-transcriptomics-derived tissue niche segmentation into a histology-only student model, on the premise that gene expression is a richer substrate for niche learning than morphology alone; the student replicates the teacher's fine-grained segmentation, including tumor epithelial regions and invasive carcinoma nest boundaries, without transcriptomic profiling at inference time. This supports the design choice, in our EEG/MEG paradigm, of using a modality-rich measurement (MEG source estimates) to supervise interpretation of a cheaper one (EEG), rather than treating the two as independent channels.

Temporal-network theory [4] supplies the formal vocabulary for our latency data. Its foundational observation is that one learns more about a system if the first simplification does not "discard information about when things happen," and its basic data object is the event, a triple $(i,j,t)$ recording that nodes $i$ and $j$ are in contact at time $t$, with connectivity defined along time-respecting paths of strictly increasing timestamps. Our asynchrony trials are exactly such events—$(\text{visual}, \text{auditory}, t)$ triples—and the hypothesis of independent render clocks predicts violations of the exchangeability of timestamps across trials that a static analysis would average away. Finally, [1] offers a structural precedent for the logic of the whole paper: it compares an illumination model against a hydrodynamic simulation of the same laser-irradiated target, evaluating irradiation non-uniformity under circular and elliptical super-gaussian profiles and optimizing the scheme by Polar Direct Drive. The method—two models of one phenomenon, compared on a shared observable to localize discrepancy—is precisely the inferential structure we apply, with the biological noise model and the render-clock model playing the two roles.

The conceptual background for locating the test at the mind-world interface is set out in the QNFO outline [9], which identifies post-hoc narration and predictive processing as a "potential fault line where simulation 'patches' or inconsistencies could be revealed," reviews the Libet finding that the readiness potential precedes conscious intention by several hundred milliseconds as establishing "a temporal disconnect between unconscious brain preparation and subjective experience," and proposes that a discrete or hierarchical time metric (as in p-adic ultrametric spaces) "could lead to a temporal window of integration with a discrete, hierarchical structure." Our contribution is to convert that qualitative fault line into distributions, test statistics, and sample sizes.

## 3. Methods

### 3.1 Hypothesis and observables

We define the measured audiovisual asynchrony for trial $k$ as

$$a_k = t_k^{(resp)} - \left( t_k^{(V)} - t_k^{(A)} \right),$$

where $t_k^{(V)} - t_k^{(A)}$ is the physical stimulus offset and $t_k^{(resp)}$ is the observer's point of subjective simultaneity expressed in the same units. Under the null hypothesis $H_0$ (pure neurophysiology), $a_k \sim \mathcal{N}(\mu_{bio}, \sigma_{bio}^2)$ with parameters determined by the observer's temporal binding window. Under the render hypothesis $H_1$, the delivered stimulus times are quantized by independent render clocks:

$$t_k^{(V)} = \Delta_V \left\lfloor \frac{\tilde{t}_k^{(V)}}{\Delta_V} \right\rfloor, \qquad t_k^{(A)} = \Delta_A \left\lfloor \frac{\tilde{t}_k^{(A)}}{\Delta_A} \right\rfloor,$$

with clock periods $\Delta_V$, $\Delta_A$, so that $a_k$ becomes a mixture of Gaussian biological noise and deterministic quantization error.

### 3.2 Test statistics

We use three statistics: (i) a two-sample $z$-test on the mean asynchrony between a low-load and a high-load, or low-complexity and high-complexity, stimulus condition; (ii) a Kolmogorov-Smirnov (KS) test of the pooled asynchrony distribution against the fitted Gaussian null, which is sensitive to the lattice structure quantization produces even when the mean is unchanged; (iii) a log-variance $z$-test for load-induced changes in binding-window width. Sample sizes follow from standard formulas, derived in Section 4. EEG/MEG recording of the 40 Hz auditory steady-state and visual flicker responses provides a physiological anchor: the phase of the 40 Hz response indexes the binding window, and a render-clock artifact should appear in the stimulus-locked but not in the endogenous phase statistics.

### 3.3 Assumptions

The grounding supplies no numerical values for biological timing, so we state all inputs as explicit assumptions, chosen conservatively from the range over which synchrony-judgment experiments are typically designed: $\sigma_{bio} = 50$ ms (the scale of the temporal binding window), inter-hemispheric transfer time $5$-$25$ ms, render clock 60 Hz ($\Delta = 16.67$ ms) as the baseline and 120 Hz as the alternative. Every result below is a function of these inputs and is recomputable from Section 4.

## 4. Analysis

### 4.1 Quantization noise from a discrete render clock

A uniform quantizer with step $\Delta$ produces error uniform on $[-\Delta/2, \Delta/2]$, with variance

$$\sigma_q^2 = \int_{-\Delta/2}^{\Delta/2} \frac{x^2}{\Delta}\, dx = \frac{\Delta^2}{12}.$$

At a 60 Hz clock, $\Delta = 1000/60 = 16.667$ ms:

$$\sigma_q^2 = \frac{(16.667)^2}{12} = \frac{277.78}{12} = 23.148 \ \text{ms}^2, \qquad \sigma_q = \sqrt{23.148} = 4.811 \ \text{ms}.$$

At 120 Hz, $\Delta = 8.333$ ms:

$$\sigma_q^2 = \frac{69.444}{12} = 5.787 \ \text{ms}^2, \qquad \sigma_q = 2.406 \ \text{ms}.$$

The total asynchrony variance under $H_1$ is the sum, since quantization error and biological noise are independent:

$$\sigma_{tot}^2 = \sigma_{bio}^2 + \sigma_q^2.$$

At 60 Hz: $\sigma_{tot}^2 = 2500 + 23.148 = 2523.148$, so $\sigma_{tot} = 50.231$ ms. At 120 Hz: $\sigma_{tot}^2 = 2505.787$, $\sigma_{tot} = 50.058$ ms. The variance inflation is small (0.46% at 60 Hz), which is why the mean and variance tests alone are weak and the shape-sensitive KS test is the primary statistic.

### 4.2 KS distance between the quantized mixture and the pure Gaussian

The quantized-mixture distribution is the convolution of $\mathcal{N}(0, \sigma_{bio}^2)$ with a uniform lattice; to first order its shape is well approximated by comparing the Gaussian to a uniform distribution of equal variance (the dominant shape difference is the bounded, flat-tailed uniform component). A uniform distribution with variance $\sigma_{bio}^2 = 2500$ has half-width

$$a = \sigma_{bio}\sqrt{3} = 50 \times 1.7321 = 86.603 \ \text{ms}.$$

Its CDF is $F_U(x) = (x + a)/(2a)$ on $[-a, a]$. The KS distance against the standard Gaussian scaled to the same variance, $F_N(x) = \Phi(x/50)$, is maximized where the slopes differ most near the center. Evaluating:

- At $x = 40$ ms: $F_U = (40 + 86.603)/173.205 = 126.603/173.205 = 0.7309$; $\Phi(40/50) = \Phi(0.80) = 0.7881$; $D = 0.0572$.
- At $x = 43.3$ ms: $F_U = 129.903/173.205 = 0.7500$; $\Phi(0.866) = 0.8068$; $D = 0.0568$.
- At $x = 30$ ms: $F_U = 116.603/173.205 = 0.6732$; $\Phi(0.60) = 0.7257$; $D = 0.0525$.
- At $x = 50$ ms: $F_U = 136.603/173.205 = 0.7887$; $\Phi(1.00) = 0.8413$; $D = 0.0526$.

The maximum over the scanned grid is $D \approx 0.0572$ at $x \approx 40$ ms. (The true maximum lies between the grid points; we take $D = 0.057$ as the working value and carry its rounding into the sample size.)

The KS critical value at significance level $\alpha = 0.05$ is $D_{crit} = 1.36/\sqrt{n}$. Requiring $D \geq D_{crit}$ with the observed $D = 0.057$:

$$n = \left(\frac{1.36}{0.057}\right)^2 = (23.860)^2 = 569.3 \approx 570 \ \text{trials per condition}.$$

Using the unrounded grid maximum $D = 0.0572$ gives $n = (1.36/0.0572)^2 = (23.776)^2 = 565.3 \approx 566$. We report $n \approx 566$-$570$ trials per condition; the range reflects only the grid resolution of $D$.

### 4.3 Power for mean offset and binding-window width

**Mean offset.** To detect a mean asynchrony shift $\delta$ between two conditions with common standard deviation $\sigma_{tot}$, at $\alpha = 0.05$ (two-sided, $z_{0.975} = 1.960$) and 80% power ($z_{0.80} = 0.842$), the required per-group sample size is

$$n = \frac{(z_{0.975} + z_{0.80})^2 (\sigma_1^2 + \sigma_2^2)}{\delta^2}.$$

For $\delta = 10$ ms and $\sigma_1^2 = \sigma_2^2 = 2523.148$ ms$^2$ (the 60 Hz mixture):

$$n = \frac{(1.960 + 0.842)^2 \times (2523.148 + 2523.148)}{100} = \frac{(2.802)^2 \times 5046.296}{100} = \frac{7.851 \times 5046.296}{100} = \frac{39618.7}{100} = 396.2.$$

Rounding up, $n = 397$ per condition. (With the pure biological $\sigma = 50$ ms the same formula gives $n = 392$; the render-clock variance inflation costs 5 trials per condition.)

**Binding-window width under load.** Suppose cognitive load widens the biological window by 10%, i.e., $\sigma_2/\sigma_1 = 1.1$ and the variance ratio is $1.21$. The statistic $\ln s^2$ has approximate standard error $\sqrt{2/(n-1)}$. To detect $\ln(1.21) = 0.1906$ at 80% power:

$$n - 1 = 2\left(\frac{1.960 + 0.842}{0.1906}\right)^2 = 2\left(\frac{2.802}{0.1906}\right)^2 = 2 \times (14.701)^2 = 2 \times 216.12 = 432.2,$$

so $n \approx 433$ per condition. A 10% width change is thus detectable with a few hundred trials per condition, comparable to the mean-offset requirement.

**False-positive control for outlier structure.** Under $H_0$, the probability that a single trial shows $|a| > 3\sigma_{bio} = 150$ ms is $2\Phi(-3) = 2 \times 0.00135 = 0.0027$. In $n = 1000$ trials the expected number of such excursions is $2.7$; a render clock with occasional dropped or repeated frames would produce excess excursions beyond this baseline, which is a separate, cheaply powered signature.

### 4.4 Inter-hemispheric delays

The grounding hypothesis predicts inter-hemispheric delays inconsistent with known corpus callosum latencies; we take the callosal transfer range as $5$-$25$ ms (assumption, Section 3.3). A one-frame render artifact at 60 Hz is $16.667$ ms, which lies inside this range, so a single-frame delay is not discriminative on its own:

$$16.667 \in [5, 25] \ \text{ms}.$$

What would be discriminative is structure: (i) a delay that quantizes to multiples of $\Delta$ (a lattice in the inter-hemispheric difference distribution, testable by KS as in Section 4.2 with the same $n \approx 566$); or (ii) a delay that scales with scene complexity, which no callosal mechanism predicts. We therefore do not claim the inter-hemispheric channel is individually decisive; it is confirmatory, and its falsification condition is stated in Section 6.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions ($\sigma_{bio} = 50$ ms, 60 Hz baseline clock, $\alpha = 0.05$, 80% power where applicable).

1. **Quantization contribution.** A 60 Hz render clock contributes $\sigma_q = 4.811$ ms of latency noise; a 120 Hz clock contributes $\sigma_q = 2.406$ ms. The total standard deviation of measured asynchrony becomes $50.231$ ms at 60 Hz and $50.058$ ms at 120 Hz, against $50.000$ ms under the pure-neural null.

2. **Distribution-shape signature.** The KS distance between the render-clock mixture and the pure Gaussian is $D \approx 0.057$ (grid maximum $0.0572$ at $x \approx 40$ ms). Detection at $\alpha = 0.05$ requires $n \approx 566$-$570$ trials per condition. This is the primary signature: it survives even when the render clock introduces no mean offset.

3. **Mean-offset signature.** A 10 ms systematic asynchrony offset between conditions is detectable with $n = 397$ per condition under the render-clock variance ($392$ under the pure-neural variance).

4. **Load-modulation signature.** A 10% cognitive-load-induced widening of the binding window is detectable with $n \approx 433$ per condition via the log-variance test.

5. **Inter-hemispheric channel.** A single 60 Hz frame artifact ($16.667$ ms) falls within the assumed callosal range of 5-25 ms and is not individually discriminative; only lattice structure or complexity-scaling in the inter-hemispheric difference distribution would be.

6. **Outlier channel.** Under the null, $|a| > 150$ ms occurs with probability $0.0027$ per trial ($2.7$ expected excursions per 1000 trials); excess excursions are a low-cost secondary signature.

No empirical data are reported in this paper; all values are analytical consequences of the stated model and assumptions.

## 6. Discussion

The framework's strength is that every claim reduces to arithmetic on stated inputs; its weakness is that the inputs are assumptions. The central result—$D \approx 0.057$ and $n \approx 566$—scales linearly in the KS distance's inverse square, so it is sensitive to the assumed $\sigma_{bio}$: if the true binding-window noise is $\sigma_{bio} = 30$ ms, the equal-variance uniform half-width becomes $a = 30\sqrt{3} = 51.96$ ms, and recomputing the KS scan (e.g., at $x = 24$ ms: $F_U = (24+51.96)/103.92 = 0.7310$, $\Phi(24/30) = \Phi(0.80) = 0.7881$, $D = 0.0571$) gives essentially the same $D$—the KS distance between a uniform and a Gaussian of equal variance is scale-invariant, so $n$ is robust to $\sigma_{bio}$, but the *interpretation* of the lattice spacing is not: at $\sigma_{bio} = 30$ ms the quantization step of 16.667 ms is a larger fraction of the window and the first-order uniform approximation degrades.

**Failure modes.** The uniform-approximation step in Section 4.2 is the weakest link: the exact convolution of a Gaussian with a uniform lattice has a slightly different CDF, and the true $D$ could differ from 0.057 by a factor of order unity. A Monte Carlo evaluation of the exact convolution is the obvious refinement. Second, physiological noise is not Gaussian: trial-to-trial attentional state, adaptation, and motor-response variability add heavy tails that could mimic or mask the quantization signature; the KS test would then reject the Gaussian null for mundane reasons. Third, display chains in any real experiment have their own quantization (monitor refresh at 60 Hz is itself a 16.67 ms clock), so the experiment must use stimulus presentation hardware whose timing is measured independently, or the render signature is confounded with the laboratory's own.

**Falsification.** The observation that would falsify the main claim is explicit: if a well-timed experiment with $n \geq 600$ trials per condition, using presentation hardware with independently verified sub-millisecond timing, finds (a) no mean asynchrony offset beyond the $z$-test threshold, (b) no KS rejection of the Gaussian null beyond $D_{crit} = 1.36/\sqrt{n}$, and (c) no load- or complexity-dependent structure beyond the log-variance threshold, then the render-clock model as specified is excluded at the stated significance for clock periods in the range tested, and the simulation-glitch hypothesis loses its proposed mind-world signature. Conversely, a KS rejection alone would not confirm the hypothesis, since non-Gaussian physiological noise produces the same outcome; confirmation requires the lattice spacing to track a single clock period across stimulus conditions, which physiological mechanisms have no reason to do.

**Limitations list.** (1) $\sigma_{bio} = 50$ ms is an assumption; the sample sizes for mean and variance tests scale as $\sigma^2$ and would change proportionally. (2) The KS distance uses a uniform-vs-Gaussian approximation rather than the exact convolution; $D$ is uncertain to a factor of order one. (3) The callosal range 5-25 ms is an assumption; if the true range were wider, the inter-hemispheric non-discriminability conclusion weakens. (4) The model assumes independent visual and auditory clocks; a single shared clock produces no cross-modal offset at all, and the framework would have no signature. (5) Physiological non-Gaussianity is unmodeled and is the main confound for the KS statistic. (6) The framework assumes the simulation, if it exists, renders at a fixed clock period; adaptive or event-driven rendering would leave no lattice. (7) No empirical data were collected; all results are analytical projections from the stated model.

## 7. Practical Implications and Engineering Pathways

**(a) Users and decisions.** The immediate users are psychophysicists and perception laboratories deciding whether to allocate EEG/MEG beam time and participant budget to a simulation-glitch experiment: the paper gives them the effect size ($D \approx 0.057$), the sample size ($n \approx 566$ per condition for the shape test; $n = 397$ for a 10 ms offset), and the decision rule, which are exactly the inputs a funding or ethics decision requires. A second user group is designers of audiovisual synchrony calibration standards (broadcast, videoconferencing, clinical fitting), for whom the result, if the null survives, certifies that synchrony judgments measure neurophysiology alone; if the null is rejected in the specific lattice pattern, those standards are measuring a composite and would need re-derivation. The work is otherwise