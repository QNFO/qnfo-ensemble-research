# Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout

## Abstract

Is the qubit a pre-existing object that control pulses and readout merely probe, or a two-level subsystem constituted by the very operations that define it? Existing critiques of qubit ontology assert the circularity of control and readout but do not state when that circularity is harmless and when it hides genuine ontological underdetermination. We formalize the question as a self-referential calibration problem: an ontology map $\Phi$ assigns Hilbert-space identifications to operational data, and calibration seeks a fixed point of the composite loop $T = \Gamma \circ \Phi$, in which states are defined by measurements that are themselves defined by states. When $T$ is a contraction with Lipschitz constant $L < 1$, Banach's fixed-point theorem guarantees a unique self-consistent identification and the circularity is benign, as in ordinary instrument calibration; when the loop admits multiple fixed points or a continuous equivariant symmetry, physically inequivalent ontologies—an energy eigenmode, a field excitation, a collective variable—remain compatible with identical operational data. We exhibit an explicit two-branch toy model in which the final ontology is fixed by the initial guess rather than by the data. Adopting a working single-shot readout fidelity $F = 0.99991$, we compute the shot budget for ontology discrimination: $N \approx 2.65 \times 10^{6}$ shots for a discrepancy $\delta = 10^{-3}$ at $1\%$ failure probability. Uniqueness is thus a property of the calibration dynamics, not of the qubit, and we state falsifiable conditions for both outcomes.

## 1. Introduction

Quantum computing hardware is calibrated, characterized, and operated through a loop that has no outside. To implement a control pulse on a qubit, an engineer needs a model of the qubit: its transition frequency, its drive coupling, its relaxation channels. To validate that model, the engineer runs tomography or gate-set characterization; but tomography is defined by a measurement apparatus whose own calibration presupposes a model of the states being measured. States are defined by measurements, and measurements are defined by states. Every working quantum computing team—superconducting-circuit groups tuning transmon readout chains, trapped-ion groups optimizing state-dependent fluorescence, spin-qubit groups calibrating charge sensors—faces this loop daily, and the field's standard practice is to treat it as a nuisance that more calibration data will dissolve. What is at stake is more than nuisance: if the loop can converge to different, physically inequivalent identifications of the controlled entity on different platforms or from different starting points, then statements such as "the gate acted on the $|0\rangle$–$|1\rangle$ energy eigenmode" are conventions rather than findings, and cross-platform comparisons, benchmarking claims, and error budgets inherit an unexamined ambiguity. If instead the loop is provably contractive with a unique fixed point, the ambiguity dissolves and the qubit's operational identity is well defined. Which of these holds determines whether "what is actually manipulated" is answerable in principle or only operationally.

We call this situation **operational circularity** and study when it is benign. Two regimes must be distinguished:

1. **Benign circularity (calibration self-consistency).** The loop converges to a unique operational identification: a single assignment of Hamiltonian parameters, readout observables, and error channels that is stable under further calibration. This is the regime of ordinary instrument calibration, and it is formally a contraction fixed-point iteration.

2. **Ontological underdetermination.** Multiple, physically inequivalent identifications of the controlled entity—"the qubit is an energy eigenmode," "the qubit is a localized field excitation," "the qubit is a collective variable of many degrees of freedom"—are each exactly self-consistent with the same operational data. In this regime, no amount of calibration *inside the loop* distinguishes them.

The physical critique underlying this question has been developed in the QNFO corpus. [9] explains what control pulses actually manipulate and what readout measures across superconducting transmon, trapped-ion, and spin-qubit platforms, and includes a formalization of self-referential metrology; [10] asks what minimal ontological commitments survive the critique of the qubit-as-particle picture; [11] proposes an operational measure, semantic fidelity, for when borrowed quantum vocabulary becomes decision-relevantly misleading. The present paper sharpens the formal core of that program into a definite mathematical question with computable answers.

Our contribution is fourfold:

- We define the calibration fixed-point problem—an ontology map $\Phi$, a realization map $\Gamma$, and the composite loop $T = \Gamma \circ \Phi$—and state the contraction condition under which the fixed point is unique (Section 3, Proposition 1).
- We exhibit an explicit two-branch toy model in which two physically inequivalent ontologies are both exact fixed points and the final ontology is selected by the initial guess, with all arithmetic shown (Section 4.4).
- We derive, from an explicitly labeled working fidelity input, the shot budget $N = 2.649159 \times 10^{6}$ shots needed to resolve an ontology-discriminating discrepancy $\delta = 10^{-3}$ at failure probability $\alpha = 0.01$, and the statistical floor and symmetry-sensitivity scales that govern any such test (Section 4, Derivations 4.1–4.5).
- We state falsifiable conditions for both regimes and translate the formalism into a concrete experimental proposal and engineering pathway (Sections 6 and 7).

## 2. Background and Related Work

The relevant literature falls into two groups: formal ontology engineering, which supplies the vocabulary of "ontology" we adapt, and the QNFO corpus, which supplies the physical critique.

**Ontology as a formal artifact.** The Gene Ontology project is described in [1] as the largest resource for cataloguing gene function, combining solid conceptual underpinnings with practical features that have made it a widely adopted and essential resource for data analysis, and the work provides a concise primer introducing the structure of the ontology. We borrow from this tradition the idea that an ontology is an explicit, structured assignment of entities and relations—not a metaphysical thesis but a representational commitment. Our "ontology map" $\Phi$ (Section 3) is exactly such a commitment, applied to Hilbert-space identifications rather than gene functions.

Crucially, ontologies can be used without understanding their construction, and this is a double-edged property. [2] states that the Gene Ontology is sufficiently simple that it can be used without deep understanding of its structure or how it is developed, which is both a strength and a weakness, and discusses common misinterpretations of the ontology and their remedies. This is precisely the failure mode we attribute to qubit ontology: the two-level abstraction is usable without knowing what it commits us to, and the misuse is invisible until the abstraction is pushed beyond its calibration domain.

Ontologies are not static. [4] analyzes how mappings between popular life-science ontologies change, evaluating ontology and mapping evolution across three domains (Anatomy, Molecular Biology, Chemistry) and finding that Molecular Biology and Chemistry undergo heavy extensions and revisions while Anatomy is relatively stable; the same work finds that mappings produced by the structural matcher Context are rather unstable whereas mappings based on the Name matcher are relatively stable, and proposes two prediction methods for estimating future correspondence additions and deletions. This supports our dynamic treatment: the ontology identification of a qubit is not fixed once but is the output of an evolving calibration process, and the stability of that process—by analogy, the stability of the structural matcher rather than the name matcher—is the object of study.

Ontology matching—the problem of finding correspondences between entities in different ontologies so that they can be aligned or merged—is addressed by [3], which presents GraphMatcher, an ontology matching system using a graph attention approach with a new neighbourhood aggregation method, developed in Python with PyTorch and Ontospy and evaluated in the OAEI 2022 conference track. Its reported results include F1-measures between 0.39 and 0.71 across the M1–M3 evaluation variants, better performance in the M1 and M3 variants than in M2, and the highest F1-measure (72% in both) on uncertain reference alignments among the matchers evaluated in that track. Our multi-platform question—does calibration on a transmon, an ion, and a spin qubit converge to the *same* identification?—is structurally an ontology-matching problem: we ask whether the operational ontologies of different platforms admit a common alignment or only a family of partial correspondences, and the moderate, variant-dependent matching scores of [3] are a reminder that alignment success is neither automatic nor uniform.

That ontologies can be built for domains far from biology is shown by [6], which presents the Magnetic Materials Ontology (MagMO), developed within the MaMMoS project, motivated by the complex multiscale behaviour of magnetic materials and the coexistence of multiple unit systems that hinder consistent data exchange and interpretation; the work aligns with the Elementary Multiperspective Material Ontology (EMMO) and emphasizes a human-readable, programmatic implementation that supports versioning and FAIR data reuse, with interfaces that store units and unique identifiers so that quantities from different datasets are interpreted unambiguously. The unit-system problem is a direct analogue of ours: the same physical magnet can be described in multiple unit conventions, and the ontology must manage the equivalence rather than pretend only one description exists. Similarly, [5] proposes an ontology-based approach to formally define qualitative conversational features by deriving quantitative definitions from linguistic descriptors; in its Proficiency-Level Control use case, a decision tree classifier is trained to map descriptor values to CEFR levels A1–C2, yielding explicit belonging rules for each class. This is an example of pinning down an entity (a conversational feature) that has no pre-existing sharp definition—exactly the situation of the qubit, whose "two-level system" label is applied to entities as diverse as collective circuit modes and electronic states. Finally, [7] develops an ontological model for business intelligence in which an ontology captures competitor information from web semantics and the relations between the data are mined using a decision tree; it illustrates the general pattern that an ontology can be *derived from data* rather than stipulated—the direction of constitution our fixed-point formalism makes precise.

**The physical critique.** [9] is a pedagogical bridge between the qubit ontology critique and working physics: it explains, platform by platform, what control pulses actually manipulate and what readout measures—for instance, that in a transmon the control pulses couple to the electric dipole of the plasmon mode and the "Bloch sphere rotation" and "mode excitation" pictures are mathematically equivalent, and that readout measures a macroscopic observable correlating with the qubit state through a chain of near-quantum-limited amplifiers. Its summary states that self-referential metrology is genuinely circular but has an anchor, namely multi-level spectroscopy of the bare Hamiltonian as an independent reference for the computational subspace; and its discussion of layering identifies the compounding risk that the gauge freedom at the error-model level compounds with the gauge freedom of gate set tomography and the residual circularity of readout calibration. Our fixed-point formalism is a sharpening of exactly this problem: we ask when the circularity has an anchor in the form of a unique attracting fixed point. [10], the companion paper, argues that diagnosis without prescription is incomplete, strips quantum mechanics to its minimal ontological commitments after removing the classical projections of particle, wave, measurement-as-revelation, and observer, and surveys constructive paradigms for post-particle computation; it also records the motivating puzzle that decades of effort and an estimated \$35 billion of investment have not produced a commercially viable quantum computer under the incumbent paradigm. Our uniqueness/underdetermination dichotomy is a tool for deciding, in a specific and falsifiable way, whether the diagnosis of ontological projection has operational content. [11] proposes the operational quantity semantic fidelity $F_S$, defined as one minus the total variation distance between the decision-relevant outcome distributions implied by two readings of the same term, and derives for the term "photon" a per-element divergence $D_{TV}^{(1)} = 1/2$ at a balanced two-boson beamsplitter, a compounding law $D_{TV}^{(k)} = 1 - 2^{-k}$ across $k$ independent interference elements, and a threshold crossing at $k^{*} = 4$ elements for a stipulated threshold $\varepsilon = 0.9$. Our smallest-detectable-asymmetry scale $\epsilon_{\min}$ (Derivation 4.5) plays the analogous role here: a vocabulary-neutral number that says when an ontological difference becomes operationally visible.

**The prior formulation.** [8] is the prior version of the present manuscript. It formulates the ontology map $\Phi : \mathcal{D} \to \mathcal{O}$ and the composite loop $T = \Gamma \circ \Phi$, reports the contraction-regime convergence count ($n = 14$ rounds for illustrative inputs $L = 0.6$, $d_0 = 1$, $\varepsilon = 10^{-3}$), the two-branch toy model with fixed points $x_A^{*} = 0$ and $x_B^{*} = 1$, and a shot-budget computation, and flags in its own discussion that real calibration loops may have state-dependent Lipschitz constants and that unmodeled drift can violate the contraction condition between rounds. The present paper is a revision of [8]: we retain its formalism and derivations, restate every empirical input as an explicit assumption (the revision removes an unsourced attribution of the readout fidelity figure), and add the practical pathway of Section 7.

## 3. Methods

### 3.1 Operational ontology maps

Let $\mathcal{D}$ be the space of operational data: sequences of control waveforms, their applied settings, and readout records. Let $\mathcal{O}$ be the space of Hilbert-space identifications: assignments of the form "the manipulated degree of freedom is the two-level system spanned by $\{|0\rangle, |1\rangle\}$ with Hamiltonian $H = \frac{\hbar}{2}(\omega_0 \sigma_z + \Omega_x \sigma_x + \Omega_y \sigma_y)$, readout observable $M$, error channels $\{L_k\}$," together with the physical interpretation of each symbol (eigenmode, field excitation, collective variable).

An **ontology map** is a function

$$\Phi : \mathcal{D} \to \mathcal{O},$$

which takes a body of operational data and returns an identification. Calibration is the search for a **self-consistent datum** $x^{*} \in \mathcal{D}$ satisfying

$$x^{*} = \Gamma\big(\Phi(x^{*})\big),$$

where $\Gamma : \mathcal{O} \to \mathcal{D}$ is the **realization map**: given an identification, it produces the operational data that the identified system would generate under the calibrated protocol. A pair $(x^{*}, \Phi(x^{*}))$ satisfying this equation is a **fixed point of the operational loop**.

### 3.2 Benign circularity: the contraction condition

Let $d_{\mathcal{D}}$ be a metric on $\mathcal{D}$ (for example, total-variation distance between predicted readout distributions plus a weighted parameter distance). Define the composite calibration operator

$$T = \Gamma \circ \Phi : \mathcal{D} \to \mathcal{D}.$$

**Proposition 1 (Benign circularity).** If $T$ is a contraction with Lipschitz constant $L < 1$,

$$d_{\mathcal{D}}\big(T(x), T(x')\big) \leq L\, d_{\mathcal{D}}(x, x') \quad \text{for all } x, x' \in \mathcal{D},$$

then by the Banach fixed-point theorem $T$ has a unique fixed point $x^{*}$, and iteration from any initial guess $x_0$ converges to it, with

$$d_{\mathcal{D}}(x_n, x^{*}) \leq L^{n}\, d_{\mathcal{D}}(x_0, x^{*}).$$

Convergence to tolerance $\varepsilon$ requires

$$n \geq \frac{\ln\!\big(\varepsilon / d_{\mathcal{D}}(x_0, x^{*})\big)}{\ln L}.$$

Since $0 < L < 1$, $\ln L < 0$; with $\varepsilon < d_{\mathcal{D}}(x_0, x^{*})$ the numerator is negative and $n$ is positive, as required. In this regime the circularity is benign: the loop defines a unique operational identification regardless of the starting ontology. This is the formal sense in which the anchor discussed in [9]—an independent reference that breaks the circle—can be replaced by a dynamical guarantee: uniqueness of the attracting fixed point plays the same role.

### 3.3 Ontological underdetermination

If $T$ is not globally contractive, uniqueness can fail. The physically interesting failure is not chaos but **multiplicity**: several fixed points, each corresponding to a different physical interpretation of the same symbols. We say the qubit ontology is **underdetermined** on a data set $x^{*}$ if there exist two ontology maps $\Phi_A, \Phi_B$ and realization maps $\Gamma_A, \Gamma_B$ such that

$$x^{*} = \Gamma_A\big(\Phi_A(x^{*})\big) = \Gamma_B\big(\Phi_B(x^{*})\big),$$

with $\Phi_A(x^{*})$ and $\Phi_B(x^{*})$ physically inequivalent (differing in the interpretation of the controlled entity, not merely in parameter values).

A second, continuous route to underdetermination is **equivariance**: if a group $G$ acts on the identification space and $T$ commutes with the action, then $g \cdot x^{*}$ is a fixed point whenever $x^{*}$ is, and no iteration inside the loop selects a member of the orbit. For a qubit, the natural candidate is $SO(3)$ acting on the Bloch-sphere axis labeling; $\dim SO(3) = 3$, so three continuous descriptive parameters (two axis angles plus one basis phase) are invisible to any equivariant operational statistic. This is the compounding concern raised in [9] for layered abstractions: gauge freedoms at successive levels of the stack do not automatically cancel, and here we quantify what it would take to break them.

### 3.4 Discriminating observable and shot budget

To escape the loop, one needs an observable whose expectation differs between candidate ontologies by an amount $\delta$, resolved against readout noise. Given single-shot readout fidelity $F$, the per-shot error probability is $p_e = 1 - F$. By Hoeffding's inequality, estimating a Bernoulli mean to additive accuracy $\delta$ with failure probability $\alpha$ requires

$$N \geq \frac{\ln(2/\alpha)}{2\,\delta^{2}}$$

shots. This gives the minimal experimental budget for any ontology-discriminating test, instantiated in Section 4.3.

## 4. Analysis

All numbers in this section are computed here from stated inputs. The only empirical-style input is a readout fidelity figure carried over from the prior version of this manuscript [8]; because the current reference list contains no experimental source reporting it, we treat it as an explicit working assumption, and every number derived from it is labeled a projection.

**Input 1 (working assumption, carried over from [8]).** Single-shot readout fidelity $F = 0.99991$, i.e. $99.991\%$, with an associated uncertainty of one unit in the last digit, stated in [8] as arising from $N_{\text{trials}} = 10^{6}$ trials. We assume this value throughout; no claim of this paper depends on which physical platform produced it.

### 4.1 Readout error probability and error counts

**Derivation 4.1.** Per-shot error probability:

$$p_e = 1 - F = 1 - 0.99991 = 9 \times 10^{-5}.$$

One readout shot in $1/p_e = 1/(9 \times 10^{-5}) \approx 1.1111 \times 10^{4}$ is wrong on average. Over the assumed $10^{6}$ trials, the expected number of wrong single-shot outcomes is

$$N_{\text{err}} = p_e \, N_{\text{trials}} = 9 \times 10^{-5} \times 10^{6} = 90.$$

The assumed last-digit uncertainty corresponds to $\pm 1 \times 10^{-5}$ in $F$, i.e. $\pm 10$ counts in $N_{\text{err}}$; a binomial fluctuation of order $\sqrt{N_{\text{err}}} = \sqrt{90} \approx 9.487$ is of the same order, so the assumed fidelity uncertainty is consistent with pure counting statistics.

### 4.2 Statistical floor and the contraction regime

**Derivation 4.2 (tomographic statistical floor; projection).** Assume $N = 10^{4}$ shots per tomographic setting (a stated assumption, not a measurement) and worst-case Bernoulli parameter $p = 1/2$:

$$\sigma_p = \sqrt{\frac{p(1-p)}{N}} = \sqrt{\frac{0.25}{10^{4}}} = \sqrt{2.5 \times 10^{-5}} \approx 5.00 \times 10^{-3}.$$

The readout systematic floor is $p_e = 9 \times 10^{-5}$, smaller by the factor

$$\frac{\sigma_p}{p_e} = \frac{5.00 \times 10^{-3}}{9 \times 10^{-5}} \approx 55.6.$$

So at $10^{4}$ shots, statistics dominate readout error by a factor of about $56$. The crossover shot count at which the readout floor takes over is

$$N \gtrsim \frac{p(1-p)}{p_e^{2}} = \frac{0.25}{(9 \times 10^{-5})^{2}} = \frac{0.25}{8.1 \times 10^{-9}} \approx 3.0864 \times 10^{7}$$

shots per setting.

**Derivation 4.3 (contraction convergence; projection).** Model a single-parameter calibration loop as the linear contraction $T(x) = x^{*} + L(x - x^{*})$ with labeled illustrative inputs $L = 0.6$, initial discrepancy $d_0 = d_{\mathcal{D}}(x_0, x^{*}) = 1$ in normalized units, and target tolerance $\varepsilon = 10^{-3}$. Then

$$n \geq \frac{\ln(\varepsilon / d_0)}{\ln L} = \frac{\ln(10^{-3})}{\ln(0.6)}.$$

Evaluate the logarithms:

$$\ln(10^{-3}) = -3\ln 10 \approx -3 \times 2.302585 = -6.907755,$$
$$\ln(0.6) = \ln 6 - \ln 10 \approx 1.791759 - 2.302585 = -0.510826.$$

Divide:

$$n \geq \frac{-6.907755}{-0.510826} \approx 13.524,$$

so $n = 14$ rounds suffice. Check by direct evaluation: $0.6^{2} = 0.36$, $0.6^{4} = 0.1296$, $0.6^{8} = 0.01679616$, and

$$0.6^{14} = 0.6^{8} \times 0.6^{4} \times 0.6^{2} = 0.01679616 \times 0.1296 \times 0.36 \approx 7.836 \times 10^{-4} < 10^{-3},$$

while $0.6^{13} = 0.6^{14}/0.6 \approx 1.306 \times 10^{-3} > 10^{-3}$, so $n = 14$ is exactly the minimum. A variant projection with a smaller initial discrepancy $d_0 = 5 \times 10^{-2}$ and the readout floor $\varepsilon = p_e = 9 \times 10^{-5}$ as target gives $\varepsilon/d_0 = 9 \times 10^{-5} / 5 \times 10^{-2} = 1.8 \times 10^{-3}$, i.e.

$$n \geq \frac{\ln(1.8 \times 10^{-3})}{\ln 0.6} = \frac{-6.319968}{-0.510826} \approx 12.372,$$

so $n = 13$ cycles reach the readout-limited floor under those assumptions.

### 4.3 Shot budget for ontology discrimination

**Input:** $F = 0.99991$ (Input 1), so $p_e = 9 \times 10^{-5}$ (Derivation 4.1). Suppose two candidate ontologies differ in the expectation value of some readout-accessible observable by $\delta$. At confidence level $\alpha = 0.01$, Hoeffding's inequality requires

$$N \geq \frac{\ln(2/\alpha)}{2\,\delta^{2}} = \frac{\ln 200}{2\,\delta^{2}}.$$

Evaluate $\ln 200 = \ln 2 + \ln 100 \approx 0.693147 + 4.605170 = 5.298317$. For a discriminability target $\delta = 10^{-3}$:

$$N \geq \frac{5.298317}{2 \times 10^{-6}} = 2.649159 \times 10^{6}.$$

Compare with the assumed trial count $N_{\text{rep}} = 10^{6}$ associated with Input 1:

$$\frac{N}{N_{\text{rep}}} = \frac{2.649159 \times 10^{6}}{10^{6}} \approx 2.65.$$

For a harder target $\delta = 10^{-4}$:

$$N \geq \frac{5.298