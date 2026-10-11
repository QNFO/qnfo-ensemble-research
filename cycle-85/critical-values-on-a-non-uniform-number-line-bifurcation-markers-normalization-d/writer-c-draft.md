# Constants as Bifurcation Markers on a Non-Uniform Number Line: A Formalization Program

## Abstract

We propose and partially formalize a conjecture: that the real number line, treated as a uniform continuum, is a misleading projection of physical state spaces, and that certain special values — integers reached by normalized energy in pendulum dynamics, or dimensionless constants such as the fine-structure constant $\alpha \approx 1/137$ — function as bifurcation markers rather than as arbitrary points on a homogeneous axis. We construct a "number-to-phase-space" map for canonical mechanical systems, using the simple pendulum as a fully worked case: its normalized energy $\varepsilon = E/(mgL)$ separates qualitatively distinct dynamics (libration versus rotation) exactly at $\varepsilon = 2$, a value we derive explicitly. We introduce a logarithmic parameter measure under which the "distance" between qualitatively distinct regimes is non-uniform, connecting to visualization work on non-uniform sampling. We review bifurcation literature — secondary bifurcations, Hamiltonian Hopf bifurcations, and resonant normal forms — as the dynamical-systems substrate for the conjecture, and arithmetic-geometric literature on covers and Frobenius fields as evidence that number-theoretic structure is intrinsically non-uniform. We show that $1/\alpha \approx 137.036$ can be framed as a candidate threshold under our map, but we demonstrate that no computation in this paper establishes this; it remains an explicitly labeled hypothesis with a proposed falsification protocol.

## 1. Introduction

Physics pedagogy and practice overwhelmingly treat the real numbers as a uniform stage: the interval between $1.0$ and $1.1$ is, by assumption of the formalism, "the same kind" of interval as that between $2.0$ and $2.1$. Yet working dynamical intuition contradicts this. In pendulum systems, crossing a single normalized energy value changes the qualitative character of all future motion; on either side of that value, infinitesimally nearby parameter points belong to dynamically distinct worlds. The source conjecture motivating this paper states that the real number line is a misleading projection of physical state spaces, that intervals between numbers are not uniform, and that certain values — such as the integer $1$ for the double pendulum's flip threshold under a suitable normalization — act as topological phase boundaries rather than smooth increments [9], [11]. The conjecture further speculates that fundamental constants such as the fine-structure constant $\alpha \approx 1/137$ may similarly mark bifurcation points separating qualitatively different dynamical regimes, for example bound helical versus unbound motion in a Zitterbewegung-type self-interacting particle model [10], [12].

This paper makes three contributions. First, we formalize a number-to-phase-space map $\Phi$ that assigns to each parameter value the topology of the accessible phase-space region, making precise in what sense a parameter value can be a "boundary" rather than a point like any other. Second, we work a canonical example in full arithmetic: the simple pendulum, whose normalized energy threshold is exactly $2$, and we compute the logarithmic measure of the regime it guards. Third, we state, with explicit epistemic labeling, the hypothesis that $\alpha$ plays an analogous role in a helical self-interacting particle model, and we define what would count as confirmation and as falsification. We are careful throughout to separate what is derived here from what is conjectured: no simulation is reported, and every number in Section 5 is computed in Section 4 from stated inputs.

The paper's discipline is deliberately conservative. The literature base supplied to us is heterogeneous — power-line wildfire risk optimization, thermo-convective bifurcation experiments, galactic Hamiltonian dynamics, resonant normal forms, non-uniform sampling in visualization, arithmetic geometry of covers, and Frobenius fields — and we use each strand only for what its own summary supports. The QNFO corpus entries [9]–[12] supply the philosophical framing (time as epistemic construct, critique of the continuum, constants as invariant relations) but their supplied summaries contain no technical detail, and we flag this explicitly.

## 2. Background and Related Work

**Bifurcation phenomenology.** The dynamical-systems literature establishes that parameter space is generically *not* qualitatively uniform: it is stratified by bifurcation sets across which the phase portrait changes type. Three supplied works ground this. Conti and collaborators present experimental results on quenching dynamics in an extended thermo-convective system — a network array of approximately $100$ convective oscillators — going through a secondary subcritical bifurcation, and characterize the resulting dynamical phase transition through the nature of the domain walls (one-dimensional fronts) connecting the basic multicellular pattern with the new oscillating one [3]. This is directly relevant to our program: it is an experimental demonstration that a control parameter's crossing of a critical value reorganizes the *global* topology of the pattern, with fronts mediating between coexisting regimes — precisely the "boundary between worlds" structure our number-to-phase-space map is meant to capture.

Patsis and collaborators study orbital behavior in the neighborhood of complex unstable periodic orbits in a three-dimensional autonomous Hamiltonian system of galactic type, showing that at the transition of a family of periodic orbits from stability to complex instability (the Hamiltonian Hopf bifurcation), the four eigenvalues of the stable periodic orbits move out of the unit circle and the orbits become complex unstable [4]. This supplies a concrete, eigenvalue-based criterion for a qualitative regime change: the unit circle in the complex eigenvalue plane is itself a "special locus" in parameter space, an instance of our thesis that the relevant geometry of parameters is not the linear ordering of reals but the topology of stability regions.

The review of bifurcation sequences in the symmetric $1{:}1$ Hamiltonian resonance surveys periodic-orbit bifurcations in families of resonant Hamiltonian normal forms with nearly equal unperturbed frequencies, invariant under $Z_2 \times Z_2$ symmetry, investigated with geometric methods and related to the singularity-theory approach [5]. This work matters to us because it shows that even near a single resonance, parameter space is carved into a *sequence* of bifurcation regions — the qualitative structure is dense and hierarchical, not a smooth gradient.

**Non-uniformity of representation.** The visualization literature confronts non-uniformity from a different direction: Mortara and colleagues introduce a formal environment modeling, in a virtual space, image features of interest such as absolute and relative density and clusters, and propose non-uniform sampling to preserve relative density when visualizing large datasets, arguing that uniform treatment fails at scale [6]. We borrow the conceptual move — that a uniform grid over a domain misrepresents the domain's structure — and invert it: we claim the physical parameter domain itself, not merely its visualization, is non-uniform.

**Threshold prioritization as a decision-theoretic analogy.** Two supplied works on wildfire risk illustrate the practical consequence of treating a continuous risk parameter as if it were uniform. The risk-assessment framework of [1] addresses prioritizing expensive line upgrades (such as converting overhead lines to underground cables) on the lines that will reduce wildfire ignition risk the most, i.e., explicitly non-uniform allocation over a nominally continuous infrastructure network. The co-optimization work of [2] proposes a mathematical optimization problem for deciding where and when to implement preemptive power shutoffs, which mitigate ignition risk from power lines but cause widespread outages [2]. Both works treat a continuous underlying quantity (risk) as carrying discrete, qualitatively distinct decision regions — an operational echo of our claim that parameter values near a threshold are not interchangeable with values far from it. We use them only as analogy; their summaries say nothing about physics.

**Arithmetic non-uniformity.** Two number-theoretic works support the idea that number systems carry intrinsic, non-uniform structure. The study of $a$-numbers of $\mathbb{Z}/p^2\mathbb{Z}$-covers of the projective line in characteristic $p > 2$ extends a technique of Farnell and Pries for $\mathbb{Z}/p\mathbb{Z}$-covers and shows that the $a$-numbers of "minimal" $\mathbb{Z}/9\mathbb{Z}$-covers can be deduced from the associated branching datum [7]. The relevance is structural: in positive characteristic, the arithmetic of a cover is governed by discrete branching data, not by continuous deformation — special integers ($p$, $9$) control qualitative behavior. On the Frobenius fields of abelian varieties over number fields, the supplied work defines $F(A,v)$ as the Frobenius field generated by the Frobenius eigenvalues at a place $v$ of good reduction and proves, assuming connected monodromy groups, that the set of places $v$ with $F(A,v)$ isomorphic to a fixed number field has upper Dirichlet density zero [8]. This is a rigorous statement that certain arithmetic configurations are *rare* in a precise density sense — a model for what "special value" could mean quantitatively.

**The QNFO corpus.** Four QNFO entries frame the philosophical program: time as an epistemic cognitive fiction [9], a "commutative physics" program [10], the Continuum Critique Trilogy [11], and the thesis that fundamental constants and formulas function as invariant structural relations [12]. The supplied summaries for [9]–[12] contain only titles and identifiers and give no further technical detail; we therefore relate them to our argument only at the level of thesis statements — the continuum is a critiqueable construct, and constants are invariant relations rather than arbitrary decimals — and draw no technical claim from them.

## 3. Methods

### 3.1 The number-to-phase-space map

Let a physical system be given by a parameterized Hamiltonian $H_\lambda$ with parameter $\lambda \in \mathbb{R}$. Define the *regime partition* $\mathcal{P}(\lambda)$ as the equivalence class of the phase portrait of $H_\lambda$ under topological conjugacy of its invariant sets (fixed points, periodic orbits, separatrices). Define the map

$$\Phi : \mathbb{R} \to \{\text{regime classes}\}, \qquad \Phi(\lambda) = \mathcal{P}(\lambda).$$

A value $\lambda_c$ is a *bifurcation marker* if $\Phi$ is discontinuous at $\lambda_c$: arbitrarily small changes $|\lambda - \lambda_c| < \delta$ produce regime classes not reachable for $|\lambda - \lambda_c| \geq \delta$ on the other side. The conjecture of this paper is that the set of bifurcation markers $B = \{\lambda_c\}$ is what makes the number line "non-uniform" for physics: intervals $(\lambda_a, \lambda_b)$ containing many markers are qualitatively dense, while marker-free intervals are qualitatively flat. We define a logarithmic regime measure

$$\mu_{\log}(a, b) = \left| \ln \frac{b}{a} \right|,$$

so that multiplicative rather than additive proximity is the natural metric near thresholds — consistent with the non-uniform sampling philosophy of [6].

### 3.2 Canonical test systems

We use two test systems. (i) The simple pendulum, whose phase portrait is exactly solvable, providing a closed-form bifurcation marker. (ii) The conjectured helical self-interacting particle model of [10], [12], for which we specify only the qualitative question — bound helical versus unbound motion — and the form a stability threshold would take, without asserting any numerical value.

### 3.3 Epistemic labeling

Every quantitative statement carries one of three labels: **[D]** derived in Section 4 with shown arithmetic; **[P]** projection, with stated assumptions and uncertainty bounds; **[H]** hypothesis, explicitly not established here.

## 4. Analysis

### 4.1 Simple pendulum separatrix [D]

The simple pendulum of mass $m$, length $L$, under gravity $g$, has energy

$$E = \frac{1}{2} m L^2 \dot{\theta}^2 + m g L (1 - \cos\theta).$$

The minimum energy is $E_{\min} = 0$ at $\theta = 0$, $\dot{\theta} = 0$. The separatrix — the orbit asymptotic to the unstable equilibrium at $\theta = \pi$ — has energy

$$E_{\text{sep}} = m g L (1 - \cos\pi) = m g L (1 - (-1)) = 2 m g L.$$

Define the normalized energy $\varepsilon = E / (m g L)$. Then:

$$\varepsilon_{\text{sep}} = \frac{2 m g L}{m g L} = 2.$$

For $\varepsilon < 2$ all orbits are librations (oscillation about $\theta = 0$); for $\varepsilon > 2$ all orbits are rotations (full turns). The bifurcation marker is the integer $2$ in this normalization — a clean instance of the source conjecture's claim that integers act as topological phase boundaries under natural normalization [9], [11].

### 4.2 Logarithmic measure of the guarded regime [D]

Using the measure of Section 3.1, the logarithmic distance from the libration floor to the separatrix is

$$\mu_{\log}(1, 2) = \ln\frac{2}{1} = \ln 2 \approx 0.693147.$$

(Arithmetic: $\ln 2 = 0.6931471805\ldots$, rounded to $0.693147$.) By contrast, the additive distance is $2 - 1 = 1$. The two measures disagree by a factor $\frac{1}{0.693147} \approx 1.4427$ (computed as $1 / 0.693147 = 1.44269\ldots$), illustrating concretely that "how far" a parameter value is from a threshold depends on the measure chosen — the operational content of non-uniformity.

### 4.3 The fine-structure constant as candidate marker [H, with D arithmetic on the constant itself]

The fine-structure constant is stated in the source material as $\alpha \approx 1/137$. Taking the conventional value $\alpha^{-1} = 137.035999$ as input (source: the research idea's framing of $\alpha \approx 1/137$; we use the standard quoted inverse to six decimal places as the input number), we compute:

$$\alpha = \frac{1}{137.035999}.$$

Long division: $1 / 137.035999 \approx 0.00729735$ (check: $137.035999 \times 0.00729735 = 137.035999 \times 0.007 = 0.959251993$; $137.035999 \times 0.00029735 = 0.040748\ldots$; sum $\approx 0.9999999$, confirming the reciprocal to the stated precision). Thus $\alpha \approx 7.29735 \times 10^{-3}$ **[D]**.

We emphasize: this arithmetic establishes only the value of $\alpha$, not any dynamical role for it. The claim that $\alpha$ marks a bifurcation between bound helical and unbound motion in a Zitterbewegung-type model is **[H]**: the supplied source material conjectures it [10], [12]; no derivation or simulation in this paper supports it; and Section 6 defines the falsification conditions.

### 4.4 A candidate threshold criterion for the helical model [P]

As a projection only, suppose a helical self-interacting particle model possesses a dimensionless coupling $g_{\text{eff}}$ and a stability threshold $g_c$ at which the character of motion changes. Under our map, the conjecture $\alpha$-as-marker amounts to $g_c = \alpha$. A falsifiable projection: if the model is tuned so that $g_{\text{eff}}$ sweeps through $\alpha$, the sign of the discriminant controlling bound versus unbound motion should change at $g_{\text{eff}} = \alpha$ to within numerical-integration error. We assign no uncertainty bound to $g_c = \alpha$ itself (it is a hypothesis, not a measurement); the uncertainty in any future test would be that of the simulation's threshold localization, which we cannot state without running it.

### 4.5 Rarity heuristic from the Frobenius-density result [D, arithmetic on the stated property only]

The work of [8] states that the set of places with $F(A,v)$ isomorphic to a fixed number field has upper Dirichlet density zero. We use this only qualitatively: "density zero" means the counting proportion tends to $0$, i.e., for any $\eta > 0$, eventually fewer than a fraction $\eta$ of places qualify. No numerical computation follows from the supplied summary beyond this stated property, and we make none.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured.

1. **[D]** The simple pendulum's separatrix occurs at normalized energy $\varepsilon_{\text{sep}} = 2$ exactly, derived from $E_{\text{sep}} = 2mgL$ and $\varepsilon = E/(mgL)$. The integer $2$ is a bifurcation marker in the sense of Section 3.1: $\Phi$ is discontinuous there, separating libration from rotation.

2. **[D]** The logarithmic regime measure from the libration floor to the separatrix is $\mu_{\log}(1,2) = \ln 2 \approx 0.693147$, versus additive distance $1$; the measures differ by a factor $\approx 1.4427$.

3. **[D]** With input $\alpha^{-1} = 137.035999$, the fine-structure constant is $\alpha \approx 0.00729735 \approx 7.29735 \times 10^{-3}$.

4. **[H]** The conjecture that $\alpha$ functions as a bifurcation marker between bound helical and unbound motion in a helical self-interacting particle model is stated as a hypothesis, not a result. No number in this paper supports it beyond the value of $\alpha$ itself.

5. **[P]** The testable form of the hypothesis (Section 4.4): a sign change in the bound/unbound discriminant at $g_{\text{eff}} = \alpha$ under a parameter sweep. This is a projection conditional on the model existing with the stated structure; its uncertainty is the (unquantified) threshold-localization error of the future simulation.

## 6. Discussion

**Limitations.** The formalization of Section 3.1 is deliberately coarse: topological conjugacy of phase portraits is a strong equivalence, and weaker (or stronger) notions of "same regime" would move the location of markers. The simple pendulum is the friendliest possible example — one degree of freedom, exactly solvable, one separatrix. The double pendulum, whose flip threshold the source conjecture cites at normalized value $1$ [9], has two degrees of freedom, chaotic dynamics, and no closed-form separatrix; our map applies in principle but we have not computed anything for it here, and we do not assert the value $1$ as established. The helical-particle model of [10], [12] is specified in the source only at the level of qualitative description; the supplied QNFO summaries contain no equations, so we could not and did not derive a threshold.

**What would falsify the program.** Three failure modes. (i) If, across a broad class of canonical systems, bifurcation markers under natural normalizations are *not* concentrated on small integers or simple rationals but are generically irrational and non-repeating, then "special values" reduce to convention and the non-uniformity thesis loses content. (ii) If a helical self-interacting model can be constructed whose bound/unbound threshold is continuously tunable away from $\alpha$ by changing innocuous model choices, then $\alpha$-as-marker is falsified for that model class. (iii) If the logarithmic measure $\mu_{\log}$ fails to track any physical or informational quantity better than the additive measure does, the non-uniformity is purely formal.

**Against ourselves.** The strongest objection is that the pendulum's integer threshold is an artifact of normalization: choose $\tilde{\varepsilon} = E/(2mgL)$ and the marker becomes $1$; choose $\hat{\varepsilon} = E/(\pi m g L)$ and it becomes $2/\pi$. The conjecture's content therefore cannot be "the marker is an integer" but must be "a natural normalization exists in which the marker is structurally distinguished" — a much weaker claim, and one we can only illustrate, not prove, here. Similarly, the analogy to [7] and [8] is structural, not derivational: nothing in the supplied summaries connects arithmetic-geometric rarity to physical constants, and we claim no such connection. The bifurcation literature [3], [4], [5] supplies the phenomenology of regime change but is silent on which parameter values host it; our thesis adds a hypothesis about that localization which these works neither support nor refute.

**Open questions.** Can the regime partition $\mathcal{P}(\lambda)$ be made computable for the double pendulum, and does its flip threshold land on a distinguished value under a canonical normalization? Does any well-posed self-interacting particle model yield a threshold within an order of magnitude of $\alpha \approx 7.29735 \times 10^{-3}$? Is there a measure-theoretic definition of "special value" for physical parameters mirroring the density-zero rarity of [8]?

## 7. Conclusion

We have formalized the conjecture that physical parameter space is non-uniform by defining a number-to-phase-space map under which certain values are bifurcation markers, and we have verified the map's basic behavior in the exactly solvable pendulum, where the marker is the integer $2$ in normalized energy, with logarithmic distance $\ln 2 \approx 0.693147$ from the regime floor. We computed the fine-structure constant $\alpha \approx 7.29735 \times 10^{-3}$ from its stated inverse and framed its conjectured role as a dynamical threshold as an explicit, falsifiable hypothesis — derived nowhere, asserted nowhere as fact. The program's value, if any, lies in the proposed simulations and in whether natural normalizations repeatedly land thresholds on structurally distinguished numbers; the paper's contribution is the map, the worked example, and the falsification criteria.

## References

[1] arXiv:2110.07348v3 | A Framework for Risk Assessment and Optimal Line Upgrade Selection to Mitigate Wildfire Risk

[2] arXiv:2204.02507v3 | Co-optimization of power line shutoff and restoration under high wildfire ignition risk

[3] arXiv:1103.1495v1 | Exploring the Kibble-Zurek mechanism in a secondary bifurcation

[4] arXiv:1012.2463v2 | The structure and evolution of confined tori near a Hamiltonian Hopf Bifurcation

[5] arXiv:1512.00707v1 | Bifurcation sequences in the symmetric 1:1 Hamiltonian resonance

[6] arXiv:1701.07110v1 | By chance is not enough: Preserving relative density through non uniform sampling

[7] arXiv:2309.12153v2 | $a$-Numbers of Cyclic Degree $p^2$ Covers of the Projective Line

[8] arXiv:2402.07935v3 | On the Frobenius fields of abelian varieties over number fields

[9] QNFO: Time as Epistemic Cognitive Fiction | DOI 10.5281/zenodo.19109392

[10] QNFO: COMMUTATIVE PHYSICS

[11] QNFO: The Continuum Critique Trilogy | DOI 10.5281/zenodo.21691415

[12] QNFO: Invariant Structural Value: Fundamental Constants and Formulas as Invariant Relations | DOI 10.5281/zenodo.21929902