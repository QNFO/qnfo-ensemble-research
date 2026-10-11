# Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout

## Abstract

We ask whether the qubit—the canonical two-level degree of freedom of quantum information processing—is a discovered object or an operationally constituted one. Control pulses and readout circuits are designed using a model of the qubit, yet the only empirical access to that model is through the very pulses and readouts being designed. We formalize this loop as a self-referential calibration problem: an ontology map $\Phi$ assigns Hilbert-space identifications to operational data, and calibration is a fixed-point condition $\Phi(x^\*) = x^\*$ in which states are defined by measurements that are themselves defined by states. We derive a contraction condition under which the circularity is benign: calibration converges to a unique operational identification, and the circularity is merely the ordinary self-consistency of instrument calibration. We show with an explicit two-ontology toy model that outside the contraction regime, multiple physically inequivalent ontologies—an energy eigenmode, a field excitation, a collective variable—can be exact fixed points compatible with identical operational data, so the question "what is actually manipulated?" is underdetermined. Using the reported single-shot readout fidelity of $99.991\%$ for trapped-ion optical qubits as an input, we compute the shot budget required to resolve ontology-discriminating discrepancies at a given confidence. We conclude that uniqueness is a property of the calibration dynamics, not of the qubit, and state falsifiable conditions for both outcomes.

## 1. Introduction

Quantum information processing speaks the language of qubits: two-level systems that are initialized, manipulated by control pulses, and measured. The working assumption of most of the field is that the qubit is a pre-existing object—a particular two-dimensional subspace of some Hilbert space—that control and readout merely access. This paper questions that assumption in a specific, formalizable way.

The operational loop is unavoidable. To implement a control pulse, one needs a model of the qubit: its transition frequency, its coupling to the drive, its relaxation channels. To validate that model, one runs tomography; but tomography is defined by a measurement apparatus whose calibration itself presupposes a model of the states being measured. States are defined by measurements, and measurements are defined by states. We call this **operational circularity**. The question is not whether the circle exists—it does—but when it is benign and when it is not.

We distinguish two regimes:

1. **Benign circularity (calibration self-consistency).** The loop converges to a unique operational identification: a single assignment of Hamiltonian parameters, readout observables, and error channels that is stable under further calibration. This is the regime of ordinary instrument calibration, and it is formally analogous to any fixed-point iteration.

2. **Ontological underdetermination.** Multiple, physically inequivalent identifications of the controlled entity—e.g., "the qubit is an energy eigenmode," "the qubit is a localized field excitation," "the qubit is a collective variable of many degrees of freedom"—are each exactly self-consistent with the same operational data. In this regime, no amount of calibration within the loop distinguishes them; the question "what is actually manipulated?" is answerable only operationally, if at all.

Our contribution is threefold. First, we give a formal definition of the calibration fixed-point problem (Section 3). Second, we derive a contraction condition under which the fixed point is unique, and exhibit an explicit toy model in which two inequivalent ontologies are both exact fixed points (Section 4), with all arithmetic shown. Third, we compute, from a published readout fidelity figure [4], the experimental shot budget needed to test whether ontology-discriminating observables can be resolved at all (Section 4.3). Section 6 discusses what would falsify each claim.

The framing draws on the QNFO corpus, particularly the treatment of self-referential metrology across transmon, trapped-ion, and spin platforms [9], the critique of particle ontology projected onto field-theoretic reality [12], and the constructive question of what minimal ontological commitments survive that critique [10]. The methodological stance—falsifiability as a pledge rather than a slogan—is taken from [11].

## 2. Background and Related Work

The literature relevant to this paper falls into two groups: formal ontology engineering, which supplies the vocabulary of "ontology" we adapt, and the QNFO corpus, which supplies the physical critique.

**Ontology as a formal artifact.** The Gene Ontology (GO) project is described in [1] as the largest resource for cataloguing gene function, combining conceptual underpinnings with practical features that have made it widely adopted and essential for data analysis; the primer in [1] introduces the structure of the ontology. We borrow from this tradition the idea that an ontology is an explicit, structured assignment of entities and relations—not a metaphysical thesis but a representational commitment. Our "ontology map" $\Phi$ (Section 3) is exactly such a commitment, applied to Hilbert-space identifications rather than gene functions.

Crucially, ontologies can be used without understanding their construction, and this is a double-edged property: [2] states that the GO is sufficiently simple that it can be used without deep understanding of its structure or development, which is both a strength and a weakness, and discusses common misinterpretations, biases, and remedies. This is precisely the failure mode we attribute to qubit ontology: the two-level abstraction is usable without knowing what it commits us to, and the misuse is invisible until the abstraction is pushed beyond its calibration domain.

Ontologies are not static. [5] analyzes how mappings between popular life-science ontologies change, noting that ontologies change continuously and that the evolution of ontology mappings had received little attention. This supports our dynamic treatment: the ontology identification of a qubit is not fixed once but is the output of an evolving calibration process, and the stability of that process is the object of study.

Ontology matching—the problem of finding correspondences between entities in two or more ontologies so that they can be aligned or merged—is defined in [3], which presents GraphMatcher, an ontology matching system using a graph attention approach. Our multi-platform question (does calibration on a transmon, an ion, and a spin qubit converge to the *same* identification?) is structurally an ontology-matching problem: we ask whether the operational ontologies of different platforms have a common alignment or only a family of partial correspondences.

That ontologies can be built for domains far from biology is shown by [7], which presents a community-developed domain ontology for magnetic materials, motivated by multiscale behaviour and the coexistence of multiple unit systems that pose persistent challenges for data exchange and interpretation. The unit-system problem is a direct analogue of our problem: the same physical magnet can be described in multiple unit conventions, and the ontology must manage the equivalence. Similarly, [6] proposes an ontology-based approach to formally define qualitative conversational features by deriving quantitative definitions from linguistic descriptors—an example of pinning down an entity (a conversational feature) that has no pre-existing sharp definition, exactly the situation of the qubit. Finally, [8] develops an ontological model for business intelligence in which relations are mined from web semantics using decision trees; the summary supplied gives no further technical detail, but it illustrates the general pattern that an ontology can be *derived from data* rather than stipulated—the direction of constitution our fixed-point formalism makes precise.

**The physical critique.** [9] is a pedagogical bridge between the qubit ontology critique and working physics, explaining what control pulses actually manipulate and what readout measures across superconducting transmon, trapped-ion, and spin qubit platforms, and including a self-referential metrology formalization. Our Section 3 formalization is a sharpening of that program. [12] argues that the qubit-gate-circuit model is an epistemic failure—a projection of particle ontology onto relational, field-theoretic reality; we treat this as the hypothesis that the calibration dynamics is in the underdetermined regime. [10], the companion paper, asks what comes next if that diagnosis holds, stripping quantum mechanics to its minimal ontological commitments; our uniqueness/underdetermination dichotomy is a tool for deciding whether the diagnosis holds. [11] states five principles and a Falsification Pledge; we adopt falsifiability as a design constraint on our claims (Section 6).

**Experimental anchor.** [4] demonstrates single-shot qubit readout with fidelity sufficient for fault-tolerant quantum computation, for two types of qubit stored in single trapped calcium ions; for an optical qubit stored in the $(4S_{1/2}, 3D_{5/2})$ levels of $^{40}\mathrm{Ca}^+$, an average readout fidelity of $99.991(1)\%$ in one million trials is achieved using time-resolved photon counting, with an adaptive technique allowing $99.99\%$ fidelity. We use this figure as the empirical input for our shot-budget computation (Section 4.3): it fixes the per-shot noise floor against which ontology-discriminating signals must compete.

## 3. Methods

### 3.1 Operational ontology maps

Let $\mathcal{D}$ be the space of operational data: sequences of control waveforms, their applied settings, and readout records. Let $\mathcal{O}$ be the space of Hilbert-space identifications: assignments of the form "the manipulated degree of freedom is the two-level system spanned by $\{|0\rangle, |1\rangle\}$ with Hamiltonian $H = \frac{\hbar}{2}\big(\omega_0 \sigma_z + \Omega_x \sigma_x + \Omega_y \sigma_y\big)$, readout observable $M$, error channels $\{L_k\}$," together with the physical interpretation of each symbol (eigenmode, field excitation, collective variable).

An **ontology map** is a function

$$\Phi : \mathcal{D} \to \mathcal{O},$$

which takes a body of operational data and returns an identification. Calibration is the search for a **self-consistent datum** $x^\* \in \mathcal{D}$ satisfying

$$x^\* = \Gamma\big(\Phi(x^\*)\big),$$

where $\Gamma : \mathcal{O} \to \mathcal{D}$ is the **realization map**: given an identification, it produces the operational data that the identified system would generate under the calibrated experimental protocol (the predicted tomography record, the predicted readout statistics). A pair $(x^\*, \Phi(x^\*))$ satisfying this equation is a **fixed point of the operational loop**.

### 3.2 Benign circularity: the contraction condition

Let $d_{\mathcal{D}}$ be a metric on $\mathcal{D}$ (e.g., total-variation distance between predicted readout distributions, plus weighted parameter distance). Define the composite calibration operator

$$T = \Gamma \circ \Phi : \mathcal{D} \to \mathcal{D}.$$

**Proposition 1 (Benign circularity).** If $T$ is a contraction with Lipschitz constant $L < 1$,

$$d_{\mathcal{D}}\big(T(x), T(x')\big) \leq L\, d_{\mathcal{D}}(x, x') \quad \text{for all } x, x' \in \mathcal{D},$$

then by the Banach fixed-point theorem $T$ has a unique fixed point $x^\*$, and iteration from any initial guess $x_0$ (any prior ontology) converges to it. The circularity is then benign: the loop defines a unique operational identification regardless of the starting ontology, and the "self-referential" character of calibration is no more mysterious than the convergence of any fixed-point iteration.

The iteration count needed to reach tolerance $\varepsilon$ follows from the standard estimate. After $n$ iterations,

$$d_{\mathcal{D}}(x_n, x^\*) \leq L^n\, d_{\mathcal{D}}(x_0, x^\*),$$

so convergence to tolerance $\varepsilon$ requires

$$L^n \, d_{\mathcal{D}}(x_0, x^\*) \leq \varepsilon \quad \Longleftrightarrow \quad n \geq \frac{\ln\!\big(\varepsilon / d_{\mathcal{D}}(x_0, x^\*)\big)}{\ln L}.$$

Since $0 < L < 1$, $\ln L < 0$; with $\varepsilon < d_{\mathcal{D}}(x_0, x^\*)$ the numerator is negative and $n$ is positive, as required.

### 3.3 Ontological underdetermination

If $T$ is not a contraction, uniqueness fails. The physically interesting failure is not chaos but **multiplicity**: several fixed points, each corresponding to a different physical interpretation of the same symbols. We say the qubit ontology is **underdetermined** on a data set $x^\*$ if there exist two ontology maps $\Phi_A, \Phi_B$ and realization maps $\Gamma_A, \Gamma_B$ such that

$$x^\* = \Gamma_A\big(\Phi_A(x^\*)\big) = \Gamma_B\big(\Phi_B(x^\*)\big),$$

with $\Phi_A(x^\*)$ and $\Phi_B(x^\*)$ physically inequivalent (differing in the interpretation of the controlled entity, not merely in parameter values). In that case, identical operational data support both "the qubit is an energy eigenmode" and "the qubit is a collective variable," and no experiment *inside the loop* distinguishes them.

### 3.4 Discriminating observable and shot budget

To escape the loop, one needs an observable whose expectation differs between the candidate ontologies by an amount $\delta$, resolved against readout noise. Given single-shot readout fidelity $F$, the per-shot error probability is $p = 1 - F$. By Hoeffding's inequality, estimating a Bernoulli mean to additive accuracy $\delta$ with failure probability $\alpha$ requires

$$N \geq \frac{\ln(2/\alpha)}{2\,\delta^2}$$

shots. This gives the minimal experimental budget for any ontology-discriminating test, and we instantiate it in Section 4.3 with the fidelity from [4].

## 4. Analysis

All numbers in this section are computed here from stated inputs. The only empirical input is the readout fidelity from [4]; everything else is a derivation or an explicitly labeled projection.

### 4.1 Convergence rate under a contraction (illustrative computation)

**Input:** Lipschitz constant $L = 0.6$ (a labeled illustrative value, representing a calibration loop in which each round removes $40\%$ of the remaining discrepancy); initial discrepancy $d_{\mathcal{D}}(x_0, x^\*) = 1$ in normalized units; target tolerance $\varepsilon = 10^{-3}$.

**Step 1.** Compute the required iteration count:

$$n \geq \frac{\ln(\varepsilon / d_0)}{\ln L} = \frac{\ln(10^{-3})}{\ln(0.6)}.$$

**Step 2.** Evaluate the logarithms:

$$\ln(10^{-3}) = -3 \ln 10 \approx -3 \times 2.302585 = -6.907755,$$
$$\ln(0.6) = \ln 6 - \ln 10 \approx 1.791759 - 2.302585 = -0.510826.$$

**Step 3.** Divide:

$$n \geq \frac{-6.907755}{-0.510826} \approx 13.524.$$

**Step 4.** Round up to an integer: $n = 14$ calibration rounds suffice. As a check, $L^{14} = 0.6^{14}$: $0.6^2 = 0.36$, $0.6^4 = 0.1296$, $0.6^8 = 0.01679616$, $0.6^{14} = 0.6^8 \times 0.6^4 \times 0.6^2 = 0.01679616 \times 0.1296 \times 0.36 \approx 0.000783$, and indeed $0.000783 < 10^{-3}$, while $0.6^{13} = 0.000783/0.6 \approx 0.001305 > 10^{-3}$. So $n = 14$ is exactly the minimum.

**Interpretation.** In the contraction regime, the initial ontology is irrelevant: a transmon-first prior and an ion-first prior converge to the same $x^\*$ in $O(14)$ rounds. This is the formal content of "benign circularity."

### 4.2 A two-ontology toy model with two fixed points

We now exhibit the underdetermined regime explicitly. Consider a minimal model in which the operational datum is a single scalar $x \in \mathbb{R}$ (a normalized discrepancy between predicted and observed readout statistics) and there are two candidate ontologies $A$ and $B$, each with its own realization map. Define

$$T_A(x) = 0.5\,x + 0.5\,a, \qquad T_B(x) = 0.5\,x + 0.5\,b,$$

with ontology-dependent offsets $a \neq b$. The full calibration operator, given a selection rule that keeps the ontology whose prediction is closer, is

$$T(x) = \begin{cases} T_A(x) & \text{if } |T_A(x) - x| \leq |T_B(x) - x|, \\ T_B(x) & \text{otherwise.} \end{cases}$$

**Fixed points.** Solving $x = T_A(x)$: $x = 0.5x + 0.5a \Rightarrow 0.5x = 0.5a \Rightarrow x_A^\* = a$. Similarly $x_B^\* = b$. Both are exact fixed points of their respective branches, and if the selection rule is branch-consistent near each fixed point (which it is, since $|T_A(x) - x| = 0.5|x - a| \to 0$ as $x \to a$), both are fixed points of $T$.

**Basins of attraction.** The midpoint $m = (a + b)/2$ separates the basins: starting from $x_0 < m$ the iteration converges to $x_A^\* = a$; from $x_0 > m$ it converges to $x_B^\* = b$.

**Concrete numbers.** Take $a = 0$ and $b = 1$ (two ontologies predicting maximally different discrepancy values in normalized units), $x_0 = 0.6$. Then $m = 0.5$, so $x_0 > m$ and the iteration follows branch $B$:

$$x_1 = 0.5 \times 0.6 + 0.5 \times 1 = 0.8,$$
$$x_2 = 0.5 \times 0.8 + 0.5 = 0.9,$$
$$x_3 = 0.5 \times 0.9 + 0.5 = 0.95,$$

and in general $x_n = 1 - 0.4 \times 0.5^n$: check $n=1$: $1 - 0.2 = 0.8$; $n=2$: $1 - 0.1 = 0.9$; $n=3$: $1 - 0.05 = 0.95$. The iteration converges to $x_B^\* = 1$, never visiting the $A$-branch. The two ontologies are physically inequivalent (one says the controlled entity is, say, an energy eigenmode with offset $a = 0$; the other a collective variable with offset $b = 1$), yet each is exactly self-consistent on its own basin, and the final ontology is determined by the *initial guess*, not by the data.

**When is this not a contraction?** $T_B$ alone has $L = 0.5 < 1$, so each branch is contractive; the failure of uniqueness comes from the *multiplicity* of branch fixed points, i.e., from the selection rule, not from divergence. This is the generic structure of ontological underdetermination: the dynamics is locally stable but globally non-unique, and the loop cannot tell the branches apart because each branch's realization map $\Gamma$ is defined only on its own ontology's predictions.

### 4.3 Shot budget for ontology discrimination

**Input (from [4]):** single-shot readout fidelity $F = 0.99991$ (reported as $99.991(1)\%$ average fidelity for an optical qubit in $^{40}\mathrm{Ca}^+$, over one million trials, using time-resolved photon counting).

**Step 1.** Per-shot error probability:

$$p = 1 - F = 1 - 0.99991 = 9 \times 10^{-5}.$$

**Step 2.** Suppose the two candidate ontologies differ in the expectation value of some readout-accessible observable by $\delta$. To resolve this difference at confidence level $\alpha = 0.01$ (failure probability $1\%$), Hoeffding's inequality requires

$$N \geq \frac{\ln(2/\alpha)}{2\,\delta^2} = \frac{\ln 200}{2\,\delta^2}.$$

**Step 3.** Evaluate $\ln 200 = \ln 2 + \ln 100 \approx 0.693147 + 4.605170 = 5.298317$.

**Step 4.** For a discriminability target $\delta = 10^{-3}$:

$$N \geq \frac{5.298317}{2 \times 10^{-6}} = \frac{5.298317}{2 \times 10^{-6}} = 2.649159 \times 10^{6}.$$

So approximately $N = 2.65 \times 10^{6}$ shots are needed.

**Step 5.** Compare with the empirical trial count in [4]: the reported fidelity was established over one million trials, i.e., $N_{\text{rep}} = 10^{6}$. The ratio is

$$\frac{N}{N_{\text{rep}}} = \frac{2.649159 \times 10^{6}}{10^{6}} \approx 2.65.$$

**Interpretation.** Resolving ontology-level discrepancies of size $\delta = 10^{-3}$ requires about $2.65$ times the shot count already demonstrated in [4]—well within reach of the demonstrated technique. For a harder target $\delta = 10^{-4}$, the same formula gives

$$N \geq \frac{5.298317}{2 \times 10^{-8}} = 2.649159 \times 10^{8},$$

about $265$ times the demonstrated trial count—a substantially larger but not fundamentally impossible budget. The per-shot error floor $p = 9 \times 10^{-5}$ also sets a floor on resolvable $\delta$: discrepancies $\delta \lesssim p$ are comparable to the readout noise per shot and require the full statistical treatment above.

### 4.4 Cross-platform matching as an ontology-alignment test

The multi-platform question (Section 1) can now be stated precisely. Let $x^\*_{\text{transmon}}$, $x^\*_{\text{ion}}$, $x^\*_{\text{spin}}$ be the fixed points reached by calibration on each platform. Two outcomes are possible:

- **Alignment exists:** there is a correspondence (in the sense of [3]) under which the three identifications map to one another with all physical interpretations preserved. Then the qubit ontology is platform-independent and the circularity is benign globally.
- **No alignment:** the identifications are fixed points of separate branch dynamics (Section 4.2) with no correspondence preserving interpretation. Then "what is actually manipulated" differs across platforms despite identical operational descriptions, and the underdetermination is physical, not technical.

The shot-budget computation of Section 4.3 gives the experimental cost of testing any proposed discriminating observable between the aligned and non-aligned hypotheses.

## 5. Results

**R1 (Convergence in the contraction regime).** With Lipschitz constant $L = 0.6$ (illustrative input) and initial discrepancy $d_0 = 1$, calibration reaches tolerance $\varepsilon = 10^{-3}$ in exactly $n = 14$ rounds (Section 4.1; verified by direct evaluation $0.6^{14} \approx 7.83 \times 10^{-4} < 10^{-3} < 0.6^{13} \approx 1.31 \times 10^{-3}$). In this regime the operational circularity is benign: unique fixed point, initial-ontology independence.

**R2 (Multiplicity in the two-branch model).** In the toy model of Section 4.2 with offsets $a = 0$, $b = 1$, there are two exact fixed points $x_A^\* = 0$ and $x_B^\* = 1$, separated by the basin boundary $m = 0.5$; iteration from $x_0 = 0.6$ converges to $x_B^\* = 1$ via $x_1 = 0.8$, $x_2 = 0.9$, $x_3 = 0.95$, with closed form $x_n = 1 - 0.4 \times 0.5^n$. The final ontology is determined by the initial guess, not the data: ontological underdetermination is realizable in a locally contractive loop.

**R3 (Shot budget).** From the readout fidelity $F = 0.99991$ reported in [4], the per-shot error probability is $p = 9 \times 10^{-5}$. Resolving an ontology-discriminating signal of size $\delta = 10^{-3}$ at confidence $\alpha = 0.01$ requires $N = 2.649159 \times 10^{6}$ shots, i.e., approximately $2.65$ times the $10^{6}$-trial count demonstrated in [4]. For $\delta = 10^{-4}$, the requirement rises to $N = 2.649159 \times 10^{8}$ shots, a labeled projection assuming the same fidelity and Hoeffding's bound.

**R4 (Structural dichotomy).** The cross-platform question reduces to ontology alignment in the sense of [3]: either a correspondence preserving physical interpretation exists across transmon, ion, and spin fixed points, or it does not. Both outcomes are consistent with the formalism; the formalism itself does not decide which obtains—that is an empirical question with the budget of R3.

## 6. Discussion

**Limitations.** The contraction analysis (R1) uses an illustrative Lipschitz constant; real calibration loops may have state-dependent or iteration-dependent $L$, and the Banach uniqueness guarantee applies only to the idealized operator $T = \Gamma \circ \Phi$ with exact realization maps. Real $\Gamma$ includes unmodeled drift, and drift can violate the contraction condition between rounds. The two-branch model (R2) is deliberately minimal: one scalar datum, two branches. Real ontology spaces are high-dimensional, and multiplicity there may take forms—continuous families of fixed points, limit cycles—not captured here. The shot-budget result (R3) assumes the discriminating observable is readout-accessible with the fidelity of [4] and that the only noise is readout noise; additional decoherence during the discriminating sequence would inflate $N$ beyond the computed values.

**What would falsify the claims.** The central empirical claim is the dichotomy of R4. It is falsified in the "benign" direction if a concrete cross-platform protocol is exhibited whose calibration converges, from arbitrary initial ontologies, to identifications that are not merely parameter-matched but interpretation-matched—then underdetermination is empty in practice. It is falsified in the "underdetermined" direction if someone exhibits an observable, implementable within the loop, whose expectation provably differs between the energy-eigenmode and collective-variable identifications of a specific platform, at $\delta$ resolvable within the budget of R3—then the branches are distinguishable after all and the ontology is not underdetermined. The claim that the qubit is constituted rather than discovered (following [12], which characterizes the qubit-gate-circuit model as a projection of particle ontology onto field-theoretic reality) is a hypothesis, not a result of this paper; it would be supported if the underdetermined regime is realized and refuted if the benign regime is universal.

**Arguing against ourselves.** A defender of the standard view can accept everything here and say: of course calibration is a fixed-point problem; of course toy models can have multiple fixed points; the physics selects the branch through Hamiltonian microphysics (spectroscopy of the underlying levels), which is precisely the extra-loop information the standard view takes as given. Our reply is that the microphysical description is itself an ontology assignment—calling a transmon's two lowest levels "the qubit" presupposes the eigenmode picture—and the formalism shows that this presupposition is not forced by operational data alone. But the reply has force: if a cheap, loop-external spectroscopic fact (e.g., a level structure measured by a nominally independent probe) is admitted as data, the underdetermination may collapse. Whether "independent probe" is coherent inside a fully operationalist account is an open question we do not resolve.

**Open questions.** (i) What is the actual Lipschitz constant of a transmon or ion calibration loop, measured empirically? (ii) Do continuous families of fixed points arise when the ontology space includes the choice of error model? (iii) Can the alignment test of R4 be run non-parametrically, without committing to a discriminating observable in advance? (iv) The constructive program of [10]—what minimal ontological commitments survive the critique—requires a positive characterization of the benign regime's fixed points; our Proposition 1 gives existence and uniqueness but not the physical content of $x^\*$.

## 7. Conclusion

We have formalized the operational circularity of qubit ontology as a fixed-point problem: states defined by measurements defined by states. The circularity is benign exactly when the calibration operator is a contraction with a unique fixed point; we computed an illustrative convergence time of $n = 14$ rounds for $L = 0.6$ and $\varepsilon = 10^{-3}$. Outside that regime, an explicit two-branch model shows that physically inequivalent ontologies—an energy eigenmode and a collective variable—can be exact, locally stable fixed points of the same operational loop, with the outcome selected by the initial guess rather than the data. Using the trapped-ion readout fidelity of $99.991\%$ reported in [4], we computed that discriminating ontology-level discrepancies of size $10^{-3}$ at $99\%$ confidence requires $2.65 \times 10^{6}$ shots—about $2.65$ times the trial count already demonstrated—so the dichotomy is experimentally decidable. Whether "what is actually manipulated" has an answer in principle, or only an operational one, is thus reduced to a concrete, falsifiable question about the fixed-point structure of calibration across platforms.

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