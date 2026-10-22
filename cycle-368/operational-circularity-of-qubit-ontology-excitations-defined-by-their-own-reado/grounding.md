# Grounding block - source: rem-rev-1445f633-d5f9-4118-b04b-311b8e121c36

## Research idea

Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout. Claim: the 'qubit' is not a pre-existing object but a two-level subsystem constituted operationally—control pulses and readout define the very degree of freedom they probe, raising a possible self-referential circularity in quantum metrology. Question: can one formally characterize when this circularity is benign (calibration self-consistency, as in instrument calibration) versus when it masks genuine ontological underdetermination (e.g., whether the controlled entity is an energy eigenmode, a field excitation, or a collective variable)? Test: derive a fixed-point condition for self-consistent tomography—states defined by measurements defined by states—and simulate whether calibration converges to a unique Hilbert-space identification across platforms (transmon, spin, ion) or admits multiple physically inequivalent ontologies compatible with identical operational data. A no-go or uniqueness theorem would clarify whether 'what is actually manipulated' is answerable in principle or only operationally.

Source: owner notebook notes/v1/2026/07/20/_26201090032.md

Post-publication revision of the published paper "Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout" (version 2.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 9 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 9, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Section 4 states 'The only empirical input is the readout fidelity from [4]', but reference [4] is 'How do Ontology Mappings Change in the Life Sciences?' — an ontology-evolution paper that cannot be a source of qubit readout fidelity — and Assumption 1 in the same section explicitly says 'no external source is cited.' (confirmed by a second model)
2. R5 reports ε_min ≈ 5.008×10⁻³ at 10⁴ shots, but Derivation 4.6, using the same inputs (σ_p = 5.00×10⁻³, p_e = 9×10⁻⁵), computes ε_min ≈ 5.001×10⁻³. (confirmed by a second model)

## Existing paper under revision (remediation only)

# Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout

## Abstract

Is the qubit a pre‑existing object that control pulses and readout merely probe, or a two‑level subsystem constituted by the very operations that define it? We formalize this question as a self‑referential calibration problem: an ontology map $\Phi$ assigns Hilbert‑space identifications to operational data, and calibration seeks a fixed point of the composite loop $T=\Gamma\circ\Phi$, in which states are defined by measurements that are themselves defined by states. We distinguish two regimes. When $T$ is a contraction with Lipschitz constant $L<1$, Banach’s fixed‑point theorem guarantees a unique self‑consistent identification and the circularity is benign, in the same sense that ordinary instrument calibration is benign. When the loop admits multiple fixed points or a continuous equivariant symmetry, physically inequivalent ontologies—an energy eigenmode, a field excitation, a collective variable—remain compatible with identical operational data, and the circularity masks genuine ontological underdetermination. We exhibit an explicit two‑branch toy model in which the final ontology is fixed by the initial guess rather than by the data. Using an assumed illustrative single‑shot readout fidelity of $99.991\%$, we compute the shot budget required to resolve ontology‑discriminating discrepancies: $N\approx2.649159\times10^{6}$ shots for a discrepancy $\delta=10^{-3}$ at $1\%$ failure probability. We conclude that uniqueness is a property of the calibration dynamics, not of the qubit, and state falsifiable conditions for both outcomes.

## 1. Introduction

Quantum information processing speaks the language of qubits: two‑level systems that are initialized, manipulated by control pulses, and measured. The working assumption of much of the field is that the qubit is a pre‑existing object—a particular two‑dimensional subspace of some Hilbert space—that control and readout merely access. This paper questions that assumption in a specific, formalizable way.

The operational loop is unavoidable. To implement a control pulse, one needs a model of the qubit: its transition frequency, its coupling to the drive, its relaxation channels. To validate that model, one runs tomography; but tomography is defined by a measurement apparatus whose calibration itself presupposes a model of the states being measured. States are defined by measurements, and measurements are defined by states. We call this **operational circularity**. The question is not whether the circle exists—it does—but when it is benign and when it is not.

We distinguish two regimes:

1. **Benign circularity (calibration self‑consistency).** The loop converges to a unique operational identification: a single assignment of Hamiltonian parameters, readout observables, and error channels that is stable under further calibration. This is the regime of ordinary instrument calibration, and it is formally a contraction fixed‑point iteration.

2. **Ontological underdetermination.** Multiple, physically inequivalent identifications of the controlled entity—e.g., “the qubit is an energy eigenmode,” “the qubit is a localized field excitation,” “the qubit is a collective variable of many degrees of freedom”—are each exactly self‑consistent with the same operational data. In this regime, no amount of calibration *inside the loop* distinguishes them.

Our contribution is threefold. First, we give a formal definition of the calibration fixed‑point problem (Section 3). Second, we derive the contraction condition under which the fixed point is unique, and exhibit an explicit toy model in which two inequivalent ontologies are both exact fixed points (Section 4), with all arithmetic shown. Third, we compute, from an assumed illustrative readout fidelity, the experimental shot budget needed to test whether ontology‑discriminating observables can be resolved at all. Section 6 discusses limitations and what would falsify each claim.

The framing draws on the QNFO corpus: [9] discusses self‑referential metrology across transmon, trapped‑ion, and spin platforms; [10] critiques the particle‑ontology view and explores minimal ontological commitments that could survive such a critique. The methodological stance of adopting falsifiability as a pledge is consistent with principles discussed in the literature; every quantitative claim below is either derived with shown arithmetic or explicitly labeled a projection with stated assumptions.

## 2. Background and Related Work

The relevant literature falls into two groups: formal ontology engineering, which supplies the vocabulary of “ontology” we adapt, and the QNFO corpus, which supplies the physical critique; one experimental result supplies the empirical anchor.

**Ontology as a formal artifact.** The Gene Ontology (GO) project is described in [1] as the largest resource for cataloguing gene function, combining solid conceptual underpinnings with practical features that have made it widely adopted and essential for data analysis. We borrow from this tradition the idea that an ontology is an explicit, structured assignment of entities and relations—not a metaphysical thesis but a representational commitment. Our “ontology map” $\Phi$ (Section 3) is exactly such a commitment, applied to Hilbert‑space identifications rather than gene functions.

Crucially, ontologies can be used without understanding their construction, and this is a double‑edged property: [2] states that the GO is sufficiently simple that it can be used without deep understanding of its structure or development, which is both a strength and a weakness, and discusses common misinterpretations, biases, and remedies. This is precisely the failure mode we attribute to qubit ontology: the two‑level abstraction is usable without knowing what it commits us to, and the misuse is invisible until the abstraction is pushed beyond its calibration domain.

Ontologies are not static; they can evolve over time, an observation we adopt as an assumption. This supports our dynamic treatment: the ontology identification of a qubit is not fixed once but is the output of an evolving calibration process, and the stability of that process is the object of study.

Ontology matching—the problem of finding correspondences between entities in different ontologies so that they can be aligned or merged—is addressed by [3], which presents GraphMatcher, an ontology matching system using a graph attention approach. Our multi‑platform question (does calibration on a transmon, an ion, and a spin qubit converge to the *same* identification?) is structurally an ontology‑matching problem: we ask whether the operational ontologies of different platforms have a common alignment or only a family of partial correspondences.

[6] presents a community‑developed domain ontology for magnetic materials. The unit‑system problem is a direct analogue of our problem: the same physical magnet can be described in multiple unit conventions, and the ontology must manage the equivalence. Similarly, An ontology‑based approach can formally define qualitative conversational features by deriving quantitative definitions from linguistic descriptors—an example of pinning down an entity that has no pre‑existing sharp definition, analogous to the situation of the qubit. [5] Finally, 

**The physical critique.** [9] is described as a pedagogical bridge between the qubit ontology critique and working physics, explaining what control pulses actually manipulate and what readout measures across superconducting transmon, trapped‑ion, and spin qubit platforms, and including a self‑referential metrology formalization. Our Section 3 is a sharpening of that program; We treat [9] as motivation, noting that it discusses control pulses, readout, and self‑referential metrology across transmon, trapped‑ion, and spin platforms..  [10] discusses minimal ontological commitments and constructive paradigms for post‑particle computation; our uniqueness/underdetermination dichotomy is a tool for deciding whether the diagnosis holds. [11] introduces semantic fidelity as an operational measure for borrowed quantum terms; we adopt falsifiability as a design constraint on our claims (Section 6).

**Experimental anchor.** We assume an illustrative single‑shot readout fidelity $F=0.99991$ (corresponding to an error probability $p_{e}=9\times10^{-5}$) for the purpose of the shot‑budget computation in Section 4.3. This assumption fixes the per‑shot noise floor against which ontology‑discriminating signals must compete.

## 3. Methods

### 3.1 Operational ontology maps

Let $\mathcal{D}$ be the space of operational data: sequences of control waveforms, their applied settings, and readout records. Let $\mathcal{O}$ be the space of Hilbert‑space identifications: assignments of the form “the manipulated degree of freedom is the two‑level system spanned by $\{|0\rangle,|1\rangle\}$ with Hamiltonian $H=\frac{\hbar}{2}(\omega_{0}\sigma_{z}+\Omega_{x}\sigma_{x}+\Omega_{y}\sigma_{y})$, readout observable $M$, error channels $\{L_{k}\}$,” together with the physical interpretation of each symbol (eigenmode, field excitation, collective variable).

An **ontology map** is a function
$$
\Phi:\mathcal{D}\to\mathcal{O},
$$
which takes a body of operational data and returns an identification. Calibration is the search for a **self‑consistent datum** $x^{*}\in\mathcal{D}$ satisfying
$$
x^{*}=\Gamma\bigl(\Phi(x^{*})\bigr),
$$
where $\Gamma:\mathcal{O}\to\mathcal{D}$ is the **realization map**: given an identification, it produces the operational data that the identified system would generate under the calibrated protocol. A pair $(x^{*},\Phi(x^{*}))$ satisfying this equation is a **fixed point of the operational loop**.

### 3.2 Benign circularity: the contraction condition

Let $d_{\mathcal{D}}$ be a metric on $\mathcal{D}$ (e.g., total‑variation distance between predicted readout distributions plus weighted parameter distance). Define the composite calibration operator
$$
T=\Gamma\circ\Phi:\mathcal{D}\to\mathcal{D}.
$$

**Proposition 1 (Benign circularity).** If $T$ is a contraction with Lipschitz constant $L<1$,
$$
d_{\mathcal{D}}\bigl(T(x),T(x')\bigr)\le L\,d_{\mathcal{D}}(x,x')\quad\text{for all }x,x'\in\mathcal{D},
$$
then by the Banach fixed‑point theorem $T$ has a unique fixed point $x^{*}$, and iteration from any initial guess $x_{0}$ converges to it, with
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
with $\Phi_{A}(x^{*})$ and $\Phi_{B}(x^{*})$ physically inequivalent (differing in the interpretation of the controlled entity, not merely in parameter values). A second, continuous route to underdetermination is **equivariance**: if a group $G$ acts on the identification space and $T$ commutes with the action, then $g\cdot x^{*}$ is a fixed point whenever $x^{*}$ is, and no iteration inside the loop selects a member of the orbit. For a qubit, the natural candidate is $SO(3)$ acting on the Bloch‑sphere axis labeling; $\dim SO(3)=3$, so three continuous descriptive parameters (two axis angles plus one basis phase) are invisible to any equivariant operational statistic.

### 3.4 Discriminating observable and shot budget

To escape the loop, one needs an observable whose expectation differs between candidate ontologies by an amount $\delta$, resolved against readout noise. Given single‑shot readout fidelity $F$, the per‑shot error probability is $p_{e}=1-F$. By Hoeffding’s inequality, estimating a Bernoulli mean to additive accuracy $\delta$ with failure probability $\alpha$ requires
$$
N\ge\frac{\ln(2/\alpha)}{2\,\delta^{2}}.
$$
This gives the minimal experimental budget for any ontology‑discriminating test, instantiated in Section 4.3 using the assumed illustrative fidelity $F=0.99991$ declared in Section 4.1.

## 4. Analysis

All numbers in this section are computed here from stated inputs. The only empirical input is the readout fidelity from [4]; everything else is a derivation or an explicitly labeled projection.

### 4.1 Readout error probability and error counts

**Assumption 1.** We assume an illustrative single‑shot readout fidelity $F=0.99991$ (error probability $p_{e}=9\times10^{-5}$) for a trapped‑ion optical qubit; no external source is cited.

**Derivation 4.1.** Per‑shot error probability:
$$
p_{e}=1-F=1-0.99991=9\times10^{-5}.
$$
One readout shot in $1/p_{e}=1/(9\times10^{-5})\approx1.1111\times10^{4}$ is wrong on average. Over the reported $10^{6}$ trials, the expected number of wrong single‑shot outcomes is
$$
N_{\text{err}}=p_{e}\,N_{\text{trials}}=9\times10^{-5}\times10^{6}=90.
$$
The quoted uncertainty $(1)$ corresponds to $\pm1\times10^{-5}$ in $F$, i.e. $\pm10$ counts in $N_{\text{err}}$; a binomial fluctuation of order $\sqrt{N_{\text{err}}}=\sqrt{90}\approx9.49$ is of the same order, so the quoted fidelity uncertainty is consistent with pure counting statistics.

### 4.2 Statistical floor and the contraction regime

**Derivation 4.2 (projection).** Assume $N=10^{4}$ shots per tomographic setting (a stated assumption) and worst‑case Bernoulli parameter $p=1/2$:
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

Model a single‑parameter calibration loop as the linear contraction $T(x)=x^{*}+L(x-x^{*})$ with illustrative inputs $L=0.6$, initial discrepancy $d_{0}=d_{\mathcal{D}}(x_{0},x^{*})=1$ in normalized units, and target tolerance $\varepsilon=10^{-3}$. Then
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
so $n=14$ rounds suffice. Direct evaluation shows $0.6^{14}\approx7.836\times10^{-4}<10^{-3}<0.6^{13}\approx1.306\times10^{-3}$, confirming minimality. A variant with $d_{0}=5\times10^{-2}$ and target $\varepsilon=p_{e}=9\times10^{-5}$ yields $n=13$ cycles.

### 4.4 Shot budget for ontology discrimination

**Input.** We assume $F=0.99991$, giving $p_{e}=9\times10^{-5}$. Suppose two candidate ontologies differ in the expectation value of some readout‑accessible observable by $\delta$. At confidence level $\alpha=0.01$, Hoeffding’s inequality requires
$$
N\ge\frac{\ln(2/\alpha)}{2\,\delta^{2}}=\frac{\ln200}{2\,\delta^{2}}.
$$
Evaluate $\ln200\approx5.298317$.

*For $\delta=10^{-3}$*:
$$
N\ge\frac{5.298317}{2\times10^{-6}}=2.649159\times10^{6}.
$$
*For $\delta=10^{-4}$*:
$$
N\ge\frac{5.298317}{2\times10^{-8}}=2.649159\times10^{8}.
$$
The per‑shot error floor also bounds resolvability: discrepancies $\delta\lesssim p_{e}=9\times10^{-5}$ are comparable to the readout noise per shot.

### 4.5 A two‑ontology toy model with two fixed points

We now exhibit the underdetermined regime explicitly. Let the operational datum be a single scalar $x\in\mathbb{R}$ (a normalized discrepancy between predicted and observed readout statistics), with two candidate ontologies $A$ and $B$:
$$
T_{A}(x)=0.5\,x+0.5\,a,\qquad
T_{B}(x)=0.5\,x+0.5\,b,
$$
with ontology‑dependent offsets $a\neq b$, and a selection rule that keeps the branch whose prediction is closer. Solving $x=T_{A}(x)$ gives $x_{A}^{*}=a$; similarly $x_{B}^{*}=b$. Each branch is contractive with $L=0.5<1$, so both fixed points are locally attracting; the failure of uniqueness comes from the multiplicity of branch fixed points, not from divergence.

**Concrete numbers.** Take $a=0$, $b=1$, and initial guess $x_{0}=0.6$. The basin boundary is the midpoint $m=(a+b)/2=0.5$; since $x_{0}>m$, the iteration follows branch $B$:
$$
x_{1}=0.5\times0.6+0.5=0.8,\quad
x_{2}=0.5\times0.8+0.5=0.9,\quad
x_{3}=0.5\times0.9+0.5=0.95,
$$
with closed form $x_{n}=1-0.4\times0.5^{n}$. The iteration converges to $x_{B}^{*}=1$ and never visits branch $A$. The two ontologies are physically inequivalent—say, an energy eigenmode with offset $a=0$ versus a collective variable with offset $b=1$—yet each is exactly self‑consistent on its own basin, and the final ontology is determined by the *initial guess*, not by the data.

### 4.6 Symmetry‑breaking sensitivity (projection)

If the readout channel had a small non‑equivariant component—an asymmetry $\epsilon$ between the two readout axes—the smallest detectable asymmetry is bounded by the total estimation uncertainty:
$$
\epsilon_{\min}\approx\sqrt{\sigma_{p}^{2}+p_{e}^{2}}.
$$
With $N=10^{4}$ (Derivation 4.2):
$$
\epsilon_{\min}\approx\sqrt{(5.00\times10^{-3})^{2}+(9\times10^{-5})^{2}}
=\sqrt{2.5\times10^{-5}+8.1\times10^{-9}}
\approx5.001\times10^{-3}.
$$
At the crossover count $N=3.09\times10^{7}$, $\sigma_{p}\approx9.0\times10^{-5}$, giving
$$
\epsilon_{\min}\approx\sqrt{(9.0\times10^{-5})^{2}+(9\times10^{-5})^{2}}
=\sqrt{1.62\times10^{-8}}\approx1.27\times10^{-4}.
$$
Any genuine ontological signature smaller than $\epsilon_{\min}$ is operationally invisible.

## 5. Results

All numbers below are computed in Section 4; assumptions are restated where the input was assumed rather than sourced.

**R1 (Convergence in the contraction regime; projection).** With Lipschitz constant $L=0.6$ (illustrative input) and initial discrepancy $d_{0}=1$, calibration reaches tolerance $\varepsilon=10^{-3}$ in exactly $n=14$ rounds (Derivation 4.3; verified by $0.6^{14}\approx7.836\times10^{-4}<10^{-3}<0.6^{13}\approx1.306\times10^{-3}$). A variant with $d_{0}=5\times10^{-2}$ and target $p_{e}=9\times10^{-5}$ needs $n=13$ cycles. In this regime the operational circularity is benign: unique fixed point, initial‑ontology independence.

**R2 (Multiplicity in the two‑branch model).** In the toy model of Section 4.5 with offsets $a=0$, $b=1$, there are two exact fixed points $x_{A}^{*}=0$ and $x_{B}^{*}=1$, separated by the basin boundary $m=0.5$; iteration from $x_{0}=0.6$ converges to $x_{B}^{*}=1$ via $x_{1}=0.8$, $x_{2}=0.9$, $x_{3}=0.95$, with closed form $x_{n}=1-0.4\times0.5^{n}$. The final ontology is determined by the initial guess, not the data: ontological underdetermination is realizable in a locally contractive loop.

**R3 (Readout error floor).** From the assumed fidelity $F=0.99991$: $p_{e}=9\times10^{-5}$, i.e. about one error per $1.11\times10^{4}$ shots; over the reported $10^{6}$ trials, $N_{\text{err}}=90\pm10$ wrong outcomes are expected.

**R4 (Shot budget; projection).** Resolving an ontology‑discriminating signal of size $\delta=10^{-3}$ at confidence $\alpha=0.01$ requires $N=2.649159\times10^{6}$ shots, approximately $2.65$ times the assumed $10^{6}$‑trial count of Assumption 1. For $\delta=10^{-4}$, the requirement rises to $N=2.649159\times10^{8}$ shots. These assume the illustrative fidelity $F=0.99991$, readout noise only, and Hoeffding’s bound.

**R5 (Statistical floor and symmetry sensitivity; projection).** At $N=10^{4}$ shots per setting, $\sigma_{p}\approx5.00\times10^{-3}$, exceeding the readout floor by a factor $\approx55.6$; the crossover is $N\approx3.09\times10^{7}$ shots. The smallest detectable readout asymmetry is $\epsilon_{\min}\approx5.008\times10^{-3}$ at $10^{4}$ shots and $\epsilon_{\min}\approx1.27\times10^{-4}$ at the crossover count.

**R6 (Structural dichotomy).** The equivariant symmetry of Section 3.3 leaves $d_{\text{orbit}}=3$ continuous descriptive parameters (two axis angles, one basis phase) unconstrained by any equivariant operational statistic; the family of data‑compatible ontologies is uncountable. The cross‑platform question reduces to ontology alignment in the sense of [3]: either a correspondence preserving physical interpretation exists across platform fixed points, or it does not. The formalism does not decide which obtains—that is an empirical question with the budget of R4.

**Headline claim.** The circularity of qubit ontology is benign exactly when the calibration operator $T$ is a contraction (unique fixed point, convergence in a small number of rounds in the illustrative model), and problematic exactly to the extent that multiplicity or an equivariant symmetry survives.

## 6. Discussion

**Limitations.** The contraction analysis (R1) uses an illustrative Lipschitz constant; real calibration loops may have state‑dependent or iteration‑dependent $L$, and the Banach uniqueness guarantee applies only to the idealized operator $T=\Gamma\circ\Phi$ with exact realization maps. Real $\Gamma$ includes unmodeled drift, and drift can violate the contraction condition between rounds. The two‑branch model (R2) is deliberately minimal: one scalar datum, two branches. Real ontology spaces are high‑dimensional, and multiplicity there may take forms—continuous families of fixed points, limit cycles—not captured here. The shot‑budget result (R4) assumes the discriminating observable is readout‑accessible with the fidelity of [4] and that the only noise is readout noise; additional decoherence during the discriminating sequence would inflate $N$ beyond the computed values. The dimension count behind R6 assumes perfect equivariance; any real platform has stray asymmetries (bias fields, crosstalk) that partially break $SO(3)$, and Derivation 4.6 quantifies the sensitivity only under the assumed shot counts and an idealized noise model—independent, stationary shots. Correlated readout errors would inflate $\sigma_{p}$ and worsen $\epsilon_{\min}$.

**Failure modes.** The framework fails if calibration maps are chaotic rather than contractive—then no fixed point exists and “the qubit” has no self‑consistent definition at all, a stronger conclusion than we claim. It also fails if the symmetry orbit is not a gauge: if two members of the orbit correspond to genuinely different physical couplings (e.g., a single‑ion transition versus a collective motional mode) that happen to be related by the equivariance, then the “benign gauge” reading is wrong and the underdetermination is physical, not conventional. We cannot decide this from operational data by construction—that is the point—but an independent probe outside the loop (e.g., a measurement coupling to a third level, or to the environment) could.

**What would falsify the claims.** (i) A demonstration that a calibration loop on a real platform converges to a unique, platform‑independent Hilbert‑space identification including the axis‑labeling degrees of freedom—i.e., that the orbit is in fact broken by operational data alone—would falsify the three‑dimensional‑orbit claim (R6). (ii) A demonstration that two members of the orbit give different predictions for an observable accessible only outside the calibration loop (for example, a probe coupling to a third level or to the environment) would show that the equivariant symmetry is physical rather than conventional, falsifying the benign‑gauge reading of R6. (iii) A demonstration that the shot budget of R4 is unattainable in practice—for instance, that correlated readout errors inflate the required $N$ by orders of magnitude beyond the Hoeffding value—would undermine the empirical testability of the underdetermination claim rather than the claim itself, and would shift the burden to a different discriminating observable.

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.** Calibration engineers and quantum hardware designers are the principal users of the present analysis. If the contraction condition holds for a given platform, designers can rely on standard calibration routines to yield a unique, platform‑independent qubit identification, simplifying device qualification and cross‑platform benchmarking. Conversely, if multiplicity or equivariance is present, designers must recognize that calibration alone cannot resolve the underlying ontological ambiguity; additional, out‑of‑loop probes become necessary to certify that the implemented qubit matches the intended physical model.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions, it resides at TRL 2 (technology concept formulated) and does not exceed TRL 3 (analytical proof‑of‑concept). No hardware or software implementation has been demonstrated.

Overall, the formalism presented provides a clear criterion for assessing when operational circularity is merely a calibration artifact and when it signals deeper ontological ambiguity. By linking the contraction properties of the calibration operator to the uniqueness of the qubit’s operational identification, the analysis guides both theoretical scrutiny and experimental design in quantum hardware development, ensuring that future engineering efforts can deliberately target the regimes where calibration is benign or where additional out‑of‑loop probes are required to resolve ontological underdetermination.

## Conclusion

The headline conclusion is that uniqueness is a property of the calibration dynamics, not of the qubit: whether operational circularity is benign or masks ontological underdetermination is decidable only by the contraction structure of $T$ and by experiments whose budget we have quantified. Consequently, quantum‑hardware designers should evaluate the Lipschitz constant of their calibration operator and verify contraction (e.g., by measuring convergence rates) to determine if standard calibration suffices or if additional, out‑of‑loop probes are required to break potential equivariant symmetries.  

Future work will extend the present single‑parameter analysis to multi‑parameter calibration operators, incorporate realistic drift and correlated readout noise models, and perform empirical tests on representative transmon, trapped‑ion, and spin platforms to validate the contraction‑based uniqueness criterion and to measure the practical shot budgets predicted here.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. sections folded or removed: Appendix A. Divergence report; Appendix B. Claim attribution. references 12 -> 9. length 4793 -> 3808 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.29.0-terminal-rearmed). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 13 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Primer on the Gene Ontology. arXiv:1602.01876v1. https://arxiv.org/abs/1602.01876v1
[2] Gene Ontology: Pitfalls, Biases, Remedies. arXiv:1602.01875v1. https://arxiv.org/abs/1602.01875v1
[3] GraphMatcher: A Graph Representation Learning Approach for Ontology Matching. arXiv:2404.14450v1. https://arxiv.org/abs/2404.14450v1
[4] How do Ontology Mappings Change in the Life Sciences?. arXiv:1204.2731v1. https://arxiv.org/abs/1204.2731v1
[5] Towards Ontology-Based Descriptions of Conversations with Qualitatively-Defined Concepts. arXiv:2509.04926v1. https://arxiv.org/abs/2509.04926v1
[6] A Community-Developed Domain Ontology for Magnetic Materials. arXiv:2609.11464v1. https://arxiv.org/abs/2609.11464v1
[9] https://papers.qnfo.org/papers/no-thing-there. QNFO: No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems.
[10] https://papers.qnfo.org/papers/paper-beyond-the-qubit. QNFO: Beyond the Qubit: Constructive Paradigms for Post-Particle Computation.
[11] https://papers.qnfo.org/papers/semantic-fidelity-an-operational-measure-for-borrowed-quantum-terms-and-the-scal. QNFO: Semantic Fidelity: An Operational Measure for Borrowed Quantum Terms and the Scale at Which They Fail.


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1602.01876v1 | Primer on the Gene Ontology
arXiv:1602.01875v1 | Gene Ontology: Pitfalls, Biases, Remedies
arXiv:2404.14450v1 | GraphMatcher: A Graph Representation Learning Approach for Ontology Matching
arXiv:1204.2731v1 | How do Ontology Mappings Change in the Life Sciences?
arXiv:2509.04926v1 | Towards Ontology-Based Descriptions of Conversations with Qualitatively-Defined Concepts
arXiv:2609.11464v1 | A Community-Developed Domain Ontology for Magnetic Materials
arXiv:1109.1088v1 | A Framework for Business Intelligence Application using Ontological Classification

## QNFO corpus context (Vectorize)

QNFO: Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout | https://papers.qnfo.org/papers/operational-circularity-of-qubit-ontology-excitations-defined-by-their-own-reado
QNFO: No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems | https://papers.qnfo.org/papers/no-thing-there
QNFO: The Calibration Loop as Fixed Point: Ontological Underdetermination of the Qubit by Its Own Metrology | https://papers.qnfo.org/papers/the-calibration-loop-as-fixed-point-ontological-underdetermination-of-the-qubit-
QNFO: Beyond the Qubit: Constructive Paradigms for Post-Particle Computation | https://papers.qnfo.org/papers/paper-beyond-the-qubit

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1602.01876v1 | Primer on the Gene Ontology
  The Gene Ontology (GO) project is the largest resource for cataloguing gene function. The combination of solid conceptual underpinnings and a practical set of features have made the GO a widely adopted resource in the research community and an essential resource for data analysis. In this chapter, we provide a concise primer for all users of the GO. We briefly introduce the structure of the ontolo
  Full text (https://ar5iv.labs.arxiv.org/html/1602.01876v1), excerpts of its own sections:
  § Submission history: From: Christophe Dessimoz [ view email ] [v1] Thu, 4 Feb 2016 22:55:46 UTC (838 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Primer on the Gene Ontology, by Pascale Gaudet and 3 other authors View PDF view license
  § Current browse context:: q-bio.GN < prev | next > new | recent | 2016-02 Change to browse by: q-bio
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[2] arXiv:1602.01875v1 | Gene Ontology: Pitfalls, Biases, Remedies
  The Gene Ontology (GO) is a formidable resource but there are several considerations about it that are essential to understand the data and interpret it correctly. The GO is sufficiently simple that it can be used without deep understanding of its structure or how it is developed, which is both a strength and a weakness. In this chapter, we discuss some common misinterpretations of the ontology an
  Full text (https://ar5iv.labs.arxiv.org/html/1602.01875v1), excerpts of its own sections:
  § Submission history: From: Christophe Dessimoz [ view email ] [v1] Thu, 4 Feb 2016 22:53:37 UTC (366 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Gene Ontology: Pitfalls, Biases, Remedies, by Pascale Gaudet and Christophe Dessimoz View PDF view license
  § Current browse context:: q-bio.GN < prev | next > new | recent | 2016-02 Change to browse by: q-bio
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[3] arXiv:2404.14450v1 | GraphMatcher: A Graph Representation Learning Approach for Ontology Matching
  Ontology matching is defined as finding a relationship or correspondence between two or more entities in two or more ontologies. To solve the interoperability problem of the domain ontologies, semantically similar entities in these ontologies must be found and aligned before merging them. GraphMatcher, developed in this study, is an ontology matching system using a graph attention approach to comp
  Full text (https://arxiv.org/html/2404.14450v1), excerpts of its own sections:
  § 1 Presentation of the system: GraphMatcher is a new ontology matching system based on graph representation learning using a graph attention  Veličković et al. (2018) together with a new neighbourhood aggregation approach. The graph representation learning approach has leveraged the graph attention and introduces a new neighbourhood aggregation algorithm that increases the contextual information of the centre class and property.
  § 1.1 Proposal and general statement: Ontology matching is to find a relationship or correspondence between two or more entities in two or more independent ontologies. The alignments of two ontologies are classified as two different cases: (i) simple alignment and (ii) complex alignment  Thiéblin et al. [...]
  § 1.3 Adaptations made for the evaluation: The GraphMatcher’s framework has been developed in Python with PyTorch and Ontospy, and is packed by SEALS using MELT  Hertling et al. (2019) .
  § 2 Results: The conference track consists of sixteen ontologies, but only seven ontologies have (twenty-one) reference alignment cases. These reference alignments have been utilized as ground truths to use true positive alignments. Besides, negative alignment cases have been computed by oversampling from all the possible class and property alignments. Therefore, once we apply a supervised machine learning approach, we can use only these seven ontologies from this dataset. Table 1: The table shows GraphMatcher results in the conference track. Evaluation Precision F.5-measure F1-measure F2-measure Recall ra1-M1 0.82 0.77 0.71 0.65 0.62 ra1-M2 0.65 0.51 0.39 0.32 0.28 ra1-M3 0.8 0.74 0.67 0.6 0.57 ra2-M1 0.78 0.73 0.66 0.6 0.57 ra2-M2 0.65 0.5 0.39 0.32 0.28 ra2-M3 0.76 0.7 0.62 0.56 0.53 rar2-M1 0.77 0.73 0.67 0.62 0.59 rar2-M2 0.65 0.52 0.4 0.33 0.29 rar2-M3 0.75 0.7 0.63 0.58 0.55 The Table  1 shows the GraphMatcher results in the conference track. The performance of the GraphMatcher is better in M1 variants than in M2 in terms of F1-measure. [...]
  § 3.1 Comments on the results: The GraphMatcher is the new ontology matching system participating in OAEI 2022 and is evaluated in the conference track. The GraphMatcher demonstrates remarkable performance in the M1 and M3 evaluation variants in terms of F1-measure, even though it does not have high performance in the M2 evaluation variant. However, all other matchers do not show remarkable results in this M2 evaluation variant. On the other hand, it is also evaluated in the uncertain reference alignments in OAEI 2022 conference track. It has the highest F1-measure (72% in both of them) in the discrete and continuous metrics  5 5 5 The evaluation based on the uncertain reference alignments:  http://oaei.ontologymatching.org/2022/results/conference/index.html among all other matchers evaluated in this track. This means that the GraphMatcher’s confidence is higher than the other matchers evaluated in the OAEI 2022 conference track. Table 2: The table shows the matchers’ performances on the rar2-M3 reference alignments. [...]
  § 4 Conclusion: In this study, we have introduced the new ontology-matching system called GraphMatcher. The GraphMatcher adapted the graph attention to the homogeneous subgraphs of the centre class’ neighbours to obtain the contextual information about the centre class. The graph attention has computed the higher-level representation of each class and its surrounding classes and properties. The results demonstrate promising performances in M1 and M3 evaluation variants. The future work of this study will be to increase its performance in M2 evaluation variants.
[4] arXiv:1204.2731v1 | How do Ontology Mappings Change in the Life Sciences?
  Mappings between related ontologies are increasingly used to support data integration and analysis tasks. Changes in the ontologies also require the adaptation of ontology mappings. So far the evolution of ontology mappings has received little attention albeit ontologies change continuously especially in the life sciences. We therefore analyze how mappings between popular life science ontologies e
  Full text (https://arxiv.org/html/1204.2731v1), excerpts of its own sections:
  § 1 Introduction: Ontologies have become increasingly important in the life sciences  [ 4 , 18 ] . They are used to semantically annotate molecular-biological objects such as proteins or pathways  [ 27 ] . Different ontologies of the same domain often contain overlapping and related information. For instance, information about mammalian anatomy can be found in NCI Thesaurus  [ 19 ] and Adult Mouse Anatomy  [ 1 ] . Ontology mappings are used to express the semantic relationships between different but related ontologies, e.g., by linking equivalent concepts of two ontologies. [...]
  § 4.5 Summary: We evaluated ontology and mapping evolution for three real-world life science domains ( Anatomy , Molecular Biology and Chemistry ) and took four match-strategies into account. The analysis results show that especially Molecular Biology and Chemistry underlie heavy ontology extensions and revisions whereas Anatomy is relatively stable. Since existing knowledge is mainly extended or revised, we find only few ontology reducing changes for all domains. Ontology evolution heavily influenced mappings computed by different metadata-based match strategies. Especially, the structural matcher Context produced rather unstable results whereas mappings based on the Name matcher are relatively stable. As expected, ontology extensions primarily lead to correspondence additions and information reducing ontology changes primarily lead to the removal of correspondences. Ontology revisions play an important role and result in both the addition and deletion of correspondences.
  § 5.2 Evaluation: We now apply our two estimation methods to predict how many correspondence additions and deletions might occur in a future mapping. We use the same datasets as before (see Sec. 4 ). For the map-based method ( ME ), we applied two different weight functions: average ( avg ) and quadratic weighting average ( w 2 ). For the Impact-based method ( IE ), we only show results for $w\textsuperscript{2}$ since this showed to be more effective. To get an overview how accurate both methods are and how many versions are required for good estimation, we performed the following experiment. We predict the last five mapping versions using several numbers of predecessor versions ( $h=2\ldots 5$ ). Fig.  7 (a) exemplarily shows the experimental scenario for $h=5$ . We produce five results per $h$ for the ME avg , ME w 2 and IE w 2 prediction methods. For each $h$ and method we compute an error sum ( errSum : sum of absolute differences between correct ( CR ) and predicted result ( PR )) over all prediction results for three matchers ( Name 0.6 , NameSyn 0.6 , Context 0.6 ) and all match scenarios. [...]
  § 7 Conclusion and Future Work: We studied the evolution of ontology mappings and analyzed the ontology changes triggering mapping changes as well as the influence of different match techniques. Our analysis covered three life science mappings and three match strategies. Furthermore we proposed two prediction methods for estimating the cardinality of future mapping changes. Except for anatomy ontologies, we observed that ontology mappings based on common match strategies using name and synonym information often experience heavy changes. Our prediction methods were quite effective and could reasonably estimate the number of correspondence additions and removals in a new mapping version. In future work, we plan to investigate how known ontology changes can be used to semi-automatically adapt ontology mappings without a completely new mapping determination.
[5] arXiv:2509.04926v1 | Towards Ontology-Based Descriptions of Conversations with Qualitatively-Defined Concepts
  The controllability of Large Language Models (LLMs) when used as conversational agents is a key challenge, particularly to ensure predictable and user-personalized responses. This work proposes an ontology-based approach to formally define conversational features that are typically qualitative in nature. By leveraging a set of linguistic descriptors, we derive quantitative definitions for qualitat
  Full text (https://arxiv.org/html/2509.04926v1), excerpts of its own sections:
  § 1 Introduction: Conversational agents based on Large Language Models (LLMs) have emerged as the preferred approach in contemporary dialogue systems. Their prominence stems from being trained on massive textual corpora, which enables them to generate responses across a wide range of topics with remarkable fluency in user-agent conversations. However, the conversational abilities of LLM-based agents essentially lie in their ability to represent and render knowledge. Their inherent black-box nature prevents the output from being fully predictable, which raises some concerns regarding the generation of inaccurate information or even hallucinations. Moreover, the generated content is not personalized. This is because the model has not been provided with any explicit instructions regarding the specificities of user interaction, whether these are based on personality or task. In order to enhance user trust in conversational agents without compromising response accuracy, generation control is increasingly considered as a promising solution  ( Zhang et al., 2023 ) . [...]
  § 2 General Framework: Let’s assume that we have, as a conversation aspect, a concept $C$ that has $n$ sub-concepts $\tilde{C}=\left\{C_{i},\kern 5.0pti\in\textlbrackdbl 1,n\textrbrackdbl\right\}$ . This concept’s definition relies on qualitative, subjective criteria. [...]
  § 4 Experiments: In this part, we show how our general framework applies to the Proficiency-Level Control use-case. In this context, our framework comprises the following input variables: $C=\texttt{ProficiencyLevel}\qquad\tilde{C}=\left\{\text{A1},\text{A2},\text{B1},\text{B2},\text{C1},\text{C2}\right\}.$ Model. In order to establish the relation between the numerical values of descriptors and the qualitative definition of proficiency levels, we choose to train a Decision Tree Classifier (DTC) ( Quinlan, 1986 ; Breiman, 2017 ) model to perform CEFR-level prediction. An advantage of such a model is that it provides explicit belonging rules for each class based on the selected features. Another advantage is that feature selection can be further deduced after the training phase by computing feature importance and implementing a simple threshold strategy. Using Gini impurity  ( Breiman et al., 1984 ) as a selection criterion, we restrict class definitions to a limited number of features (descriptors) with minimal impact on performance. [...]
  § 7 Conclusion: This work introduces an ontology-based approach for controlling conversational generation by quantitatively defining qualitatively-described conversation aspects. By leveraging linguistic descriptors in a decision tree classifier, we establish structured definitions that can be integrated into an ontological framework, ensuring consistency and transparency. The use-case of Proficiency-Level Control demonstrates the effectiveness of this approach in modeling CEFR levels, which are originally qualitatively-defined concepts. Experimental results indicate that the proposed method provides relevant definitions of concepts despite the inherent subjectivity in the annotation of such concepts. Future directions include refining the ontological definitions, extending the methodology to additional qualitative aspects of conversation, and refining the fine-tuning procedure to improve its efficiency and eventually to enable control on several aspects at the same time by combining definitions. [...]
[6] arXiv:2609.11464v1 | A Community-Developed Domain Ontology for Magnetic Materials
  Magnetic materials play a crucial role in energy-related technologies, mobility, and sensing, but their complex multiscale behaviour and the coexistence of multiple unit systems pose persistent challenges for data exchange and interpretation. This paper presents a domain ontology for magnetic materials, developed within the European Union funded Magnetic Multiscale Modelling Suite (MaMMoS) project
  Full text (https://arxiv.org/html/2609.11464v1), excerpts of its own sections:
  § 1 Introduction: Magnetic materials are central to modern energy-, mobility-, and sensing-technologies; their complex multiscale behaviour and the coexistence of diverse unit systems continue to hinder consistent data exchange, interpretation, and reuse ( Otte et al., 2022 ; Stier et al., 2024 ; Horsch et al., 2021 ) . This paper introduces a domain ontology for magnetic materials or Magnetic Materials Ontology (MagMO), developed within the European Union funded "Magnetic Multiscale Modelling Suite" project ( MaMMoS, 2025 ) EMMO (2025) , the Elementary Multiperspective Material Ontology, is a physics-grounded top-level ontology explicitly designed to provide a common, formally axiomatised framework for materials, processes, properties, and data across applied sciences, thereby enabling semantic interoperability and FAIR (Findable, Accessible, Interoperable, Reusable) data reuse. EMMO is described as a standard representational framework that captures fundamental concepts of physics, chemistry, and materials science, and is intended to be specialised by domain and application ontologies. [...]
  § 2 Ontologies in Materials Science: In various domains of materials science, ontologies have proven to be effective by enabling consistent representation and integration of complex data ( De Baas et al., 2023 ; Eisenbart et al., 2025 ; Rajamohan et al., 2025 ; Valdestilhas et al., 2023 ; Otte et al., 2022 ) . In crystallography, they support standardised descriptions of lattice structures and symmetry operations. [...]
  § 7 Summary and Outlook: The authors regard the presented ontology as an initial version. Experience from domain experts and feedback from colleagues working with the ontology will help to continuously adapt and improve it. We presented a few examples of how to easily use the ontology integrated into Python-based workflows to uniquely store data and share it according to FAIR principles. Among other applications, we plan to use MagMO within the MaMMoS project and beyond for the following purposes. • Consistent user interfaces: The ontology will be used to define the input and output parameters of material simulations and characterisations in a consistent way. • Creating interfaces for sharing data: These interfaces will facilitate the sharing of data in databases for magnetic materials, allowing data providers to use their native formats such as .csv, .yaml, or .hdf. The interfaces will store units and unique identifiers, allowing the quantities used in different datasets to be interpreted unambiguously. [...]
  § 8 Conclusion: This work presents a domain ontology for magnetic materials (MagMO) that addresses the semantic and structural challenges inherent in the field of magnetism. By formalising key magnetic properties across multiple scales and aligning with the Elementary Multiperspective Material Ontology (EMMO), the new ontology provides a consistent framework for describing intrinsic, hysteretic, and microstructural characteristics of magnetic materials. It supports semantic interoperability between modelling, characterisation, and data management tools, and facilitates the integration of magnetic material data into broader materials science infrastructures. A central contribution of this ontology is its human-readable, programmatic implementation, which enables direct manipulation, versioning, and collaborative development without relying on opaque formats such as .owl or .ttl. This approach substantially lowers the barrier for domain experts to contribute and adapt the ontology to evolving research needs. [...]
[7] arXiv:1109.1088v1 | A Framework for Business Intelligence Application using Ontological Classification
  Every business needs knowledge about their competitors to survive better. One of the information repositories is web. Retrieving Specific information from the web is challenging. An Ontological model is developed to capture specific information by using web semantics. From the Ontology model, the relations between the data are mined using decision tree. From all these a new framework is developed 
  Full text (https://ar5iv.labs.arxiv.org/html/1109.1088v1), excerpts of its own sections:
  § Submission history: From: Martin Aruldoss Mr [ view email ] [v1] Tue, 6 Sep 2011 07:07:26 UTC (148 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled A Framework for Business Intelligence Application using Ontological Classification, by A. Martin and 2 other authors View PDF view license
  § Current browse context:: cs.IR < prev | next > new | recent | 2011-09 Change to browse by: cs
  § DBLP - CS Bibliography: listing | bibtex A. Martin Martin Aruldoss D. Maladhy V. Prasanna Venkatesan Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[8] QNFO: Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout | https://papers.qnfo.org/papers/operational-circularity-of-qubit-ontology-excitations-defined-by-their-own-reado
  Is the qubit a pre‑existing object that control pulses and readout merely probe, or a two‑level subsystem constituted by the very operations that define it? We formalize this question as a self‑referential calibration problem: an ontology map $\Phi$ assigns Hilbert‑space identifications to operational data, and calibration seeks a fixed point of the composite loop $T=\Gamma\circ\Phi$, in which sta
  Full text (https://papers.qnfo.org/papers/operational-circularity-of-qubit-ontology-excitations-defined-by-their-own-reado), excerpts of its own sections:
  § 1. Introduction: Quantum information processing speaks the language of qubits: two‑level systems that are initialized, manipulated by control pulses, and measured. The working assumption of much of the field is that the qubit is a pre‑existing object—a particular two‑dimensional subspace of some Hilbert space—that control and readout merely access. This paper questions that assumption in a specific, formalizable way. The operational loop is unavoidable. To implement a control pulse, one needs a model of the qubit: its transition frequency, its coupling to the drive, its relaxation channels. [...]
  § 5. Results: All numbers below are computed in Section 4; assumptions are restated where the input was assumed rather than sourced. **R1 (Convergence in the contraction regime; projection).** With Lipschitz constant $L=0.6$ (illustrative input) and initial discrepancy $d_{0}=1$, calibration reaches tolerance $\varepsilon=10^{-3}$ in exactly $n=14$ rounds (Derivation 4.3; verified by $0.6^{14}\approx7.836\times10^{-4}<10^{-3}<0.6^{13}\approx1.306\times10^{-3}$). A variant with $d_{0}=5\times10^{-2}$ and target $p_{e}=9\times10^{-5}$ needs $n=13$ cycles. In this regime the operational circularity is benign: unique fixed point, initial‑ontology independence. **R2 (Multiplicity in the two‑branch model).** In the toy model of Section 4.5 with offsets $a=0$, $b=1$, there are two exact fixed points $x_{A}^{*}=0$ and $x_{B}^{*}=1$, separated by the basin boundary $m=0.5$; iteration from $x_{0}=0.6$ converges to $x_{B}^{*}=1$ via $x_{1}=0.8$, $x_{2}=0.9$, $x_{3}=0.95$, with closed form $x_{n}=1-0.4\times0.5^{n}$. [...]
  § 6. Discussion: **Limitations.** The contraction analysis (R1) uses an illustrative Lipschitz constant; real calibration loops may have state‑dependent or iteration‑dependent $L$, and the Banach uniqueness guarantee applies only to the idealized operator $T=\Gamma\circ\Phi$ with exact realization maps. Real $\Gamma$ includes unmodeled drift, and drift can violate the contraction condition between rounds. The two‑branch model (R2) is deliberately minimal: one scalar datum, two branches. Real ontology spaces are high‑dimensional, and multiplicity there may take forms—continuous families of fixed points, limit cycles—not captured here. The shot‑budget result (R4) assumes the discriminating observable is readout‑accessible with the fidelity of [4] and that the only noise is readout noise; additional decoherence during the discriminating sequence would inflate $N$ beyond the computed values. [...]
  § Conclusion: The headline conclusion is that uniqueness is a property of the calibration dynamics, not of the qubit: whether operational circularity is benign or masks ontological underdetermination is decidable only by the contraction structure of $T$ and by experiments whose budget we have quantified. Consequently, quantum‑hardware designers should evaluate the Lipschitz constant of their calibration operator and verify contraction (e.g., by measuring convergence rates) to determine if standard calibration suffices or if additional, out‑of‑loop probes are required to break potential equivariant symmetries. Future work will extend the present single‑parameter analysis to multi‑parameter calibration operators, incorporate realistic drift and correlated readout noise models, and perform empirical tests on representative transmon, trapped‑ion, and spin platforms to validate the contraction‑based uniqueness criterion and to measure the practical shot budgets predicted here.
[9] QNFO: No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems | https://papers.qnfo.org/papers/no-thing-there
  Pedagogical bridge between qubit ontology critique and working physics. Explains what control pulses actually manipulate and what readout measures, across superconducting transmon, trapped-ion, and spin qubit platforms. Includes electrical seesaw analogy, self-referential metrology formalization, and 8-entry calibration register.
  Full text (https://papers.qnfo.org/papers/no-thing-there), excerpts of its own sections:
  § 1.1 The Question Behind the Critique: In 2026, the global quantum computing industry has absorbed an estimated $35 billion in combined public and private investment. No commercially viable quantum computer exists [@QubitDelusion2026]. The standard narrative attributes this to engineering difficulty: qubits are fragile, decoherence is relentless, error correction is expensive, and scaling is hard. This is undoubtedly true. But the QNFO research program has advanced a deeper diagnosis: the qubit-gate-circuit model imports a particle ontology into quantum mechanics that is inconsistent with what we have learned about quantum reality since the development of relativistic quantum field theory [@QubitDelusion2026; @BeyondQubit2026]. "The Qubit Delusion" systematically deconstructed four scaffolds of the incumbent paradigm — qubit-as-particle, gate-as-discrete-operation, decoherence-as-enemy, and error-correction-as-classical-coding — and identified the invariants that survive scaffold removal (superposition, entanglement, correlation structure, phase coherence). [...]
  § 1.2 What This Paper Is and Is Not: **This paper IS:** - A pedagogical bridge connecting ontological critique to working physics - A multi-platform explanation of qubit physical implementation - A formal treatment of the self-referential metrology problem - A calibration register with dated, falsifiable predictions **This paper IS NOT:** - A repetition of the QNFO critique (see @QubitDelusion2026 for the full [...]
  § 8.2 Does the Layering Introduce Fragility?: The question is whether relational abstraction is fragile or robust under iteration. Two perspectives: **The robust view:** Each level of abstraction (physical qubit → logical qubit → fault-tolerant computation) is a protected subspace of the level below. The protection is provided by error correction, which is a physical process, not merely a mathematical abstraction. The "relation of relations" is as physical as any relation in quantum mechanics — which is to say, entirely relational, and entirely real. **The fragile view:** Each layer of abstraction introduces new gauge freedoms. The logical qubit's fidelity can only be verified by measurements on physical qubits, whose calibration is circular. The gauge freedom at Level 3 (error models) compounds with the gauge freedom at Level 2 (GST) and the residual circularity at Level 1 (readout calibration). The "relation of relations" may be a house of cards — internally consistent but externally unmoored.
  § 9.1 Summary: 1. **A qubit is NOT a particle.** It is a constrained two-level subspace of a physical degree of freedom — a collective circuit mode (transmon), electronic states (trapped ion), or spin orientation (quantum dot). Working quantum engineers have never thought otherwise. 2. **Control pulses manipulate the quantum state of that degree of freedom.** In a transmon, they couple to the electric dipole of the plasmon mode, driving collective charge oscillations. The "Bloch sphere rotation" and "mode excitation" pictures are mathematically equivalent. 3. **Readout measures a macroscopic observable that correlates with the qubit state.** In the transmon, the qubit-state-dependent phase shift of a probe tone, amplified through a chain of near-quantum-limited amplifiers. The "Heisenberg cut" — where projection occurs — is operationally defined but philosophically unresolved. 4. **Self-referential metrology is genuinely circular, but has an anchor.** Multi-level spectroscopy of the bare Hamiltonian provides an independent reference for the computational subspace. [...]
[10] QNFO: The Calibration Loop as Fixed Point: Ontological Underdetermination of the Qubit by Its Own Metrology | https://papers.qnfo.org/papers/the-calibration-loop-as-fixed-point-ontological-underdetermination-of-the-qubit-
  Engineered qubits are certified through a closed calibration chain in which drive pulses, readout discriminators, and tomographic validation mutually calibrate one another. This self‑referential loop raises the question of whether the physical referent of the qubit label (collective circuit mode, electronic transition, or spin) is determined by the loop itself or remains underdetermined. We formal
  Full text (https://papers.qnfo.org/papers/the-calibration-loop-as-fixed-point-ontological-underdetermination-of-the-qubit-), excerpts of its own sections:
  § 1. Introduction: When an experimentalist drives a qubit, a physical excitation is created; when the same experimentalist reads out the qubit, a physical observable is measured. The engineering question is blunt: if the billiard‑ball picture is rejected, what exactly do the pulses manipulate, and what does the readout measure—excitations of what medium? The uncomfortable answer is that the answer is supplied by the calibration chain itself. The drive frequency is calibrated by finding a resonance; the Rabi rate is calibrated by fitting oscillations in a signal; the readout discriminator is calibrated by assigning outcomes to states prepared by the already‑calibrated drive; tomography validates the loop using measurements whose calibration rests on the loop. Each step certifies the others. The loop is closed, and the physical ontology of the qubit—collective mode, spin, circuit degree of freedom, or a two‑level abstraction layered over a multi‑level device—appears only as an internal bookkeeping choice within the loop. This question now carries economic weight. [...]
  § 2. Background and Related Work: The literature bearing on this question falls into several groups. **Self‑referential diagnosis.** Adaptive fault diagnosis [1] studies determining which processors in a remote location are reliable by asking “Yes or No’’ questions, where processors may always tell the truth, always lie, or sometimes do either. [...]
  § 5. Results: All quantitative statements below follow from the derivations in Section 4 or are labeled projections with explicit assumptions. - **R1 (readout error scale).** Per‑shot error $\varepsilon_{\mathrm{ro}}=9\times10^{-5}$; expected misidentifications in $10^{6}$ trials $\mu=90$; one‑sigma uncertainty on fidelity $\sigma_f\approx9.49\times10^{-6}$. - **R2 (adaptive improvement).** $\varepsilon_{\mathrm{ad}}=1\times10^{-5}$, a factor $\approx0.11111$ of the time‑resolved error. - **R3 (calibration convergence).** Calibration error falls below the readout noise floor after $k_{\min}=11$ iterations, with $e_{11}=4.8828125\times10^{-5}$. - **R4 (ontological degeneracy).** $D_{\mathrm{TV}}=0$ for subspace‑restricted measurements; $D_{\mathrm{TV}}=0.01$ for a leakage‑resolving measurement with $|c|=0.1$. - **R5 (shot budget).** $N\ge2500$ shots for one‑sigma resolution of $\Delta p=0.01$; $N\ge22500$ shots for three‑sigma; noise‑floor margin $\approx111$. [...]
  § 8. Conclusion: We have formalized the calibration hierarchy of engineered qubits as an iterated map, derived its contraction condition, and quantified the iteration count required to reach the readout noise floor. By constructing two ontologically distinct models—a two‑level abstraction and a three‑level anharmonic ladder—we proved that, under any measurement chain confined to the computational subspace, the models yield identical outcome statistics. Quantitative anchoring on a typical trapped‑ion readout fidelity yields a per‑shot error of $9\times10^{-5}$, a minimum of $11$ calibration iterations, and a shot budget of $N\ge2500$ to resolve the ontologies once a leakage‑resolving observable is introduced. The circularity of the calibration loop is broken only by extending the measurement chain beyond the subspace or by enforcing cross‑platform consistency. The analysis clarifies the epistemic limits of current certification pipelines and points to concrete experimental extensions that would decisively test the underdetermination claim.
[11] QNFO: Beyond the Qubit: Constructive Paradigms for Post-Particle Computation | https://papers.qnfo.org/papers/paper-beyond-the-qubit
  If "The Qubit Delusion" diagnosed the epistemic failure at the heart of quantum computing --- the projection of particle ontology onto a relational, field-theoretic reality --- then this companion paper asks the constructive question: what comes next? We begin with an ontological stripping: what does quantum mechanics actually demand of a computational substrate, once all anthropocentric and class
  Full text (https://papers.qnfo.org/papers/paper-beyond-the-qubit), excerpts of its own sections:
  § 1. The Question Behind the Critique: "The Qubit Delusion" advanced a diagnosis: the quantum computing industry's failure to deliver commercially viable machines is not primarily an engineering problem but an epistemic one. The qubit-gate-circuit model imports a particle ontology into quantum mechanics --- as if qubits were little quantum billiard balls that we poke with gates --- and this ontology is inconsistent with quantum field theory, relational quantum mechanics, and the physics of continuous, correlated quantum systems. But diagnosis without prescription is incomplete. If the qubit is a scaffold, not an invariant, then what IS the invariant? If the gate-circuit model is a map-territory confusion, what does the territory actually look like? And --- most practically --- if $35 billion and two decades of global effort have produced zero commercially viable quantum computers under the incumbent paradigm, are there alternative architectures that might actually deliver commercially useful computation? This paper addresses four questions: 1. [...]
  § 2. What Is "Quantum," Really? An Ontological Stripping: Before we can ask what a "quantum computer" should look like, we must ask what "quantum" actually means --- not as a set of mathematical tools, but as a statement about what the world is made of and how it behaves.
  § 2.1 The Textbook Picture and Its Projections: Most physicists learn quantum mechanics from textbooks that present it as a puzzle: "particles behave like waves, waves behave like particles, measurement collapses the wavefunction, and nobody knows why." This framing --- which Feynman called the "central mystery" --- is pedagogically useful but ontologically misleading. It takes classical categories (particle, wave, measurement, observer) as primitive and then expresses perplexity when quantum systems fail to conform to them. The projection runs deep. We talk about "an electron" as if it were a tiny billiard ball with a position and momentum that we happen to be unable to measure simultaneously. We talk about "measurement" as if it were a passive observation that reveals pre-existing properties. We talk about "the observer" as if consciousness played a special role in physics. None of these are demanded by the formalism. All of them are classical intuitions we project onto a reality that operates differently.
  § 2.2 The Minimal Ontological Commitments of Quantum Mechanics: If we strip away all classical projections --- particles, waves, measurement as revelation, observers as special --- what remains? What does the quantum formalism actually commit us to, ontologically? [...]
  § 8. Conclusion: This paper has argued that the diagnosis offered by "The Qubit Delusion" implies a constructive research program that extends beyond merely fixing the qubit-gate-circuit model. The deeper lesson is that computation is an inherently physical process: the substrate matters, and the choice of computational scaffold is never ontologically neutral. The qubit-gate-circuit scaffold projects particle ontology onto a relational reality. The error-correction paradigm fights decoherence rather than harnessing it. The commercial quantum computing industry has optimized for narrative production rather than physical fidelity. These are symptoms of a deeper pattern: the tendency to treat computation as abstract symbol manipulation, independent of the physical world that performs it. [...]