# Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout (Version 2.1.0, Post-Publication Revision)

## Abstract

Is the qubit a pre-existing object that control pulses and readout merely probe, or a two-level subsystem constituted by the very operations that define it? We formalize this question as a self-referential calibration problem: an ontology map $\Phi$ assigns Hilbert-space identifications to operational data, and calibration seeks a fixed point of the composite loop $T=\Gamma\circ\Phi$, in which states are defined by measurements that are themselves defined by states. We distinguish two regimes. When $T$ is a contraction with Lipschitz constant $L<1$, Banach's fixed-point theorem guarantees a unique self-consistent identification and the circularity is benign, in the same sense that ordinary instrument calibration is benign. When the loop admits multiple fixed points or a continuous equivariant symmetry, physically inequivalent ontologies—an energy eigenmode, a field excitation, a collective variable—remain compatible with identical operational data, and the circularity masks genuine ontological underdetermination. We exhibit an explicit two-branch toy model in which the final ontology is fixed by the initial guess rather than by the data. Anchoring the per-shot readout error at $p_{e}=9\times10^{-5}$, the value derived in the companion calibration-loop analysis [10], we compute the shot budget required to resolve ontology-discriminating discrepancies: $N\approx2.649159\times10^{6}$ shots for a discrepancy $\delta=10^{-3}$ at $1\%$ failure probability, and $N\approx2.649159\times10^{8}$ shots for $\delta=10^{-4}$. We conclude that uniqueness is a property of the calibration dynamics, not of the qubit, and state falsifiable conditions for both outcomes.

## 1. Introduction

Quantum information processing speaks the language of qubits: two-level systems that are initialized, manipulated by control pulses, and measured. The working assumption of much of the field is that the qubit is a pre-existing object—a particular two-dimensional subspace of some Hilbert space—that control and readout merely access. This paper questions that assumption in a specific, formalizable way, and the question is not academic: calibration engineers who certify qubit devices, and hardware designers who compare platforms, currently have no criterion that tells them when their calibration loop can in principle settle what the device is, and when it cannot.

The stakes are concrete. The global quantum computing industry has absorbed an estimated $35 billion in combined public and private investment without a commercially viable quantum computer, and the QNFO research program has argued that part of the reason is epistemic rather than purely engineering: the qubit-gate-circuit model imports a particle ontology into quantum mechanics that is inconsistent with what we have learned since relativistic quantum field theory [9], [11]. If that diagnosis is even partially correct, then a decision procedure for "is my calibration loop telling me what the device is, or only telling me what I assumed?" changes how device qualification and cross-platform benchmarking are done.

The operational loop is unavoidable. To implement a control pulse, one needs a model of the qubit: its transition frequency, its coupling to the drive, its relaxation channels. To validate that model, one runs tomography; but tomography is defined by a measurement apparatus whose calibration itself presupposes a model of the states being measured. States are defined by measurements, and measurements are defined by states. We call this **operational circularity**. The question is not whether the circle exists—it does—but when it is benign and when it is not.

We distinguish two regimes:

1. **Benign circularity (calibration self-consistency).** The loop converges to a unique operational identification: a single assignment of Hamiltonian parameters, readout observables, and error channels that is stable under further calibration. This is the regime of ordinary instrument calibration, and it is formally a contraction fixed-point iteration.

2. **Ontological underdetermination.** Multiple, physically inequivalent identifications of the controlled entity—"the qubit is an energy eigenmode," "the qubit is a localized field excitation," "the qubit is a collective variable of many degrees of freedom"—are each exactly self-consistent with the same operational data. In this regime, no amount of calibration *inside the loop* distinguishes them.

Our contribution is fourfold:

- We give a formal definition of the calibration fixed-point problem: an ontology map $\Phi:\mathcal{D}\to\mathcal{O}$ and a realization map $\Gamma:\mathcal{O}\to\mathcal{D}$ whose composite $T=\Gamma\circ\Phi$ is the calibration operator (Section 3).
- We derive the contraction condition under which the fixed point is unique, and exhibit an explicit toy model in which two inequivalent ontologies are both exact fixed points, with the selected branch fixed by the initial guess (Section 4, Derivations 4.3 and 4.5).
- We quantify the statistical floor of ontology discrimination: with per-shot readout error $p_{e}=9\times10^{-5}$ anchored to the companion analysis [10], the shot budget for resolving a discrepancy $\delta$ at confidence $\alpha$ is $N\ge\ln(2/\alpha)/(2\delta^{2})$, giving $2.649159\times10^{6}$ shots at $\delta=10^{-3}$, $\alpha=0.01$ (Section 4.4).
- We derive the smallest readout asymmetry detectable at a given shot count, $\epsilon_{\min}\approx\sqrt{\sigma_{p}^{2}+p_{e}^{2}}$, and correct the published value at $10^{4}$ shots to $\epsilon_{\min}\approx5.001\times10^{-3}$ (Section 4.6).

Section 6 discusses limitations and what would falsify each claim.

## 2. Background and Related Work

The relevant literature falls into two groups: formal ontology engineering, which supplies the vocabulary of "ontology" we adapt, and the QNFO corpus, which supplies the physical critique and the quantitative anchors.

**Ontology as a formal artifact.** The Gene Ontology (GO) project is described in [1] as the largest resource for cataloguing gene function, combining solid conceptual underpinnings with practical features that have made it widely adopted and essential for data analysis. We borrow from this tradition the idea that an ontology is an explicit, structured assignment of entities and relations—not a metaphysical thesis but a representational commitment. Our "ontology map" $\Phi$ (Section 3) is exactly such a commitment, applied to Hilbert-space identifications rather than gene functions.

Crucially, ontologies can be used without understanding their construction, and this is a double-edged property: [2] states that the GO is sufficiently simple that it can be used without deep understanding of its structure or how it is developed, which is both a strength and a weakness, and the same work discusses common misinterpretations of the ontology and their remedies. This is precisely the failure mode we attribute to qubit ontology: the two-level abstraction is usable without knowing what it commits us to, and the misuse is invisible until the abstraction is pushed beyond its calibration domain.

Ontologies are not static. [4] analyzes how mappings between life-science ontologies evolve, evaluating three real-world domains (Anatomy, Molecular Biology, Chemistry) and four match strategies, and finding that Molecular Biology and Chemistry undergo heavy ontology extensions and revisions whereas Anatomy is relatively stable; notably, mappings produced by the structural matcher Context were rather unstable while name-based mappings were relatively stable. We adopt this dynamic picture as an assumption about qubit ontologies: the identification of a qubit is not fixed once but is the output of an evolving calibration process, and the stability of that process—its contraction or lack thereof—is the object of study. The observation that a structurally defined correspondence is less stable than a name-defined one has a direct analogue here: identifications pinned to operational structure (the calibration loop) may be less stable than identifications pinned to an external reference.

Ontology matching—the problem of finding correspondences between entities in different ontologies so they can be aligned or merged—is addressed by [3], which presents GraphMatcher, an ontology matching system using a graph attention approach together with a new neighbourhood aggregation method. In the OAEI 2022 conference track it achieved its best F1-measures in the M1 and M3 evaluation variants and reached the highest F1-measure (72% in both) on the uncertain reference alignments among all matchers evaluated in that track. Our multi-platform question (does calibration on a transmon, an ion, and a spin qubit converge to the *same* identification?) is structurally an ontology-matching problem: we ask whether the operational ontologies of different platforms have a common alignment or only a family of partial correspondences. The existence of working matching systems with quantified precision and recall shows that alignment across ontologies is decidable in practice when a reference alignment exists; our Section 5 asks the analogous question for platform ontologies.

[6] presents a community-developed domain ontology for magnetic materials (MagMO), developed in the MaMMoS project, explicitly motivated by the coexistence of multiple unit systems that hinders consistent data exchange, and aligned with the physics-grounded top-level ontology EMMO. The unit-system problem is a direct analogue of our problem: the same physical magnet can be described in multiple unit conventions, and the ontology must manage the equivalence so that quantities are interpreted unambiguously. MagMO's design choice—a human-readable, programmatic implementation that enables versioning and collaborative adaptation—models what a qubit ontology register would need: an explicit, versioned record of what the calibration loop has committed to.

An ontology-based approach can also pin down an entity that has no pre-existing sharp definition. [5] proposes formally defining qualitative conversational features by deriving quantitative definitions from linguistic descriptors, instantiating the framework on a Proficiency-Level Control use case in which a decision tree classifier maps descriptor values to CEFR proficiency levels A1–C2. The analogy to the qubit is exact in one respect: "the qubit" is a qualitatively described entity whose operational definition must be constructed, and [5] shows that such construction can be made explicit, testable, and consistent.

Ontological classification also functions as an operational knowledge-extraction device outside the sciences: [7] develops an ontological model to capture specific information from the web by using web semantics, and mines relations between the data using a decision tree, as part of a business-intelligence framework. We cite it for the methodological point that an ontology can serve as the operative substrate of a decision pipeline even when its referents are not physical—exactly the status "the qubit" has inside a calibration loop.

**The physical critique.** [9] is a pedagogical bridge between the qubit ontology critique and working physics: it explains what control pulses actually manipulate and what readout measures across superconducting transmon, trapped-ion, and spin qubit platforms, includes an electrical seesaw analogy, a self-referential metrology formalization, and an 8-entry calibration register with dated, falsifiable predictions. Two of its conclusions anchor our formalism. First, a qubit is not a particle but a constrained two-level subspace of a physical degree of freedom—a collective circuit mode (transmon), electronic states (trapped ion), or spin orientation (quantum dot)—and working quantum engineers have never thought otherwise. Second, self-referential metrology is genuinely circular but has an anchor: multi-level spectroscopy of the bare Hamiltonian provides an independent reference for the computational subspace. Our Section 3 sharpens this program into a fixed-point problem, and our falsifiability conditions in Section 6 correspond to [9]'s fragile-versus-robust dichotomy for layered abstraction: either each level of abstraction is a protected subspace of the level below, or gauge freedoms compound across levels into a house of cards that is internally consistent but externally unmoored.

[10] is the closest technical antecedent and our quantitative anchor. It formalizes the calibration hierarchy of engineered qubits as an iterated map, derives its contraction condition, and quantifies the iteration count required to reach the readout noise floor; it constructs two ontologically distinct models—a two-level abstraction and a three-level anharmonic ladder—and proves that, under any measurement chain confined to the computational subspace, the models yield identical outcome statistics. Its quantitative results include a per-shot readout error $\varepsilon_{\mathrm{ro}}=9\times10^{-5}$ from a typical trapped-ion readout fidelity, expected misidentifications $\mu=90$ in $10^{6}$ trials, a minimum of $k_{\min}=11$ calibration iterations to fall below the readout noise floor, total-variation distance $D_{\mathrm{TV}}=0$ for subspace-restricted measurements but $D_{\mathrm{TV}}=0.01$ for a leakage-resolving measurement with leakage coefficient $|c|=0.1$, and a shot budget $N\ge2500$ for one-sigma resolution of $\Delta p=0.01$ once a leakage-resolving observable is introduced. Our Section 4 adopts the same per-shot error anchor and extends the shot-budget analysis to the Hoeffding regime of small discrepancies, and our two-branch toy model is a scalar simplification of its two-model degeneracy result.

[11] asks the constructive question that follows from the critique: what does quantum mechanics actually demand of a computational substrate once classical projections—particles, waves, measurement as revelation, observers as special—are stripped away? It enumerates the minimal ontological commitments of quantum mechanics and argues that the choice of computational scaffold is never ontologically neutral. Our uniqueness/underdetermination dichotomy is a tool for deciding when the scaffold choice is forced by data and when it remains open; if the underdetermined regime obtains, [11]'s constructive program is not merely philosophy but an underdetermined engineering choice.

**Relation to the published version of this paper.** [8] is the prior version whose formalization (ontology map, realization map, contraction condition, two-branch model) we retain, and whose errors we correct here: the published Section 4 attributed its readout fidelity to a source that cannot supply it, and its Result R5 stated a symmetry-sensitivity value inconsistent with its own Derivation 4.6. Both corrections are carried through below; the per-shot error is now anchored to [10], which derives the same value, and the corrected $\epsilon_{\min}$ is computed in Derivation 4.6.

## 3. Methods

### 3.1 Operational ontology maps

Let $\mathcal{D}$ be the space of operational data: sequences of control waveforms, their applied settings, and readout records. Let $\mathcal{O}$ be the space of Hilbert-space identifications: assignments of the form "the manipulated degree of freedom is the two-level system spanned by $\{|0\rangle,|1\rangle\}$ with Hamiltonian $H=\frac{\hbar}{2}(\omega_{0}\sigma_{z}+\Omega_{x}\sigma_{x}+\Omega_{y}\sigma_{y})$, readout observable $M$, error channels $\{L_{k}\}$," together with the physical interpretation of each symbol (eigenmode, field excitation, collective variable).

An **ontology map** is a function
$$
\Phi:\mathcal{D}\to\mathcal{O},
$$
which takes a body of operational data and returns an identification. Calibration is the search for a **self-consistent datum** $x^{*}\in\mathcal{D}$ satisfying
$$
x^{*}=\Gamma\bigl(\Phi(x^{*})\bigr),
$$
where $\Gamma:\mathcal{O}\to\mathcal{D}$ is the **realization map**: given an identification, it produces the operational data that the identified system would generate under the calibrated protocol. A pair $(x^{*},\Phi(x^{*}))$ satisfying this equation is a **fixed point of the operational loop**.

### 3.2 Benign circularity: the contraction condition

Let $d_{\mathcal{D}}$ be a metric on $\mathcal{D}$ (e.g., total-variation distance between predicted readout distributions plus weighted parameter distance). Define the composite calibration operator
$$
T=\Gamma\circ\Phi:\mathcal{D}\to\mathcal{D}.
$$

**Proposition 1 (Benign circularity).** If $T$ is a contraction with Lipschitz constant $L<1$,
$$
d_{\mathcal{D}}\bigl(T(x),T(x')\bigr)\le L\,d_{\mathcal{D}}(x,x')\quad\text{for all }x,x'\in\mathcal{D},
$$
then by the Banach fixed-point theorem $T$ has a unique fixed point $x^{*}$, and iteration from any initial guess $x_{0}$ converges to it, with
$$
d_{\mathcal{D}}(x_{n},x^{*})\le L^{n}\,d_{\mathcal{D}}(x_{0},x^{*}).
$$
Convergence to tolerance $\varepsilon$ requires
$$
n\ge\frac{\ln\!\bigl(\varepsilon/d_{\mathcal{D}}(x_{0},x^{*})\bigr)}{\ln L}.
$$
Since $0<L<1$, $\ln L<0$; with $\varepsilon<d_{\mathcal{D}}(x_{0},x^{*})$ the numerator is negative and $n$ is positive, as required. In this regime the circularity is benign: the loop defines a unique operational identification regardless of the starting ontology.

### 3.3 Ontological underdetermination

If $T$ is not globally contractive, uniqueness can fail. The physically interesting failure is not chaos but **multiplicity**: several fixed points, each corresponding to a different physical interpretation of the same symbols. We say the qubit ontology is **underdetermined** on a data set $x^{*}$ if there exist two ontology maps $\Phi_{A},\Phi_{B}$ and realization maps $\Gamma_{A},\Gamma_{B}$ such that
$$
x^{*}=\Gamma_{A}\bigl(\Phi_{A}(x^{*})\bigr)=\Gamma_{B}\bigl(\Phi_{B}(x^{*})\bigr),
$$
with $\Phi_{A}(x^{*})$ and $\Phi_{B}(x^{*})$ physically inequivalent (differing in the interpretation of the controlled entity, not merely in parameter values). This is the scalar analogue of the result proved in [10]: a two-level abstraction and a three-level anharmonic ladder yield identical outcome statistics under any measurement chain confined to the computational subspace.

A second, continuous route to underdetermination is **equivariance**: if a group $G$ acts on the identification space and $T$ commutes with the action, then $g\cdot x^{*}$ is a fixed point whenever $x^{*}$ is, and no iteration inside the loop selects a member of the orbit. For a qubit, the natural candidate is $SO(3)$ acting on the Bloch-sphere axis labeling; $\dim SO(3)=3$, so three continuous descriptive parameters (two axis angles plus one basis phase) are invisible to any equivariant operational statistic.

### 3.4 Discriminating observable and shot budget

To escape the loop, one needs an observable whose expectation differs between candidate ontologies by an amount $\delta$, resolved against readout noise. Given single-shot readout fidelity $F$, the per-shot error probability is $p_{e}=1-F$. By Hoeffding's inequality, estimating a Bernoulli mean to additive accuracy $\delta$ with failure probability $\alpha$ requires
$$
N\ge\frac{\ln(2/\alpha)}{2\,\delta^{2}}.
$$
This gives the minimal experimental budget for any ontology-discriminating test, instantiated in Section 4.4 using the per-shot error $p_{e}=9\times10^{-5}$ anchored to [10].

## 4. Analysis

All numbers in this section are computed here from stated inputs. The per-shot readout error is anchored to the companion calibration-loop analysis [10], which derives $\varepsilon_{\mathrm{ro}}=9\times10^{-5}$ from a typical trapped-ion readout fidelity; the remaining inputs are stated assumptions.

### 4.1 Readout error probability and error counts

**Assumption 1.** We take the per-shot readout error probability $p_{e}=9\times10^{-5}$ from the quantitative anchoring of [10], which derives this value from a typical trapped-ion readout fidelity; the corresponding fidelity is $F=1-p_{e}=0.99991$.

**Derivation 4.1.** Per-shot error probability:
$$
p_{e}=9\times10^{-5},\qquad F=1-p_{e}=0.99991.
$$
One readout shot in $1/p_{e}=1/(9\times10^{-5})\approx1.1111\times10^{4}$ is wrong on average. Over $10^{6}$ trials, the expected number of wrong single-shot outcomes is
$$
N_{\text{err}}=p_{e}\,N_{\text{trials}}=9\times10^{-5}\times10^{6}=90,
$$
matching the value $\mu=90$ reported in [10]. The one-sigma uncertainty on the fidelity from pure counting statistics is
$$
\sigma_{f}=\sqrt{\frac{p_{e}(1-p_{e})}{N_{\text{trials}}}}=\sqrt{\frac{9\times10^{-5}\times0.99991}{10^{6}}}\approx\sqrt{9.0\times10^{-11}}\approx9.49\times10^{-6},
$$
also matching the value $\sigma_{f}\approx9.49\times10^{-6}$ reported in [10]; a fluctuation of this size corresponds to $\pm10$ counts in $N_{\text{err}}$, so the quoted fidelity uncertainty is consistent with pure counting statistics.

### 4.2 Statistical floor and the contraction regime

**Derivation 4.2 (projection).** Assume $N=10^{4}$ shots per tomographic setting (a stated assumption) and worst-case Bernoulli parameter $p=1/2$:
$$
\sigma_{p}=\sqrt{\frac{p(1-p)}{N}}=\sqrt{\frac{0.25}{10^{4}}}=\sqrt{2.5\times10^{-5}}\approx5.00\times10^{-3}.
$$
The readout systematic floor is $p_{e}=9\times10^{-5}$, smaller by the factor
$$
\frac{\sigma_{p}}{p_{e}}=\frac{5.00\times10^{-3}}{9\times10^{-5}}\approx55.6.
$$
So at $10^{4}$ shots, statistics dominate readout error by a factor of about $56$. The crossover shot count at which the readout floor takes over is
$$
N\gtrsim\frac{p(1-p)}{p_{e}^{2}}=\frac{0.25}{(9\times10^{-5})^{2}}=\frac{0.25}{8.1\times10^{-9}}\approx3.09\times10^{7}
$$
shots per setting.

### 4.3 Contraction convergence (projection)

Model a single-parameter calibration loop as the linear contraction $T(x)=x^{*}+L(x-x^{*})$ with illustrative inputs $L=0.6$, initial discrepancy $d_{0}=d_{\mathcal{D}}(x_{0},x^{*})=1$ in normalized units, and target tolerance $\varepsilon=10^{-3}$. Then
$$
n\ge\frac{\ln(\varepsilon/d_{0})}{\ln L}=\frac{\ln(10^{-3})}{\ln(0.6)}.
$$
Evaluate the logarithms:
$$
\ln(10^{-3})=-3\ln10\approx-6.907755,\qquad
\ln(0.6)=\ln6-\ln10\approx-0.510826.
$$
Divide:
$$
n\ge\frac{-6.907755}{-0.510826}\approx13.524,
$$
so $n=14$ rounds suffice. Direct evaluation confirms minimality:
$$
0.6^{14}\approx7.836\times10^{-4}<10^{-3}<0.6^{13}\approx1.306\times10^{-3}.
$$
A variant with $d_{0}=5\times10^{-2}$ and target $\varepsilon=p_{e}=9\times10^{-5}$: the ratio is $\varepsilon/d_{0}=9\times10^{-5}/(5\times10^{-2})=1.8\times10^{-3}$, so
$$
n\ge\frac{\ln(1.8\times10^{-3})}{\ln(0.6)}=\frac{-6.319968}{-0.510826}\approx12.37,
$$
giving $n=13$ cycles. Check: $d_{0}\,0.6^{12}=5\times10^{-2}\times2.177\times10^{-3}\approx1.09\times10^{-4}>9\times10^{-5}$, while $d_{0}\,0.6^{13}\approx6.53\times10^{-5}<9\times10^{-5}$, confirming minimality. This is of the same order as the $k_{\min}=11$ iterations reported in [10] for a different contraction model, so the conclusion "a small number of rounds suffices" is robust across the two models.

### 4.4 Shot budget for ontology discrimination

**Input.** Per Assumption 1, $p_{e}=9\times10^{-5}$ [10]. Suppose two candidate ontologies differ in the expectation value of some readout-accessible observable by $\delta$. At confidence level $\alpha=0.01$, Hoeffding's inequality requires
$$
N\ge\frac{\ln(2/\alpha)}{2\,\delta^{2}}=\frac{\ln200}{2\,\delta^{2}}.
$$
Evaluate $\ln200=\ln2+\ln100\approx0.693147+4.605170=5.298317$.

*For $\delta=10^{-3}$*:
$$
N\ge\frac{5.298317}{2\times10^{-6}}=2.649159\times10^{6}.
$$
*For $\delta=10^{-4}$*:
$$
N\ge\frac{5.298317}{2\times10^{-8}}=2.649159\times10^{8}.
$$
The per-shot error floor also bounds resolvability: discrepancies $\delta\lesssim p_{e}=9\times10^{-5}$ are comparable to the readout noise per shot. For comparison, [10] reports $N\ge2500$ shots for one-sigma resolution of the much larger discrepancy $\Delta p=0.01$ with a leakage-resolving measurement; the Hoeffding budget at $\delta=10^{-3}$ is about three orders of magnitude larger, reflecting the square-law cost of pushing discrimination to smaller signals.

### 4.5 A two-ontology toy model with two fixed points

We now exhibit the underdetermined regime explicitly. Let the operational datum be a single scalar $x\in\mathbb{R}$ (a normalized discrepancy between predicted and observed readout statistics), with two candidate ontologies $A$ and $B$:
$$
T_{A}(x)=0.5\,x+0.5\,a,\qquad
T_{B}(x)=0.5\,x+0.5\,b,
$$
with ontology-dependent offsets $a\neq b$, and a selection rule that keeps the branch whose prediction is closer. Solving $x=T_{A}(x)$ gives $x_{A}^{*}=a$; similarly $x_{B}^{*}=b$. Each branch is contractive with $L=0.5<1$, so both fixed points are locally attracting; the failure of uniqueness comes from the multiplicity of branch fixed points, not from divergence.

**Concrete numbers.** Take $a=0$, $b=1$, and initial guess $x_{0}=0.6$. The basin boundary is the midpoint $m=(a+b)/2=0.5$; since $x_{0}>m$, the iteration follows branch $B$:
$$
x_{1}=0.5\times0.6+0.5=0.8,\quad
x_{2}=0.5\times0.8+0.5=0.9,\quad
x_{3}=0.5\times0.9+0.5=0.95,
$$
with closed form $x_{n}=1-0.4\times0.5^{n}$. The iteration converges to $x_{B}^{*}=1$ and never visits branch $A$. The two ontologies are physically inequivalent—say, an energy eigenmode with offset $a=0$ versus a collective variable with offset $b=1$—yet each is exactly self-consistent on its own basin, and the final ontology is determined by the *initial guess*, not by the data.

### 4.6 Symmetry-breaking sensitivity (projection)

If the readout channel had a small non-equivariant component—an asymmetry $\epsilon$ between the two readout axes—the smallest detectable asymmetry is bounded by the total estimation uncertainty:
$$
\epsilon_{\min}\approx\sqrt{\sigma_{p}^{2}+p_{e}^{2}}.
$$
With $N=10^{4}$ (Derivation 4.2):
$$
\epsilon_{\min}\approx\sqrt{(5.00\times10^{-3})^{2}+(9\times10^{-5})^{2}}
=\sqrt{2.5\times10^{-5}+8.1\times10^{-9}}
=\sqrt{2.50081\times10^{-5}}.
$$
Since $\sqrt{2.5\times10^{-5}}=5.00\times10^{-3}$ and the correction