# Distinction, Discretisation, and the Cost of Law: A Quantitative Sketch of Approximation Entropy

## Abstract

The deepest question in physics is often posed as "What are the laws?", but a prior question is "What does it cost to state, and to compute with, a law?" Building on the distinction-based formalism of Spencer-Brown's *Laws of Form* as consolidated in the Quantum Laws of Form (QNFO) programme, and on the QNFO thesis that physical law requires only the rational numbers, we develop a quantitative sketch of *approximation entropy*: the irreducible information cost of translating continuous bosonic physics into discrete digital computation. We define a rational-grid discretisation of a continuous parameter, count the admissible rational states via a Farey-type estimate, and derive the scaling $H_{\mathrm{app}}(\varepsilon) = \log_{2}\!\bigl(3/(\pi^{2}\varepsilon)\bigr)$ for the bits required to specify a parameter to relative tolerance $\varepsilon$. We compute a concrete value, $H_{\mathrm{app}}(10^{-4}) \approx 11.57$ bits, with full arithmetic, and project the Trotter-step cost of digital simulation of a continuous evolution, obtaining a wall $N_{\mathrm{step}} \propto T^{2}/\varepsilon$. We situate the framework against community-scale strategy documents in particle physics [1], linear-collider design [2], fusion pathway analysis [3], conservation-law pedagogy [4], philosophy of laws [5], neutrino-facility physics [6], anomaly detection [7], sociophysics [8], and the QNFO corpus [9]-[12]. The framework yields a falsifiable calorimetry proposal [12] and identifies open problems.

## 1. Introduction

Physics traditionally answers the question "What are the laws?" by discovering regularities and expressing them as equations. The QNFO research programme inverts the order of interrogation: before asking what the laws are, it asks what the *act of stating* a law presupposes. Following Spencer-Brown as consolidated in the QNFO synthesis [9], the primitive operation is the drawing of a distinction; logic, mathematics, and physics are then constructed on top of distinctions. A second QNFO thesis holds that physical law requires only the rational numbers $\mathbb{Q}$, not the full continuum $\mathbb{R}$ [11]. A third, developed in v2.0 of the Two-Level Lie document, introduces *approximation entropy* as a meta-mathematical framework quantifying the irreducible cost of translating continuous bosonic physics to discrete digital computation, together with named structures — the Rosetta Constant, the Trotter Wall, and the Fractal Wall theorem — and a falsifiable calorimetry experimental programme [12].

The present paper takes these programmatic statements and asks what a minimal, fully explicit quantitative core looks like. Our contribution is deliberately modest and self-contained:

1. We define a rational-grid discretisation of a single continuous physical parameter and derive, with every arithmetic step shown, the number of bits needed to specify that parameter to a stated tolerance (Section 4.1).
2. We derive the scaling of the number of Trotter steps needed to simulate a continuous unitary evolution digitally to a stated error, the "Trotter Wall" of [12], as a projection with stated assumptions (Section 4.2).
3. We combine the two into a single figure of merit, the *translation cost* $C_{\mathrm{tr}}$, and exhibit one fully computed numerical example (Section 4.3).

We emphasise scope: this is a sketch of a framework, not a derivation of any established physical theory. All quantitative claims are either computed here with shown arithmetic or explicitly labelled projections with stated assumptions.

## 2. Background and Related Work

We discuss the supplied bibliography in its exact order and numbering. Because several entries carry only truncated summaries, we confine every statement about a work to what its own supplied text states.

[1] The *Physics Briefing Book* describes the European Particle Physics Strategy Update (EPPSU) process, which takes a bottom-up approach: the community is first invited to submit proposals (inputs) for projects it would like to see realised in the near-term, mid-term and longer-term future, with national inputs and inputs from national laboratories also important elements. We cite it as a model of how a large community aggregates candidate research directions — the same aggregation problem the QNFO consolidation performs when it identifies 7 open problem categories and proposes 4 extensions [9].

[2] The Snowmass '96 report on the Next Linear Collider presents the then-current expectations for the design and physics programme of an $e^{+}e^{-}$ linear collider of centre-of-mass energy $500\,\mathrm{GeV}$ to $1\,\mathrm{TeV}$, reviews the experiments that would be carried out, demonstrates the machine's key role in exploring physics beyond the Standard Model over the full range of theoretical possibilities, and shows feasibility of construction. It is a canonical example of a design study in which a continuous design parameter (beam energy) must be discretised into an achievable operating point — precisely the parameter-quantisation step our formalism makes explicit.

[3] The MHD analysis of CFETR and HFRC treats two major Chinese fusion projects representative of the low-density steady-state and high-density pulsed pathways to fusion, both under intensive physical and engineering design; a primary task of the physics designs is assessment and analysis (the supplied summary truncates at this point). We cite it as an instance of two divergent discretisations — steady-state versus pulsed — of the same underlying continuous physics, echoing the two-level structure (continuous physics versus discrete description) that motivates approximation entropy.

[4] The conservation-laws paper analyses a category of common physics problems: systems with two well-delineated parts that exchange energy, eventually reaching a shared equilibrium with a loss of mechanical or electrical energy, constrained by a constant of the system such as mass, charge, momentum, or angular momentum. This is directly relevant to our Section 4.3: the equilibration of a continuous quantity between two discrete subsystems, with an irreducible loss, is the physical picture behind our translation cost $C_{\mathrm{tr}}$.

[5] *Laws of Physics* is a philosophical introduction to laws of physics, connecting them to ontology, possibility, explanation, induction, counterfactuals, time, determinism, and fundamentality, and suggesting that laws are fundamental facts that govern (the summary truncates). It supplies the philosophical frame for our opening question: whether laws are fundamental facts or constructed descriptions bears directly on whether the discretisation cost we quantify is a fact about nature or about our descriptions.

[6] The Neutrino Factory ISS physics report presents the conclusions of the Physics Working Group of the international scoping study of a future Neutrino Factory and super-beam facility, carried by the international community between NuFact05 (Rome, June 21-26, 2005) and NuFact06 (Irvine, California, 24-30 August 2006). Like [2], it is a facility study in which continuous physics goals are translated into discrete machine parameters; the supplied summary gives no further quantitative detail, and we use it only as corroborating context for the translation problem.

[7] The review of machine learning for anomaly detection in particle physics notes that detection of out-of-distribution data points is a common task, used for monitoring complex detectors or identifying rare events indicative of new phenomena or physics beyond the Standard Model, and that recent advances have encouraged such techniques. In our framework, an out-of-distribution event is precisely a point that falls outside the discretised grid on which the monitoring model was built; the review's framing supports the relevance of grid-choice questions, though its summary does not quantify this.

[8] The statistical-physics review of social dynamics describes statistical physics as a fruitful framework for phenomena outside traditional physics, with physicists studying collective phenomena emerging from interactions of individuals as elementary units in social structures, reviewing topics from opinion to culture (summary truncates). We cite it as a precedent for exporting a physics formalism to a domain of discrete elementary units — the same export direction as QNFO's distinction-based construction.

[9] The QNFO consolidation records that Spencer-Brown's *Laws of Form* (1969) proposed the act of drawing a distinction as the primitive operation from which logic, mathematics, and physics can be constructed; the consolidation synthesises known quantum correspondences, identifies 7 open problem categories, and proposes 4 extensions. This is the primary source of our formalism's primitive.

[10] The QNFO *Iceberg of Reality* entry supplies no summary text. We therefore make no claim about its content and cite it only as part of the corpus under consolidation.

[11] The QNFO *$\mathbb{Q}$-vs-$\mathbb{R}$* entry, "Why Physical Law Requires Only the Rational Numbers", likewise supplies no summary text beyond its title. We use only the thesis stated in the title — that physical law requires only $\mathbb{Q}$ — and flag in Section 6 that this is a title-level thesis, not one we can substantiate further from the supplied material.

[12] The Two-Level Lie document, v2.0, adds Part II: the Approximation Entropy, described as a meta-mathematical framework quantifying the irreducible cost of translating continuous bosonic physics to discrete digital computation, introducing the Rosetta Constant, the Trotter Wall, and the Fractal Wall theorem with a falsifiable calorimetry experimental programme. Our Sections 3-4 are an attempt to give one explicit, checkable instantiation of the quantities this entry names.

## 3. Methods

### 3.1 Distinctions and grids

Following [9], the primitive is a distinction: a partition of a space into two labelled regions. A finite sequence of distinctions induces a finite partition, which we identify with a discretisation grid. A continuous parameter $x \in [0,1]$ is represented digitally by a rational $p/q$ with $1 \le q \le Q_{\max}$, where $Q_{\max}$ is the maximal denominator admitted by the representation. This is the operational content of the $\mathbb{Q}$-only thesis of [11]: whatever the theory writes as a real number, a digital description stores a rational.

### 3.2 Counting admissible rationals

The number of distinct reduced fractions $p/q$ with $0 \le p \le q \le Q$ in $[0,1]$ is asymptotically

$$N_{\mathbb{Q}}(Q) \approx \frac{3}{\pi^{2}}\,Q^{2},$$

a standard Farey-sequence count (the density of coprime pairs is $1/\zeta(2) = 6/\pi^{2}$, and each coprime pair $(p,q)$ with $q \le Q$ contributes one reduced fraction, giving $\tfrac{1}{2}\cdot\tfrac{6}{\pi^{2}}Q^{2} = \tfrac{3}{\pi^{2}}Q^{2}$ up to endpoint corrections). We use this as the model of the size of the rational grid.

### 3.3 Approximation entropy

We define the approximation entropy at tolerance $\varepsilon$ as

$$H_{\mathrm{app}}(\varepsilon) \;=\; \log_{2}\!\bigl(N_{\mathbb{Q}}(Q_{\varepsilon})\bigr),$$

where $Q_{\varepsilon}$ is the smallest maximal denominator such that every point of $[0,1]$ lies within $\varepsilon$ of some grid rational. Since consecutive Farey fractions $a/b < c/d$ satisfy $|c/d - a/b| = 1/(bd)$, the worst-case spacing with $q \le Q$ is of order $1/Q^{2}$; we therefore set

$$\varepsilon \;=\; \frac{1}{Q_{\varepsilon}^{2}} \quad\Longrightarrow\quad Q_{\varepsilon} \;=\; \varepsilon^{-1/2},$$

and hence

$$H_{\mathrm{app}}(\varepsilon) \;=\; \log_{2}\!\left(\frac{3}{\pi^{2}\,\varepsilon}\right).$$

### 3.4 Trotter wall projection

For a digital simulation of a continuous-time evolution under a Hamiltonian $H = H_{1} + H_{2}$, a first-order Trotter-Suzuki decomposition of $e^{-i(H_{1}+H_{2})t}$ into $N_{\mathrm{step}}$ steps of size $\Delta t = t/N_{\mathrm{step}}$ incurs a per-step commutator error of order $\Delta t^{2}\,\|[H_{1},H_{2}]\|$, so total error scales as

$$\varepsilon_{\mathrm{sim}} \;\sim\; N_{\mathrm{step}}\,\Delta t^{2}\,\|[H_{1},H_{2}]\| \;=\; \frac{t^{2}}{N_{\mathrm{step}}}\,\|[H_{1},H_{2}]\|.$$

Solving for the step count gives the Trotter Wall of [12] in its simplest form:

$$N_{\mathrm{step}} \;\sim\; \frac{t^{2}\,\|[H_{1},H_{2}]\|}{\varepsilon_{\mathrm{sim}}}.$$

We treat this as a projection with stated assumptions (first-order formula, two-term Hamiltonian, norm-bounded commutator), not as a computed result.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Computed result: approximation entropy at $\varepsilon = 10^{-4}$

**Inputs.** Tolerance $\varepsilon = 10^{-4}$ (chosen as a round design tolerance, analogous to the fractional energy precision implied by quoting collider energies as in [2]); Farey density constant $3/\pi^{2}$ with $\pi = 3.14159265$ (standard mathematical constant).

**Step 1: denominator.** From Section 3.3, $Q_{\varepsilon} = \varepsilon^{-1/2} = (10^{-4})^{-1/2} = 10^{2} = 100$.

**Step 2: grid size.**

$$N_{\mathbb{Q}}(100) \approx \frac{3}{\pi^{2}} \times 100^{2}.$$

Compute $\pi^{2} = 3.14159265^{2} = 9.86960440$. Then

$$\frac{3}{9.86960440} = 0.30396355,$$

and

$$N_{\mathbb{Q}}(100) \approx 0.30396355 \times 10^{4} = 3039.6355 \approx 3040.$$

**Step 3: bits.**

$$H_{\mathrm{app}}(10^{-4}) = \log_{2}(3039.6355) = \frac{\ln(3039.6355)}{\ln 2}.$$

$\ln(3039.6355) = \ln(3.0396355 \times 10^{3}) = \ln 3.0396355 + 3\ln 10 = 1.112244 + 6.907755 = 8.019999$. With $\ln 2 = 0.693147$:

$$H_{\mathrm{app}}(10^{-4}) = \frac{8.019999}{0.693147} = 11.5715 \ \text{bits}.$$

So specifying one continuous parameter in $[0,1]$ to relative tolerance $10^{-4}$ on the rational grid costs approximately $11.57$ bits — about $12$ bits in practice, i.e. a 12-bit register per parameter, a familiar engineering scale.

### 4.2 Projection: Trotter wall for a two-term Hamiltonian

**Inputs (all assumptions, not measurements).** Evolution time $t = 1$ (in units where the commutator norm is dimensionless); commutator norm $\|[H_{1},H_{2}]\| = 1$ (order-unity assumption for a bosonic two-mode truncation); target simulation error $\varepsilon_{\mathrm{sim}} = 10^{-4}$ (matched to Section 4.1).

**Derivation.** From Section 3.4:

$$N_{\mathrm{step}} \sim \frac{t^{2}\,\|[H_{1},H_{2}]\|}{\varepsilon_{\mathrm{sim}}} = \frac{1^{2} \times 1}{10^{-4}} = 10^{4} \ \text{steps}.$$

**Combined translation cost.** If each step requires the parameter to be specified to tolerance $\varepsilon = 10^{-4}$, the total bit cost of the digital translation is the projection

$$C_{\mathrm{tr}} \;=\; N_{\mathrm{step}} \times H_{\mathrm{app}}(\varepsilon) \;\approx\; 10^{4} \times 11.5715 \;=\; 1.15715 \times 10^{5} \ \text{bits},$$

with uncertainty dominated by the order-unity commutator assumption; we state the bound $C_{\mathrm{tr}} \in [10^{4},\,10^{6}]$ bits for $\|[H_{1},H_{2}]\| \in [0.1,\,10]$ and $H_{\mathrm{app}}$ fixed, i.e. $C_{\mathrm{tr}} \in [1.15715 \times 10^{4},\,1.15715 \times 10^{6}]$ bits by direct rescaling of the computed product.

### 4.3 Connection to equilibration losses

The structure analysed in [4] — two well-delineated parts exchanging energy to a shared equilibrium with an irreducible loss of mechanical or electrical energy, under a conserved quantity — maps onto the translation picture as follows: the continuous system (part one) and the digital representation (part two) equilibrate at a shared tolerance, and the "loss" is the approximation entropy $H_{\mathrm{app}}(\varepsilon)$ computed in Section 4.1. This is an analogy at the level of structure, not a derived identity; we flag it as such.

## 5. Results

We report only numbers computed in Section 4, plus clearly labelled projections.

1. **Computed.** The rational grid with maximal denominator $Q = 100$ contains $N_{\mathbb{Q}}(100) \approx 3040$ distinct reduced fractions in $[0,1]$ (Section 4.1, Step 2).
2. **Computed.** The approximation entropy at tolerance $\varepsilon = 10^{-4}$ is $H_{\mathrm{app}}(10^{-4}) = 11.5715$ bits $\approx 12$ bits per continuous parameter (Section 4.1, Step 3).
3. **Projection.** Under the stated assumptions ($t = 1$, $\|[H_{1},H_{2}]\| = 1$, first-order Trotter), the Trotter Wall is $N_{\mathrm{step}} \sim 10^{4}$ steps at $\varepsilon_{\mathrm{sim}} = 10^{-4}$ (Section 4.2).
4. **Projection.** The combined translation cost is $C_{\mathrm{tr}} \approx 1.15715 \times 10^{5}$ bits, with the stated uncertainty band $[1.15715 \times 10^{4},\,1.15715 \times 10^{6}]$ bits (Section 4.2).

No experimental, simulation, or empirical data are reported in this paper.

## 6. Discussion

**Limitations.** The Farey count $N_{\mathbb{Q}}(Q) \approx \tfrac{3}{\pi^{2}}Q^{2}$ is asymptotic; at $Q = 100$ endpoint corrections are non-negligible, so the computed value $3040$ carries an unquantified systematic error of order unity in the prefactor. The identification $\varepsilon = 1/Q^{2}$ uses worst-case Farey spacing; a typical-case treatment would change the scaling from $\log_{2}(1/\varepsilon)$ to roughly $\tfrac{1}{2}\log_{2}(1/\varepsilon)$, halving the bit cost — a factor-of-two ambiguity we cannot resolve from the supplied material. The $\mathbb{Q}$-only thesis of [11] is supported here only at title level, since the supplied entry gives no summary text; a reader who rejects the thesis can still accept Sections 3-4 as statements about digital representation, not about nature.

**Failure modes.** If physical law is not representable by rationals — e.g. if genuinely irrational constants enter irreducibly at the level of observable quantities — the grid picture fails and $H_{\mathrm{app}}$ measures only our storage, not nature's cost. If the Trotter Wall projection is applied beyond two-term Hamiltonians or first-order formulas, the $t^{2}/\varepsilon$ scaling is wrong; higher-order formulas change it to $t^{1+\delta}/\varepsilon^{\delta}$ for small $\delta$, and the Fractal Wall theorem of [12] presumably addresses a deeper recursive structure we have not formalised here.

**What would falsify the claims.** The framework's own falsifiability hook is the calorimetry experimental programme of [12]: if the predicted irreducible cost of continuous-to-digital translation has no calorimetric signature, the physical (as opposed to informational) reading of approximation entropy is falsified. Within this paper, the computed value $H_{\mathrm{app}}(10^{-4}) = 11.5715$ bits is falsified if the Farey-density model of grid size is replaced by any counting model yielding a materially different $N_{\mathbb{Q}}(100)$; the arithmetic itself is checkable line by line.

**Open questions.** (i) What is the correct typical-case rather than worst-case tolerance-denominator relation? (ii) Does the Rosetta Constant of [12] coincide with the prefactor $3/\pi^{2}$ of the Farey density, or is it a distinct quantity? The supplied entry does not say. (iii) How do the 7 open problem categories and 4 extensions of [9] map onto quantitative benchmarks of the kind computed here? (iv) Does the two-pathway structure documented for CFETR and HFRC in [3] — steady-state versus pulsed — correspond to two distinct discretisation strategies with measurably different $C_{\mathrm{tr}}$?

## 7. Conclusion

We have given a minimal quantitative core for the QNFO programme's approximation entropy: a distinction-based discretisation of a continuous parameter, an explicit Farey-type count of the rational grid, a fully computed bit cost $H_{\mathrm{app}}(10^{-4}) = 11.5715$ bits, and a labelled projection of the Trotter Wall $N_{\mathrm{step}} \sim 10^{4}$ under stated assumptions. The exercise shows that the programme's central claims can be made concrete and checkable at small scale, while its deeper structures — the Rosetta Constant, the Fractal Wall, the $\mathbb{Q}$-only thesis — remain, on the supplied material, programmatic rather than derived. The next step is the calorimetric test proposed in [12], which would decide whether approximation entropy is a fact about descriptions or a fact about the world.

## References

[1] arXiv:1910.11775v2 | Physics Briefing Book

[2] arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96

[3] arXiv:2107.11742v1 | MHD analysis on the physical designs of CFETR and HFRC

[4] arXiv:1910.13569v1 | Conservation laws and energy transformations in a class of common physics problems

[5] arXiv:2309.03484v1 | Laws of Physics

[6] arXiv:0710.4947v3 | Physics at a future Neutrino Factory and super-beam facility

[7] arXiv:2312.14190v1 | Machine Learning for Anomaly Detection in Particle Physics

[8] arXiv:0710.3256v2 | Statistical physics of social dynamics

[9] QNFO: Quantum Laws of Form

[10] QNFO: Iceberg of Reality

[11] QNFO: The ℚ-vs-ℝ Question: Why Physical Law Requires Only the Rational Numbers

[12] QNFO: The Two-Level Lie: The Transmon Is Not a Qubit — And the Entire Field Knows It