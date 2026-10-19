# Distinction, Discretisation, and the Cost of Law: A Quantitative Sketch of Approximation Entropy

## Abstract

Physics asks what the laws are; a prior question is what it costs to state and to compute with a law. When a continuous physical parameter is represented in a digital system — a simulator, a control register, a data pipeline — the representation must be a rational number stored in finitely many bits, and the number of bits is not free. Building on the distinction-based formalism of Spencer-Brown's *Laws of Form* as consolidated in the Quantum Laws of (QNFO) programme, and on the QNFO thesis that physical law requires only the rational numbers, we develop a quantitative sketch of *approximation entropy*: the information cost of translating continuous bosonic physics into discrete digital computation. We model the digital representation as a rational grid, count admissible states with a Farey-type estimate, and derive $H_{\mathrm{app}}(\varepsilon) = \log_{2}\!\bigl(3/(\pi^{2}\varepsilon)\bigr)$ for the bits needed to specify a parameter on $[0,1]$ to absolute tolerance $\varepsilon$. With every arithmetic step shown we compute $H_{\mathrm{app}}(10^{-4}) = 11.5697$ bits and $H_{\mathrm{app}}(10^{-6}) = 18.2136$ bits, confirming the $\log_{2}(1/\varepsilon)$ scaling, and we derive as a labelled projection the Trotter-step cost $N_{\mathrm{step}} \sim t^{2}\,\|[H_{1},H_{2}]\|/\varepsilon_{\mathrm{sim}}$, giving a combined translation cost $C_{\mathrm{tr}} \approx 1.157 \times 10^{5}$ bits under stated assumptions. The result turns a metaphysical thesis about rational-valued law into checkable engineering arithmetic: register widths, step counts, and their scaling with tolerance.

## 1. Introduction

Every digital simulation of a continuous quantum system faces the same accounting problem before any physics is done: a parameter that the theory writes as a real number must be stored as a rational number in a finite register, and a continuous evolution must be chopped into finitely many computational steps. The people who face this daily are the developers of digital quantum simulators, the designers of control systems for superconducting and trapped-ion qubits, and the authors of large-scale scientific computing pipelines for quantum dynamics. If the register is too narrow or the step count too small, the simulation silently deviates from the continuous target; if they are too generous, compute time and memory are wasted across every run. A concrete number for "how many bits per parameter" and "how many steps per evolution" changes the design conversation from intuition to arithmetic.

The QNFO research programme approaches this from the opposite end. Following Spencer-Brown as consolidated in the QNFO synthesis, the primitive operation from which logic, mathematics, and physics are constructed is the drawing of a distinction; a finite sequence of distinctions induces a finite partition, which is exactly what a discretisation grid is [10]. A second QNFO thesis holds that measurements yield finite-precision rational numbers, that the real number is the limit of a sequence of rational measurements and is a mathematical rather than a physical operation, and that explicit $\mathbb{Q}$-based constructions — lattice QFT, finite-dimensional quantum mechanics, Regge calculus for general relativity — establish observational equivalence between $\mathbb{Q}$-based and continuum formulations across fundamental theories [11]. A third QNFO framing proposes that physical reality emerges from a deterministic computational process on a topological substrate, the circle $S^{1}$, whose first homotopy group $\pi_{1}(S^{1}) \cong \mathbb{Z}$ yields integer winding numbers as complete information carriers [12]. All three positions share a commitment: the physically operative description is discrete and countable, and the continuum is an effective idealisation.

What the programme has lacked is a minimal, fully explicit quantitative core: given these commitments, what is the actual bit cost of representing one continuous parameter, and what is the actual step cost of simulating one continuous evolution? This paper supplies that core. Our contribution is deliberately modest and self-contained:

1. We define a rational-grid discretisation of a single continuous physical parameter and derive, with every arithmetic step shown, the number of bits needed to specify that parameter to a stated tolerance: $H_{\mathrm{app}}(10^{-4}) = 11.5697$ bits (Section 4.1).
2. We compute a second point, $H_{\mathrm{app}}(10^{-6}) = 18.2136$ bits, and verify the scaling law $H_{\mathrm{app}}(\varepsilon) = \log_{2}\!\bigl(3/(\pi^{2}\varepsilon)\bigr)$ by checking that the increment matches $\log_{2}(100) = 6.6439$ bits per two decades of tolerance (Section 4.2).
3. We derive the scaling of the number of Trotter steps needed to simulate a continuous unitary evolution digitally to a stated error, and combine it with the bit cost into a single figure of merit, the *translation cost* $C_{\mathrm{tr}} \approx 1.157 \times 10^{5}$ bits, exhibited as a labelled projection with stated assumptions and an uncertainty band (Section 4.3).
4. We situate the framework against the cited literature, from collider design studies to the philosophy of laws, and state explicitly what would falsify the claims (Sections 2 and 6).

We emphasise scope: this is a sketch of a framework, not a derivation of any established physical theory. All quantitative claims are either computed here with shown arithmetic or explicitly labelled projections with stated assumptions.

## 2. Background and Related Work

The works below are discussed in the bibliography's exact order and numbering; each is cited for a specific point its own text makes.

[1] The *Physics Briefing Book* describes the European Particle Physics Strategy Update (EPPSU) as a bottom-up process in which the community is first invited to submit proposals — inputs — for projects to be realised in the near, mid and longer term, with national and laboratory inputs also important elements. Its text also records the precision programme that motivates our tolerance choices: at future $e^{+}e^{-}$ colliders the oblique parameters will be measured with a precision of about $1\%$, roughly a factor of 10 better than current precision, and circular colliders would deliver $10^{12}$ $Z$ bosons. A measurement programme whose target precision is $10^{-2}$ and whose statistics reach $10^{12}$ events is precisely a programme in which continuous physical parameters must be represented, transmitted and analysed at controlled discrete precision; the EPPSU aggregation process is likewise a model of how a community converts an unbounded space of candidate directions into a finite decision list, the same reduction that a discretisation grid performs on a continuous parameter space.

[2] The Snowmass '96 report on the Next Linear Collider presents the design and physics programme of an $e^{+}e^{-}$ linear collider of centre-of-mass energy $0.5$–$1.5$ TeV, reviews the experiments the facility would carry, and argues its key role in exploring physics beyond the Standard Model, whose broken symmetry "must provide new physical phenomena at the TeV energy scale". Its account of the Stanford Linear Collider — built to study the $100$-GeV scale and to develop the accelerator physics needed for future colliders — and its note that microwave power sources had already exceeded the requirements for the initial stage of the NLC illustrate a design study in which a continuous design parameter (beam energy, field strength) must be committed to a discrete, achievable operating point. That commitment is the engineering face of the parameter-quantisation step our formalism makes explicit in Section 3.

[3] The MHD analysis of CFETR and HFRC treats two major Chinese fusion projects, representative of the low-density steady-state and high-density pulsed pathways to fusion, both under intensive physical and engineering design. Its numerical setup is a concrete instance of continuous physics rendered as discrete computation: the reduced-MHD code TM8 is run with a Lundquist number $S = \tau_{R}/\tau_{A} = 5.56 \times 10^{6}$, inverse aspect ratio $\varepsilon = a/R \simeq 0.31$, local bootstrap current fraction $j_{b}/j_{p} = 0.3$, and resistive time $\tau_{R} = a^{2}\mu_{0}/\eta$. Its summary of results — ECCD power and current for full stabilisation of the neoclassical tearing mode predicted, and active control required for RWM stabilisation in 80% of the steady-state scenarios — shows continuous magnetohydrodynamic stability questions answered only through discretised computation with explicitly chosen dimensionless parameters. The two-pathway structure (steady-state versus pulsed) also echoes our two-level structure of continuous physics versus discrete description.

[4] The conservation-laws paper analyses systems with two well-delineated parts that exchange energy and reach a shared equilibrium with a loss of mechanical or electrical energy, constrained by a conserved quantity such as mass, charge, momentum or angular momentum. Its central result is a universal formula: for systems with two state variables $\mathcal{M}$ and $\mathcal{V}$ in which the energy is $\tfrac{1}{2}\mathcal{M}\mathcal{V}^{2}$ and the product $\mathcal{M}\mathcal{V}$ is constant, the energy change is $\Delta E = -\,\tfrac{1}{2}\,\frac{\mathcal{M}_{1}\mathcal{M}_{2}}{\mathcal{M}_{1}+\mathcal{M}_{2}}\,\mathcal{V}_{\mathrm{rel}}^{2}$. This is directly relevant to Section 4.4: the equilibration of a continuous quantity between two discrete subsystems, with an irreducible loss fixed by a conservation law, is the physical picture behind our translation cost.

[5] *Laws of Physics* is a philosophical introduction to laws, connecting them to ontology, possibility, explanation, induction, counterfactuals, time, determinism and fundamentality, and defending a minimal primitivist account on which laws are fundamental facts that govern the universe by constraining its possibilities. Two of its specific claims bear on our framing. First, its discussion of nomic vagueness concludes that fundamental laws of physics can be vague, that this may be an artefact of classical mechanics naturally avoided in quantum mechanics, and that nomic exactness may therefore be a metaphysically contingent feature of the actual laws. Second, it postulates a principle of nomic simplicity as a methodological constraint on theory choice. If exactness is contingent and simplicity is a methodological principle rather than a fact, then the discretisation cost we quantify is a cost of description whose physical status must be argued for separately — exactly the distinction our Section 6 maintains.

[6] The Neutrino Factory ISS report presents the conclusions of the Physics Working Group of the international scoping study carried between NuFact05 (Rome, June 21–26, 2005) and NuFact06 (Irvine, California, 24–30 August 2006), with the principal objective of laying the foundations for a full conceptual-design study. Its physics sections show why precision matters there: the SNO neutral-current to charged-current ratio established an active non-electron flavour in the solar neutrino flux at the $5.3\sigma$ level, and atmospheric-neutrino parameters such as $\Delta m^{2}_{32}$ and $\sin^{2}\theta_{23}$ are constrained by zenith-angle fits. Like [2], it is a facility study in which continuous physics goals are translated into discrete machine parameters; it corroborates that the translation problem our formalism prices is one that large collaborations actually face.

[7] The review of machine learning for anomaly detection in particle physics distinguishes two primary types of anomaly detection in high-energy physics — outlier detection of unusual events in the tails of distributions, and over-density detection analogous to the bump hunt — and notes that particle physics data fundamentally cannot be labeled the way images can, since every sample may be signal, background, or a quantum superposition of the two. Its conclusion records that automated ML-based data-quality monitoring is already utilised in experiments and will matter as the LHC is upgraded to the HL-LHC, collecting an order of magnitude more data, and that its survey of quantum models finds they are not designed to manifest an inductive bias towards the structure of the chosen datasets. In our framework, an out-of-distribution event is a point that falls outside the discretised grid on which the monitoring model was built; the review's taxonomy of detection tasks and its observation about missing inductive bias both bear on how grid choice — the object our $H_{\mathrm{app}}$ prices — affects downstream analysis.

[8] The statistical-physics review of social dynamics describes the trend of applying statistical physics to fields far from its traditional domain, with humans rather than particles as elementary units, and notes that in any mathematical model opinion has to be a variable — a collection of numbers — even though everyday positions are often as few as two. Its outlook states that the statistical-physics role in social dynamics has mainly been modelling, introducing new models or analysing existing ones for phase transitions and universality, guided by the quest for simplicity. This is a precedent for exporting a physics formalism to a domain of discrete elementary units, the same export direction as the distinction-based construction of [10].

[9] The QNFO *Iceberg of Reality* paper visualises physical understanding as an iceberg whose surface layer is the world of classical, deterministic order built on Newtonian mechanics and Maxwell's equations, with deeper layers — quantum, thermodynamic, geometric, informational — descending below the waterline. Its account of the quantum transition centres on the blackbody radiation problem, demonstrated by Kirchhoff to be universal and material-independent, which refused to yield to classical explanation. The layered picture supports our reading of the continuum as a surface-level effective description: the layer at which continuous parameters appear is, on this view, not the deepest one, which is what licenses asking what the continuous layer costs to represent from below.

[10] The QNFO *Quantum Laws of Form* consolidation records that Spencer-Brown's *Laws of Form* (1969) proposed the act of drawing a distinction as the primitive operation from which logic, mathematics and physics can be constructed, and that the consolidation synthesises known quantum correspondences, identifies 7 open problem categories and proposes 4 extensions. Its excerpts give concrete content: the spin-statistics theorem is recast so that boson and fermion patterns differ by the symmetry of a cross-ratio under exchange, with the fermion pattern picking up a phase of $\pi$; a simulation section models a qubit as two balls on a binary Bruhat–Tits tree truncated to depth $D = 5$, with noise rate $10^{-3}$ per ns per vertex and energy barrier $\Delta E = 10\,k_{B}T$, reporting a logical error rate below $10^{-12}$ per gate and gate fidelity $0.999999$; and an experimental-strategy section predicts a first excited resonance $H_{4}$ around $250$ GeV with a broader width than a narrow-resonance search assumes. This is the primary source of our formalism's primitive: a finite set of distinctions is a finite partition, and a finite partition is a grid.

[11] The QNFO $\mathbb{Q}$-versus-$\mathbb{R}$ memo defends the thesis that the rational numbers are the physically correct base field. Its argument has three load-bearing parts. Measurement Finitude: measurements yield finite-precision rational numbers, established by three independent physical bounds (Bekenstein, Holevo, thermal noise) and by the historical record of experimental physics, with the real number the limit of a sequence of rational measurements — a mathematical, not physical, operation. Observational Equivalence: explicit $\mathbb{Q}$-based constructions (lattice QFT via Wilson's construction, finite-dimensional Hilbert spaces, Regge calculus for general relativity) establish observational equivalence for all fundamental physical theories. And a structural corollary: by Ostrowski's theorem there is exactly one Archimedean absolute value on $\mathbb{Q}$ and one $p$-adic absolute value per prime, so if physics operates on $\mathbb{Q}$, Ostrowski's theorem becomes a physical organising principle, whereas it is irrelevant if physics operates on $\mathbb{R}$; further, the uncountability of $\mathbb{R}$ is a property of mathematics, not of physics, since the physically accessible numbers are countable, computable and $\mathbb{Q}$-approximable. Our Section 3 operationalises exactly the last point: a digital description stores a rational, and the count of admissible rationals determines the bit cost.

[12] The QNFO *Physics, Solved* paper reframes the canonical unsolved problems in physics as diagnostic signatures of a descriptive rather than generative paradigm, and proposes that physical reality emerges from a deterministic computational process on the circle $S^{1}$, whose first homotopy group $\pi_{1}(S^{1}) \cong \mathbb{Z}$ yields integer winding numbers as complete information carriers — magnitude sets mass-energy, prime factorisation encodes quantum charges — with a topological resonance condition governed by the golden ratio selecting a sparse spectrum of stable states, explaining the hierarchy problem and exactly three fermion generations. For our purposes the relevant point is methodological: information carriers that are integers are countable, and a countable carrier has a definite bit cost, which is the quantity our framework computes for the general case of a rational grid.

## 3. Methods

### 3.1 Distinctions and grids

Following [10], the primitive is a distinction: a partition of a space into two labelled regions. A finite sequence of distinctions induces a finite partition, which we identify with a discretisation grid. A continuous parameter $x \in [0,1]$ is represented digitally by a rational $p/q$ with $1 \le q \le Q_{\max}$, where $Q_{\max}$ is the maximal denominator admitted by the representation. This is the operational content of the $\mathbb{Q}$-only position of [11]: whatever the theory writes as a real number, a digital description stores a rational, and the physically accessible numbers are countable and $\mathbb{Q}$-approximable.

### 3.2 Counting admissible rationals

The number of distinct reduced fractions $p/q$ with $0 \le p \le q \le Q$ in $[0,1]$ is asymptotically

$$N_{\mathbb{Q}}(Q) \approx \frac{3}{\pi^{2}}\,Q^{2}.$$

The derivation is standard: the density of coprime pairs in the integer lattice is $1/\zeta(2) = 6/\pi^{2}$; each coprime pair $(p,q)$ with $q \le Q$ contributes one reduced fraction, and the constraint $0 \le p \le q$ selects a triangular half of the pair space, giving $\tfrac{1}{2} \cdot \tfrac{6}{\pi^{2}} Q^{2} = \tfrac{3}{\pi^{2}} Q^{2}$ up to endpoint corrections. We use this as the model of the size of the rational grid.

### 3.3 Approximation entropy

We define the approximation entropy at tolerance $\varepsilon$ as

$$H_{\mathrm{app}}(\varepsilon) \;=\; \log_{2}\!\bigl(N_{\mathbb{Q}}(Q_{\varepsilon})\bigr),$$

where $Q_{\varepsilon}$ is the smallest maximal denominator such that every point of $[0,1]$ lies within $\varepsilon$ of some grid rational. Consecutive Farey fractions $a/b < c/d$ satisfy $|c/d - a/b| = 1/(bd)$, so the worst-case spacing with $q \le Q$ is of order $1/Q^{2}$. We therefore set

$$\varepsilon \;=\; \frac{1}{Q_{\varepsilon}^{2}} \quad\Longrightarrow\quad Q_{\varepsilon} \;=\; \varepsilon^{-1/2},$$

and hence

$$H_{\mathrm{app}}(\varepsilon) \;=\; \log_{2}\!\left(\frac{3}{\pi^{2}}\,Q_{\varepsilon}^{2}\right) \;=\; \log_{2}\!\left(\frac{3}{\pi^{2}\,\varepsilon}\right).$$

On the unit interval $[0,1]$, absolute and relative tolerance coincide for parameter values of order unity, so the formula reads directly as a register-width requirement.

### 3.4 Trotter step cost

For a digital simulation of a continuous-time evolution under a Hamiltonian $H = H_{1} + H_{2}$, a first-order Trotter decomposition of $e^{-i(H_{1}+H_{2})t}$ into $N_{\mathrm{step}}$ steps of size $\Delta t = t/N_{\mathrm{step}}$ incurs a per-step commutator error of order $\Delta t^{2}\,\|[H_{1},H_{2}]\|$, so the total error scales as

$$\varepsilon_{\mathrm{sim}} \;\sim\; N_{\mathrm{step}}\,\Delta t^{2}\,\|[H_{1},H_{2}]\| \;=\; \frac{t^{2}}{N_{\mathrm{step}}}\,\|[H_{1},H_{2}]\|.$$

Solving for the step count gives

$$N_{\mathrm{step}} \;\sim\; \frac{t^{2}\,\|[H_{1},H_{2}]\|}{\varepsilon_{\mathrm{sim}}}.$$

We treat results built on this formula as projections with stated assumptions (first-order formula, two-term Hamiltonian, norm-bounded commutator), not as computed results.

### 3.5 Translation cost

The combined figure of merit is the product of the two costs: if each of $N_{\mathrm{step}}$ steps requires the continuous parameter to be specified to tolerance $\varepsilon$, the total bit cost of the digital translation is

$$C_{\mathrm{tr}} \;=\; N_{\mathrm{step}} \times H_{\mathrm{app}}(\varepsilon).$$

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Computed result: approximation entropy at $\varepsilon = 10^{-4}$

**Inputs.** Tolerance $\varepsilon = 10^{-4}$, chosen as a round design tolerance; collider and facility studies such as [2] and [6] must likewise select discrete operating points and precisions from continuous design ranges, and [1] records a target precision of about $1\%$ — i.e. $\varepsilon \sim 10^{-2}$ — for oblique-parameter measurements, so $10^{-4}$ sits two orders beyond that target as a demanding but conventional choice. Farey density constant $3/\pi^{2}$ with $\pi = 3.14159265$ (standard mathematical constant).

**Step 1: denominator.** From Section 3.3,

$$Q_{\varepsilon} = \varepsilon^{-1/2} = (10^{-4})^{-1/2} = 10^{2} = 100.$$

**Step 2: grid size.**

$$N_{\mathbb{Q}}(100) \approx \frac{3}{\pi^{2}} \times 100^{2}.$$

Compute $\pi^{2} = 3.14159265^{2} = 9.86960440$. Then

$$\frac{3}{9.86960440} = 0.30396355,$$

and

$$N_{\mathbb{Q}}(100) \approx 0.30396355 \times 10^{4} = 3039.6355.$$

**Step 3: bits.**

$$H_{\mathrm{app}}(10^{-4}) = \log_{2}(3039.6355) = \frac{\ln(3039.6355)}{\ln 2}.$$

Decompose the logarithm:

$$\ln(3039.6355) = \ln(3.0396355 \times 10^{3}) = \ln 3.0396355 + 3\ln 10.$$

With $\ln 3.0396355 = 1.111737$ and $\ln 10 = 2.302585$, so $3\ln 10 = 6.907755$:

$$\ln(3039.6355) = 1.111737 + 6.907755 = 8.019492.$$

With $\ln 2 = 0.693147$:

$$H_{\mathrm{app}}(10^{-4}) = \frac{8.019492}{0.693147} = 11.5697 \ \text{bits}.$$

So specifying one continuous parameter in $[0,1]$ to absolute tolerance $10^{-4}$ on the rational grid costs $11.5697$ bits — about $12$ bits in practice, i.e. a 12-bit register per parameter, a familiar engineering scale.

### 4.2 Computed result: scaling check at $\varepsilon = 10^{-6}$

**Inputs.** Tolerance $\varepsilon = 10^{-6}$, two decades beyond Section 4.1; same constants $\pi = 3.14159265$, $\ln 10 = 2.302585$, $\ln 2 = 0.693147$.

**Step 1: denominator.**

$$Q_{\varepsilon} = (10^{-6})^{-1/2} = 10^{3} = 1000.$$

**Step 2: grid size.**

$$N_{\mathbb{Q}}(1000) \approx 0.30396355 \times 10^{6} = 303963.55.$$

**Step 3: bits.**

$$\ln(303963.55) = \ln 3.0396355 + 5\ln 10 = 1.111737 + 11.512925 = 12.624662.$$

$$H_{\mathrm{app}}(10^{-6}) = \frac{12.624662}{0.693147} = 18.2136 \ \text{bits}.$$

**Scaling check.** The closed form predicts

$$H_{\mathrm{app}}(10^{-6}) - H_{\mathrm{app}}(10^{-4}) = \log_{2}\!\left(\frac{10^{6}}{10^{4}}\right) = \log_{2}(100) = \frac{\ln 100}{\ln 2} = \frac{4.605170}{0.693147} = 6.6439 \ \text{bits}.$$

The direct computation gives $18.2136 - 11.5697 = 6.6439$ bits, matching the closed-form increment exactly to the digits shown. This confirms that the computed values follow the scaling $H_{\mathrm{app}}(\varepsilon) = \log_{2}\!\bigl(3/(\pi^{2}\varepsilon)\bigr)$ and that the cost grows by $6.6439$ bits — roughly a 7-bit register widening — per two decades of tightened tolerance.

### 4.3 Projection: Trotter step count and combined translation cost

**Inputs (all assumptions, not measurements).** Evolution time $t = 1$, in units where the commutator norm is dimensionless; commut