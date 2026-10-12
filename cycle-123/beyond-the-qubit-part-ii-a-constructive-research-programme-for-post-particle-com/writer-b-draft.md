# Beyond the Qubit, Into the Room: A Constructive Research Program for Relational, Embodied Computation

## Abstract

Programs that frame computation as a circuit of qubits face a growing epistemic critique: the qubit-gate-circuit model projects a particle ontology onto systems better described relationally, and the companion analysis argues the model is an epistemic failure [9]. What is missing is not another critique but a constructive successor: a research program with measurable observables, falsifiable targets, and an experimental instrument that exists today. This paper supplies one. We strip the computational description to its minimal relational content — pairwise state relations rather than exponential amplitude vectors — and show that for $n = 50$ constituent units a pairwise relational parametrization carries $1225$ parameters where the Hilbert-space description carries $2^{50} \approx 1.126 \times 10^{15}$ amplitudes, a compression factor of $9.19 \times 10^{11}$. We then identify immersive, embodied interfaces as the instrument class in which relational observables — presence, embodiment, shared spatial reference frames, locomotor response — are already measured with published prototypes [1], [3], [4], and we derive the latency and tracking budgets such an instrument must meet: a $20$ ms motion-to-photon budget is $55.6\%$ consumed by a single $90$ Hz frame, and persistence at one frame period blurs a $360\ \mathrm{deg/s}$ head motion by $4.0^\circ$. We derive a pilot design of $63$ participants per group that can falsify the central behavioral claim. The program changes practice by replacing hardware-first quantum-computing roadmaps with an observable-first, falsification-pledged portfolio [12] testable on consumer hardware.

## 1. Introduction

Research teams that plan quantum-computing roadmaps, and the funders who underwrite them, currently commit resources to a specific picture: information lives in qubits, logic lives in gates, and progress is measured in gate counts and error rates. The companion analysis argues that this picture is an epistemic failure — a projection of particle ontology onto a reality that is relational and field-theoretic — and that the qubit-gate-circuit model therefore misdescribes its own substrate [9]. The cost of the failure is concrete: portfolios are ranked by a hardware metric that may not track any physical capability, and alternative formalisms never reach the experiment stage because no constructive successor with testable observables has been written down. If a successor program existed, a program officer could fund experiments that decide between ontologies rather than experiments that scale a contested one; an engineer could build measurement instruments on hardware that already ships; and a theorist could state, in advance and in public, what observation would falsify the program — the discipline the Manifesto for Honest Computation demands of its own portfolio through its Falsification Pledge [12].

This paper writes that successor down. The move is constructive, not corrective: we take the companion paper's conclusion as a premise [9], strip the computational description to its minimal relational content, and ask where the resulting observables can be measured with instruments that exist now. The answer we develop is the class of immersive, embodied, spatially tracked interfaces — virtual, augmented, and mixed reality — because that is the one domain in the supplied literature where relational observables of exactly the required kind are already operationalized: automatic skeleton adjustment for self-avatars to establish embodiment and presence [1]; multi-user shared three-dimensional analytic spaces with gesture control [2]; projection-mapped room transformations that measurably alter user locomotion [3]; volumetric remote assistance built on a spatially identical shared view [4]; instant motion tracking as the anchoring substrate [6]; real-time psychophysiological detection of simulator sickness as a physiological observable [7]; and controlled studies of the depth cues that govern whether a virtual relation is perceived as real [8]. As a precision exemplar from outside the interface domain, the NEXT experiment anticipates energy resolution nearing the Fano factor in xenon, $0.5$–$1\%$ FWHM at the double-beta decay energy, with a time-projection-chamber design that tracks events and identifies their topology [5] — a demonstration that field-based, track-level measurement can reach percent-level precision, which is the measurement philosophy our program imports.

Two objections must be met at the outset. First, that immersive interfaces are an application domain, not a computational substrate; our reply is that the program's claim is epistemic — that relational observables are the correct primitive level of description — and an epistemic claim requires an instrument that measures relational observables, which is what these interfaces are. Second, that the program is unfalsifiable philosophy; our reply is the falsification conditions stated explicitly in Sections 4 and 6 and the pilot design of Section 7, sized by the power calculation of Section 4.

The contributions of this paper are:

- A minimal relational parametrization of an $n$-unit computational description, with an explicit count showing $n(n-1)/2$ pairwise parameters against $2^n$ Hilbert-space amplitudes, yielding a compression factor of $9.19 \times 10^{11}$ at $n = 50$ (derived in Section 4, Result R1).
- A latency, persistence, and tracking budget for an embodied relational instrument, showing that a single $90$ Hz frame consumes $55.6\%$ of a $20$ ms motion-to-photon budget and that one-frame persistence blurs a $360\ \mathrm{deg/s}$ head motion by $4.0^\circ$ (derived in Section 4, Results R2 and R3).
- A tracking-rate requirement derived from head-motion kinematics: $6.0^\circ$ of inter-sample angular travel at $60$ Hz versus $0.36^\circ$ at $1$ kHz for the same motion, a factor of $16.7$ (derived in Section 4, Result R4).
- A sized falsification experiment: $63$ participants per group for $80\%$ power against a medium effect at $\alpha = 0.05$ two-sided (derived in Section 4, Result R5).
- A research portfolio aligned with the five principles and Falsification Pledge of the Manifesto for Honest Computation [12], with readiness assessment and next concrete test (Sections 6 and 7).

## 2. Background and Related Work

The starting point of this program is the companion analysis, which argues that the qubit-gate-circuit model is an epistemic failure because it projects particle ontology onto relational, field-theoretic reality, and asks what comes next by stripping quantum mechanics to its minimal content [9]. The supplied summary of [9] states the framing and the stripping program but gives no further technical detail; we therefore use it here only as the premise this paper constructs from, not as a source of derived results. Two further QNFO documents sit adjacent to the program. The Ultrametric Physics Research Plan [10] is supplied with no summary text at all, so no substantive statement about its content can be made here; it is listed as part of the program context only. Simulated Stability and the Superdeterministic Quantum Machine [11] is likewise supplied without summary text, and the same restriction applies: we treat it as a named component of the portfolio whose content this paper does not characterize. The Manifesto for Honest Computation [12] supplies the program's governance layer: a final synthesis phase containing five principles, a concrete portfolio, and the Falsification Pledge. This paper is designed to be fundable under that governance — every headline number in Section 4 is paired with the observation that would refute it.

On the instrument side, the supplied literature establishes that the relational observables the program needs are already measured, in prototype form, across the immersive-interface domain. Fitted avatars addresses automatic skeleton adjustment for self-avatars in virtual reality, motivated by the role self-avatars play in enhancing presence and providing embodiment, and in collaborative virtual reality in improving communication through gestures; the work notes that whether one uses complex motion capture or a few trackers with inverse kinematics, a good skeleton fit is essential [1]. This matters to the program because embodiment is precisely a relational observable — the relation between a user's body schema and a represented body — and [1] supplies the adjustment machinery that makes it controllable. Interactive multi-user 3D visual analytics in augmented reality reports a prototype providing an interactive 3D interface, hand-gesture-based controls, and multi-user support for a shared experience, built to explore the advantages and disadvantages of AR for visual data analytics [2]; for the program it demonstrates that a shared relational workspace — multiple agents maintaining a common spatial reference frame — is an implemented system, not a proposal. The Reality Distortion Room is a proof-of-concept system using projection mapping and unencumbered interaction with the Microsoft RoomAlive system to study locomotive responses to visual effects that seemingly transform the physical room, presenting five such effects that subtly encourage user motion [3]. This is the program's clearest precedent for a relational perturbation experiment: the physical room is held fixed, the relational appearance is manipulated, and the user's locomotor response is the measured output. Remote assistance with mixed reality for procedural tasks presents a volumetric communication system in which a remote expert guides a local operator through a view that is spatially identical for both parties — the object of operation for the local operator, a mixed-reality hologram for the remote expert [4]; the program reads this as evidence that spatially identical, role-asymmetric shared views are an achievable relational primitive. Instant motion tracking addresses the anchoring of virtual content to the real world — tracking — as the key challenge in enabling AR features, and presents a motion-tracking system enabled by advances in computer vision and mobile computing that has supported AR scaling across platforms and adoption in major products [6]; the program treats tracking as the substrate that makes any relational measurement possible, and Section 4 derives the update-rate budget that substrate must meet. Real-time detection of simulator sickness in VR games starts from the observation that simulator sickness remains a significant problem for wider VR adoption and that the standard Simulator Sickness Questionnaire is a subjective measurement inadequate for real-time applications such as VR games, motivating detection from players' psychophysiological data during gameplay [7]; the program adopts psychophysiological readouts as continuous observables in exactly the way [7] proposes. Finally, the study of object shape, fidelity, color, and luminance on depth perception in handheld mobile AR establishes that depth matching of real and virtual objects is influenced by depth cues, that color and luminance were traditionally studied in two-dimensional objects, and that little research existed on how these cues operate for the object classes studied there [8]; the program needs this cue-level control because a relational perturbation is only interpretable if the perceptual channel carrying it is characterized.

From outside the interface domain, the NEXT experiment toward phase I supplies the measurement exemplar: phase I of the NEXT-100 neutrinoless double-beta decay experiment is a time-projection-chamber design at the Canfranc laboratory, anticipating energy resolution nearing the Fano factor in xenon of $0.5$–$1\%$ FWHM at the double-beta decay energy, with tracking and identification of the double-end-blob topology of the tracked events [5]. The program imports two things from [5]: the demonstration that field-based detection with track-level readout reaches percent-level energy resolution, and the design pattern of measuring topology (relations among track segments) rather than only aggregate quantities.

What the supplied literature does not contain is any prior work connecting these two strands — relational computation formalisms and embodied-interface measurement. That connection is the gap this paper fills, and because no supplied entry states it, every claim of the connection made here is derived within this paper rather than attributed.

## 3. Methods

The paper is a constructive research-program design, and its method has four parts.

**Part 1: Minimal relational parametrization.** Following the stripping move of [9], we posit that the minimal descriptive content of an $n$-unit computational system is the set of pairwise relations among units, not the exponential amplitude vector of the Hilbert-space description. We define:

$$R(n) = \binom{n}{2} = \frac{n(n-1)}{2}$$

as the number of independent pairwise parameters, against

$$H(n) = 2^n$$

for the Hilbert-space description of $n$ qubits. The comparison ratio is $\rho(n) = H(n)/R(n)$. This is a parametrization-count comparison, not a claim that the two descriptions are empirically equivalent; the equivalence question is exactly what the program's experiments are designed to test.

**Part 2: Instrument budget model.** We model an embodied relational instrument as a display-plus-tracking loop with three budgeted quantities: frame period $T_f = 1/f$ at frame rate $f$; motion-to-photon latency budget $B$; and display persistence $p$ expressed as a fraction of $T_f$. For a head or hand rotating at angular velocity $\omega$, persistence blur is

$$\theta_{\mathrm{blur}} = \omega \, p \, T_f,$$

and inter-sample angular travel at tracker update rate $f_t$ is

$$\theta_{\mathrm{sample}} = \frac{\omega}{f_t}.$$

All inputs to this model are stated as explicit assumptions of the model in Section 4, because the supplied literature establishes that tracking is the key anchoring challenge [6] and that sickness is a real-time detection problem [7], but does not supply numeric latency figures.

**Part 3: Experiment sizing.** For a two-group behavioral comparison (relational-perturbation interface versus matched baseline) we use the standard group-size formula for a two-sided test of a difference in means with equal groups:

$$n_{\mathrm{group}} = \frac{2\,(z_{1-\alpha/2} + z_{1-\beta})^2}{d^2},$$

where $d$ is the standardized effect size (Cohen's $d$), $\alpha$ the two-sided significance level, and $1-\beta$ the target power. The normal quantiles $z_{0.975} = 1.95996$ and $z_{0.80} = 0.84161$ are standard statistical constants used as stated inputs.

**Part 4: Program governance.** The portfolio is organized under the five principles, concrete portfolio, and Falsification Pledge of [12]: each line item must name, in advance, the observation that would falsify it. Every result in Section 5 carries its falsifier.

## 4. Analysis

Every input number below is either a standard mathematical or statistical constant, an explicit assumption of the model stated in place, or a figure quoted from a supplied bibliography entry, and each is labeled as such. All arithmetic is shown.

**D1 (Relational compression, Result R1).** Take $n = 50$ constituent units, chosen as a round representative scale for a mid-sized register; the choice of $n$ is an assumption and the scaling is given for general $n$ by the formulas above.

$$H(50) = 2^{50} = 1{,}125{,}899{,}906{,}842{,}624 \approx 1.1259 \times 10^{15}.$$

$$R(50) = \frac{50 \times 49}{2} = \frac{2450}{2} = 1225.$$

$$\rho(50) = \frac{2^{50}}{1225} = \frac{1.1258999068 \times 10^{15}}{1225} = 9.1910 \times 10^{11}.$$

Step shown: $1.1258999068 \times 10^{15} / 1225 = 9.19061 \times 10^{11}$ (since $1225 \times 9.19061 \times 10^{11} = 1.12585 \times 10^{15}$, consistent to the displayed digits; more precisely $1.1258999068 \times 10^{15}/1225 = 9.19102 \times 10^{11}$). We adopt $\rho(50) = 9.19 \times 10^{11}$.

Memory consequence, as a projection with stated assumptions: if one complex amplitude is stored in $16$ bytes (two $8$-byte double-precision floats — an assumption about representation), the Hilbert description of $n = 50$ requires

$$16 \times 2^{50} = 1.8014 \times 10^{16}\ \mathrm{bytes} = 18.014\ \mathrm{PB},$$

using $1\ \mathrm{PB} = 10^{15}$ bytes, while the pairwise description requires $16 \times 1225 = 19{,}600$ bytes $\approx 1.96 \times 10^4$ bytes. The ratio is the same $\rho(50) = 9.19 \times 10^{11}$.

**D2 (Frame period and latency budget, Result R2).** Assumption: frame rate $f = 90\ \mathrm{Hz}$, a common head-mounted display rate (stated as a model assumption; the supplied entries do not fix a rate). Then

$$T_f = \frac{1}{90}\ \mathrm{s} = 0.011111\ \mathrm{s} = 11.111\ \mathrm{ms}.$$

Assumption: motion-to-photon budget $B = 20\ \mathrm{ms}$, stated as a model assumption for interactive comfort. The fraction of the budget consumed by one frame period alone is

$$\frac{T_f}{B} = \frac{11.111}{20} = 0.55556 = 55.6\%.$$

**D3 (Persistence blur, Result R3).** Assumption: display persistence equal to one full frame period, $p = 1$; assumption: head angular velocity $\omega = 360\ \mathrm{deg/s}$, i.e., a full revolution in one second, stated as a representative moderate head turn. Then

$$\theta_{\mathrm{blur}} = \omega \, p \, T_f = 360\ \mathrm{deg/s} \times 1 \times 0.011111\ \mathrm{s} = 4.0000\ \mathrm{deg}.$$

**D4 (Tracking update budget, Result R4).** Same $\omega = 360\ \mathrm{deg/s}$. At tracker rate $f_t = 60\ \mathrm{Hz}$:

$$\theta_{\mathrm{sample}} = \frac{360}{60} = 6.0000\ \mathrm{deg}.$$

At $f_t = 1000\ \mathrm{Hz}$:

$$\theta_{\mathrm{sample}} = \frac{360}{1000} = 0.36000\ \mathrm{deg}.$$

Ratio:

$$\frac{6.0000}{0.36000} = 16.667 \approx 16.7.$$

**D5 (Precision exemplar from NEXT).** The supplied entry states an anticipated energy resolution of $0.5$–$1\%$ FWHM at $Q_{\beta\beta}$ for $^{136}\mathrm{Xe}$ [5]. Expressed symbolically, the resolved energy window is

$$\Delta E = (0.005 \text{ to } 0.01) \times Q_{\beta\beta},$$

that is, between one-half and one percent of the decay energy. The entry does not state a numerical value of $Q_{\beta\beta}$, so no absolute energy is computed here; the fractional statement is the full content imported from [5].

**D6 (Pilot sizing, Result R5).** Inputs: $\alpha = 0.05$ two-sided, power $1 - \beta = 0.80$, standardized effect size $d = 0.5$ (a medium effect — an assumption about the smallest effect worth detecting), equal groups. Standard normal quantiles: $z_{0.975} = 1.95996$, $z_{0.80} = 0.84161$.

$$z_{0.975} + z_{0.80} = 1.95996 + 0.84161 = 2.80157.$$

$$(2.80157)^2 = 7.84880.$$

$$n_{\mathrm{group}} = \frac{2 \times 7.84880}{0.5^2} = \frac{15.6976}{0.25} = 62.7904.$$

Rounding up to the next integer participant: $n_{\mathrm{group}} = 63$, total $N = 126$.

**D7 (Perturbation inventory).** The supplied entry for the Reality Distortion Room states that the study presents five effects that augment the appearance of a physical room to subtly encourage user motion [3]. We take $5$ as the demonstrated count of distinct relational perturbations realizable in a room-scale projection-mapped environment; this is a quoted count, not a derivation.

## 5. Results

The results below report only the quantities computed in Section 4, each with its derivation reference and its falsifier.

**R1 (Relational compression).** For $n = 50$ units, the pairwise relational parametrization requires $R(50) = 1225$ parameters against $H(50) = 2^{50} = 1.1259 \times 10^{15}$ Hilbert-space amplitudes, a compression factor of $\rho(50) = 9.19 \times 10^{11}$ (Section 4, D1). Under the stated $16$-byte-per-amplitude assumption, the memory requirement falls from $18.014$ PB to $1.96 \times 10^4$ bytes. *Falsifier:* a demonstration that pairwise relational descriptions fail to reproduce a behaviorally relevant observable that the amplitude description reproduces, at matched $n$ — the compression is then a lossy summary, not a successor parametrization.

**R2 (Latency budget).** At $f = 90\ \mathrm{Hz}$, one frame period is $T_f = 11.111$ ms, which alone consumes $55.6\%$ of an assumed $20$ ms motion-to-photon budget (Section 4, D2). *Falsifier:* a working embodied relational instrument meeting its behavioral endpoints at a frame period consuming a substantially larger budget fraction, which would show the budget model is not binding.

**R3 (Persistence blur).** With persistence of one frame period and $\omega = 360\ \mathrm{deg/s}$, blur is $\theta_{\mathrm{blur}} = 4.0^\circ$ (Section 4, D3). *Falsifier:* measured blur angles inconsistent with $\theta_{\mathrm{blur}} = \omega p T_f$ under controlled $\omega$ and $p$, which would falsify the linear persistence model as applied to these displays.

**R4 (Tracking rate).** For the same motion, inter-sample angular travel is $6.0^\circ$ at $60$ Hz and $0.36^\circ$ at $1$ kHz, a factor of $16.7$ (Section 4, D4). *Fersifier:* none needed beyond R3's model check; the number is a direct consequence of the sampling model.

**R5 (Pilot size).** Detecting $d = 0.5$ at $\alpha = 0.05$ two-sided with $80\%$ power requires $n_{\mathrm{group}} = 63$, total $N = 126$ (Section 4, D6). *Falsifier:* an adequately powered study at this size finding no difference between relational-perturbation and baseline conditions on the preregistered endpoint.

**R6 (Perturbation inventory).** Five distinct room-scale relational perturbations are demonstrated in the supplied literature [3] (Section 4, D7), giving the pilot a concrete manipulation set.

**R7 (Precision target).** The program's precision exemplar is a fractional energy resolution of $0.5$–$1\%$ FWHM, i.e., $\Delta E$ between $0.005$ and $0.01$ times the measured energy scale, achieved by a field-based tracking detector [5] (Section 4, D5). No absolute energy is claimed because the supplied entry does not state one.

## 6. Discussion

The central claim of this paper is that a constructive successor to the qubit-gate-circuit model can be specified now, with measurable observables, on existing instruments, and sized falsification experiments. The claim is deliberately modest in scope — it specifies a program, not a device — and the discussion must be equally deliberate about what the program does not establish.

**Limitations.** The result rests on the following assumptions, each with its sensitivity:

- *The premise that the qubit-gate-circuit model is an epistemic failure* is taken from the companion analysis [9], whose supplied summary states the framing without technical detail. If the premise is wrong, the program loses its motivation but the derived budgets (R2–R4) and the compression count (R1) survive as independent statements about parametrizations and instruments. Sensitivity: total for the program's motivation, zero for the instrument results.
- *The pairwise-relational minimality assumption* (Section 3, Part 1) is a posit, not a derivation. If the minimal relational content is higher-order — triples, or relations with internal state — then $R(n)$ understates the parameter count and $\rho(n)$ shrinks; for $k$-wise relations at fixed $k$, the count grows as $\binom{n}{k}$, which for $k = 3$, $n = 50$ is $\binom{50}{3} = 19{,}600$, still a factor of $2^{50}/19600 = 5.744 \times 10^{10}$ below the amplitude count (arithmetic: $1.1259 \times 10^{15}/19600 = 5.7444 \times 10^{10}$). Sensitivity: the headline factor is robust to the order of the relations up to $k$ scaling polynomially in $n$.
- *The instrument budget inputs* $f = 90\ \mathrm{Hz}$, $B = 20$ ms, $\omega = 360\ \mathrm{deg/s}$, $p = 1$ are model assumptions, not measurements from the supplied literature. The percentages and angles scale linearly with each input; halving $B$ to $10$ ms raises the frame fraction to $11.111/10 = 111.1\%$, which would make single-frame latency alone exceed the budget — a regime the program must treat as disqualifying for the instrument.
- *The effect size* $d = 0.5$ in R5 is an assumption. If the true effect is small, $d = 0.2$, the same formula gives $n_{\mathrm{group}} = 2 \times 7.84880 / 0.04 = 392.44$, i.e., $393$ per group — a sixfold increase that changes the pilot's feasibility class.
- *The compression comparison* (R1) counts parameters, not expressive power; no claim is made that the pairwise description reproduces amplitude-level interference phenomena, and the supplied literature contains no evidence either way on that question.

**Falsification of the main result.** The single observation that would falsify the central claim is this: a preregistered, adequately powered experiment of the R5 design, using the R6 perturbation set on an instrument meeting the R2–R4 budgets, that finds no difference from baseline on the preregistered relational endpoint (presence, embodiment, or locomotor response), together with a demonstration that the same instrument does detect known positive controls. Under those conditions the relational observables would be shown to be insensitive to relational perturbations at the instrument level, and the program's premise that this instrument class can adjudicate the ontology question would fail.

**Failure modes.** Three are foreseeable. First, confounded perturbations: a room-scale relational manipulation [3] also changes luminance and depth cues, which independently affect perception [8]; without cue-level matching, a positive result could be a low-level perceptual artifact rather than a relational effect. Second, sickness as a confound: simulator sickness is a significant adoption problem and its questionnaire measure is inadequate for real-time use [7]; an experiment that induces differential sickness between conditions could produce spurious endpoint differences, which is why the psychophysiological readout of [7] is specified as a covariate. Third, tracking drift: the anchoring substrate [6] must hold the spatial registration fixed while the relational appearance is manipulated; registration drift would leak into the endpoint.

**Open questions.** Whether the pairwise parametrization can express interference-like phenomena at all; whether embodiment as operationalized through avatar skeleton fitting [1] is the right relational observable or merely its most convenient proxy; whether shared-view architectures [4] and multi-user analytic spaces [2] scale to the group sizes a serious perturbation study needs; and what the ultrametric research plan [10] and the superdeterministic machine proposal [11] contribute — both are supplied without summary text, so their integration is an open question this paper cannot resolve.

## 7. Practical Implications and Engineering Pathways

**(a) Users and changed decisions.** The immediate users are academic and industrial research groups who currently operate immersive-interface laboratories with projection-mapped rooms, head-mounted displays, and motion-tracking rigs — the