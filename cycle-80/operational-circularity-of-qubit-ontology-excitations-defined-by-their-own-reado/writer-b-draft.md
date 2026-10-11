# Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout

## Abstract

Is the "qubit" a pre-existing object that control pulses and readout merely probe, or is it a two-level subsystem constituted by the very operations that define it? We formalize this question as a self-referential calibration problem: a tomographic map $F_{\theta}$ assigns states to measurement records, while the measurement operators themselves are defined by the calibrated state model, so that the operational definition of the qubit degree of freedom is circular. We distinguish two regimes. When the calibration map is a contraction with Lipschitz constant $L < 1$, Banach's fixed-point theorem guarantees a unique self-consistent Hilbert-space identification, and the circularity is benign in the same sense that ordinary instrument calibration is benign. When the map has a continuous symmetry—here modeled as a global rotation of the Bloch-sphere axis labeling—a family of physically inequivalent ontologies (energy eigenmode, field excitation, collective variable) remains compatible with identical operational data, and the circularity masks genuine ontological underdetermination. We derive the fixed-point condition explicitly, compute convergence bounds and error budgets with full arithmetic, and use the trapped-ion readout fidelity reported in the literature ($99.991\%$) to bound the readout-error contribution to ontological ambiguity. We conclude that "what is actually manipulated" is answerable only relative to a chosen symmetry-breaking convention, and we state the conditions under which this claim would be falsified.

## 1. Introduction

Quantum information practice speaks as if qubits are things: a transmon in a cavity, a calcium ion in a trap, a defect spin in diamond. Control pulses are calibrated, readout is optimized, and tomography returns a density matrix. Yet the chain of justification is circular. The pulse shapes used for tomography are designed assuming a model of the qubit (its transition frequency, its coupling, its relaxation); the readout discriminates two levels that the same model says are the computational basis; and the model's parameters are estimated from the readout records. States are defined by measurements, measurements are defined by states. The question of this paper is whether this circularity is merely the ordinary self-consistency of instrument calibration—harmless, convergent, and convention-like—or whether it can hide a real underdetermination: several physically inequivalent answers to "what is the controlled entity?" (an energy eigenmode, a field excitation, a collective variable of many degrees of freedom) that produce identical operational data.

This question is developed pedagogically in the QNFO corpus, which treats control, readout, and self-referential metrology across superconducting transmon, trapped-ion, and spin-qubit platforms and argues that the qubit-gate-circuit picture projects a particle ontology onto field-theoretic reality [9],[10],[12]. Our contribution here is narrower and formal: we write the circularity as a fixed-point problem, give a sharp criterion (contraction versus symmetry) separating benign from problematic circularity, and compute explicit numbers for a minimal model. We do not claim to resolve the ontology of any particular platform; we claim to characterize when the question is answerable in principle.

The plan is as follows. Section 2 reviews the supplied literature, which is dominated by ontology engineering in the life and materials sciences—a useful analogy, since those works confront exactly the problem of defining entities by their operational relationships—and by the one directly relevant quantum measurement result available to us, the trapped-ion readout demonstration [4]. Section 3 sets up the formalism. Section 4 carries out all derivations with explicit arithmetic. Section 5 reports only computed numbers and clearly labeled projections. Section 6 discusses limitations and falsification conditions.

## 2. Background and Related Work

The supplied bibliography is unusual for a quantum-foundations paper: most entries concern ontology as an engineering discipline. This is not a weakness for our purposes. Ontology engineering faces, in a mundane register, the same question we pose for qubits: what is an entity, given only its relations and uses?

[1] The Gene Ontology (GO) project is described as the largest resource for cataloguing gene function, combining solid conceptual underpinnings with practical features that have made it widely adopted and essential for data analysis; the entry supplies a primer introducing the structure of the ontology. For us, GO is the canonical example of an ontology whose entities (gene products and their functions) are defined operationally—by what they do in assays—rather than by intrinsic description. This is precisely the "operational constitution" structure we attribute to qubits.

[2] The companion chapter on GO pitfalls, biases, and remedies warns that the GO is sufficiently simple that it can be used without deep understanding of its structure or development, which the entry calls both a strength and a weakness, and discusses common misinterpretations. The lesson we draw is that operational ontologies acquire systematic misinterpretations when users mistake the operational definition for an intrinsic one—the exact error we diagnose in reading a qubit as a pre-existing two-level object.

[3] GraphMatcher is presented as an ontology matching system using a graph attention approach, addressing the interoperability problem in which semantically similar entities in different ontologies must be found and aligned before merging. This is the computational analogue of our cross-platform question: whether the "qubit" identified on a transmon and the "qubit" identified on an ion are the same entity under an ontology matching, or merely structurally similar placeholders.

[5] The study of how ontology mappings change in the life sciences analyzes mappings between popular life-science ontologies and notes that the evolution of such mappings had received little attention even though ontologies change continuously. It supports our point that entity identity across ontologies is not static: as the underlying operational practices evolve, the correspondence between entity vocabularies must be re-derived, which is what happens in physics whenever a platform's calibration model is revised.

[6] The work on ontology-based descriptions of conversations proposes to formally define qualitative conversational features by leveraging linguistic descriptors to derive quantitative definitions. It is an example of quantifying an entity that has no intrinsic metric—conversational "features" exist only through descriptors—an instructive parallel to defining a qubit's states through measurement statistics alone.

[7] The community-developed domain ontology for magnetic materials, developed within the EU-funded MaMMoS project, addresses persistent challenges for data exchange and interpretation arising from complex multiscale behaviour and the coexistence of multiple unit systems. Multiple unit systems for one physical domain is a clean instance of convention-relative description: the same magnetism, several incompatible vocabularies, all operationally adequate. We use this as the model case for our "multiple ontologies, identical data" scenario.

[8] The business-intelligence framework builds an ontological model using web semantics, mines relations from the model using a decision tree, and develops a framework for competitive-intelligence retrieval. Its relevance is structural: entities (competitors, information repositories) are constituted by relations mined from data, with no claim that the entities exist prior to the relational model. The entry's summary gives no further technical detail, so we use it only as this structural precedent.

[4] The single directly quantum entry demonstrates single-shot qubit readout with fidelity sufficient for fault-tolerant quantum computation, for two types of qubit stored in single trapped calcium ions; for an optical qubit stored in the $(4S_{1/2}, 3D_{5/2})$ levels of $\mathrm{^{40}Ca^{+}}$ it reports $99.991(1)\%$ average readout fidelity over one million trials using time-resolved photon counting, with an adaptive technique allowing $99.99\%$ fidelity. This is the empirical anchor for our error budget: it is the readout channel through which the operational definition of the ion qubit closes on itself, and its fidelity determines how tightly the circular definition can be pinned down.

[9] The QNFO work "No Thing There" is described as a pedagogical bridge between qubit ontology critique and working physics, explaining what control pulses actually manipulate and what readout measures across superconducting transmon, trapped-ion, and spin-qubit platforms, and including an electrical seesaw analogy and a self-referential metrology formalization. It is the immediate conceptual source of the circularity question formalized here; its supplied summary does not state its formal results in detail, so we treat it as motivation rather than as a source of theorems.

[10] "Beyond the Qubit" is described as a companion paper to "The Qubit Delusion" that strips quantum mechanics to its minimal ontological commitments and surveys constructive paradigms for post-particle computation, on the premise that the qubit-gate-circuit model is an epistemic failure projecting particle ontology onto relational, field-theoretic reality. Our contraction-versus-symmetry criterion can be read as a formal test of when that projection is harmless.

[12] "The Qubit Delusion" (revised v1.1) supplies the polemical thesis that particle ontology sabotaged quantum computing; its supplied entry states only the revision note, so we cite it as the position our formalism is meant to discipline rather than as a source of technical claims.

[11] The "Manifesto for Honest Computation" states 5 principles, a concrete portfolio, and a Falsification Pledge. We adopt its methodological stance explicitly: every claim below is either derived with shown arithmetic or labeled as a projection with stated assumptions, and Section 6 states what would falsify the framework.

## 3. Methods

### 3.1 The circular calibration map

Let $\Theta$ be the parameter space of a candidate Hilbert-space identification: transition frequency $\omega_q$, coupling strengths, relaxation rates, and the orientation of the computational basis on the Bloch sphere. A calibration cycle consists of (i) applying control pulses $u(\theta)$ designed using the current model $\theta \in \Theta$, (ii) recording readout statistics $d$, and (iii) updating the model. We write the cycle as a map

$$F_{\theta} : \Theta \to \Theta, \qquad \theta_{n+1} = F_{\theta}(\theta_n),$$

where the subscript records the circularity: the pulses and the readout observables used in step (ii) are functions of $\theta_n$ itself. A self-consistent qubit ontology is a fixed point $\theta_* = F_{\theta}(\theta_*)$.

### 3.2 Benign circularity: contraction

If $F_{\theta}$ is a contraction with Lipschitz constant $L < 1$ on a complete metric space $(\Theta, \rho)$,

$$\rho\big(F_{\theta}(\theta), F_{\theta}(\theta')\big) \le L\, \rho(\theta, \theta') \quad \text{for all } \theta, \theta' \in \Theta,$$

then by Banach's fixed-point theorem $F_{\theta}$ has exactly one fixed point, and iteration from any $\theta_0$ converges to it with the error bound

$$\rho(\theta_n, \theta_*) \le L^n\, \rho(\theta_0, \theta_*).$$

In this regime the circularity is benign: it is the same self-consistency structure as ordinary instrument calibration, and the ontology is unique.

### 3.3 Problematic circularity: continuous symmetry

Suppose instead that a group $G$ acts on $\Theta$ and that $F_{\theta}$ is equivariant:

$$F_{\theta}(g \cdot \theta) = g \cdot F_{\theta}(\theta) \quad \text{for all } g \in G.$$

Then if $\theta_*$ is a fixed point, so is $g \cdot \theta_*$ for every $g \in G$: the fixed-point set is at least a full orbit of $G$, and no amount of iteration within the circular loop selects a member of the orbit. For a qubit, the natural candidate is the rotation group $SO(3)$ acting on the Bloch-sphere axis labeling: if all prepared states, pulses, and readout axes are rotated by the same $R \in SO(3)$, every operational statistic is unchanged. The orbit has dimension $\dim SO(3) = 3$, so three continuous degrees of ontological description are unconstrained by any operational data. Whether the orbit members are "the same ontology, differently labeled" (benign gauge) or "physically inequivalent ontologies" (energy eigenmode versus field excitation versus collective variable) is exactly the question the operational loop cannot answer by itself; it requires an input outside the loop—a symmetry-breaking convention or an independent probe.

### 3.4 Readout error as the loop's noise floor

The circular loop closes through the readout channel. If the readout fidelity is $f$, the single-shot error probability is $p_e = 1 - f$. Over $N$ independent readout shots used to estimate a single tomographic parameter, the statistical uncertainty of an estimated probability scales as

$$\sigma_p \approx \sqrt{\frac{p(1-p)}{N}} + p_e,$$

where the second term is a systematic floor from readout error. This floor bounds how finely the fixed point can be localized, and hence how sharply any residual discrete ontological ambiguity can be resolved.

## 4. Analysis

All inputs are stated with sources; all arithmetic is shown.

**Input 1 (from [4]).** Average single-shot readout fidelity for the optical qubit in $\mathrm{^{40}Ca^{+}}$: $f = 99.991\%$, with a stated uncertainty of $(1)$ in the last digit, over $N_{\text{trials}} = 10^6$ trials.

*Derivation 4.1 (readout error probability).*

$$p_e = 1 - f = 1 - 0.99991 = 9 \times 10^{-5}.$$

So one readout shot in $1/p_e = 1/(9\times10^{-5}) \approx 11111.1$ is wrong on average. Over the reported $10^6$ trials, the expected number of wrong single-shot outcomes is

$$N_{\text{err}} = p_e \, N_{\text{trials}} = 9\times10^{-5} \times 10^{6} = 90.$$

The reported uncertainty of $(1)$ on the last digit of $99.991\%$ corresponds to $\pm 1\times10^{-5}$ in $f$, i.e. $\pm 1\times10^{-5}$ in $p_e$, i.e. $\pm 10$ counts in $N_{\text{err}}$ over $10^6$ trials; $90 \pm 10$ wrong outcomes is consistent with a binomial fluctuation of order $\sqrt{N_{\text{err}}} \approx \sqrt{90} \approx 9.49$, so the quoted fidelity uncertainty is of the same order as pure counting statistics.

*Derivation 4.2 (statistical floor of a tomographic estimate).* Take the worst case for binomial statistics, $p = 1/2$. With $N = 10^4$ shots per tomographic setting (a routine figure; we state it as an assumption of this projection, not a measurement):

$$\sigma_p = \sqrt{\frac{p(1-p)}{N}} = \sqrt{\frac{0.5 \times 0.5}{10^4}} = \sqrt{\frac{0.25}{10^4}} = \sqrt{2.5\times10^{-5}} \approx 5.00\times10^{-3}.$$

The readout systematic floor is $p_e = 9\times10^{-5}$, which is smaller by the factor

$$\frac{\sigma_p}{p_e} = \frac{5.00\times10^{-3}}{9\times10^{-5}} \approx 55.6.$$

So with $10^4$ shots, statistical noise dominates readout error by a factor of about $56$; the circular loop's localization of the fixed point is statistics-limited, not readout-limited, until $N \gtrsim p(1-p)/p_e^2 = 0.25/(9\times10^{-5})^2 = 0.25/(8.1\times10^{-9}) \approx 3.09\times10^{7}$ shots per setting, at which point the readout floor takes over.

*Derivation 4.3 (contraction convergence for a concrete calibration map).* Model a single-parameter calibration (transition-frequency trim) with the linear contraction

$$F_{\theta}(\theta) = \theta_* + L(\theta - \theta_*), \qquad L = 0.6,$$

where $L = 0.6$ is an assumed model parameter of this illustrative map (we flag it as such). Start at $\rho(\theta_0, \theta_*) = 5\times10^{-2}$ (in units of the model's own frequency scale). The Banach bound gives:

- $n=1$: $\rho \le 0.6 \times 5\times10^{-2} = 3.0\times10^{-2}$.
- $n=2$: $0.6^2 \times 5\times10^{-2} = 0.36 \times 5\times10^{-2} = 1.8\times10^{-2}$.
- $n=5$: $0.6^5 = 0.07776$, so $\rho \le 0.07776 \times 5\times10^{-2} = 3.888\times10^{-3}$.
- $n=10$: $0.6^{10} = 0.0060466176$, so $\rho \le 0.0060466176 \times 5\times10^{-2} = 3.0233\times10^{-4}$.
- $n=20$: $0.6^{20} = (0.6^{10})^2 = 0.0060466176^2 \approx 3.6562\times10^{-5}$, so $\rho \le 3.6562\times10^{-5} \times 5\times10^{-2} = 1.8281\times10^{-6}$.

To reach the readout-limited floor $p_e = 9\times10^{-5}$ requires $0.6^n \times 5\times10^{-2} \le 9\times10^{-5}$, i.e. $0.6^n \le 1.8\times10^{-3}$, i.e.

$$n \ge \frac{\ln(1.8\times10^{-3})}{\ln 0.6} = \frac{-6.3208}{-0.5108} \approx 12.37,$$

so $n = 13$ calibration cycles suffice for the contraction model to localize the fixed point below the readout error floor.

*Derivation 4.4 (dimension count of the symmetry orbit).* The rotation group acting on the Bloch-axis labeling has $\dim SO(3) = 3$. A full specification of a two-level ontology includes the axis orientation (2 angles) plus an overall phase convention for the basis states (1 angle), totaling 3 continuous parameters that are invisible to any operational statistic that is equivariant under the same rotation. The operational data constrain only the remaining parameters of $\Theta$; if $\Theta$ has dimension $d_{\Theta}$, the fixed-point set has dimension at least

$$d_{\text{orbit}} = 3,$$

independent of $d_{\Theta}$, and the number of continuously distinct ontologies compatible with identical data is uncountable. Discrete ontological hypotheses (eigenmode vs. field excitation vs. collective variable) form a finite set within this orbit; the operational loop alone cannot reduce it.

*Derivation 4.5 (can statistics break the symmetry?).* If the readout channel had even a small non-equivariant component—say an asymmetry $\epsilon$ in the two readout axes—the orbit would collapse to the fixed points of the residual symmetry. The smallest detectable asymmetry is bounded by the total estimation uncertainty:

$$\epsilon_{\min} \approx \sqrt{\sigma_p^2 + p_e^2}.$$

With $N = 10^4$: $\epsilon_{\min} \approx \sqrt{(5.00\times10^{-3})^2 + (9\times10^{-5})^2} = \sqrt{2.5\times10^{-5} + 8.1\times10^{-9}} = \sqrt{2.5081\times10^{-5}} \approx 5.008\times10^{-3}$. With $N = 3.09\times10^7$ (Derivation 4.2's crossover): $\sigma_p = \sqrt{0.25/(3.09\times10^7)} = \sqrt{8.09\times10^{-9}} \approx 8.99\times10^{-5}$, and $\epsilon_{\min} \approx \sqrt{(8.99\times10^{-5})^2 + (9\times10^{-5})^2} = \sqrt{8.08\times10^{-9} + 8.1\times10^{-9}} = \sqrt{1.618\times10^{-8}} \approx 1.272\times10^{-4}$. Any genuine ontological signature smaller than $\epsilon_{\min}$ is operationally invisible.

## 5. Results

All numbers below are computed in Section 4; assumptions are restated where the input was assumed rather than sourced.

1. **Readout error probability** (from the fidelity in [4]): $p_e = 9\times10^{-5}$, i.e. about one error per $1.11\times10^{4}$ shots; over the reported $10^6$ trials, $N_{\text{err}} = 90 \pm 10$ wrong outcomes expected.
2. **Tomographic statistical floor** (projection; assumed $N = 10^4$ shots per setting, worst-case $p=1/2$): $\sigma_p \approx 5.00\times10^{-3}$, exceeding the readout floor $p_e = 9\times10^{-5}$ by a factor $\approx 55.6$. The crossover shot count at which readout error dominates is $N \approx 3.09\times10^{7}$ per setting.
3. **Contraction convergence** (projection; assumed illustrative map with $L = 0.6$, initial error $5\times10^{-2}$): error bounds $3.888\times10^{-3}$ at $n=5$, $3.0233\times10^{-4}$ at $n=10$, $1.8281\times10^{-6}$ at $n=20$; the readout floor is reached after $n = 13$ cycles.
4. **Symmetry orbit dimension**: $d_{\text{orbit}} = 3$ continuous ontological parameters (two axis angles plus one basis phase) are unconstrained by any equivariant operational statistic; the family of data-compatible ontologies is uncountable.
5. **Symmetry-breaking sensitivity** (projection): the smallest detectable readout asymmetry is $\epsilon_{\min} \approx 5.008\times10^{-3}$ at $10^4$ shots and $\epsilon_{\min} \approx 1.272\times10^{-4}$ at the crossover count $3.09\times10^7$ shots; ontological signatures below these values are operationally invisible.

**Headline claim.** The circularity of qubit ontology is benign exactly when the calibration map is a contraction (unique fixed point, convergence in a small number of cycles in the illustrative model) and problematic exactly to the extent that an equivariant symmetry survives; in the minimal qubit case the surviving symmetry leaves a 3-dimensional orbit of ontologies that identical operational data cannot distinguish.

## 6. Discussion

**Limitations.** The contraction model of Derivation 4.3 is illustrative: the value $L = 0.6$ and the initial error $5\times10^{-2}$ are assumed, not measured, and real calibration maps on multi-parameter spaces need not be global contractions (they may have multiple basins, or drift non-stationarily, voiding the fixed-point picture). The dimension count of Derivation 4.4 assumes perfect equivariance; any real platform has stray asymmetries (bias fields, crosstalk) that partially break $SO(3)$, and the question becomes quantitative: how much of the 3-dimensional orbit is actually pinned down? Derivation 4.5 gives the sensitivity, but only under the assumed shot counts and an idealized noise model (independent shots, stationary readout). Correlated readout errors would inflate $\sigma_p$ and worsen $\epsilon_{\min}$.

**Failure modes.** The framework fails if calibration maps are chaotic rather than contractive—then no fixed point exists and "the qubit" has no self-consistent definition at all, a stronger conclusion than we claim. It also fails if the symmetry orbit is not a gauge: if two members of the orbit correspond to genuinely different physical couplings (e.g., single-ion transition versus collective motional mode) that happen to be related by the equivariance, then our "benign gauge" reading is wrong and the underdetermination is physical, not conventional. We cannot decide this from operational data by construction—that is the point—but an independent probe outside the loop (e.g., a measurement coupling to a third level, or to the environment) could.

**What would falsify the claims.** (i) A demonstration that a calibration loop on a real platform converges to a unique, platform-independent Hilbert-space identification including the axis-labeling degrees of freedom—i.e., that the orbit is in fact broken by operational data alone—would falsify the 3-dimensional-orbit claim. (ii) A demonstration that two members of the orbit give different predictions for some operational quantity would falsify the equivariance assumption and dissolve the underdetermination. (iii) A calibration map shown empirically to have Lipschitz constant $L \ge 1$ with multiple attracting fixed points would falsify the benign-circularity regime as described.

**Against ourselves.** A skeptic may say the 3-dimensional orbit is trivially a gauge, of no ontological interest, and that the real question (eigenmode vs. collective variable) is settled by the Hamiltonian used to build the device—an input outside the loop, so no circularity arises. Our reply: the Hamiltonian's interpretation is itself fixed by calibration data of the same circular type, so the "outside input" is not clearly outside. But the skeptic's stronger point stands: we have not shown that any two discrete ontologies are operationally equivalent on a real platform; we have shown only the structural possibility and the sensitivity limit. The QNFO corpus's stronger thesis—that the qubit-gate-circuit model is an epistemic failure [10],[12]—is not established by our results; our results only show where the burden of proof lies.

**Open questions.** Do cross-platform ontology matchings (in the sense of [3]) identify qubits as the same entity or merely align them? Do ontology mappings drift across platform generations as life-science mappings do across ontology versions [5]? Can the unit-system plurality documented for magnetic materials [7] recur at the level of qubit ontologies—several adequate, incompatible vocabularies for one device?

## 7. Conclusion

We formalized the operational circularity of qubit ontology as a fixed-point problem for a self-referential calibration map. Benign circularity corresponds to contraction: a unique self-consistent identification, reached in finitely many cycles, with the localization floor set by readout error ($p_e = 9\times10^{-5}$ from the trapped-ion fidelity of [4]) and, for routine shot budgets, by counting statistics ($\sigma_p \approx 5.00\times10^{-3}$ at $10^4$ shots). Problematic circularity corresponds to surviving equivariant symmetry: in the minimal qubit case, a 3-dimensional orbit of ontologies—energy eigenmode, field excitation, collective variable, or mere relabeling—that identical operational data cannot separate, with a detection sensitivity $\epsilon_{\min}$ between $5.008\times10^{-3}$ and $1.272\times10^{-4}$ depending on shot budget. The answer to "what is actually manipulated" is therefore answerable only relative to a symmetry-breaking convention or an independent probe; it is not answerable from the operational loop alone, but the loop does tightly bound how much underdetermination can hide inside it.

## References

[1] arXiv:1602.01876v1 | Primer on the Gene Ontology

[2] arXiv:1602.01875v1 | Gene Ontology: Pitfalls, Biases, Remedies

[3] arXiv:2404.14450v1 | GraphMatcher: A Graph Representation Learning Approach for Ontology Matching

[4] arXiv:0802.1684v2 | High-fidelity readout of trapped-ion qubits

[5] arXiv:1204.2731v1 | How do Ontology Mappings Change in the Life Sciences?

[6] arXiv:2509.04926v1 | Towards Ontology-Based Descriptions of Conversations with Qualitatively-Defined Concepts

[7] arXiv:2609.11464v1 | A Community-Developed Domain Ontology for Magnetic Materials

[8] arXiv:1109.1088v1 | A Framework for Business Intelligence Application using Ontological Classification

[9] QNFO: No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems | DOI 10.5281/zenodo.21451776

[10] QNFO: Beyond the Qubit: Constructive Paradigms for Post-Particle Computation | DOI 10.5281/zenodo.22753022

[11] QNFO: Manifesto for Honest Computation | DOI 10.5281/zenodo.21299278

[12] QNFO: The Qubit Delusion: How Particle Ontology Sabotaged Quantum Computing | DOI 10.5281/zenodo.21254143