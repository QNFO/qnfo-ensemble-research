# Master Calibration and the Composition of Partial Translations: A Formal Framework for Physics' Unresolved Schisms

## Abstract

Physics presents itself as convergent, yet systematic inventories of its foundations reveal dozens of unresolved bifurcations: general relativity versus quantum mechanics, continuum versus discrete descriptions, the Heisenberg cut, compositional versus holistic accounts, and the status of the observer. We propose that these schisms are not failures of individual theories but symptoms of frameworks that are each internally self-consistent over disjoint domains, lacking a "master calibration" that translates between them. We formalize this conjecture: each framework is modeled as a calibrated theory over a domain, inter-framework partial translation maps are defined (with decoherence as a quantum-to-classical calibration and coarse-graining as a micro-to-macro calibration), and we derive conditions under which translations fail to compose. We show that the number of pairwise translation maps required grows quadratically in the number of frameworks, that composition error accumulates linearly along translation chains under a worst-case bound, and that commutativity of translation squares is a non-generic property that must be checked rather than assumed. We classify schisms as structural (composition failure is unavoidable) versus conventional (a calibration choice resolves them), and connect the program to calibration methods developed for non-overlapping sensor fields of view, out-of-domain machine learning, and cosmological instrumentation. The framework yields falsifiable criteria for whether a common underlying structure could calibrate all pairs simultaneously.

## 1. Introduction

The standard narrative of physics is one of progressive unification: electricity and magnetism, space and time, matter and information. Against this narrative, the QNFO inventory "The Hidden Fractures: Self-Referential Calibration and the 29 Schisms of Physics" [9] documents 29 unresolved bifurcations and hidden assumptions, ranging from the nature of the continuum to the status of the observer, the consistency of mathematical language, and the meaning of explanation. The companion program "The Ultrametric Program" [11] claims that seven research domains are seven vocabularies for one structural object — nested hierarchical partition logic defined by the ultrametric inequality — and proposes three falsifiable hypotheses, and "The Observer Inside the Tree" [10] examines the claim that the observer-inside-versus-outside schism can be resolved by embedding the observer as a node in an ultrametric tree structure.

This paper takes a different but complementary tack. Rather than seeking one structure that subsumes all domains, we ask a calibration question: given a collection of internally consistent frameworks, each valid over its own domain, what does it take to translate between them, and when do those translations fail? The guiding metaphor is metrology. A vector network analyzer measurement is meaningless until a calibration converts raw scattering parameters into corrected device data; the thru-free multiline calibration of [8] shows that even the calibration standards themselves can be rechosen without loss of determinability. Similarly, we conjecture that the schisms of physics are calibration problems between towers of theory whose "measurement standards" — the primitives each framework treats as given — do not overlap.

The central objects of study are:

1. **Frameworks** $F_i$, each a self-consistent theory over a domain $D_i$.
2. **Partial translation maps** $\tau_{ij}: D_i \supset S_{ij} \to D_j$, defined only on overlap regions $S_{ij} = D_i \cap D_j$ where such overlap exists.
3. **Composition conditions**: when does $\tau_{jk} \circ \tau_{ij}$ agree with $\tau_{ik}$ on the relevant domain?
4. **Master calibration**: a family $\{\tau_{ij}\}$ that composes consistently for all pairs simultaneously.

Our contributions are: (i) a formal definition of framework, translation, and calibration failure; (ii) explicit counting and error-accumulation results showing that pairwise calibration alone does not guarantee global consistency; (iii) a classification criterion separating structural schisms (no translation can compose) from conventional ones (a calibration choice suffices); and (iv) a survey of calibration practice in adjacent fields that already confronts non-overlapping domains, showing that the physics problem has working analogues.

## 2. Background and Related Work

We organize the related work into three strands: physics strategy and instrumentation, calibration in engineering and machine learning, and the QNFO schisms corpus.

**Physics strategy and the limits of current programs.** The European Particle Physics Strategy Update process takes a bottom-up approach in which the community first submits proposals for projects to be realised in the near-term, mid-term and longer-term future, with national and laboratory inputs as important elements [1]. This is relevant to us as a sociological datum: prioritization of large-scale experiments proceeds through structured community input, and foundational schisms — being cross-cutting rather than facility-specific — fit awkwardly into such a process. Earlier, the report on the physics and technology of the next linear collider presented expectations for an $e^+e^-$ linear collider of center-of-mass energy 500 GeV -- 1 TeV, reviewing experiments that would explore physics beyond the Standard Model over the full range of theoretical possibilities and arguing feasibility of construction [2]. In our vocabulary, [2] treats "beyond the Standard Model" as a single extension axis; the schisms framework suggests instead that the space of unresolved questions is not one-dimensional. The MHD analysis of the CFETR and HFRC fusion designs assesses two major projects representative of the low-density steady-state and high-density pulsed pathways to fusion [4]; this is a concrete instance of two internally developed design frameworks — steady-state versus pulsed — coexisting without a shared optimization criterion, a small-scale analogue of the schism structure we formalize.

**Calibration with non-overlapping domains.** The closest engineering analogue to our problem is extrinsic calibration of sensors with non-overlapping fields of view. The "Road is Enough!" framework performs targetless extrinsic calibration of stereo cameras and LiDAR sensors with a non-overlapping field of view, exploiting road markings as static and robust features among dynamic objects [3]. This demonstrates that calibration between two measurement frameworks that share no direct overlap is possible when a third structure (the road) is visible to both — precisely the "mediating domain" move we formalize in Section 3. In microwave metrology, the thru-free multiline calibration modifies traditional thru-reflect-line (TRL) or line-reflect-line (LRL) calibration for vector network analyzers, eliminating the need for a thru standard by using an arbitrary transmissive two-port device plus a reflect standard, which allows arbitrary choice of standards [8]. This shows that the internal consistency of a calibration family can be maintained while relaxing which physical standards anchor it — an existence proof that "which primitive is assumed" can be a free choice, i.e., that some calibration constraints are conventional rather than structural. In radio astronomy, the unified calibration framework for 21 cm cosmology observes that calibration precision is a limiting systematic, and that approaches divide into "sky-based" methods relying on an extremely accurate model of foreground emission and "redundant" methods requiring a precisely regular array with near-identical antenna response patterns [6]. The two classes rely on disjoint assumptions — an external sky model versus internal array regularity — and the entry notes both classes face limits; this is a live example of two calibration paradigms whose domains of validity do not obviously compose.

**Calibration and out-of-domain generalization.** In machine learning, "On Calibration and Out-of-domain Generalization" draws a link between out-of-domain performance and model calibration, arguing that calibration across multiple domains can be viewed as a special case of an invariant representation [5]. This is the most direct conceptual precedent for our "master calibration" notion: a model that is calibrated across domains is one whose uncertainty statements translate consistently between domains, and [5] frames this as invariance. "Post-hoc Uncertainty Calibration for Domain Drift Scenarios" addresses uncertainty calibration for deep networks, noting that standard networks yield uncalibrated predictions while post-hoc methods can produce calibrated confidence scores representative of true likelihood, but that prior focus has been on in-domain calibration [7]. The entry's two-fold contribution begins from the observation that in-domain calibration does not automatically transfer — the machine-learning echo of our composition-failure thesis.

**The QNFO corpus.** "The Hidden Fractures" [9] supplies the inventory of 29 unresolved bifurcations and hidden assumptions that motivates our framework count; its summary states the inventory spans the nature of the continuum, the status of the observer, the consistency of mathematical language, and the meaning of explanation, and frames the response as self-referential calibration. "The Observer Inside the Tree" [10] subjects the claim that schism S10 (observer inside vs. outside) is resolved by embedding the observer as a node in an ultrametric tree — eliminating the need for an external vantage point — to independent scrutiny; the supplied summary indicates the paper is an evaluation of that claim rather than an unqualified endorsement, which is the right epistemic posture for our purposes: proposed resolutions of schisms must themselves be calibrated. "The Ultrametric Program" [11] claims seven research domains are vocabularies for one structural object — nested hierarchical partition logic defined by the ultrametric inequality, with p-adic/adelic arithmetic as one realization and the hierarchy as the invariant — and states three falsifiable hypotheses (H1 compression prior, H2 Ar...; the supplied summary is truncated at this point, so we cannot state H2 and H3's content and confine ourselves to noting that falsifiable hypotheses are proposed). The ultrametric program is, in our language, a candidate master calibration: a single invariant (the hierarchy) intended to translate across seven domains. Our composition analysis gives a criterion such a candidate must satisfy.

## 3. Methods

### 3.1 Frameworks and domains

**Definition 3.1 (Framework).** A framework is a pair $F_i = (D_i, \mathcal{P}_i)$ where $D_i$ is a domain (a set of states, configurations, or propositions the framework speaks about) and $\mathcal{P}_i$ is a set of primitives — quantities, operations, or axioms the framework treats as given without further calibration. A framework is *internally consistent* if no contradiction is derivable within $D_i$ using $\mathcal{P}_i$.

Examples: non-relativistic quantum mechanics $F_{\mathrm{QM}}$ with primitives including the Hilbert-space state $|\psi\rangle$ and unitary evolution $U_t = e^{-iHt/\hbar}$; classical statistical mechanics $F_{\mathrm{SM}}$ with primitives including phase-space measure and coarse-graining cells; general relativity $F_{\mathrm{GR}}$ with the metric $g_{\mu\nu}$ as primitive.

**Definition 3.2 (Translation map).** A translation from $F_i$ to $F_j$ is a partial map $\tau_{ij}: S_{ij} \to D_j$ with $S_{ij} \subseteq D_i$, together with a calibration certificate: a specification of how primitives of $F_i$ are expressed in primitives of $F_j$ on $S_{ij}$. The map is *calibrated on $S_{ij}$* if predictions about elements of $S_{ij}$ agree under $F_i$ and under $\tau_{ij}(F_i)$ within stated tolerance $\epsilon_{ij}$.

Two canonical examples, both standard physics rather than novel claims: decoherence supplies a quantum-to-classical translation $\tau_{\mathrm{QM}\to\mathrm{cl}}$ valid on the sector of states where environment-induced superselection holds; coarse-graining supplies a micro-to-macro translation $\tau_{\mu\to M}$ valid above a resolution scale $\ell_{\mathrm{cg}}$.

### 3.2 Composition and the master calibration

**Definition 3.3 (Composition failure).** Given $\tau_{ij}$ and $\tau_{jk}$, the composed map $\tau_{jk} \circ \tau_{ij}$ is defined on $\tau_{ij}^{-1}(S_{jk})$. Composition *fails* if there exists $x$ in this domain such that
$$(\tau_{jk} \circ \tau_{ij})(x) \neq \tau_{ik}(x),$$
i.e., the direct translation disagrees with the chained translation.

**Definition 3.4 (Master calibration).** A family $\mathcal{T} = \{\tau_{ij}\}_{i<j}$ is a master calibration if every square commutes:
$$\tau_{jk} \circ \tau_{ij} = \tau_{ik} \quad \text{on } \tau_{ij}^{-1}(S_{jk}) \cap S_{ik}.$$

**Definition 3.5 (Structural vs. conventional schism).** A schism between $F_i$ and $F_j$ is *structural* if no calibrated $\tau_{ij}$ exists on any nontrivial overlap (or every candidate $\tau_{ij}$ provably fails composition with all third frameworks); it is *conventional* if calibrated translations exist and the choice among them is underdetermined by the frameworks themselves, as in the thru-standard choice of [8].

### 3.3 Mediating domains

Following the strategy validated in [3] — calibrating two sensors with non-overlapping fields of view through a structure (road markings) visible to both — we define a *mediating domain* $M$ with translations $\tau_{iM}: S_{iM} \to M$ and $\tau_{Mj}: M \supset \tau_{iM}(S_{iM}) \to D_j$. The mediated translation is $\tau_{Mj} \circ \tau_{iM}$. The key question, addressed quantitatively in Section 4, is whether mediated translations compose as well as direct ones would.

### 3.4 Error model

We attach to each calibrated translation a worst-case error $\epsilon_{ij} \geq 0$: the supremum over $x \in S_{ij}$ of the disagreement between $F_i$ and translated-$F_j$ predictions, in a common figure of merit. Under a triangle-inequality assumption on the disagreement measure $d$, the chained error satisfies
$$d\big(\tau_{ik}(x), (\tau_{jk} \circ \tau_{ij})(x)\big) \leq \epsilon_{ij} + \epsilon_{jk} + \epsilon_{ik},$$
when all three pairwise calibrations exist. We test the consequences of this bound in Section 4.

## 4. Analysis

All numbers in this section are computed from stated inputs; no empirical data are used.

### 4.1 Counting translation maps

**Input:** $N = 29$ frameworks/schism-towers, taken from the inventory of [9], which states 29 unresolved bifurcations and hidden assumptions. We treat this as the number of nodes requiring mutual calibration (a modeling choice; the schisms are bifurcations, and we calibrate the two sides of each, giving at most $2 \times 29 = 58$ towers; we use the conservative $N = 29$ and note the factor-2 alternative).

**Step 1.** Number of pairwise translation maps for a complete master calibration:
$$\binom{N}{2} = \frac{29 \times 28}{2} = \frac{812}{2} = 406.$$

**Step 2.** Number of independent composition (commutativity) constraints. Each triple $\{i,j,k\}$ yields one independent square constraint $\tau_{jk} \circ \tau_{ij} = \tau_{ik}$:
$$\binom{29}{3} = \frac{29 \times 28 \times 27}{6} = \frac{21924}{6} = 3654.$$

**Step 3.** Ratio of constraints to free maps:
$$\frac{3654}{406} = 9.0.$$
Exactly $9.0$ (since $\binom{N}{3}/\binom{N}{2} = (N-2)/3 = 27/3 = 9$). Interpretation: each new framework added to a calibrated family of size $n$ contributes $n$ new maps but $\binom{n}{2}$ new constraints, so constraints grow quadratically in family size while maps grow linearly. For $n = 29$, the constraint-to-map ratio is $9$; a master calibration is therefore a strongly overdetermined system, and generic assignments of translations will not compose. This is the formal content of the claim that pairwise consistency does not imply global consistency.

**Step 4 (factor-2 alternative).** With $N = 58$ towers:
$$\binom{58}{2} = \frac{58 \times 57}{2} = 1653, \qquad \binom{58}{3} = \frac{58 \times 57 \times 56}{6} = \frac{185136}{6} = 30856,$$
ratio $= 56/3 \approx 18.67$. The qualitative conclusion (overdetermination) is unchanged; we carry $N = 29$ forward.

### 4.2 Error accumulation along translation chains

**Input:** per-map worst-case error $\epsilon = 10^{-3}$ (a stated modeling assumption, not a measurement; it represents a 0.1% calibration tolerance, chosen to be representative of demanding metrological calibrations such as those discussed in [6], where calibration precision is described as a limiting systematic).

**Step 1.** Chain of $k$ maps, worst-case accumulation under the triangle bound:
$$\epsilon_{\mathrm{chain}}(k) = k\,\epsilon.$$
For $k = 3$: $\epsilon_{\mathrm{chain}} = 3 \times 10^{-3}$. For $k = 5$: $5 \times 10^{-3}$. For $k = 10$: $10^{-2}$.

**Step 2.** Maximum chain length before error exceeds a tolerance $\epsilon_{\mathrm{tol}}$:
$$k_{\max} = \left\lfloor \frac{\epsilon_{\mathrm{tol}}}{\epsilon} \right\rfloor.$$
With $\epsilon_{\mathrm{tol}} = 10^{-2}$ and $\epsilon = 10^{-3}$: $k_{\max} = \lfloor 10 \rfloor = 10$.

**Step 3.** Mediated translation through a mediating domain $M$ (Section 3.3) incurs two map errors instead of one direct error: $\epsilon_{iM} + \epsilon_{Mj} = 2 \times 10^{-3}$ versus $\epsilon_{ij} = 10^{-3}$, a factor of $2$ penalty. This quantifies the price of the [3]-style non-overlapping-calibration strategy: it buys existence of a translation where none was directly available, at a doubling of worst-case error.

### 4.3 Genericity of commutative squares

**Model:** treat each translation direction as independently chosen with probability $p$ of being "compatible" with a given square constraint, independently across the $3654$ constraints of Section 4.1.

**Step 1.** Probability that all constraints hold:
$$P_{\mathrm{master}} = p^{3654}.$$

**Step 2.** For $p = 0.9$ (optimistic: 90% of squares commute by luck):
$$P_{\mathrm{master}} = 0.9^{3654}.$$
Compute: $\ln(0.9) = -0.10536$, so $\ln P_{\mathrm{master}} = 3654 \times (-0.10536) = -385.2$, hence
$$P_{\mathrm{master}} = e^{-385.2} \approx 10^{-167.3}$$
(since $-385.2 / \ln 10 = -385.2 / 2.3026 = -167.3$).

**Step 3.** Largest family size $n$ for which a random master calibration has probability above $0.01$ at $p = 0.9$: require $n$-constraint count $\binom{n}{3} \leq \ln(0.01)/\ln(0.9) = (-4.6052)/(-0.10536) = 43.7$, so $\binom{n}{3} \leq 43$. Since $\binom{6}{3} = 20$ and $\binom{7}{3} = 35$ and $\binom{8}{3} = 56 > 43$, we get $n_{\max} = 7$.

**Interpretation.** Under this independence model, a family of at most $7$ mutually calibrated frameworks can plausibly compose by unstructured choices; beyond that, composition must be enforced by construction. It is notable — and we report it as a numerical coincidence of the model, not a finding about nature — that the ultrametric program of [11] claims exactly seven research domains as vocabularies of one structural object; our model independently indicates $n = 7$ as the boundary beyond which a shared invariant structure becomes necessary rather than optional.

### 4.4 Classification test

A schism is structural, under our definitions, iff (a) no overlap $S_{ij}$ with nontrivial content exists, or (b) every candidate $\tau_{ij}$ violates composition for all third frameworks. Criterion (a) is checkable case by case; criterion (b) reduces to showing that the constraint set of Section 4.1 is infeasible for the translations in question. We do not claim to have executed this classification for all 29 schisms; we state it as the decision procedure the program must follow, and apply it illustratively: the observer schism S10 examined in [10] is a case where the proposed resolution (embedding the observer as a node in an ultrametric tree) is precisely a candidate translation $\tau_{\mathrm{obs}}$ whose composition with other translations must be checked — and [10]'s independent scrutiny is exactly the composition test our framework demands.

## 5. Results

All results below are computed in Section 4 from stated inputs; the error parameter $\epsilon = 10^{-3}$ and compatibility probability $p = 0.9$ are labeled modeling assumptions, not measurements.

**R1 (Counting).** A master calibration over $N = 29$ frameworks requires $\binom{29}{2} = 406$ pairwise translation maps subject to $\binom{29}{3} = 3654$ independent composition constraints — a constraint-to-map ratio of exactly $9.0$. Under the factor-2 reading ($N = 58$ towers), the counts are $1653$ maps and $30856$ constraints, ratio $\approx 18.67$.

**R2 (Overdetermination).** Constraints grow as $\binom{n}{3}$ in family size $n$ while maps grow as $\binom{n}{2}$; pairwise calibration is therefore generically insufficient for global consistency, and master calibration is an overdetermined problem.

**R3 (Error accumulation).** Under the triangle bound with per-map error $\epsilon = 10^{-3}$ (assumption), a chain of $k$ translations accumulates worst-case error $k \times 10^{-3}$; a tolerance of $10^{-2}$ admits chains of length at most $k_{\max} = 10$. Mediated translation through a mediating domain doubles the worst-case error ($2 \times 10^{-3}$ versus $10^{-3}$).

**R4 (Genericity, projection).** Under the independence model with $p = 0.9$ (assumption), the probability that all $3654$ squares commute is $P_{\mathrm{master}} = 0.9^{3654} \approx 10^{-167.3}$. The largest family size for which random composition succeeds with probability $\geq 0.01$ is $n_{\max} = 7$. These are projections of the stated model, with uncertainty dominated by the unknown true $p$; if $p = 0.99$, $\ln P_{\mathrm{master}} = 3654 \times (-0.01005) = -36.72$, giving $P_{\mathrm{master}} \approx 10^{-15.9}$ — still negligible, so the qualitative conclusion (beyond small families, composition must be enforced by construction) is robust to an order of magnitude in $1 - p$.

**R5 (Classification criterion).** Structural schisms are those for which no overlap exists or all candidate translations fail composition with every third framework; conventional schisms admit calibrated translations whose choice is underdetermined. The decision procedure is stated (Section 4.4) but not executed for all 29 schisms; this is a program, not a completed classification.

## 6. Discussion

**Limitations.** First, the identification of $N = 29$ frameworks with the 29 bifurcations of [9] is a modeling choice: bifurcations are dichotomies, and calibrating both sides yields up to $58$ towers; we showed the qualitative conclusions are insensitive to this factor, but the counts themselves are not canonical. Second, the error model assumes a common figure of merit across all translations and a triangle inequality on disagreement; for frameworks as different as quantum state vectors and classical phase points, no canonical common metric exists, and the bound of Section 3.4 is a formal device, not a physical measurement. Third, the genericity model of Section 4.3 assumes independence of square constraints, which is almost certainly false — constraints are correlated through shared maps — so $P_{\mathrm{master}} \approx 10^{-167.3}$ should be read as an illustration of how quickly overdetermination bites, not as a physical probability. Fourth, we have not executed the structural/conventional classification for any complete list of schisms; the S10 discussion via [10] is illustrative only, and [10] itself is an independent scrutiny of a resolution claim, whose outcome we do not prejudge here.

**Failure modes.** The framework fails if frameworks cannot be individuated — if, e.g., quantum mechanics and quantum field theory are not separable towers but one framework at different resolutions. It also fails if "internal consistency" is unattainable in practice, since consistency of rich mathematical languages is itself listed among the hidden assumptions of [9]; a framework whose consistency is open cannot be certified as a node. Finally, the mediating-domain strategy can fail when the mediating structure is visible to only one framework, or when the doubled error of R3 exceeds tolerance.

**What would falsify the claims.** The central falsifiable claim is R2/R4: that pairwise consistency does not imply global consistency and that beyond small families composition must be enforced. This is falsified if a concrete family of many physics frameworks is shown to admit a master calibration whose translations were chosen independently and yet compose — i.e., if commutativity turns out to be generic rather than exceptional. A second falsifiable claim: the classification criterion of Section 4.4, applied to any schism, must yield stable answers under refinement of the domains; a schism that flips between structural and conventional under harmless reformulation would show the framework individuation is wrong. Third, the coincidence noted in R4 — $n_{\max} = 7$ matching the seven domains of [11] — is explicitly labeled a model coincidence; it is falsified as a structural claim if a principled derivation of the number seven from the ultrametric inequality is absent, in which case the match is chance.

**Open questions.** (i) Can the constraint system of Section 4.1 be given a cohomological formulation, where master calibrations are "global sections" and schisms are obstructions? (ii) Does the ultrametric hierarchy of [11], with the p-adic/adelic realization it names, provide enough structure to prove commutativity of the relevant squares rather than assume it? (iii) How do the two 21 cm calibration paradigms of [6] — sky-based and redundant — map onto our direct versus mediated translations, and does their noted tension instantiate a composition failure? (iv) Is the observer-embedding translation of [10] composable with thermodynamic and gravitational translations, or does it generate new squares that fail?

**Relation to strategy documents.** Community prioritization processes such as the EPPSU's bottom-up input structure [1] and facility-driven programs such as the 500 GeV -- 1 TeV linear collider case of [2] and the CFETR/HFRC dual-pathway assessment [4] allocate resources within frameworks; our claim is that a complementary, cheap, theoretical activity — auditing the composition of translations between frameworks — is currently missing from such processes and could be added without new facilities.

## 7. Conclusion

We have formalized the conjecture that physics' unresolved schisms are calibration failures between internally consistent frameworks over disjoint domains. The formalism defines frameworks, partial translation maps, composition failure, and master calibration; it yields quantitative structure: 406 pairwise maps and 3654 composition constraints for 29 frameworks (ratio exactly $9.0$), linear worst-case error accumulation along chains with a chain-length cap of $10$ at representative tolerances, a factor-2 error penalty for mediated translations, and a genericity analysis showing that beyond roughly seven mutually calibrated frameworks, composition must be enforced by construction rather than hoped for. The framework separates structural from conventional schisms via a stated decision procedure, connects to working calibration practice for non-overlapping sensor fields [3], relaxed metrological standards [8], dual-paradigm cosmological calibration [6], and out-of-domain machine learning calibration [5, 7], and engages the QNFO schisms corpus [9, 10, 11] as both motivation and testbed. The immediate next step is executing the structural/conventional classification for the 29 bifurcations of [9] and testing whether the ultrametric invariant of [11] enforces, rather than merely suggests, the commutativity of translation squares.

## References

[1] arXiv:1910.11775v2 | Physics Briefing Book

[2] arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96

[3] arXiv:1902.10586v2 | Road is Enough! Extrinsic Calibration of Non-overlapping Stereo Camera and LiDAR using Road Information

[4] arXiv:2107.11742v1 | MHD analysis on the physical designs of CFETR and HFRC

[5] arXiv:2102.10395v4 | On Calibration and Out-of-domain Generalization

[6] arXiv:2004.08463v2 | A Unified Calibration Framework for 21 cm Cosmology

[7] arXiv:2012.10988v2 | Post-hoc Uncertainty Calibration for Domain Drift Scenarios

[8] arXiv:2305.03597v2 | A Thru-free Multiline Calibration

[9] QNFO: The Hidden Fractures: Self-Referential Calibration and the 29 Schisms of Physics | DOI 10.5281/zenodo.21458373

[10] QNFO: The Observer Inside the Tree: Can Self-Location in an Ultrametric Structure Resolve the Inside/Outside Schism? | DOI 10.5281/zenodo.21473899

[11] QNFO: The Ultrametric Program: One Structural Object Across Seven Research Domains, and Its Falsifiable Tests | DOI 10.5281/zenodo.22076816