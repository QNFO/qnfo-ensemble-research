# Completion-Invariance of Physical Ontology: The Rational Base Field in Quantum Foundations

## Abstract

We propose and formalize a *completion-invariance* principle for quantum ontology: the physical content of quantum mechanics resides in rational measurement outcomes, so any ontological commitment attached to the real numbers $\mathbb{R}$ must, to be consistent, also be attachable to the $p$-adic numbers $\mathbb{Q}_p$, since both are instrumental completions of the same rational base field $\mathbb{Q}$. We give three contributions. First, we formulate a finite-precision, rational quantum mechanics in which all amplitudes are rationals of bounded denominator size, and we prove a quantitative reproduction theorem: for any observable on a $d$-dimensional system, truncating amplitudes to $n$ bits perturbs every Born probability by at most $2\sqrt{d}\,2^{-n}$, a bound we derive explicitly and evaluate for double precision ($n = 53$, $d = 4$), obtaining $\approx 4.44\times 10^{-16}$, far below any plausible measurement precision. Second, we identify the regimes where archimedean and ultrametric completions can genuinely diverge — scale-invariant and hierarchical systems — and argue that no presently described divergence is observable in principle without new physics. Third, we state the symmetry caveat as a transfer thesis: any realist argument for $\mathbb{R}$-reality transfers mutatis mutandis to $\mathbb{Q}_p$-reality, so consistent realism must accept both completions or neither. The principle converts a metaphysical dispute into a sharp formal question: do standard quantum predictions depend on the archimedean completion at all?

## 1. Introduction

Quantum mechanics is written in the language of real Hilbert spaces: states are vectors over $\mathbb{R}$ (or $\mathbb{C}$, itself a completion of $\mathbb{Q}(i)$), observables are real operators, and probabilities are real numbers. Yet every experiment terminates in a rational number: a count, a ratio of counts, a finite-precision reading. The real numbers enter as a *completion* of the rationals — a convenient analytic envelope, not a datum of experience. The $p$-adic numbers $\mathbb{Q}_p$ are an equally legitimate completion of the same base field $\mathbb{Q}$, obtained by a different absolute value. If the physical content of the theory lives in the rational outcomes, then the choice between $\mathbb{R}$ and $\mathbb{Q}_p$ is instrumental, and ontology should be *invariant* under that choice. We call this the completion-invariance principle.

The principle has a sharp consequence. Any argument that the continuum is "physically real" — because it is needed for the theory's structure, its predictive success, or its explanatory unity — applies equally to the ultrametric completions, which support the same algebraic substrate. A realist who accepts $\mathbb{R}$-reality but rejects $\mathbb{Q}_p$-reality must therefore point to a *physical* asymmetry between the completions, not a calculational one. We argue that no such asymmetry is presently demonstrable at the level of accessible observables.

This program converges with recent work on finite-precision physics. The Gisin–Del Santo program, as summarized in the QNFO corpus, argues that physical quantities contain only finite information and that real numbers are physically unreal — they are *de facto* finite specifications [9]. A companion three-axis framework separates the continuum into Depth (computable reals), Breadth (non-computable reals, deemed physically vacuous), and Valuation (p-adic completions as information carriers), with falsifiable predications for quantum error correction and gauge structure [10]. Our contribution differs in emphasis: rather than arguing that the continuum is too rich, we argue that the *choice among completions* is underdetermined by physics, and we quantify exactly how much of standard quantum theory survives when the archimedean completion is discarded.

The paper is organized as follows. Section 2 situates the proposal in the supplied literature. Section 3 defines rational quantum mechanics and the completion-invariance principle. Section 4 carries out the explicit derivations, including the truncation-error bound. Section 5 states results. Section 6 discusses limitations and failure modes, and Section 7 concludes.

## 2. Background and Related Work

We work from a supplied bibliography of twelve entries; we discuss eight here and note the remainder where relevant. The entries are heterogeneous, and we use each only for what its own summary supports.

**Quantum foundations and ontology.** The introduction to the volume *Quantum Theory: Informational Foundations and Foils* surveys recent trends in quantum foundations and overviews contributions to that volume [3]. It is useful to us as evidence that informational and operational readings of quantum theory form an active, organized research line: our completion-invariance principle is a natural extension of the operational stance, since it takes measurement outcomes — the operational currency — as the ontologically load-bearing layer. The forewords to the special issue *Pilot-wave and beyond* document that the journal *Foundations of Physics* hosted a topical collection on the quest for a quantum ontology in the de Broglie–Bohm lineage, with contributions from physicists and philosophers debating the scientific legacy of Bohm and de Broglie [7]. This establishes that realist ontology-building in quantum theory is a live, contested enterprise; our transfer thesis is addressed precisely to such realist programs. Most directly relevant, the work on bounded ontological distinctness generalizes the Leibniz principle of the identity of indiscernibles to equate the operational distinguishability of a set of physical entities with the distinctness of their ontological counterparts [8]. Our principle is a sibling of this move: where [8] ties ontology to operational distinguishability, we tie ontology to operational *numerical content*, which is rational by construction. If two completions agree on all operationally distinguishable outcomes, bounded ontological distinctness in the sense of [8] gives reason to treat them as ontologically identical.

**Finite-precision physics.** The QNFO analysis of the Gisin–Del Santo program reports that program's two central claims: physical quantities contain only finite information, and real numbers are physically unreal, being *de facto* finite specifications [9]. Our Section 3–4 can be read as a quantitative audit of claim (2) in the quantum setting: we show how much of the real formalism is actually exercised by predictions, and with what error it can be replaced by rationals. The three-axis framework of Depth, Breadth, and Valuation treats p-adic completions as information carriers alongside computable and non-computable reals, and issues falsifiable predications for quantum error correction and gauge structure [10]. Our completion-invariance principle supplies the symmetry axiom that this framework implicitly assumes: no axis of the continuum is privileged as *the* physical one.

**Structural analogy: ontologies as engineered artifacts.** Four further entries support our methodological framing. The Gene Ontology primer describes the GO as the largest resource for cataloguing gene function, emphasizing solid conceptual underpinnings and practical features behind its wide adoption [1]; the companion pitfalls paper stresses that the GO is sufficiently simple to be used without deep understanding of its structure, which is both a strength and a weakness [2]. The lesson we import is that a representational framework can be enormously successful while its users remain largely innocent of its underlying structure — exactly the status of $\mathbb{R}$ in physics. The GraphMatcher paper defines ontology matching as finding correspondences between entities in different ontologies to solve interoperability problems, using a graph attention approach [6]. Completion-invariance is, formally, an interoperability thesis between the $\mathbb{R}$-ontology and the $\mathbb{Q}_p$-ontology of quantum mechanics: we seek the correspondence map under which predictions are preserved. Finally, homotopy type theory presents the univalence axiom, implying that isomorphic structures can be identified [4]. This is the logical template for our principle: if the $\mathbb{R}$- and $\mathbb{Q}_p$-formalisms are isomorphic *as theories of rational outcomes*, univalence-style reasoning licenses identifying them ontologically. Two remaining entries carry too little supplied detail to support substantive claims: the summary for the Stability Compiler [11] and for the Alpha Pi Project [12] are empty, so we cite them only as corpus items and draw no content from them. The INRIM "Carlo Novero" lab report presents recent experimental work on quantum information and foundations [5]; its summary gives no specific results, so we use it only as evidence that foundational experiments are actively performed, which motivates our demand that any $\mathbb{R}$-versus-$\mathbb{Q}_p$ divergence be experimentally articulable.

## 3. Methods

### 3.1 Rational quantum mechanics

Fix a finite-dimensional system of dimension $d$. Define the *rational state space* $\mathcal{H}_{\mathbb{Q}}(d)$ as the set of vectors $\ket{\psi_{\mathbb{Q}}} = (q_1, \dots, q_d)$ with $q_i \in \mathbb{Q}$ and $\sum_{i=1}^{d} |q_i|^2 = 1$, where the norm is the ordinary rational arithmetic norm. Observables are $d \times d$ matrices with rational entries $A_{\mathbb{Q}}$. Born probabilities are

$$
p_i = \big|\langle i \mid \psi_{\mathbb{Q}} \rangle\big|^2 = |q_i|^2 \in \mathbb{Q},
$$

and expectation values $\langle A_{\mathbb{Q}} \rangle = \sum_{i,j} q_i^* A_{ij} q_j$ are rationals. Every prediction of this theory is a rational number, hence exactly a possible finite-precision measurement record. Normalization is the one place where rationals strain: we require $\sum_i |q_i|^2 = 1$ exactly, which is achievable (e.g., Pythagorean-type vectors) but not for every unit vector; we return to this in Section 6.

### 3.2 The truncation map

Given a real state $\ket{\psi} \in \mathbb{R}^d$ and a bit budget $n$, define the truncation map $T_n$ by rounding each amplitude to the nearest multiple of $\epsilon_n = 2^{-n}$:

$$
T_n(\psi)_i = \epsilon_n \left\lfloor \frac{\psi_i}{\epsilon_n} \right\rceil \in \mathbb{Q},
\qquad
\big|\psi_i - T_n(\psi)_i\big| \le \frac{\epsilon_n}{2}.
$$

The truncated vector is rational by construction; after renormalization it lies in $\mathcal{H}_{\mathbb{Q}}(d)$ up to the same error scale.

### 3.3 Completion-invariance principle

Two completions $\mathbb{K}_1, \mathbb{K}_2$ of $\mathbb{Q}$ (here $\mathbb{R}$ and $\mathbb{Q}_p$) are *physically equivalent* if for every experimentally realizable observable and every state, the rational outcomes and their probabilities coincide to within measurement precision $\delta_{\mathrm{exp}}$. The principle states: ontology is invariant under physically equivalent completions. Its contrapositive is the transfer thesis: any realist argument for $\mathbb{R}$-reality that appeals only to physical equivalence transfers mutatis mutandis to $\mathbb{Q}_p$-reality.

## 4. Analysis

### 4.1 Probability perturbation under truncation

**Inputs.** (i) Truncation bound: each amplitude error satisfies $|\Delta \psi_i| \le \epsilon_n / 2$ with $\epsilon_n = 2^{-n}$ (from the rounding definition in Section 3.2). (ii) Dimension $d$ (state-space size, a modeling choice). (iii) Bit budget $n$ (a modeling choice; we take $n = 53$, the mantissa width of IEEE double precision, as the standard computational baseline).

**Derivation.** The Born probability for outcome $i$ is $p_i = |\psi_i|^2$. Under truncation,

$$
\big|\,|\psi_i|^2 - |T_n(\psi)_i|^2\,\big|
= \big|\psi_i - T_n(\psi)_i\big| \cdot \big|\psi_i + T_n(\psi)_i\big|
\le \frac{\epsilon_n}{2} \cdot \big(|\psi_i| + |T_n(\psi)_i|\big).
$$

Since $|\psi_i| \le 1$ (unit vector) and $|T_n(\psi)_i| \le |\psi_i| + \epsilon_n/2 \le 1 + \epsilon_n/2$, we get

$$
|\Delta p_i| \le \frac{\epsilon_n}{2}\left(2 + \frac{\epsilon_n}{2}\right) = \epsilon_n + \frac{\epsilon_n^2}{4}.
$$

For a general observable, the probability of any measurement outcome is a quadratic form $p = \psi^{\dagger} P \psi$ with $\|P\| \le 1$; a first-order perturbation calculation gives

$$
|\Delta p| \le 2\,\|\Delta \psi\| \cdot \|\psi\| \cdot \|P\| \le 2 \sqrt{d} \cdot \frac{\epsilon_n}{2} = \sqrt{d}\,\epsilon_n,
$$

using $\|\Delta\psi\| \le \sqrt{d}\,\epsilon_n/2$ (each of $d$ components off by at most $\epsilon_n/2$) and $\|\psi\| = 1$. To be conservative against second-order terms we state the headline bound with a factor 2:

$$
|\Delta p| \le 2\sqrt{d}\,\epsilon_n = 2\sqrt{d}\,2^{-n}.
$$

**Numerical evaluation.** Take $d = 4$ (two qubits, the smallest nontrivial entangling setting) and $n = 53$.

- $\epsilon_{53} = 2^{-53}$. Since $2^{10} = 1024 \approx 10^3$, we have $2^{-53} = 2^{-3} \cdot 2^{-50} \approx 0.125 \times 10^{-15} = 1.25\times 10^{-16}$; more precisely $2^{-53} = 1 / 9007199254740992 \approx 1.1102\times 10^{-16}$.
- $\sqrt{d} = \sqrt{4} = 2$.
- Bound: $2 \times 2 \times 1.1102\times 10^{-16} = 4.4409\times 10^{-16}$.

$$
|\Delta p| \le 2\sqrt{4}\,2^{-53} \approx 4.44\times 10^{-16}.
$$

**Comparison with measurement precision.** A typical high-precision quantum measurement resolves probabilities to roughly $\delta_{\mathrm{exp}} \approx 10^{-6}$ (one part in a million, achievable in repeated-count experiments; we state this as an assumed benchmark, not a measured value). The ratio is

$$
\frac{4.44\times 10^{-16}}{10^{-6}} = 4.44\times 10^{-10}.
$$

The truncation error is nine orders of magnitude below the benchmark precision. Even at the extreme of $\delta_{\mathrm{exp}} = 10^{-12}$, the ratio is $4.44\times 10^{-4}$, still safely below.

### 4.2 Bit budget needed to hide the completion

Invert the bound: to guarantee $|\Delta p| \le \delta$, require

$$
n \ge \log_2\!\left(\frac{2\sqrt{d}}{\delta}\right).
$$

For $d = 4$, $\delta = 10^{-6}$:

$$
n \ge \log_2\!\left(\frac{4}{10^{-6}}\right) = \log_2(4\times 10^{6}) = \log_2 4 + \log_2 10^{6} \approx 2 + 6 \times 3.3219 = 21.93,
$$

so $n = 22$ bits suffice. For $\delta = 10^{-12}$: $n \ge 2 + 12 \times 3.3219 \approx 41.86$, so $n = 42$ bits. Both are far below the 53 bits of standard double precision. This is the quantitative core of the reproduction claim: *the archimedean completion is exercised by quantum predictions only through roughly 22–42 bits per amplitude*, and everything beyond is ontologically inert at accessible precision.

### 4.3 Where completions can diverge

The completions $\mathbb{R}$ and $\mathbb{Q}_p$ differ in their topologies: $\mathbb{R}$ is ordered and archimedean, $\mathbb{Q}_p$ is ultrametric, satisfying $|x + y|_p \le \max(|x|_p, |y|_p)$. Divergence requires observables sensitive to the *global* analytic structure, not just rational data. Candidate regimes, stated as hypotheses rather than results:

- **Scale-invariant systems.** Systems with no intrinsic scale (e.g., critical points) are sensitive to how "closeness" is defined; the archimedean and ultrametric metrics induce different scaling hierarchies.
- **Hierarchical/treelike structures.** Ultrametric spaces are naturally tree-structured; if a physical system's state space is genuinely hierarchical (as the Valuation axis of [10] suggests for certain error-correction contexts), $\mathbb{Q}_p$ may organize it more naturally than $\mathbb{R}$.

Whether either regime yields an *observable-in-principle* divergence is open; we return to it in Section 6.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

**R1 (Reproduction bound).** For a $d$-dimensional system with amplitudes truncated to $n$ bits, every Born probability deviates from its real-valued value by at most

$$
|\Delta p| \le 2\sqrt{d}\,2^{-n}.
$$

For $d = 4$, $n = 53$: $|\Delta p| \le 4.44\times 10^{-16}$.

**R2 (Sufficient bit budget).** To hold deviations below a target precision $\delta$ for $d = 4$: $n = 22$ bits for $\delta = 10^{-6}$; $n = 42$ bits for $\delta = 10^{-12}$ (both from the inversion $n \ge \log_2(2\sqrt{d}/\delta)$, rounded up).

**R3 (Margin).** Against the assumed benchmark $\delta_{\mathrm{exp}} = 10^{-6}$, the double-precision truncation error is smaller by a factor of $4.44\times 10^{-10}$, i.e., nine orders of magnitude.

**R4 (Projection, labeled).** *Projection with stated assumptions:* if experimental precision improves by two orders of magnitude per decade of effort (an assumed trend, not a measurement), reaching $\delta_{\mathrm{exp}} = 10^{-12}$ would still leave the rational reproduction intact with $n = 42 < 53$ bits, with margin factor $4.44\times 10^{-4}$. Uncertainty: the projection inherits the assumed trend; if precision plateaus above $10^{-16}$, the reproduction theorem holds indefinitely at $n = 53$.

**R5 (Qualitative).** No divergence between $\mathbb{R}$ and $\mathbb{Q}_p}$ completions is demonstrable for observables on finite-dimensional systems at accessible precision; candidate divergence regimes (scale-invariant, hierarchical) are identified but not shown to be observable.

## 6. Discussion

**Limitations.** First, the reproduction theorem covers finite-dimensional systems and Born probabilities; it does not yet cover continuous-spectrum observables, scattering amplitudes, or field-theoretic quantities, where the archimedean topology may be exercised more deeply. Extending the bound to infinite dimensions is the main open technical problem. Second, exact rational normalization is restrictive: not every unit vector truncates to an exactly normalized rational vector, and our renormalization step introduces an additional error of the same order $\epsilon_n$ that we have absorbed into the conservative factor 2; a tighter treatment would track it separately. Third, the benchmark $\delta_{\mathrm{exp}} = 10^{-6}$ is an assumed precision level, not a measured one; the qualitative conclusion (nine orders of margin) is robust to several orders of variation, but a reader requiring a specific experimental claim must supply their own precision figure.

**Failure modes.** The completion-invariance principle fails if someone exhibits (a) an experimentally realizable observable whose prediction is not approximable by rationals within $\delta_{\mathrm{exp}}$, or (b) a physical effect that distinguishes the archimedean from an ultrametric topology — for instance, a scale-invariant system whose critical exponents depend on the completion. Our candidate regimes in Section 4.3 are precisely where such a counterexample would live; a demonstration there would falsify the principle's universality, though not its validity for ordinary laboratory quantum mechanics.

**Against ourselves.** A critic may grant the reproduction theorem but deny it bears on ontology: instrumental equivalence, the critic says, does not entail ontological equivalence (a simulation of a system is not the system). We reply via the bounded-ontological-distinctness stance [8]: if ontological distinctness is tied to operational distinguishability, then completions that agree on all distinguishable outcomes are ontologically one. But this reply inherits the contested premise of [8]; a robust realist who rejects that premise is not yet refuted, only presented with a burden: state the physical asymmetry between $\mathbb{R}$ and $\mathbb{Q}_p$. A second critic may note that our univalence analogy [4] identifies isomorphic structures, and we have not exhibited an isomorphism between the $\mathbb{R}$- and $\mathbb{Q}_p$-formalisms — only an approximation result on the $\mathbb{R}$ side. That is correct: the transfer thesis is currently a conjecture with one quantitative leg (R1–R3) and one qualitative leg (the symmetry of realist arguments). Formalizing the $\mathbb{Q}_p$-side reproduction theorem is the natural next step. A third critic may observe that the finite-information stance of [9] and the Depth/Breadth/Valuation framework [10] already assert physical unreality of the continuum; our contribution is to have *quantified* the assertion for quantum probabilities, but we have not independently justified the stance itself.

**Open questions.** (i) Does the truncation bound extend to infinite-dimensional Hilbert spaces with explicit trace-class conditions? (ii) Is there a natural $\mathbb{Q}_p$-valued quantum mechanics whose predictions coincide with standard ones on all finite-precision experiments, making the equivalence theorem two-sided? (iii) Do the falsifiable predications for quantum error correction proposed in [10] constitute the sought archimedean/ultrametric discriminator?

## 7. Conclusion

We have formulated completion-invariance as a principle of physical ontology: because quantum predictions terminate in rational outcomes, and because $\mathbb{R}$ and $\mathbb{Q}_p$ are equally instrumental completions of $\mathbb{Q}$, ontology should not depend on the choice of completion. We substantiated the principle quantitatively with an explicit reproduction theorem: truncating amplitudes to $n$ bits perturbs every Born probability by at most $2\sqrt{d}\,2^{-n}$, which for two-qubit systems at double precision is $\approx 4.44\times 10^{-16}$ — nine orders of magnitude below an assumed $10^{-6}$ measurement benchmark, with only 22–42 bits needed to hide the completion entirely at realistic precisions. We identified scale-invariant and hierarchical regimes as the candidate loci of genuine completion divergence, and we stated the symmetry caveat: consistent realism about the continuum commits one to $\mathbb{Q}_p$-reality as well, or to realism about neither. The metaphysical dispute over the continuum is thereby converted into a sharp formal question — do standard quantum predictions depend on the archimedean completion at all? — to which our analysis answers: not at any accessible precision, in finite dimension.

## References

[1] arXiv:1602.01876v1 | Primer on the Gene Ontology

[2] arXiv:1602.01875v1 | Gene Ontology: Pitfalls, Biases, Remedies

[3] arXiv:1805.11483v3 | Introduction to the book "Quantum Theory: Informational Foundations and Foils"

[4] arXiv:1308.0729v1 | Homotopy Type Theory: Univalent Foundations of Mathematics

[5] arXiv:0705.3203v1 | Recent experiments performed at "Carlo Novero" lab at INRIM on Quantum Information and Foundations of Quantum Mechanics

[6] arXiv:2404.14450v1 | GraphMatcher: A Graph Representation Learning Approach for Ontology Matching

[7] arXiv:2212.13186v1 | Forewords for the special issue `Pilot-wave and beyond: Louis de Broglie and David Bohm's quest for a quantum ontology'

[8] arXiv:1909.07293v2 | Quantum prescriptions are more ontologically distinct than they are operationally distinguishable

[9] QNFO: Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure | DOI 10.5281/zenodo.21647362

[10] QNFO: Depth, Breadth, and Valuation: A Unified Ontology of the Physical Continuum | DOI 10.5281/zenodo.21672990

[11] QNFO: Stability Compiler | DOI 10.5281/zenodo.17762911

[12] QNFO: Alpha Pi Project | DOI 10.5281/zenodo.19479493