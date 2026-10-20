# Grounding block - source: rem-rev-796a89e8-cdc8-4b5b-b308-fcd683af3ab8

## Research idea

Physics schisms as non-overlapping domains needing a master calibration. The author conjectures that physics' unresolved bifurcations (GR vs QM, continuum vs discrete, Heisenberg cut, compositional vs holistic, etc.) are not failures of any single theory but symptoms of frameworks that are each internally self-consistent over disjoint domains, with no 'master calibration' translating between them. The cracks between towers are where deeper structure lives. A paper could formalize this: model each framework as a consistent theory over a domain, define partial translation maps (e.g., decoherence as a QM→classical calibration, coarse-graining as micro→macro), and prove or simulate where translations fail to compose—identifying which schisms are genuinely structural versus merely conventional, and whether a common underlying structure could calibrate all pairs simultaneously.

Source: owner notebook notes/v1/2026/07/20/_26201092413.md

Post-publication revision of the published paper "Master Calibration for Non-Overlapping Physical Frameworks: Composition, Closure, and the Limits of Partial Translation" (version 2.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 11 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 8 references (70 percent of 11, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Derivation 2: 'Since N_schism = 29 > 21, at least 29 − 21 = 8 schisms lie outside any pairwise reduction involving only the seven claimed vocabularies.' (confirmed by a second model)
2. Falsifiability criterion (Section 6): demonstrating an n≥10 family with commuting squares 'would contradict the combinatorial bound that random families succeed only up to n_max = 7.' (confirmed by a second model)

## Existing paper under revision (remediation only)

# Master Calibration for Non-Overlapping Physical Frameworks: Composition, Closure, and the Limits of Partial Translation

## Abstract

Physics presents itself as convergent, yet systematic inventories list dozens of unresolved bifurcations—general relativity versus quantum mechanics, continuum versus discrete description, the Heisenberg cut, and the status of the observer. We conjecture that such schisms are symptoms of frameworks that are each internally self‑consistent over disjoint domains, lacking a *master calibration*: a family of partial translation maps that calibrates pairs of domains and composes consistently. We formalize frameworks as calibrated theories over domains, define translation maps with quantified error, and bound composition failure by a cycle‑closure error. By counting pairwise maps and composition constraints for the 29‑schism inventory [10] and for a hypothesized seven‑domain family, we derive closed‑form bounds showing that pairwise consistency does not guarantee global consistency. We classify schisms as structural (no admissible translation within a tolerance) or conventional (translations exist but are costly). Numerical examples illustrate closure‑error budgets for three‑framework loops, a two‑framework corner, and genericity projections for random translation families. The results indicate that beyond small families, global consistency must be enforced by construction rather than hoped for.

## 1. Introduction

Experimental and theoretical physicists repeatedly encounter pairs of successful theories that resist unification: general relativity and quantum mechanics, continuum field descriptions versus discrete spectra, the Heisenberg cut separating quantum from classical apparatus, and competing compositional versus holistic readings of state structure. The cost of this impasse is concrete: multi‑year international facility programs, such as the European strategy process for future colliders [1] and the linear‑collider design study of [2], aim to create a shared observable bridging these domains, yet no single framework currently yields a universally applicable predictive tool. If a family of partial translation maps could be constructed that composes consistently across all frameworks, design decisions for future colliders, fusion reactors, and quantum technologies could be guided by a unified calibration budget rather than by ad‑hoc compromises. The present work therefore asks: **under what conditions does a master calibration exist, and how large is the combinatorial burden of enforcing global consistency?**

Our contributions are:
- **C1** – Formal definitions of framework, translation map, composition failure, and master calibration (Section 3).
- **C2** – Derivation of the pairwise‑map count $\binom{29}{2}=406$ and composition‑constraint count $\binom{29}{3}=3654$ for the 29‑schism inventory, yielding an exact constraint‑to‑map ratio of $9.0$ (Section 4, Derivation 1).
- **C3** – Computation of the three‑framework closure bound $\Delta_{\gamma}\le3.4965\times10^{-3}$ for illustrative edge errors $10^{-3},2\times10^{-3},5\times10^{-4}$ (Section 4, Derivation 3).
- **C4** – Classification criterion separating structural from conventional schisms based on per‑edge error floors and tolerance $\tau$ (Section 3.5 and Derivation 4).
- **C5** – Application of the combinatorial machinery to the ultrametric program’s seven‑domain claim, showing that at least eight schisms lie outside any pairwise reduction (Section 4, Derivation 2).
- **C6** – Projection that a random translation family with per‑constraint compatibility probability $p=0.9$ succeeds with probability $10^{-167.3}$, and that the largest family with $>1\%$ success probability is $n_{\max}=7$ (Section 4, Derivation 5).
- **C7** – Worked two‑framework corner for the Feynman‑Shor bifurcation, showing that a pair of frameworks carries no composition constraint (Section 4, Derivation 2′).
- **C8** – Energy‑scale window factor $2$ for the linear‑collider design and mean schisms per domain $\approx4.14$ under a uniformity assumption (Section 4, Derivation 6).

## 2. Background and Related Work

**Calibration with non‑overlapping coverage.** Targetless extrinsic calibration of a stereo camera and a LiDAR whose fields of view do not overlap exploits static road markings as a mediating structure, demonstrating that two internally consistent instruments can be jointly used via an indirect calibration chain [3]. A thru‑free multiline calibration for vector network analyzers replaces the traditional thru standard with an arbitrary two‑port device and an additional reflect standard, showing that a calibration family can be constructed from weaker standards while preserving internal consistency [8].

**Calibration as a limiting systematic.** In 21 cm cosmology, calibration precision is identified as the dominant systematic limiting the extraction of the cosmological signal, with two paradigms—sky‑based and redundant—relying on distinct assumptions about external models and instrument regularity [6]. This illustrates how two calibration paradigms coexist for the same instrument class, mirroring a physics schism that requires a unifying framework.

**Calibration under domain shift.** Machine‑learning work links out‑of‑domain generalization to multi‑environment calibration, defining calibration as the equality of predicted confidence and empirical accuracy across environments [5]. Post‑hoc uncertainty calibration for domain‑drift scenarios shows that standard models become uncalibrated under translation, and that dedicated correction methods can restore calibrated confidence scores [7]. Both studies support the view that a model calibrated on its home domain may be uncalibrated after translation, reinforcing the need for explicit translation maps between frameworks.

**Community‑scale priority setting and shared observables.** The European Particle Physics Strategy Update aggregates community proposals for near‑, mid‑, and long‑term projects, treating theory choice as an aggregation problem over partially incommensurable inputs [1]. The design study for a $e^{+}e^{-}$ linear collider specifies a center‑of‑mass energy range of $500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ and emphasizes its role in exploring physics beyond the Standard Model, thereby acting as a proposed shared observable intended to bridge theoretical domains [2]. The parallel design efforts for the China Fusion Engineering Test Reactor (CFETR) and the Huazhong Field Reversed Configuration (HFRC) represent two internally coherent magnetic‑confinement pathways whose joint assessment remains an open task, providing a concrete analogue of a physics schism [4].

**The schisms inventory.** The QNFO corpus reports 29 unresolved bifurcations spanning topics from the nature of the continuum to the status of the observer, and enumerates concrete examples of each [10]. The QNFO analysis of the Feynman‑Shor bifurcation partitions quantum computing into two ontologies, providing a worked example of a two‑sided foundational split [11].

## 3. Methods

### 3.1 Frameworks and domains

**Definition 3.1 (Framework).** A framework is a pair $F_i=(D_i,\mathcal{P}_i)$ where $D_i$ is a domain (set of states, configurations, or propositions) and $\mathcal{P}_i$ is a set of primitives (quantities, operations, or axioms) taken as given without further calibration. Internally consistency means no contradiction is derivable within $D_i$ using $\mathcal{P}_i$.

*Examples.* Non‑relativistic quantum mechanics $F_{\mathrm{QM}}$ with primitives $|\psi\rangle$ and $U_t=e^{-iHt/\hbar}$; classical statistical mechanics $F_{\mathrm{SM}}$ with phase‑space measure and coarse‑graining cells; general relativity $F_{\mathrm{GR}}$ with metric $g_{\mu\nu}$.

### 3.2 Translation maps and error

**Definition 3.2 (Translation map).** A translation $\tau_{ij}:S_{ij}\to D_j$ is a partial map defined on overlap $S_{ij}\subseteq D_i$, equipped with a *translation error* $\varepsilon_{ij}\in[0,1)$ measured as the fraction of propositions on a chosen test battery for which $\tau_{ij}$ disagrees with the best $F_j$‑native rendering. Directionality is allowed: $\varepsilon_{ij}\neq\varepsilon_{ji}$.

*Canonical examples.* Decoherence supplies $\tau_{\mathrm{QM}\to\mathrm{cl}}$ on the sector where environment‑induced superselection holds; coarse‑graining supplies $\tau_{\mu\to M}$ above a resolution scale $\ell_{\mathrm{cg}}$.

### 3.3 Composition and closure

For composable translations $\tau_{ij}$ and $\tau_{jk}$, the composed error obeys the first‑order bound  

$$\varepsilon_{ij\circ jk}\le\varepsilon_{ij}+\varepsilon_{jk}+\varepsilon_{ij}\,\varepsilon_{jk}.$$

**Definition 3.3 (Composition failure).** Failure occurs if there exists $x\in\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$ such that $(\tau_{jk}\circ\tau_{ij})(x)\neq\tau_{ik}(x)$.  

For a cycle $\gamma$ with edges $e\in\gamma$ and errors $\varepsilon_e$, the *closure error* satisfies  

$$\Delta_{\gamma}\le1-\prod_{e\in\gamma}(1-\varepsilon_e).$$

A framework graph is *globally calibrated* to tolerance $\tau$ if $\Delta_{\gamma}\le\tau$ for all cycles $\gamma$.

**Definition 3.4 (Master calibration).** A family $\mathcal{T}=\{\tau_{ij}\}_{i<j}$ is a master calibration if every square commutes: $\tau_{jk}\circ\tau_{ij}=\tau_{ik}$ on $\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$.

### 3.4 Mediating domains

Following the engineering strategy of [3], we introduce a mediating domain $M$ with translations $\tau_{iM}:S_{iM}\to M$ and $\tau_{Mj}:M\supset\tau_{iM}(S_{iM})\to D_j$. The mediated translation $\tau_{Mj}\circ\tau_{iM}$ incurs two edge errors instead of one direct error, a price quantified in Section 4.

### 3.5 Structural versus conventional schisms

**Definition 3.5.** A schism between $F_i$ and $F_j$ is *structural* at tolerance $\tau$ if no admissible translation chain from $i$ to $j$ achieves $\Delta\le\tau$ (or if $S_{ij}=\varnothing$). It is *conventional* if such a chain exists but is costly (e.g., long, or requiring strong auxiliary assumptions such as the “extremely accurate foreground model” of [6]). The master‑calibration problem asks whether an assignment of edge errors can make all cycles close within $\tau$.

## 4. Analysis

All inputs below are stated with sources; all arithmetic is shown step by step. No empirical data are used.

**Input 1 (from [10]):** the number of unresolved bifurcations is $N_{\mathrm{schism}}=29$.

**Input 2 (assumption):** we hypothesize a candidate family of $n=7$ research domains as a modeling scenario for a small master‑calibration problem; no cited work is relied upon for this number.

**Input 3 (from [11]):** the Feynman‑Shor bifurcation partitions quantum computing into $m=2$ ontologies.

**Input 4 (from [2]):** the proposed linear‑collider center‑of‑mass energy range is $E_{\mathrm{cm}}=500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ (abstract) and $0.5$–$1.5\ \mathrm{TeV}$ (preface).

**Input 5 (from [6]):** calibration precision is a limiting systematic in 21 cm cosmology (qualitative; used to justify non‑zero error floors).

**Input 6 (from [1]):** oblique parameters at future $e^{+}e^{-}$ colliders are expected to be measured with a precision of $\sim1\%$.

### Derivation 1: counting maps and composition constraints.

Treating the 29 bifurcations as 29 frameworks, the number of unordered pairwise translation maps is  

$$\binom{N}{2}=\frac{29\times28}{2}=406.$$

Each unordered triple $\{i,j,k\}$ yields one independent square constraint, giving  

$$\binom{29}{3}=\frac{29\times28\times27}{6}=3654.$$

The constraint‑to‑map ratio is  

$$\frac{3654}{406}=9.0,$$

exactly because $\binom{N}{3}/\binom{N}{2}=(N-2)/3=27/3=9$.

### Derivation 2: pairwise count for the ultrametric program.

For $n=7$ domains, unordered pairs are  

$$P=\binom{7}{2}=\frac{7\times6}{2}=21,$$

and directed pairs $7\times6=42$. Since $N_{\mathrm{schism}}=29>21$, at least  

$$29-21=8$$  

schisms lie outside any pairwise reduction involving only the seven claimed vocabularies.

### Derivation 2′: two‑framework corner (Feynman‑Shor).

For $m=2$ ontologies, the number of unordered pairs is  

$$\binom{2}{2}=1,$$

and the number of unordered triples is  

$$\binom{2}{3}=0.$$

Thus a pair of frameworks carries no composition constraint: any single translation map, however imperfect, trivially satisfies the master‑calibration condition for that pair because there is no third framework to create a cycle.

### Derivation 3: closure‑error budget for a three‑framework loop.

Choose edge errors  

$$\varepsilon_{12}=10^{-3},\qquad\varepsilon_{23}=2\times10^{-3},\qquad\varepsilon_{31}=5\times10^{-4}.$$

The closure bound is  

\[
\Delta_{\gamma}\le1-(1-10^{-3})(1-2\times10^{-3})(1-5\times10^{-4}).
\]

Compute each factor:  

$(1-10^{-3})=0.999$,  

$(1-2\times10^{-3})=0.998$,  

$(1-5\times10^{-4})=0.9995$.  

Product: $0.999\times0.998=0.997002$;  

$0.997002\times0.9995=0.996503499$.  

Thus  

\[
\Delta_{\gamma}\le1-0.996503499=0.003496501\approx3.4965\times10^{-3}.
\]

The additive first‑order bound $\varepsilon_{12}+\varepsilon_{23}+\varepsilon_{31}=3.5\times10^{-3}$ agrees to within $3.5\times10^{-6}$.

### Derivation 4: tolerance at which a schism becomes structural.

Assume a translation chain of $k=4$ edges, each with a floor $\varepsilon_{\min}=10^{-2}$ (assumption motivated by the qualitative limit in [6]). The closure bound is  

\[
\Delta\le1-(1-10^{-2})^{4}=1-0.99^{4}=1-0.96059601=0.03940399\approx3.94\times10^{-2}.
\]

Hence any application demanding $\tau<3.94\times10^{-2}$ classifies the schism as structural under this chain. Solving $1-(1-\varepsilon_{\min})^{k}\le\tau$ for $k$ yields  

\[
k\le\frac{\ln(1-\tau)}{\ln(1-\varepsilon_{\min})}.
\]

For $\tau=10^{-2}$ and $\varepsilon_{\min}=10^{-2}$, $k\le1$, showing that only direct translations can meet a $1\%$ tolerance.

### Derivation 5: genericity of commutative squares (projection).

Assume each of the $3654$ square constraints holds independently with probability $p$. The probability that **all** constraints hold is  

\[
P_{\mathrm{master}}=p^{3654}.
\]

For $p=0.9$, $\ln p=-0.1053605$, so  

\[
\ln P_{\mathrm{master}}=3654\times(-0.1053605)=-385.2,
\]
\[
P_{\mathrm{master}}=e^{-385.2}\approx10^{-167.3}.
\]

To achieve success probability $\ge0.01$, we require  

\[
\binom{n}{3}\le\frac{\ln(0.01)}{\ln(0.9)}\approx43.7,
\]

giving $n_{\max}=7$ because $\binom{7}{3}=35$ and $\binom{8}{3}=56>43$. With $p=0.99$, $P_{\mathrm{master}}\approx10^{-15.9}$, still negligible. The coincidence that the ultrametric program claims exactly seven domains aligns with this bound.

### Derivation 6: energy‑scale window and schism density.

The collider energy window spans a factor  

\[
\frac{1\ \mathrm{TeV}}{500\ \mathrm{GeV}}=2,
\]

so any translation requiring phenomena outside this factor‑of‑2 band cannot be calibrated solely by this shared observable. Assuming a uniform distribution of the $29$ schisms over the $7$ domains, the mean per‑domain count is  

\[
\frac{29}{7}=4.142857\approx4.14.
\]

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

**R1 (computed).** A master calibration over $N=29$ frameworks requires $\binom{29}{2}=406$ pairwise translation maps subject to $\binom{29}{3}=3654$ independent composition constraints—a constraint‑to‑map ratio of exactly $9.0$. Under the factor‑2 reading ($N=58$) the counts are $1653$ maps and $30856$ constraints, ratio $18.667$.

**R2 (computed, under the Input‑2 assumption).** For the hypothesized $n=7$ domain family, the number of unordered pairwise translations is $P=21$ (directed: $42$). Since $N_{\mathrm{schism}}=29$ [10] and $29>21$, at least $8$ schisms would lie outside the pairwise relations of a seven‑domain set.

**R3 (computed).** For a three‑edge cycle with edge errors $10^{-3},2\times10^{-3},5\times10^{-4}$, the closure error is bounded by $\Delta_{\gamma}\le3.4965\times10^{-3}$, consistent with the additive bound $3.5\times10^{-3}$.

**R4 (computed, under stated assumptions).** With a per‑edge error floor of $10^{-2}$ and a $4$‑edge chain, the minimum achievable closure error is $\approx3.94\times10^{-2}$; demanding $\tau=10^{-2}$ restricts admissible chains to $k\le1$.

**R5 (computed).** The collider energy window of [2] spans a factor of $2$, so it can serve as a shared observable only for translations whose discriminating phenomena fall within that band.

**R6 (computed, under a uniformity assumption).** Mean schisms per domain under uniform distribution of $29$ over $7$ is $\approx4.14$.

**R7 (computed).** For the Feynman‑Shor bifurcation ($m=2$), there is $1$ unordered pair and $0$ composition constraints, so any single translation trivially satisfies the master‑calibration condition for that pair.

**Projection P1 (labeled projection).** Assuming independent square‑constraint success probability $p=0.9$, the probability that all $3654$ squares commute is $P_{\mathrm{master}}\approx10^{-167.3}$, and the largest family size with $\ge1\%$ success probability is $n_{\max}=7$. At $p=0.99$ the probability is $\approx10^{-15.9}$, still negligible. Uncertainty is dominated by the unknown true $p$ and by correlations among constraints (ignored in the independence model).

**Projection P2 (labeled projection).** Halving each edge error in the R3 cycle (factor $f=0.5$) yields a new closure bound  

\[
\Delta_{\gamma}'\le1-(0.9995)(0.999)(0.99975)=1.749\times10^{-3},
\]

approximately a factor of two reduction, consistent with first‑order behavior.

## 6. Discussion

**Limitations.**  
1. *Framework identification.* Mapping the $29$ bifurcations of [9] to $29$ frameworks is a modeling choice; calibrating both sides of each dichotomy would double the tower count to $58$, but the qualitative overdetermination persists.  
2. *Error model abstraction.* The translation error $\varepsilon_{ij}$ depends on a chosen test battery of propositions, itself a convention. Correlated errors across frameworks would violate the independence assumption underlying the composition bound and could worsen closure beyond our estimates.  
3. *Empirical measurability.* For frameworks as disparate as general relativity and quantum mechanics, no shared test battery currently exists, so $\varepsilon_{ij}$ cannot be measured today; this renders many schisms structural at any non‑trivial tolerance.  
4. *Genericity projection.* The probability estimates in Derivation 5 assume independent constraints with a uniform success probability $p$, an assumption that is unlikely to hold in practice; the numbers therefore illustrate overdetermination rather than predict actual success rates.

**Falsifiability.** The framework would be falsified by an explicit construction of a family of $n\ge10$ frameworks admitting translation maps whose squares commute to a tolerance $\tau$ without any engineered enforcement (e.g., without mediating domains or auxiliary standards). Demonstrating such a family would contradict the combinatorial bound that random families succeed only up to $n_{\max}=7$.

**Open questions.**  
- Can the ultrametric program’s seven‑domain claim be reformulated as an explicit master calibration that satisfies the closure criterion?  
- What concrete mediating domains are feasible for high‑energy physics (e.g., shared observables from collider data) versus low‑energy condensed‑matter contexts?  
- How does the choice of test battery affect the classification of a schism as structural versus conventional?  
- Are there natural physical processes that provide correlated translation errors, and how would they modify the composition bound?

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.**  
The principal users are theoretical physicists and framework developers who must decide whether to invest resources in constructing mediating domains (e.g., shared observables such as collider experiments or quantum‑optical testbeds) or to accept conventional, costly translation chains. A master‑calibration analysis informs the design of future facilities by quantifying the minimal error budget required for global consistency, thereby guiding funding decisions and experimental priorities.

**(b) Technology readiness.**  
The work is purely analytical, unreviewed, and has not been validated experimentally; according to NASA’s Technology Readiness Level definitions, it resides at TRL 1 (basic principles observed) to TRL 2 (technology concept formulated). It does not exceed TRL 3 because no prototype or hardware implementation has been demonstrated.

**(c) Smallest next experiment.**  
A feasible pilot study would construct a mediating domain between two well‑understood frameworks: quantum optics (decoherence‑based quantum‑to‑classical translation) and classical interferometry (phase‑based classical description). The experiment would measure the translation error $\varepsilon_{ij}$ for each direction using a standardized test battery of optical fringe patterns, then assemble a three‑framework loop (adding a third, e.g., a microwave resonator) to evaluate the closure error $\Delta_{\gamma}$. Observation of a closure error exceeding the bound $3.5\times10^{-3}$ (as computed in R3) would falsify the assumed independence of edge errors.

**(d) Engineering constraints.**  
- *Test‑battery definition*: requires a community‑agreed set of propositions spanning the overlapping domain.  
- *Error‑floor assumption*: the per‑edge floor $\varepsilon_{\min}=10^{-2}$ is motivated by the limiting systematic in 21 cm cosmology [6]; any reduction below this floor demands improved calibration standards.  
- *Mediating domain construction*: must provide observable features accessible to both frameworks (e.g., road markings for sensor calibration [3] or calibrated reference sources for quantum‑classical translation).  
- *Data acquisition*: high‑precision measurement of translation errors demands stable instrumentation and repeatable environmental conditions.

**(e) Cost and performance projections.**  
Using the edge errors from R3, the closure error is $\Delta_{\gamma}\approx3.5\times10^{-3}$. If engineering advances halve each edge error (Projection P2), the closure error reduces to $\approx1.75\times10^{-3}$. Assuming a linear cost scaling with error reduction—a common engineering heuristic—achieving the halved error budget would roughly double the calibration effort and associated cost, though exact monetary figures are not derived from the present analysis.

**(f) Risks and misuse.**  
- *Misclassification*: treating a conventional schism as structural could lead to unnecessary abandonment of viable translation strategies.  
- *Overreliance on abstract error models*: real‑world correlations may invalidate the independence assumption, causing underestimation of closure errors.  
- *Policy misuse*: funding agencies might allocate resources based on the numerical constraint‑to‑map ratio without appreciating the underlying modeling choices, potentially diverting effort from more productive lines of inquiry.

## 8. Conclusion

We have proposed the master‑calibration conjecture: foundational schisms in physics are symptoms of internally self‑consistent frameworks over disjoint domains that lack a family of partial translation maps composing consistently. We formalized frameworks, partial translations with quantified error, composition and cycle‑closure bounds, and a structural‑versus‑conventional classification of schisms relative to a tolerance $\tau$. Applying the machinery to the count of [10] and to the assumed seven‑domain family, we computed: $\binom{29}{2}=406$ pairwise maps and $\binom{29}{3}=3654$ composition constraints for the 29‑bifurcation inventory of [10], a constraint‑to‑map ratio of exactly $9.0$; $\binom{7}{2}=21$ pairwise relations for the hypothesized seven‑domain family, leaving at least $8$ schisms outside any pairwise reduction under that assumption; a worked three‑edge closure budget of $\Delta_{\gamma}\le3.4965\times10^{-3}$; and, as a projection under an independence model, that random composition of $3654$ squares succeeds with probability $\approx10^{-167.3}$ at $p=0.9$, with the largest self‑calibrating family size $n_{\max}=7$. We also showed that a two‑framework pair carries no composition constraint, illustrating why some schisms are conventional at the pair level but become structural when embedded in larger families. The upshot is that beyond small families, global consistency must be enforced by construction rather than hoped for; a candidate master calibration such as the ultrametric program must therefore be checked against the closure criterion, not merely asserted. The framework’s own test battery is conventional, and the counts are modeling choices; both weaknesses are stated so that the conjecture can be falsified by the criteria of Section 6.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement; Appendix A. Divergence report; Appendix B. Claim attribution. references 11 -> 11. length 4644 -> 3852 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.4-claim-order-owner). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Physics Briefing Book. arXiv:1910.11775v2. https://arxiv.org/abs/1910.11775v2
[2] Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96. arXiv:hep-ex/9605011v1. https://arxiv.org/abs/hep-ex/9605011v1
[3] Road is Enough! Extrinsic Calibration of Non-overlapping Stereo Camera and LiDAR using Road Information. arXiv:1902.10586v2. https://arxiv.org/abs/1902.10586v2
[4] MHD analysis on the physical designs of CFETR and HFRC. arXiv:2107.11742v1. https://arxiv.org/abs/2107.11742v1
[5] On Calibration and Out-of-domain Generalization. arXiv:2102.10395v4. https://arxiv.org/abs/2102.10395v4
[6] A Unified Calibration Framework for 21 cm Cosmology. arXiv:2004.08463v2. https://arxiv.org/abs/2004.08463v2
[7] Post-hoc Uncertainty Calibration for Domain Drift Scenarios. arXiv:2012.10988v2. https://arxiv.org/abs/2012.10988v2
[8] A Thru-free Multiline Calibration. arXiv:2305.03597v2. https://arxiv.org/abs/2305.03597v2
[9] https://papers.qnfo.org/papers/master-calibration-for-non-overlapping-physical-frameworks-composition-closure-a. QNFO: Master Calibration for Non-Overlapping Physical Frameworks: Composition, Closure, and the Limits of Partial Translation.
[10] https://papers.qnfo.org/papers/29-schism-synthesis. QNFO: The Hidden Fractures: Self-Referential Calibration and the 29 Schisms of Physics.
[11] https://papers.qnfo.org/papers/feynman-shor-quantum-bifurcation. QNFO: Feynman-Shor Quantum Bifurcation.

## Appendix A. Divergence report

**Divergence 1 – Framework count convention.** Draft A maps each of the $29$ bifurcations of [10] to one framework, giving $N=29$; Draft B calibrates both sides of each dichotomy, giving $N=58$. Convention chosen: the main text uses $N=29$ and reports the factor‑2 reading ($N=58$, $1653$ maps, $30856$ constraints, ratio $18.667$) in R1.

**Divergence 2 – Status of the seven‑domain family.** Draft A treated the seven‑domain family as a claim attributed to a cited source; Draft B treated it as a modeling assumption. Convention chosen: the main text states the seven‑domain family as the paper's own assumption (Input 2), because no work in the reference list states it.

**Divergence 3 – Collider energy range.** Draft A uses the abstract range $500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ of [2], a factor of $2$; Draft C uses the preface range $0.5$–$1.5\ \mathrm{TeV}$, a factor of $3$. Convention chosen: the abstract range, giving the factor‑2 window of Derivation 6; the preface range would widen the window without changing the qualitative conclusion.

**Divergence 4 – Compatibility probability for the genericity projection.** Draft A uses $p=0.9$ only; Draft B reports both $p=0.9$ and $p=0.99$. Convention chosen: $p=0.9$ as the headline number, with $p=0.99$ reported alongside in Derivation 5 and Projection P1.

## Appendix B. Claim attribution

| Claim | Substance | Drafts | Status |
|---|---|---|---|
| C1 | Definitions of framework, translation map, composition failure, master calibration | A, B, C | CONVERGENT |
| C2 | $\binom{29}{2}=406$ maps, $\binom{29}{3}=3654$ constraints, ratio $9.0$ | A, B, C | CONVERGENT |
| C3 | Three‑edge closure bound $\Delta_{\gamma}\le3.4965\times10^{-3}$ | A, B, C | CONVERGENT |
| C4 | Structural versus conventional classification at tolerance $\tau$ | A, B, C | CONVERGENT |
| C5 | Seven‑domain pairwise count $P=21$, at least $8$ schisms outside | A, B | CONVERGENT (as assumption; see Divergence 2) |
| C6 | Genericity projection $P_{\mathrm{master}}\approx10^{-167.3}$ at $p=0.9$; $n_{\max}=7$ | A, B | CONVERGENT |
| C7 | Two‑framework corner: $1$ pair, $0$ constraints for $m=2$ | A, C | CONVERGENT |
| C8 | Energy‑scale window factor $2$; mean schisms per domain $\approx4.14$ | A, B, C | CONVERGENT |
| C9 | Factor‑2 reading $N=58$: $1653$ maps, $30856$ constraints | B | SINGLE |
| C10 | Projection P2: halved edge errors give $\Delta_{\gamma}'\le1.749\times10^{-3}$ | A, B | CONVERGENT |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1910.11775v2 | Physics Briefing Book
arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96
arXiv:1902.10586v2 | Road is Enough! Extrinsic Calibration of Non-overlapping Stereo Camera and LiDAR using Road Information
arXiv:2107.11742v1 | MHD analysis on the physical designs of CFETR and HFRC
arXiv:2102.10395v4 | On Calibration and Out-of-domain Generalization
arXiv:2004.08463v2 | A Unified Calibration Framework for 21 cm Cosmology
arXiv:2012.10988v2 | Post-hoc Uncertainty Calibration for Domain Drift Scenarios
arXiv:2305.03597v2 | A Thru-free Multiline Calibration

## QNFO corpus context (Vectorize)

QNFO: Master Calibration for Non-Overlapping Physical Frameworks: Composition, Closure, and the Limits of Partial Translation | https://papers.qnfo.org/papers/master-calibration-for-non-overlapping-physical-frameworks-composition-closure-a
QNFO: The Hidden Fractures: Self-Referential Calibration and the 29 Schisms of Physics | https://papers.qnfo.org/papers/29-schism-synthesis

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1910.11775v2 | Physics Briefing Book
  The European Particle Physics Strategy Update (EPPSU) process takes a bottom-up approach, whereby the community is first invited to submit proposals (also called inputs) for projects that it would like to see realised in the near-term, mid-term and longer-term future. National inputs as well as inputs from National Laboratories are also an important element of the process. All these inputs are the
  Full text (https://arxiv.org/html/1910.11775v2), excerpts of its own sections:
  § 1.10 A diverse experimental physics programme: There is a variety of tools to progress in addressing the fundamental puzzles of Nature, with no solution in the Standard Model, the list of which (on the particle-physics side: the origin of electroweak symmetry breaking, the nature of the Higgs boson, the pattern of quark and lepton masses, the neutrino nature and mass; on the cosmology side: dark matter, dark energy, inflation, the matter-antimatter asymmetry) did not change in the post-Run 2 LHC era. To decipher the fundamental laws of nature, a judicious combination of abstract methods in theoretical physics and precise experimental scrutiny is needed. These two elements are complementary and are both essential for progress in particle physics. Experimentally, one way ahead in the exploration is to increase the reach of direct searches by increasing the energy scale at which the puzzles can be explored. The alternative way is to perform precision measurements of rare processes fuelled by quantum-mechanical effects of the theory at short distances. These indirect searches can in principle be performed at much lower energies. [...]
  § 3.15 Summary and conclusions: There is a very rich programme of precision measurements to be made of the properties of the Higgs boson, and of the other particles and parameters that are relevant to the electroweak force. Both electroweak precision observables and Higgs couplings can be related directly to the naturalness problem, the problem of why the Higgs mass is unstable in the SM and whether there is new physics that stabilises it at the electroweak scale. Precise measurements of the $Z$ boson could be made at future $e^{+}e^{-}$ colliders, in particular at circular colliders where $10^{12}$ $Z$ -bosons would be available. At linear colliders a significant advance compared to the current precision is also expected, thanks in part to the polarisation that is available. The oblique parameters will be measured with a precision of $\sim 1\%$ , about a factor 10 better than the current precision. Furthermore, several low-energy experiments are expected to also contribute to the precise determination of important parameters of the electroweak aspects of the SM. [...]
  § 4.17.1 QCD and collider experiments (LHC, HL-LHC, HE-LHC, FCC, CEPC): Although QCD is not the main driving force behind future colliders, QCD is crucial for many $pp$ , $ee$ measurements, both as signals and backgrounds. The precision needed to fully exploit all future $ee/pp/ep/eA/AA$ Standard Model and BSM programs require exquisite control of perturbative and non-perturbative QCD physics. There are unique QCD precision studies accessible at FCC-ee, ILC, CEPC, the Super Charm-Tau Factory (SCT@BINP), and at FCC-pp and SPPC. The main themes are detailed in the following. The QCD coupling parameter $\alpha_{s}$ is the least-known coupling of the standard model. Its value impacts all QCD cross sections and decays, it is a leading parametric uncertainty (in some cases together with the charm and bottom masses) in calculations of key quantities in Higgs, top quark, and electroweak physics  [ 112 ] , and its energy evolution affects the range of stability of the electroweak vacuum approaching the Planck scale. [...]
  § 4.18.2 Fixed-target experiments (LHC, HL-LHC, SPS M2 beamline): The multi-TeV LHC proton- and ion-beams allow for the most energetic fixed-target (LHC-FT) experiments ever performed opening the way for unique studies of the nucleon and nuclear structure at high $x$ , of the spin content of the nucleon and of the nuclear-matter [...]
[2] arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96
  We present the current expectations for the design and physics program of an e+e- linear collider of center of mass energy 500 GeV -- 1 TeV. We review the experiments that would be carried out at this facility and demonstrate its key role in exploring physics beyond the Standard Model over the full range of theoretical possibilities. We then show the feasibility of constructing this machine, by re
  Full text (https://ar5iv.labs.arxiv.org/html/hep-ex/9605011v1), excerpts of its own sections:
  § PREFACE: We present the prospects for the next generation of high-energy physics experiments with electron-positron colliding beams. This report summarizes the current status of the design and technological basis of a linear collider of center-of-mass energy 0.5–1.5 TeV, and the opportunities for high-energy physics experiments that this machine is expected to open. Over the past two decades, particle physics experiments have made an increasingly precise confirmation of the “Standard Model” of strong, weak, and electromagnetic interactions. High-energy physicists feel confident that the basic structure of these once-mysterious interactions of elementary particles is now well understood. But the verification of this model has brought with it the realization that there is a missing piece to the story: although the structure of the weak interactions is based on a symmetry principle, we observe that symmetry to be broken, by an agent that we do not yet know. This agent, whatever its source, must provide new physical phenomena at the TeV energy scale. [...]
  § 1.1 Goals for the Next Linear Collider: For the past 25 years accelerator facilities with colliding beams have been the forefront instruments used to study elementary particle physics at high energies (Fig.  1.1 ). Both hadron-hadron and electron-positron colliders have been used to make important observations and discoveries. Direct observations of the $W^{\pm}$ and $Z^{0}$ bosons at CERN and investigations of the top quark at Fermilab are examples of physics done at hadron colliders. Electron-positron colliders provide well-controlled and well-understood experimental environments in which new phenomena stand out and precise measurements can be made. The discoveries of the charm quark and $\tau$ lepton at SPEAR, discovery of the gluon and establishment of QCD at PETRA and PEP, and precision exploration of electroweak phenomena at the SLC and LEP are highlights of the results produced by experiments at electron-positron colliders. Figure 1.1: The energy frontier of particle physics. The effective constituent energy of existing and planned colliders and the year of first physics results from each. [...]
  § 1.2 Accelerator Design Choices: Figure 1.3: The Stanford Linear Collider (SLC).
  § 1.2.1 The Stanford Linear Collider: The Stanford Linear Collider (Fig.  1.3 ) was conceived and built to accomplish two goals: to study particle physics at the 100-GeV energy scale, and to develop the accelerator physics and technology necessary for the realization of future high-energy colliders. [...]
  § 1.4 Outlook for the Next Linear Collider: As the SLC has systematically increased its luminosity, the accelerator physics and technologies of linear colliders have matured. Experiences and lessons learned from the task of making this first collider perform as an instrument for particle physics studies make a firm foundation on which to base the design and technology choices for the next linear collider. At the same time, essential demonstrations of new collider technologies have either taken place or soon will be underway. The experimental program with the FFTB is providing the experience needed to evaluate limitations to designs of final focus and interaction regions. The ability to demagnify beams by the amount required for the NLC has already been achieved. Microwave power sources have exceeded requirements for the initial stage of the NLC, and critical tests assure us that this technology can be expected to drive beams to center-of-mass energies of a TeV or more. [...]
[3] arXiv:1902.10586v2 | Road is Enough! Extrinsic Calibration of Non-overlapping Stereo Camera and LiDAR using Road Information
  This paper presents a framework for the targetless extrinsic calibration of stereo cameras and Light Detection and Ranging (LiDAR) sensors with a non-overlapping Field of View (FOV). In order to solve the extrinsic calibrations problem under such challenging configuration, the proposed solution exploits road markings as static and robust features among the various dynamic objects that are present 
  Full text (https://arxiv.org/html/1902.10586v2), excerpts of its own sections:
  § I Introduction: Autonomous vehicles are often equipped with several multi-modal sensors for environmental perception. Typical perceptual sensors include range sensors which measure the distance to objects using signals (e.g., light, radio waves, and sound waves) and vision sensors which project 3D information onto a 2D image frame. If multiple sensor types are equipped, obtaining relative coordinate transformations via extrinsic calibration becomes an essential pre-processing module. According to literature, accurate extrinsic calibration enhances the performance of data fusion between multiple sensors and the complementary exploitation of other modalities. For example, Shin et al.   [ 1 ] utilized depth information from LiDAR to calculate the photometric error of two images. Zhang and Singh   [ 2 ] implemented a fast odometry method featuring low drift by fusing visual odometry and LiDAR odometry methods. Han et al.   [ 3 ] conducted a study to estimate road area using LiDAR data and camera images using a conditional random field framework. [...]
  § V Experimental Results: This section presents experimental results to evaluate the defined cost in both a quantitative and qualitative manner. We also verified the repeatability and sensitivity of the extrinsic parameter between the stereo camera and LiDAR during the proposed extrinsic calibration.
  § V-A Evaluation of Cost Function: We started by depicting the cost function with respect to the perturbation from the optimal values. The variation of each cost and total cost are plotted in Fig.  9 by increasing the number of selected images. From the first row to the fourth row, up to four informative images were incrementally included in the information order , from the most informative to the fourth most informative image. For these cases, the cost was calculated using only the information on the road region. As shown in the results , the proposed cost reshapes the function in all parameter spaces. The NID cost has a smooth curve shape compared to the edge cost, whereas the segment for converging to the global optimal point is relatively narrow. On the other hand, the edge cost graph is somewhat noisier but has a broader segment to converge to the global optimal point. This feature of the edge cost helps to converge to the global optimal point even with a large initial error of calibration. [...]
  § VI Conclusion and Future Works: This paper proposed an automatic extrinsic calibration method for estimating the rigid body transformation between a stereo camera and LiDAR with no overlapping FOV . By exploiting the static features in the urban environment such as road markings , it was confirmed that extrinsic parameters could be calculated with a degree of accuracy of approximately $0.02\text{\,}\mathrm{m}$ and $0.086^{\circ}$ without manual operation by a human operator . In this paper, we used the assumption that the odometry for generating poitncloud is locally accurate. However, in cases where the motion of a vehicle undergoes several accelerations and decelerations, there may be a distortions in the 3D map due to errors in motion estimation. Therefore, it is preferable to avoid making assumptions about the accuracy of the odometry to use the proposed method in all situations. Therefore, if the uncertainty of the odometry and the SLAM framework are included in the calibration framework, these two problems can be simultaneously solved together through the optimization process.
[4] arXiv:2107.11742v1 | MHD analysis on the physical designs of CFETR and HFRC
  The China Fusion Engineering Test Reactor (CFETR) and the Huazhong Field Reversed Configuration (HFRC), currently both under intensive physical and engineering designs in China, are the two major projects representative of the low-density steady-state and high-density pulsed pathways to fusion. One of the primary tasks of the physics designs for both CFETR and HFRC is the assessment and analysis o
  Full text (https://arxiv.org/html/2107.11742v1), excerpts of its own sections:
  § 1 Introduction: Based on the extrapolation from the empirical scaling laws obtained from decades of research efforts on tokamaks, for a sufficiently large size and a sufficiently strong magnetic field, the tokamak plasma may achieve steady-state self-sustained ignition. The complexity and economic cost associated with the tokamak size is expected to far exceed the existing tokamak devices in the world, often requiring collaborative efforts of multiple countries and unions for many years. [...]
  § 3.3.2 MD simulation results on ECCD control of NTMs: For the MD simulations, Westerhof-Pratt’s closure relation  [ 33 ] is employed for the ECCD density $j_{d}$ appearing in the Ohm’s law Eq. ( 12 ), which can be calculated based on the following equations $\displaystyle\frac{\partial j_{d1}}{\partial t}=-j_{sc}-\nu_{1}j_{d1}+\upsilon_{\parallel,res}\nabla_{\parallel}j_{d1}$ (3) $\displaystyle\frac{\partial j_{d2}}{\partial t}=-j_{sc}-\nu_{2}j_{d2}+\upsilon_{\parallel,res}\nabla_{\parallel}j_{d2}$ (4) $\displaystyle j_{d}=j_{d1}+j_{d2}$ (5) Here, $\nu_{1}$ and $\nu_{2}$ denote the collision rates near the electron cyclotron waves driven ’hole’ and ’bulge’ at small and high perpendicular velocities respectively. $\upsilon_{\parallel,res}$ is the parallel velocity of the resonant electrons. [...]
  § 3.3.3 TM8 simulation results on ECCD control of NTMs: The evolution of neoclassical tearing mode and its stabilization by electron cyclotron current drive for the hybrid scenario of CFETR are also numerically performed using the reduced MHD code TM8. The parameters of our numerical calculations are set as the following if not mentioned elsewhere: a localized distribution of current density from ECCD is applied at the resonant surface with $w_{cd}/a=0.04$ , $\chi_{\perp}=12.5a^{2}/\tau_{R}$ and $\chi_{\parallel}/\chi_{\perp}=10^{8}$ , where $a$ is the minor radius, $w_{cd}$ the half width of driven current, $\tau_{R}=a^{2}\mu_{0}/\eta$ the resistive time, $\chi_{\parallel}$ and $\chi_{\perp}$ are the parallel and perpendicular heat transport coefficients, respectively. The Lundquist number $S=\tau_{R}/\tau_{A}$ is taken to be $5.56\times 10^{6}$ , where $\tau_{A}$ is the Alfvén time. And $r_{s}=0.51a$ is the minor radius of the $q=2$ surface. The local bootstrap current density fraction at the resonant surface is set to be $j_{b}/j_{p}=0.3$ initially. The inverse aspect ratio $\varepsilon=a/R\simeq 0.31$ as designed. [...]
  § 5 Summary and discussion: In summary, CFETR and HFRC physical and engineering designs have provided unprecedented opportunities to the advancement in MHD theory and simulations. Comprehensive efforts on the assessment of MHD stability of CFETR and HFRC baseline scenarios have led to following preliminary progresses that may further benefit engineering designs. For CFETR, the ECCD power and current required for the full stabilization on NTM have been predicted in this work, as well as the corresponding modulated magnetic island width. A thorough investigation on RWM stability for CFETR is performed. For 80% of the SSO scenarios, active control methods may be required for RWM stabilization. The process of disruption mitigation with massive neon injection on CFETR is simulated. The time scale of and consequences of plasma disruption on CFETR are estimated, which are found equivalent to ITER. Major MHD instabilities such as NTM and RWM remain challenge to steady state tokamak operation. On this basis, next steps on CFETR MHD study are planned. [...]
[5] arXiv:2102.10395v4 | On Calibration and Out-of-domain Generalization
  Out-of-domain (OOD) generalization is a significant challenge for machine learning models. Many techniques have been proposed to overcome this challenge, often focused on learning models with certain invariance properties. In this work, we draw a link between OOD performance and model calibration, arguing that calibration across multiple domains can be viewed as a special case of an invariant repr
  Full text (https://arxiv.org/html/2102.10395v4), excerpts of its own sections:
  § 1 Introduction: Machine learning models have recently displayed impressive success in a plethora of fields [ 19 , 9 , 41 ] . [...]
  § 2.2 Invariance and Calibration on Multiple Domains: We define calibration, along with a straightforward generalization to the multiple environment setting. Definition 1 . Let $P[X,Y]$ be a joint distribution over the features and label, and $f:\mathcal{X}\rightarrow[0,1]$ a classifier. Then $f({\mathbf{x}})$ is calibrated w.r.t to $P$ if for all $\alpha\in{[0,1]}$ in the range of $f$ , $\mathbb{E}_{P}{\left[Y\mid f(X)=\alpha\right]}=\alpha$ . In the multiple environments setting, $f({\mathbf{x}})$ is calibrated on $E_{\text{train}}$ if for all $e_{i}\in{E_{\text{train}}}$ and $\alpha$ in the range of $f$ restricted to $e_{i}$ , $\mathbb{E}{\left[Y\mid f(X)=\alpha,E=e_{i}\right]}=\alpha$ . For regression problems, we consider regressors that output estimates for the mean and variance of $Y$ , and say they are calibrated if they match the true values similarly to the definition above. The precise definition can be found in the supplementary material. We now tie the notion of calibration on multiple environments with OOD generalization, starting with its correspondence with our definition of spurious correlations. [...]
  § 5 Proactively Achieving Multi-Domain Calibration: So far we have seen a general argument why calibration can limit spurious correlations, and that in linear-Gaussian models multi-domain calibration guarantees OOD generalization. Now we turn to a more applied perspective and show how can we optimize models so they achieve this type of calibration in practice. We propose three approaches: (1) using calibration measures for model selection, (2) post-processing calibration, and (3) a calibration objective building on a method proposed by [ 26 ] . Section  A.1 in the supplementary provides a slightly broader introduction to notions we use here. We will assess model calibration by the Expected Calibration Error ( ECE ) of the calibration curve  [ 7 ] , which is the average deviation between model accuracy and model confidence.
  § 5.3 Learning with Multi-Domain Calibration Error: The above model selection and post-processing methods are easy to apply and (as we will soon see) surprisingly effective. However, both are limited in their power to learn a model that is truly well-calibrated across multiple domains. We now propose a more powerful approach: an objective function that directly penalizes calibration errors on multiple domains during training. Specifically, we propose learning a parameterized classifier $f_{\theta}({\mathbf{x}})$ using a learning rule of the form: $\min_{\theta}{\sum_{e\in{E_{\text{train}}}}{l^{e}(f_{\theta})}+\lambda\cdot r(f_{\theta})}$ , where $l:\mathbb{R}\times\mathbb{R}\rightarrow\mathbb{R}$ is an empirical loss function (e.g. cross-entropy) and $l^{e}(f_{\theta})$ denotes the expected loss over data from training environment $e$ , and $r(f_{\theta})$ is a regularization term over multiple environments. [...]
  § 7 Conclusion: In this paper we highlight a novel connection between multi-domain calibration and OOD generalization, arguing that such calibration can be viewed as an invariant representation. We proved in a linear setting that models calibrated on multiple domains are free of spurious correlations and therefore generalize out of domain. We then proposed multi-domain calibration as a practical and measurable surrogate for the OOD performance of a classifier. [...]
[6] arXiv:2004.08463v2 | A Unified Calibration Framework for 21 cm Cosmology
  Calibration precision is currently a limiting systematic in 21 cm cosmology experiments. While there are innumerable calibration approaches, most can be categorized as either `sky-based,' relying on an extremely accurate model of astronomical foreground emission, or `redundant,' requiring a precisely regular array with near-identical antenna response patterns. Both of these classes of calibration 
  Full text (https://arxiv.org/html/2004.08463v2), excerpts of its own sections:
  § I Introduction: Measurement of the 21 cm cosmological power spectrum would constrain models of the Epoch of Reionization (EoR), Dark Ages, and Dark Energy. These measurements are contaminated by astrophysical foreground emission that is 4-5 orders-of-magnitude brighter than the cosmological signal. Separating the cosmological and foreground signals requires extremely precise instrumental calibration. As a result, development and characterization of precision calibration techniques for 21 cm cosmology has become an active area of research [ 64 , 49 , 36 , 29 , 28 , 17 , 42 , 50 , 68 , 66 , 3 , 7 , 11 , 15 , 18 , 48 , 69 , 65 , 44 , 13 , 19 , 26 , 34 , 55 , 8 , 32 , 35 , 45 , 1 , 14 , 27 , 31 , 37 , 53 ] . In general, calibration approaches for cosmological 21 cm power spectrum measurements can be categorized as one of two types. ‘Sky-based’ calibration uses models of the sky and instrument to simulate data. Calibration then consists of fitting measurements to the simulation. [...]
  § II Statistical Formalism: In this section we present statistical underpinnings of the calibration problem. We use Bayes’ theorem to formulate a likelihood function with a statistical prior. Calibration consists of maximizing this likelihood function to calculate the instrumental response. Variable or Expression Definition $\boldsymbol{v}$ data (for interferometric data, these are the measured visibilities) $\langle\boldsymbol{v}\rangle$ expectation value of the data $\boldsymbol{\theta}$ tunable calibration parameters $\hat{\boldsymbol{\theta}}$ maximum-likelihood calibration parameters $\boldsymbol{\zeta}(\boldsymbol{\theta})$ function that maps the calibration parameters to the model of the data $P(\boldsymbol{\theta}|\boldsymbol{v})$ likelihood function, equal to the probability that $\boldsymbol{\theta}$ parameterizes the model given the data $\boldsymbol{v}$ $P(\boldsymbol{v}|\boldsymbol{\theta})$ probability that the model parameterized by $\boldsymbol{\theta}$ produces data $\boldsymbol{v}$ $P(\boldsymbol{\theta})$ prior probability of $\boldsymbol{\theta}$ $P(\boldsymbol{v})$ marginalized probability [...]
  § V Simulation Results: In this section we present results from a simplified simulation exploring the novel calibration approaches described in § IV . The simulation results illustrate that a unified calibration approach that combines redundant calibration with a sky model prior can improve calibration performance.
  § VIII Conclusion: Precision calibration is essential to the success of 21 cm cosmology experiments. Low-level calibration errors contaminate the cosmological signal by limiting the separability of bright astrophysical foregrounds. As current experiments approach a detection of the 21 cm power spectrum from the EoR, novel calibration approaches must achieve new levels of precision. While a diversity of interferometric calibration techniques exist, the current paradigm in the field delineates between sky-based and redundant calibration approaches. Sky-based calibration assumes very good a priori models of the sky and instrument response. It further assumes independent visibility measurements, neglecting visibility covariance from baseline response overlap in the uv plane. On the other hand, redundant calibration assumes that baselines within a redundant set are perfectly redundant both in antenna positions and response shapes, that baselines from different redundant baseline sets exhibit no covariance, and that a sky model can accurately constrain the absolute calibration parameters. [...]
[7] arXiv:2012.10988v2 | Post-hoc Uncertainty Calibration for Domain Drift Scenarios
  We address the problem of uncertainty calibration. While standard deep neural networks typically yield uncalibrated predictions, calibrated confidence scores that are representative of the true likelihood of a prediction can be achieved using post-hoc calibration methods. However, to date the focus of these approaches has been on in-domain calibration. Our contribution is two-fold. First, we show 
  Full text (https://arxiv.org/html/2012.10988v2), excerpts of its own sections:
  § 4.1 Baseline methods and experimental setup: We assess the performance of the following post-hoc uncertainty calibration methods in domain drift scenarios: • Base: Uncalibrated baseline model • Temperature scaling (TS) [ 4 ] and Ensemble Temperature Scaling (ETS) [ 24 ] • Isotonic Regression (IR) [ 23 ] • Accuracy preserving version of Isotonic Regression (IRM) [ 24 ] • Composite model combining Temperature Scaling and Isotonic Regression (TS-IR) [ 24 ] We quantify calibration under domain shift for 28 distinct perturbation types not seen during training, including 9 affine transformations, 19 image perturbations introduced by [ 6 ] and a dedicated bias-controlled dataset [ 1 ] . Each perturbation strategy mimics a scenario where the data of a deployed model encounters stems from a distribution that gradually shifts away from the training distribution in a different manner. For each model and each perturbation, we compute the micro-averaged ECE by first perturbing each sample in the test set at 10 different levels and then calculating the overall ECE across all samples; we denote relative perturbation strength as epsilon. [...]
  § 4.2 Improving calibration under domain drift: Existing methods for post-hoc uncertainty calibration are based on a validation set, which is drawn from the same generative distribution $\pi(X,Y)$ as the training set and the test set. Using these data to optimize a post-hoc calibration method results in low calibration errors for data drawn from $\pi(X,Y)$ . If we would like to generalise this approach to calibration under domain drift, we need access to samples from the generative distribution along the axis of domain drift. However, such robustness under domain drift is a challenging requirement since in practice for a $D$ -dimensional input domain drift can occur in any of the $2^{D}$ directions in $\{-1,1\}^{D}$ , and to any degree. Manifestations of such domain shifts include for example changes in viewpoint (Fig. 1), lighting condition, object rotation or background. To obtain a transformed validation set representing a generic domain shift, we therefore sample domain drift scenarios by randomly choosing direction and magnitude of the domain drift. [...]
  § 5 Experiments and results: (a) CIFAR-10 (b) Imagenet Figure 4 : Micro-averaged calibration error for individual test domain shift scenarios We first illustrate limitations of post-hoc uncertainty calibration methods in domain drift scenarios using CIFAR-10. We show that while excellent in-domain calibration can be achieved using standard baselines, the quality of uncertainty decreases with increasing domain shift for all methods, resulting in highly overconfident predictions for images far away from the training domain. Next, we show on a variety of architectures and datasets that replacing the validation set by a transformed validation set as outlined in section 4.2, substantially improves calibration under domain shift. We further assess the effect of our new approach on in-domain calibration and demonstrate that for selected post-hoc calibration methods, in-domain calibration can be maintained at competitive levels. Finally, we show that our tuning approach results in better uncertainty awareness in truly OOD settings.
  § 5.1 Post-hoc calibration results in overconfident predictions under domain drift: We tuned all post-hoc calibration baseline methods on the CIFAR-10 validation set and first assessed in-domain calibration on the test set. [...]
[8] arXiv:2305.03597v2 | A Thru-free Multiline Calibration
  This paper proposes a modification to the traditional multiline thru-reflect-line (TRL) or line-reflect-line (LRL) calibration method used for vector network analyzers (VNAs). Our proposed method eliminates the need for a thru (or line) standard by using an arbitrary transmissive two-port device in combination with an additional reflect standard. This combination of standards allows us to arbitrar
  Full text (https://arxiv.org/html/2305.03597v2), excerpts of its own sections:
  § I Introduction: The precision of measurements taken by a vector network analyzer (VNA) heavily relies on the calibration method’s accuracy. Over the years, numerous improvements have been made to VNA calibration methods [ 1 ] . Since its inception in 1979 [ 2 ] , the thru-reflect-line (TRL) calibration method is still regarded as the most precise method for traceable VNA calibration. Although the TRL method is inherently bandlimited, an extension of the method called multiline TRL was proposed, which uses multiple line standards of varying lengths to expand the usable frequency range [ 3 ] . For both TRL and multiline TRL, a fully defined thru standard (a zero-length line) is required to determine the location of the calibration plane. However, in some applications, such a thru standard cannot be realized. For example, in on-wafer applications, the calibration plane should be at the tip of the probes [ 4 ] . Undesirable effects can occur if the probes are placed too close to each other [ 5 , 6 ] . In waveguide applications, the calibration plane is typically set at the adapter flanges. [...]
  § II The Thru Standard in TRL calibration: The error box model of a two-port VNA measuring a line standard is depicted in Fig.  1 . The error box model can be simplified into seven terms as follows: $\boldsymbol{M}_{i}=\underbrace{k_{a}k_{b}}_{k}\underbrace{\left[\begin{matrix}a_{11}&a_{12}\\[5.0pt] \ a_{21}&1\end{matrix}\right]}_{\boldsymbol{A}}\begin{bmatrix}e^{-\gamma l_{i}}&0\\[5.0pt] 0&e^{\gamma l_{i}}\end{bmatrix}\underbrace{\left[\begin{matrix}b_{11}&b_{12}\\[5.0pt] [...]
  § IV-B Results and discussion: The raw S-parameter measurements of the calibration standards were collected over multiple frequency sweeps. For each standard, 25 frequency sweeps were collected at an IF-bandwidth of $100\,\mathrm{Hz}$ and a source power of $-10\,\mathrm{dBm}$ . Each frequency sweep covers the range $1-150\,\mathrm{GHz}$ with 299 frequency points. The collected data was processed in Python with help of the package scikit-rf [ 15 ] , and the multiline TRL algorithm from [ 12 ] was used. We also applied the same eigenvalue formulation from [ 12 ] for the thru-free multiline calibration. Both methods result in the same normalized error terms, as a thru definition is not required in the formulation of the eigenvalue problem. We denormalized the error terms for the multiline TRL calibration using the reflect standard (short) and the thru standard ( $0\,\mathrm{mm}$ line) to define the location of the calibration plane at the center of the thru standard. [...]
  § V Conclusion: We presented a modified version of multiline TRL calibration that eliminates the need for explicitly defining a thru standard. The proposed thru-free multiline calibration was compared to multiline TRL using measurements of microstrip lines fabricated on a PCB with a stepped-impedance DUT for verification. We observed excellent agreement between the proposed method and the multiline TRL calibration when a thru standard was used to set the reference plane. In cases where a thru standard is not available, the multiline TRL method requires shifting the calibration plane in post-processing to the desired location. This is in contrast to the proposed method, where the location of the calibration plane is set automatically by the measured artifacts. The advantage of the proposed thru-free method is that it eliminates the requirement to explicitly define a thru standard in multiline TRL calibration, making all calibration standards in the thru-free method partially defined.
[9] QNFO: Master Calibration for Non-Overlapping Physical Frameworks: Composition, Closure, and the Limits of Partial Translation | https://papers.qnfo.org/papers/master-calibration-for-non-overlapping-physical-frameworks-composition-closure-a
  Physics presents itself as convergent, yet systematic inventories list dozens of unresolved bifurcations—general relativity versus quantum mechanics, continuum versus discrete description, the Heisenberg cut, and the status of the observer. We conjecture that such schisms are symptoms of frameworks that are each internally self‑consistent over disjoint domains, lacking a *master calibration*: a fa
  Full text (https://papers.qnfo.org/papers/master-calibration-for-non-overlapping-physical-frameworks-composition-closure-a), excerpts of its own sections:
  § 3.1 Frameworks and domains: **Definition 3.1 (Framework).** A framework is a pair $F_i=(D_i,\mathcal{P}_i)$ where $D_i$ is a domain (set of states, configurations, or propositions) and $\mathcal{P}_i$ is a set of primitives (quantities, operations, or axioms) taken as given without further calibration. Internally consistency means no contradiction is derivable within $D_i$ using $\mathcal{P}_i$. *Examples.* Non‑relativistic quantum mechanics $F_{\mathrm{QM}}$ with primitives $|\psi\rangle$ and $U_t=e^{-iHt/\hbar}$; classical statistical mechanics $F_{\mathrm{SM}}$ with phase‑space measure and coarse‑graining cells; general relativity $F_{\mathrm{GR}}$ with metric $g_{\mu\nu}$.
  § 3.4 Mediating domains: Following the engineering strategy of [3], we introduce a mediating domain $M$ with translations $\tau_{iM}:S_{iM}\to M$ and $\tau_{Mj}:M\supset\tau_{iM}(S_{iM})\to D_j$. The mediated translation $\tau_{Mj}\circ\tau_{iM}$ incurs two edge errors instead of one direct error, a price quantified in Section 4.
  § 5. Results: We report only quantities computed in Section 4, plus clearly labeled projections. **R1 (computed).** A master calibration over $N=29$ frameworks requires $\binom{29}{2}=406$ pairwise translation maps subject to $\binom{29}{3}=3654$ independent composition constraints—a constraint‑to‑map ratio of exactly $9.0$. Under the factor‑2 reading ($N=58$) the counts are $1653$ maps and $30856$ constraints, ratio $18.667$. **R2 (computed, under the Input‑2 assumption).** For the hypothesized $n=7$ domain family, the number of unordered pairwise translations is $P=21$ (directed: $42$). Since $N_{\mathrm{schism}}=29$ [10] and $29>21$, at least $8$ schisms would lie outside the pairwise relations of a seven‑domain set. **R3 (computed).** For a three‑edge cycle with edge errors $10^{-3},2\times10^{-3},5\times10^{-4}$, the closure error is bounded by $\Delta_{\gamma}\le3.4965\times10^{-3}$, consistent with the additive bound $3.5\times10^{-3}$. [...]
  § 6. Discussion: **Limitations.** 1. *Framework identification.* Mapping the $29$ bifurcations of [9] to $29$ frameworks is a modeling choice; calibrating both sides of each dichotomy would double the tower count to $58$, but the qualitative overdetermination persists. 2. *Error model abstraction.* The translation error $\varepsilon_{ij}$ depends on a chosen test battery of propositions, itself a convention. Correlated errors across frameworks would violate the independence assumption underlying the composition bound and could worsen closure beyond our estimates. 3. *Empirical measurability.* For frameworks as disparate as general relativity and quantum mechanics, no shared test battery currently exists, so $\varepsilon_{ij}$ cannot be measured today; this renders many schisms structural at any non‑trivial tolerance. 4. *Genericity projection.* The probability estimates in Derivation 5 assume independent constraints with a uniform success probability $p$, an assumption that is unlikely to hold in practice; the numbers therefore illustrate overdetermination rather than predict actual success rates. [...]
  § 8. Conclusion: We have proposed the master‑calibration conjecture: foundational schisms in physics are symptoms of internally self‑consistent frameworks over disjoint domains that lack a family of partial translation maps composing consistently. We formalized frameworks, partial translations with quantified error, composition and cycle‑closure bounds, and a structural‑versus‑conventional classification of schisms relative to a tolerance $\tau$. [...]
[10] QNFO: The Hidden Fractures: Self-Referential Calibration and the 29 Schisms of Physics | https://papers.qnfo.org/papers/29-schism-synthesis
  Physics is often presented as a monolithic, converging body of knowledge. Yet a systematic inventory reveals 29 unresolved bifurcations and hidden assumptions -- from the nature of the continuum to the status of the observer, the consistency of mathematical language, and the meaning of explanation itself. These schisms are not isolated philosophical puzzles; they are deeply interconnected and coll
  Full text (https://papers.qnfo.org/papers/29-schism-synthesis), excerpts of its own sections:
  § 1. Introduction: The Fractures Beneath the Surface: Physics occupies a unique position among the sciences. It claims the deepest reach -- from the Planck scale to the cosmic horizon -- and the widest explanatory scope. Its mathematical formalism is among the most precise ever developed: quantum electrodynamics predicts the electron's magnetic moment to eleven decimal places, and general relativity describes the orbital decay of binary pulsars to within seconds per century. Yet beneath this edifice of apparent unity lies a landscape of fractures. General relativity and quantum mechanics use mathematically incompatible structures. Quantum field theory and the Standard Model coexist uneasily, the latter appearing as a baroque island in a sea of possibilities. The quantum measurement problem remains unresolved after a century. The arrow of time has no agreed-upon origin. The cosmological constant is off by 120 orders of magnitude from naive expectations. These are the *visible* schisms -- the ones physicists acknowledge and debate. But a deeper inventory reveals fractures that are rarely even recognized as assumptions. [...]
  § 1.1. Prior Work: A substantial body of work within the QNFO research program has developed the mathematical and conceptual infrastructure for this synthesis. This includes: - **Quantum Laws of Form** [@quantum-lawsof-form]: Syntactic Token Calculus (STC) that discards the continuum and background spacetime, replacing them with an ultrametric Bruhat-Tits tree of distinctions. [...]
  § 4.2. The Bootstrap Theorem: **Theorem 1 (Bootstrap Fixed Point).** Let $\mathcal{T}$ be the space of all theories $T: \mathcal{P} \to \Delta(\mathcal{M})$ (where $\Delta(\mathcal{M})$ is the simplex of probability distributions over measurement outcomes). Define the calibration operator $\Phi: \mathcal{T} \to \mathcal{T}$ as: $$\Phi(T)(P) = \text{EmpiricalDistribution}(\mathcal{C}_T(P))$$ where $\mathcal{C}_T$ is the calibration loop executed using theory $T$ to interpret measurement outcomes. If the distinction function $d$ is an ultrametric on $\mathcal{P}$, then $\Phi$ is a contraction mapping on $(\mathcal{T}, d_{\mathcal{T}})$ where: $$d_{\mathcal{T}}(T_1, T_2) = \max_{P \in \mathcal{P}} \|T_1(P) - T_2(P)\|_1$$ Consequently, by the Banach fixed-point theorem, there exists a unique fixed point $T^* = \Phi(T^*)$. *Proof Sketch.* The proof proceeds in three steps: **Step 1: Ultrametricity of the distinction space.** By Ostrowski's theorem, the only completions of the rational numbers are the real numbers and the p-adic numbers. [...]
  § 11. Conclusion: The 29 schisms of physics are not independent puzzles to be solved one by one. They are 29 facets of a single diamond: the assumption that physics can be formulated from a perspective no physical agent can occupy. Abandoning this assumption -- and replacing it with the self-referential calibration framework -- transforms the schisms from contradictions into calibration parameters. The Bootstrap Theorem provides the formal foundation: self-consistent calibration converges to a unique fixed point, and that fixed point **is** the physics. The mathematical machinery exists: ultrametric geometry, Bruhat-Tits trees, the Monna projection, and Syntactic Token Calculus. The falsifiable predictions are on record: log-periodic CMB oscillations, ZBW ultrametric structure, adelic QEC intrinsic protection, and the joule-per-solution metric. What remains is the hard work of formalization, empirical testing, and external engagement. [...]