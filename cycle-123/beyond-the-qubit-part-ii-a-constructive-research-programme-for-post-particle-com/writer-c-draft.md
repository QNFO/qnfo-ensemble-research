# Beyond the Qubit, Part II: A Constructive Research Programme for Post-Particle Computation, with Quantified Instrumentation and Embodied-Verification Pathways

## Abstract

The companion programme "Beyond the Qubit" argues that the qubit-gate-circuit model is an epistemic failure — a projection of particle ontology onto relational, field-theoretic reality — and asks what comes next [9]. This paper supplies the constructive half of that answer in a form that independent researchers can act on. The specific gap is that critiques of the qubit model stop at diagnosis: they name no measurement standard to inherit, no error budget to satisfy, and no embodied test protocol by which a successor formalism could be falsified. We address the gap in three steps. First, we extract from the NEXT dark-matter-adjacent programme a precision-measurement standard — an energy resolution of 0.5–1% FWHM at the double-beta-decay energy of ${}^{136}$Xe [5] — and derive its equivalent one-sigma scale, $\sigma_E/Q_{\beta\beta} \approx 4.2465 \times 10^{-3}$ at the 1% FWHM end. Second, we derive a multiplicative error-budget arithmetic for any successor pipeline: five independent stages each contributing $10^{-2}$ relative error give a worst-case stack of $5 \times 10^{-2}$ but a root-sum-square stack of $2.2361 \times 10^{-2}$, a factor-of-$\sqrt{5}$ difference that determines whether a paradigm is buildable. Third, we map embodied XR results — skeleton fitting [1], instant tracking [6], depth-cue studies [8], locomotion response [3], and real-time sickness detection [7] — onto a verification protocol in which a human operator is the instrument. The principal result is a falsifiable acceptance criterion: a post-particle computational formalism is admissible only if its end-to-end predicted error stack, computed by the root-sum-square rule derived here, stays below the Fano-scale bound of $2.1233 \times 10^{-3}$–$4.2465 \times 10^{-3}$ relative. In practice this converts a philosophical dispute into a numerical gate that any laboratory can apply.

## 1. Introduction

The people who face the problem this paper bears on are working physicists, instrument builders, and research programme funders who must decide where to spend the next decade of scarce experimental effort. Quantum computing roadmaps assume the qubit-gate-circuit model is the correct target; the companion analysis argues instead that this model is an epistemic failure, a projection of particle ontology onto relational, field-theoretic reality [9]. If that diagnosis is right, the cost of continuing on the qubit path is not merely wasted engineering effort but the absence of any prepared alternative: no accepted measurement standard to inherit, no error budget a successor must meet, and no test protocol that could falsify a candidate formalism. Today a researcher who accepts the diagnosis has nowhere to go; the decision that would change is the go/no-go decision on candidate formalisms, and the capability that would change is the ability to reject or admit a new computational paradigm on numerical grounds rather than on philosophical taste.

The so-what is concrete. A funder holding two competing post-qubit proposals currently has no shared yardstick and must judge them by narrative. A laboratory that wants to test a relational or field-theoretic formalism has no specification of how precise its apparatus must be. And a sceptic who wants to kill the whole post-particle programme has no single number to attack. This paper supplies all three: a yardstick inherited from precision measurement practice, a budget rule that turns component errors into a system-level pass/fail figure, and an embodied verification pathway in which a human operator inside a mixed-reality apparatus serves as the readout instrument.

The strategy is deliberately conservative. We do not propose a new physics theory. We take the minimal constructive stance already announced in the companion paper — strip quantum mechanics to its minimal core and rebuild [9] — and we ask what engineering scaffolding any such rebuild must satisfy to count as science rather than as manifesto. The scaffolding has three parts: (i) a precision standard, taken from the NEXT programme, whose stated design goal is an energy resolution nearing the Fano factor in xenon, 0.5–1% FWHM at $Q_{\beta\beta,{}^{136}\mathrm{Xe}}$ [5]; (ii) an error-composition rule, derived in Section 4, that converts per-stage errors into an end-to-end figure; and (iii) a human-in-the-loop verification layer, grounded in the embodied-computing literature, in which skeleton-fitted self-avatars [1], instant motion tracking [6], calibrated depth perception [8], and real-time physiological monitoring [7] together make a human operator into a calibrated, auditable measurement channel.

The contributions of this paper are:

- A derived one-sigma equivalent of the NEXT Fano-scale resolution standard: $\sigma_E/Q_{\beta\beta} \in [2.1233 \times 10^{-3},\ 4.2465 \times 10^{-3}]$, computed from the stated 0.5–1% FWHM figure by the Gaussian FWHM-to-sigma conversion (Section 4.1).
- A derived error-composition rule with a worked example: for $n$ independent stages each at relative error $\varepsilon$, the worst-case stack is $n\varepsilon$ and the statistical stack is $\sqrt{n}\,\varepsilon$; for $n=5$, $\varepsilon=10^{-2}$, these are $5 \times 10^{-2}$ and $2.2361 \times 10^{-2}$ respectively (Section 4.2).
- A derived drift-growth bound for anchored tracking in an embodied verification rig: random-walk accumulation of per-frame anchor error gives $\delta_{\mathrm{drift}} = \varepsilon_f \sqrt{N}$, which for the stated illustrative assumptions yields $6.0 \times 10^{-2}$ m over a one-minute session (Section 4.3).
- A falsifiable acceptance criterion, the Fano-gate, combining the above into a single admissibility test for post-particle computational formalisms (Section 5).
- A mapped verification protocol and engineering pathway, in which each embodied XR capability is assigned a role in the rig and a TRL-honest readiness statement is made (Sections 3 and 7).

## 2. Background and Related Work

This section reviews the supplied bibliography in its exact numbering. Eight of the twelve entries are peer-style research papers with substantive summaries; four are QNFO programme documents, two of which carry only titles. We discuss each and state plainly where the supplied summary gives no further detail.

**Precision measurement as the inherited standard.** The NEXT experiment entry describes Phase I of the NEXT-100 $0\nu\beta\beta$ experiment (NEW), scheduled for data taking in 2015 at Laboratorio Subterráneo de Canfranc in the Spanish Pyrenees, anticipating an energy resolution nearing the Fano factor in xenon of 0.5–1% FWHM at $Q_{\beta\beta,{}^{136}\mathrm{Xe}}$, with a time-projection-chamber design allowing tracking and identification of the double end-blob feature of the decay signature [5]. Two features of this entry matter for our argument. First, the resolution figure is a design *anticipation*, not a measured result; we treat it throughout as a target standard, not as achieved performance. Second, the entry shows what a mature experimental paradigm looks like from the outside: a named site, a named technique, a quoted resolution, and a topology identifier (the double end-blob) that turns an energy measurement into a topology-verified one. Any successor computational paradigm should be held to the same standard of specificity, and Section 4 converts the quoted FWHM figure into the one-sigma scale we use as our gate.

**Embodiment and avatar calibration.** The fitted-avatars paper addresses automatic skeleton adjustment for self-avatars in virtual reality, arguing that in the era of the metaverse self-avatars enhance presence and provide embodiment, and that whether one uses complex motion capture or a few trackers with inverse kinematics, a good skeleton fit is essential [1]. The summary supplied is truncated mid-sentence and gives no quantitative results; we therefore use this work only for its architectural claim — that embodiment quality depends on a calibration step that can be automated — which is exactly the role we assign to avatar fitting in the verification rig of Section 3.

**Multi-user analytics as a model of shared instrument state.** The interactive multi-user 3D visual analytics project developed a prototype AR data-analytics application with an interactive 3D interface, hand-gesture-based controls, and multi-user support for a shared experience, explicitly to explore the advantages and disadvantages of AR for visual data analytics [2]. The relevance to our programme is structural: a shared, gesture-controlled volumetric interface is a working precedent for several operators inspecting the same computational state simultaneously, which is the collaboration mode our verification protocol requires when a formalism's predictions must be checked by more than one observer.

**Redirected locomotion as perceptual error budgeting.** The Reality Distortion Room is a proof-of-concept AR system using projection mapping and unencumbered interaction with the Microsoft RoomAlive system to study users' locomotive responses to visual effects that seemingly transform the physical room; it presents five effects that augment the appearance of a physical room to subtly encourage user motion [3]. The entry's summary is truncated before its results, so we cite no outcome numbers from it. What we take from it is the existence proof that a physical room can be perceptually re-specified by controlled visual offsets, and the concrete count of five effect families, which we use as the stage count $n=5$ in the worked error-budget example of Section 4.2 — an explicitly labelled modelling assumption, not a finding of [3].

**Remote guidance as the expert-operator channel.** The mixed-reality remote-assistance system is a volumetric communication system for procedural tasks in which a remote expert visually guides a local operator; the two parties share a spatially identical view, of the real object for the local operator and of a mixed-reality "hologram" for the remote expert [4]. This is the communication topology our rig inherits: a formalism's predicted state can be rendered as the hologram layer while the apparatus's actual state is the local layer, and disagreement between expert view and operator view is the observable that constitutes a test.

**Tracking as the anchoring primitive.** The instant motion tracking paper identifies proper anchoring of virtual content to the real world — tracking — as a key challenge in enabling AR features, and presents a motion-tracking system that, per the summary, leverages advances in computer vision and mobile computing to support AR across platforms and products [6]. The summary is truncated before method details, so we take from it only the problem statement: anchoring error is the fundamental per-frame quantity in any AR system. Section 4.3 builds a drift model on exactly this quantity, with the per-frame error value stated as an assumption of ours, not of [6].

**Real-time physiological monitoring as the operator readout.** The simulator-sickness paper states that simulator sickness remains a significant problem for wider VR adoption, that the standard Simulator Sickness Questionnaire is a subjective measurement inadequate for real-time applications such as VR games, and that the work therefore targets real-time detection of simulator sickness from players' psychophysiological data during gameplay [7]. The summary is truncated before its detection results. Its role in our programme is methodological: it establishes that operator state can be read continuously from physiological signals rather than by post-hoc questionnaires, which is what makes a human operator usable as an in-loop instrument rather than as an end-of-session report.

**Depth perception as the calibration target.** The depth-perception study investigates how object shape, fidelity, color, and luminance affect depth perception in handheld mobile AR, noting that many AR applications require depth matching of real and virtual objects and that color and luminance are depth cues traditionally studied in 2D, with little prior research on these factors in the mobile AR setting described [8]. The summary is truncated before its findings. We use it as the citation for the claim that depth matching between real and virtual objects is an active, factor-decomposable calibration problem — the same problem our rig faces when a rendered hologram layer must be co-registered with the physical apparatus.

**The QNFO programme documents.** The companion paper "Beyond the Qubit: Constructive Paradigms for Post-Particle Computation" is described as the companion to "The Qubit Delusion" (v1.1), posing the question of what comes next if the qubit-gate-circuit model is an epistemic failure — a projection of particle ontology onto relational, field-theoretic reality — and announcing the stripping of quantum mechanics to its minimal core [9]. This paper is the constructive continuation of that question. The "Ultrametric Physics Research Plan" and the "Simulated Stability and the Superdeterministic Quantum Machine" entries carry titles only; the supplied summaries give no further detail, so we relate them to our argument only as named strands of the same programme and draw no findings from them [10], [11]. Finally, the "Manifesto for Honest Computation" entry states that it contains a Phase VI (Final Synthesis) with 5 principles, a concrete portfolio, and the Falsification Pledge [12]. We adopt the Falsification Pledge as a normative commitment: every acceptance criterion in this paper is stated so that a named observation would refute it. We do not reproduce the five principles or the portfolio, since the supplied summary does not state their content.

In summary, the literature supplies three things this paper needs: a precision standard with a quoted resolution target [5], a set of embodied-interaction primitives each addressing one calibration channel [1], [3], [4], [6], [7], [8], [2], and a programme-level mandate for falsifiable constructive work [9], [12]. What none of them supplies — and what this paper derives — is the arithmetic that connects per-stage errors to a single admissibility number.

## 3. Methods

The method is constructive derivation plus protocol mapping, with no new data collection. It has three components.

**Component 1: standard extraction and unit conversion.** We take the NEXT design target — energy resolution nearing the Fano factor in xenon, 0.5–1% FWHM at $Q_{\beta\beta,{}^{136}\mathrm{Xe}}$ [5] — and convert it from FWHM to one-sigma form under the assumption, stated here and carried through the paper, that the resolution figure behaves as a Gaussian width for the purpose of budget composition. The conversion constant is $2\sqrt{2\ln 2}$. This yields the relative one-sigma scale $\sigma_E/Q_{\beta\beta}$ that we adopt as the "Fano-gate" admissibility band. We emphasize that [5] states this figure as an anticipation for Phase I, not a measurement; our gate inherits it as a target, and Section 6 treats this inheritance as a load-bearing assumption.

**Component 2: error-composition arithmetic.** We model any candidate computational pipeline — from formalism to rendered prediction to physical readout — as $n$ independent stages, each contributing a relative error $\varepsilon_i$. Two composition rules bound the end-to-end error: the worst-case linear stack $\sum_i \varepsilon_i$, appropriate when stage errors are correlated or adversarially aligned, and the root-sum-square (RSS) stack $\sqrt{\sum_i \varepsilon_i^2}$, appropriate when stage errors are independent and zero-mean. We derive both, state the independence assumption explicitly, and compute the worked example with $n=5$ and $\varepsilon=10^{-2}$. The choice of $n=5$ is a modelling assumption motivated by the five effect families of the Reality Distortion Room study [3]; it is not a measured stage count, and Section 6 lists its sensitivity.

**Component 3: embodied verification protocol.** We define a verification rig in which a candidate formalism's predictions are rendered as a mixed-reality hologram layer over the physical apparatus, following the shared-view topology of the remote-assistance system [4]. The rig's calibration channels are: automatic skeleton fitting of the operator's self-avatar [1]; instant motion tracking for anchoring the hologram to the apparatus [6]; depth matching between hologram and apparatus, decomposed by the shape/fidelity/color/luminance factors of the mobile-AR depth study [8]; continuous physiological monitoring of the operator in place of retrospective questionnaires [7]; and, where the apparatus occupies a room-scale volume, projection-mapped room re-specification of the kind demonstrated by the Reality Distortion Room [3]. Multi-operator review uses the shared gesture-controlled 3D interface pattern of the multi-user analytics prototype [2]. For the tracking channel we derive a random-walk drift model with all numerical inputs stated as assumptions of this paper.

No empirical measurement is reported in this paper. Every number in Sections 4 and 5 is either (a) quoted from a bibliography entry and cited, (b) derived from such a quote by shown arithmetic, or (c) explicitly labelled a projection under stated assumptions.

## 4. Analysis

### 4.1 Derivation of the Fano-gate band from the NEXT resolution target

**Input (cited).** The NEXT Phase I design anticipates an energy resolution nearing the Fano factor in xenon of 0.5–1% FWHM at $Q_{\beta\beta,{}^{136}\mathrm{Xe}}$ [5].

**Step 1: express the FWHM band in relative form.** The stated band is

$$\frac{\mathrm{FWHM}_E}{Q_{\beta\beta}} \in [0.005,\ 0.01].$$

**Step 2: convert FWHM to one sigma.** For a Gaussian, $\mathrm{FWHM} = 2\sqrt{2\ln 2}\,\sigma$. The constant is

$$2\sqrt{2\ln 2} = 2\sqrt{2 \times 0.693147} = 2\sqrt{1.386294} = 2 \times 1.177410 = 2.354820.$$

Therefore

$$\sigma_E = \frac{\mathrm{FWHM}_E}{2.354820}.$$

**Step 3: compute the relative one-sigma band.** At the 1% FWHM end:

$$\frac{\sigma_E}{Q_{\beta\beta}} = \frac{0.01}{2.354820} = 4.2465 \times 10^{-3}.$$

Arithmetic: $0.01 / 2.354820 = 4.24646 \times 10^{-3}$, rounded to $4.2465 \times 10^{-3}$. At the 0.5% FWHM end:

$$\frac{\sigma_E}{Q_{\beta\beta}} = \frac{0.005}{2.354820} = 2.1233 \times 10^{-3}.$$

Arithmetic: $0.005 / 2.354820 = 2.12323 \times 10^{-3}$, rounded to $2.1233 \times 10^{-3}$.

**Result 4.1.** The Fano-gate band is

$$\boxed{\frac{\sigma_E}{Q_{\beta\beta}} \in \left[2.1233 \times 10^{-3},\ 4.2465 \times 10^{-3}\right]}$$

under the stated Gaussian-width assumption. This is the one-sigma scale a successor formalism's predicted observables must respect to inherit the NEXT-class precision standard.

### 4.2 Derivation of the error-composition rule and the worked five-stage example

**Inputs (assumptions of this paper, stated).** $n = 5$ independent stages; each stage contributes relative error $\varepsilon = 10^{-2}$. The stage count is motivated by the five effect families demonstrated in the Reality Distortion Room study [3]; the per-stage value $10^{-2}$ is chosen to sit at the coarse end of the Fano-gate band derived in Section 4.1, so that the example is diagnostic rather than flattering.

**Step 1: worst-case linear stack.** If stage errors align in sign,

$$\varepsilon_{\mathrm{WC}} = \sum_{i=1}^{n} \varepsilon_i = n\varepsilon = 5 \times 10^{-2} = 5 \times 10^{-2}.$$

**Step 2: statistical RSS stack.** If stage errors are independent and zero-mean,

$$\varepsilon_{\mathrm{RSS}} = \sqrt{\sum_{i=1}^{n} \varepsilon_i^2} = \sqrt{n\,\varepsilon^2} = \varepsilon\sqrt{n} = 10^{-2}\sqrt{5}.$$

Computing: $\sqrt{5} = 2.236068$, so

$$\varepsilon_{\mathrm{RSS}} = 2.2361 \times 10^{-2}.$$

**Step 3: the ratio and its meaning.**

$$\frac{\varepsilon_{\mathrm{WC}}}{\varepsilon_{\mathrm{RSS}}} = \frac{5 \times 10^{-2}}{2.2361 \times 10^{-2}} = \sqrt{5} = 2.2361.$$

**Result 4.2.** For the stated assumptions, the same five one-percent stages compose to $5 \times 10^{-2}$ worst-case or $2.2361 \times 10^{-2}$ statistically — a factor of $\sqrt{5} \approx 2.2361$ apart. The practical consequence is that whether a candidate paradigm is buildable can hinge entirely on whether its stage errors are independent: a pipeline that is admissible under the RSS rule fails the identical per-stage numbers under the linear rule. Any admissibility claim must therefore state, and ideally test, the independence assumption.

### 4.3 Derivation of the tracking drift-growth bound

**Inputs (assumptions of this paper, stated).** The instant-tracking literature identifies anchoring of virtual content to the real world as the key enabling challenge for AR features [6]; it supplies no per-frame error figure in the summary provided. We therefore assume, for illustration only: per-frame anchor error $\varepsilon_f = 10^{-3}$ m (one millimetre, a round figure at the scale of handheld-AR depth-matching studies [8]); session length $T = 60$ s; frame rate $f = 60$ Hz, giving $N = fT = 3600$ frames. We assume frame-to-frame anchor errors are independent and zero-mean, so drift grows as a random walk.

**Step 1: frame count.**

$$N = fT = 60 \times 60 = 3600.$$

**Step 2: random-walk drift.** For $N$ independent zero-mean steps each of magnitude $\varepsilon_f$, the root-mean-square accumulated displacement is

$$\delta_{\mathrm{drift}} = \varepsilon_f \sqrt{N} = 10^{-3} \times \sqrt{3600}.$$

Computing: $\sqrt{3600} = 60$, so

$$\delta_{\mathrm{drift}} = 10^{-3} \times 60 = 6.0 \times 10^{-2}\ \mathrm{m}.$$

**Step 3: worst-case contrast.** If per-frame errors align (e.g., a constant bias in the anchor estimate), the linear stack is

$$\delta_{\mathrm{lin}} = \varepsilon_f N = 10^{-3} \times 3600 = 3.6\ \mathrm{m},$$

which is sixty times the random-walk figure ($3.6 / 0.06 = 60$).

**Result 4.3.** Under the stated assumptions, one minute of anchored tracking accumulates $6.0 \times 10^{-2}$ m of random-walk drift but $3.6$ m of drift if a constant bias is present. The operational conclusion is that bias elimination, not variance reduction, is the binding requirement on the tracking channel of the verification rig: a bias of even $10^{-3}$ m per frame destroys room-scale co-registration within a minute, while the same variance is tolerable.

### 4.4 Composition of the gate

Combining Results 4.1–4.3: a candidate formalism is admissible if (i) its predicted observable's relative one-sigma scale falls in $[2.1233 \times 10^{-3},\ 4.2465 \times 10^{-3}]$; (ii) its pipeline's stage errors, composed by the RSS rule with independence demonstrated or conservatively replaced by the linear rule, remain within that band; and (iii) its embodied readout channel's bias-corrected drift stays below the co-registration tolerance set by the depth-matching calibration [8], with the $6.0 \times 10^{-2}$ m figure of Result 4.3 as the illustrative one-minute budget. The gate is a conjunction; failing any limb refutes admissibility of the candidate as stated.

## 5. Results

This paper reports no empirical measurements. Its results are the derived quantities of Section 4, restated with their status:

1. **Fano-gate band (derived, from the cited NEXT target [5] plus the stated Gaussian assumption).** $\sigma_E/Q_{\beta\beta} \in [2.1233 \times 10^{-3},\ 4.2465 \times 10^{-3}]$. Status: arithmetic conversion of a cited design target; the target itself is an anticipation stated in [5], not a measurement.

2. **Error-composition example (derived, under stated assumptions $n=5$, $\varepsilon=10^{-2}$).** Worst-case stack $5 \times 10^{-2}$; RSS stack $2.2361 \times 10^{-2}$; ratio $\sqrt{5} = 2.2361$. Status: exact arithmetic under the stated independence assumption; the stage count and per-stage error are this paper's modelling assumptions, with $n=5$ motivated by the five effect families of [3].

3. **Tracking drift bound (derived, under stated assumptions $\varepsilon_f = 10^{-3}$ m, $f = 60$ Hz, $T = 60$ s).** Random-walk drift $\delta_{\mathrm{drift}} = 6.0 \times 10^{-2}$ m; linear (biased) drift $\delta_{\mathrm{lin}} = 3.6$ m; ratio $60$. Status: exact arithmetic under the stated assumptions; the input values are illustrative and are not measurements from any cited work.

4. **Projection: admissibility discrimination power.** Under the assumptions of Results 1–3, the gate distinguishes candidate pipelines whose composed error differs by more than the band width. The band width is $4.2465 \times 10^{-3} - 2.1233 \times 10^{-3} = 2.1232 \times 10^{-3}$ in relative one-sigma terms. A pipeline whose RSS-composed error exceeds $4.2465 \times 10^{-3}$ is rejected; one below $2.1233 \times 10^{-3}$ is admitted at the strict end. This is a projection conditional on the Gaussian-width and independence assumptions; it is not a claim about any existing system.

No number in this section is an empirical finding, and none should be cited as one.

## 6. Discussion

The central claim of this paper is that the post-particle programme can be converted from a philosophical position into a numerical admissibility gate, and that the gate's inputs can be inherited from existing precision-measurement practice and embodied-interaction engineering. We now argue against ourselves.

**The inheritance problem.** The Fano-gate band is only as authoritative as the target it inherits. The NEXT entry states 0.5–1% FWHM at $Q_{\beta\beta,{}^{136}\mathrm{Xe}}$ as a Phase I *anticipation* [5], not as a achieved resolution. If the anticipation was optimistic, the gate inherits the optimism. Worse, the gate assumes the resolution figure behaves as a Gaussian width for budget composition; if the underlying resolution mechanism is non-Gaussian (the Fano factor itself is a statement about discrete charge statistics, and the entry's "nearing the Fano factor" language signals exactly that the limit is not instrumental Gaussian noise), the FWHM-to-sigma conversion of Section 4.1 is a category error. The honest reading is that Result 4.1 defines a *convention*, not a law: a convention this paper fixes and documents, but one a critic could reject wholesale.

**The independence problem.** Result 4.2 shows the composed error differs by $\sqrt{5} \approx 2.2361$ between the linear and RSS rules. The RSS rule requires independent, zero-mean stage errors; in a real rig, calibration channels share sensors, clocks, and software stacks, so independence is an idealisation. The five-stage count itself is borrowed as a motif from the five effects of [3], which studied locomotion responses, not error propagation; using it as a stage count is a rhetorical convenience, and a different stage count changes the numbers as $\sqrt{n}$. For $n = 10$ at the same $\varepsilon$, the RSS stack would be $10^{-2}\sqrt{10} = 3.1623 \times 10^{-2}$ and the linear stack $10^{-1}$ — the discrimination conclusion survives, but every figure moves.

**The illustrative-input problem.** The drift bound of Result 4.3 uses $\varepsilon_f = 10^{-3}$ m, $f = 60$ Hz, $T = 60$ s, none of which is measured here or stated in the cited summaries. The qualitative conclusion — bias dominates variance for anchored tracking — is robust to the exact values (the linear-to-random-walk ratio is always $\sqrt{N}$), but the specific $6.0 \times 10^{-2}$ m figure is only as good as the assumed millimetre-scale per-frame error.

**What would falsify the main result.** The main result is the claim that a single numerical gate can adjudicate candidate post-particle formalisms. This claim is falsified if any of the following holds: (i) a candidate formalism is demonstrably productive — makes correct, novel, reproducible predictions — while violating the gate, showing the gate rejects valid paradigms (a false-negative counterexample); (ii) two formalisms both pass the gate while making incompatible predictions, showing the gate fails to discriminate (a false-positive pair); or (iii) the inherited band is shown to be convention-dependent in a way that changes accept/reject decisions, i.e., that some admissible candidate passes under one FWHM-to-sigma convention and fails under another. Observation (i) is the sharpest refutation and is fully checkable by the Falsification Pledge standard adopted from [12].

**Limitations list.** The result rests on the following assumptions, with sensitivity: (1) the NEXT 0.5–1% FWHM figure is an appropriate inherited standard — the gate moves proportionally if the standard changes, since the band scales linearly with the FWHM input; (2) Gaussian width behaviour — if violated, the $2.354820$ conversion constant is wrong and the band shifts by up to a factor of $2.354820$; (3) stage independence — violation moves the composed error from $2.2361 \times 10^{-2}$ toward $5 \times 10^{-2}$ in the worked example, a factor of $2.2361$; (4) the stage count $n=5$ — the RSS stack scales as $\sqrt{n}$; (5) the illustrative tracking inputs — the drift figure scales linearly in $\varepsilon_f$ and as $\sqrt{T}$ at fixed frame rate; (6) no empirical validation — every number here is arithmetic on stated assumptions, and the gate has never been applied to a real candidate formalism; (7) bibliography truncation — several cited summaries ([1], [3], [6], [7], [8]) are truncated before their results, so this paper draws no outcome claims from them and its protocol mapping rests on problem statements rather than demonstrated performance.

**Open questions.** What is the correct stage decomposition of a real candidate pipeline? Does the Fano-factor