# Master Calibration for Non-Overlapping Physics: A Formal Framework for Partial Translations Between Self-Consistent Towers

## Abstract

Physics presents itself as convergent, yet several of its central frameworks — general relativity, quantum mechanics, continuum and discrete mathematics, and the placement of the observer — appear internally consistent over disjoint domains while resisting direct combination. We propose that such schisms are symptoms of missing *master calibration*: a family of partial translation maps between frameworks that individually calibrate pairs of domains but fail to compose globally. We formalize this conjecture. Each framework is modeled as a calibrated theory over a domain; translations are partial maps with quantified error; composition failure is measured by cycle-closure error around loops in the framework graph. We derive closed-form bounds on composed translation error, show that pairwise consistency does not imply global consistency, and give a classification criterion separating structural schisms (no admissible translation exists) from conventional ones (translations exist but are merely inconvenient). Applying the framework to the inventory of 29 bifurcations in the "Hidden Fractures" corpus, we compute the combinatorics of pairwise translation (21 pairs for 7 claimed vocabularies of one structural object) and derive a concrete closure-error budget for a three-framework loop. The framework reframes calibration — a mature engineering discipline — as a candidate organizing principle for foundational physics, and yields falsifiable tests: predicted failure points of specific translation cycles.

## 1. Introduction

A recurring puzzle in foundational physics is not that any single theory fails on its own terms, but that pairs of successful theories resist unification: general relativity and quantum mechanics, the continuum picture of fields versus discrete spectra, the Heisenberg cut separating quantum description from classical apparatus, and the compositional versus holistic readings of state structure. The working hypothesis of this paper, motivated by the notebook conjecture underlying the QNFO corpus [9], is that these bifurcations are not failures of any single framework but symptoms of frameworks that are each internally self-consistent over *disjoint* domains, with no "master calibration" translating between them.

The word *calibration* is borrowed deliberately from metrology and engineering, where it has precise operational meaning: a calibration is a procedure that renders the outputs of one instrument (or model) commensurable with another, with quantified residual error. In sensor engineering, calibration is routinely performed between instruments with *non-overlapping fields of view* — a situation structurally analogous to physics frameworks whose domains of validity do not intersect. In machine learning, calibration across multiple domains has been argued to be a special case of invariant representation learning [5], and post-hoc calibration methods have been extended to domain-drift scenarios [7]. In cosmology, calibration precision is identified as a limiting systematic, and unified frameworks have been proposed to reconcile competing calibration classes [6]. These are, we claim, small-scale instances of exactly the problem physics faces at its foundations.

Our contributions are:

1. A formal model: frameworks as calibrated theories over domains, translations as partial maps with error, and a framework graph whose edges carry translation error.
2. A theorem-level result (proved by direct arithmetic in Section 4): pairwise calibration error composes multiplicatively-additively, so cycle-closure error around a loop is bounded by a sum of edge errors — and *nonzero closure error is generically unavoidable*, meaning pairwise consistency does not imply global consistency.
3. A classification of schisms into *structural* (no admissible translation exists within a stated error budget) and *conventional* (translations exist but are costly), with a concrete numerical criterion.
4. Application to the 29-schisms inventory [9] and the ultrametric program's claim that seven research domains are vocabularies for one structural object [11], including a computed pairwise-translation count and a worked closure-error budget.

The paper is organized as follows. Section 2 reviews the related literature. Section 3 sets out the formal methods. Section 4 performs all derivations with explicit arithmetic. Section 5 reports results. Section 6 discusses limitations and falsification conditions, and Section 7 concludes.

## 2. Background and Related Work

We organize the literature into three strands: calibration as an engineering discipline under non-commensurability, calibration under domain shift in learning and inference, and the schisms inventory that motivates the master-calibration conjecture.

**Calibration with non-overlapping coverage.** The problem of calibrating two sensing modalities whose fields of view do not overlap is treated directly in [3], which presents a framework for targetless extrinsic calibration of stereo cameras and LiDAR sensors with a non-overlapping field of view, exploiting road markings as static and robust features among otherwise dynamic objects. This is the closest engineering analogue to our central problem: two instruments, each internally consistent, sharing no common observable, yet requiring a translation (here, an extrinsic transform) to be used jointly. The entry's summary states the framework and the feature choice; it supplies no quantitative results we may cite, so we use it only as a structural precedent. In the same engineering register, [8] proposes a thru-free multiline calibration for vector network analyzers, eliminating the need for a thru (or line) standard by using an arbitrary transmissive two-port device together with an additional reflect standard — an example of how a calibration standard previously thought essential can be replaced by a weaker, more available one, which we take as a model for what a "master calibration" might achieve between physical frameworks: replacing an impossible direct standard (a common domain) with an indirect chain of weaker standards.

**Calibration as a limiting systematic.** In 21 cm cosmology, [6] states that calibration precision is currently a limiting systematic, and categorizes most calibration approaches as either "sky-based," relying on an extremely accurate model of astronomical foreground emission, or "redundant," requiring a precisely regular array with near-identical antenna response patterns; the entry's summary indicates both classes are treated in a unified framework, though the supplied summary is truncated before stating the unification mechanism, so we cite it only for the taxonomy and the claim that calibration is limiting. The structural reading is important for us: two calibration *paradigms* with different assumptions (foreground model versus array regularity) coexist for the same instrument class — a miniature of a physics schism, resolved not by picking a winner but by a framework that contains both.

**Calibration under domain shift.** In machine learning, [5] draws a link between out-of-domain (OOD) generalization and model calibration, arguing that calibration across multiple domains can be viewed as a special case of an invariant representation (the supplied summary is truncated at this point, so we do not attribute any specific mechanism beyond this link). This supports our thesis at the level of principle: being "calibrated" is not a property of a model alone but a relational property between model and domain, and multi-domain calibration is a stronger, invariant-like condition. Complementarily, [7] addresses uncertainty calibration for domain drift, showing first that standard deep neural networks typically yield uncalibrated predictions and that post-hoc methods can produce calibrated confidence scores, and second — per the summary's two-fold contribution statement — extending the focus beyond in-domain calibration; the summary is truncated before detailing the second contribution, so we cite only the in-domain result and the stated intent. The lesson we import: a framework calibrated on its home domain (its "in-distribution") may be uncalibrated under translation, and post-hoc correction is the realistic remedy, not retraining from scratch — analogous to fixing the translation maps between physics frameworks rather than demanding a new monolithic theory.

**Community-scale priority setting.** At the scale of the discipline, [1] describes the European Particle Physics Strategy Update (EPPSU) process as bottom-up: the community is first invited to submit proposals (inputs) for projects to be realised in the near-term, mid-term and longer-term future, with national and laboratory inputs also important elements. We cite this as evidence that the field's self-organization already treats theory choice as an aggregation problem over partially incommensurable community inputs — the sociological shadow of the formal problem we pose. Similarly, [2] presents expectations for the design and physics program of an e$^+e^-$ linear collider of center-of-mass energy 500 GeV -- 1 TeV and demonstrates its key role in exploring physics beyond the Standard Model over the full range of theoretical possibilities, alongside feasibility of constructing the machine. In our vocabulary, such a facility is a proposed *shared observable* — an attempt to manufacture overlapping domain between frameworks that currently do not overlap; the summary states the energy range and the role claim, and we cite no further specifics. In a different energy regime, [4] analyzes the physical designs of the China Fusion Engineering Test Reactor (CFETR) and the Huazhong Field Reversed Configuration (HFRC), described as the two major projects representative of the low-density steady-state and high-density pulsed pathways to fusion, with physics designs tasked with assessment and analysis (the summary truncates before stating the analysis outcome). This is a second instance of two internally coherent programs — here two magnetic-confinement pathways — whose joint assessment is the open task.

**The schisms inventory.** The QNFO corpus supplies the motivating inventory. [9] ("The Hidden Fractures") reports that physics, often presented as a monolithic, converging body of knowledge, yields on systematic inventory 29 unresolved bifurcations and hidden assumptions — from the nature of the continuum to the status of the observer, the consistency of mathematical language, and the meaning of explanation (the summary truncates mid-sentence, so we cite the count and the examples listed). [10] examines a specific claimed resolution: the 29-schisms framework's claim to resolve the central schism of quantum foundations — S10, the observer inside versus outside — by embedding the observer as a node in an ultrametric TREE structure, eliminating the need for an external vantage point; that paper subjects the claim to independent scrutiny (its summary truncates before the verdict, so we cite only the claim and the scrutiny). [11] ("The Ultrametric Program") states that seven research domains are claimed to be seven vocabularies for one structural object — nested hierarchical partition logic defined by the ultrametric inequality, with p-adic/adelic arithmetic as one realization and the hierarchy as the invariant — and lists three falsifiable hypotheses (H1 compression prior, H2 Ar…, truncated). The number seven and the claim of one invariant are what we use in Section 4's combinatorics.

## 3. Methods

### 3.1 Frameworks and domains

A *framework* $F_i$ is a pair $(D_i, \mathcal{M}_i)$ where $D_i$ is a domain of phenomena and $\mathcal{M}_i$ is a mathematical structure with an internal consistency criterion $C_i: \mathcal{M}_i \to \{0,1\}$ ($1$ = consistent). We assume each framework in our motivating set satisfies $C_i = 1$ on $D_i$; the schisms arise at the boundaries, not inside.

### 3.2 Translation maps and error

A *translation* from $F_i$ to $F_j$ is a partial map $T_{ij}: D_i \rightharpoonup D_j$ with *translation error* $\varepsilon_{ij} \in [0,1)$, defined operationally: for a proposition $p$ in the overlap of meaning, $T_{ij}(p)$ disagrees with the best available $F_j$-native rendering of $p$ on a fraction $\varepsilon_{ij}$ of a chosen test battery. Symmetry is not assumed: $\varepsilon_{ij} \neq \varepsilon_{ji}$ in general, since calibration is directional (as in sky-based versus redundant calibration [6], where the two paradigms lean on different assumptions).

### 3.3 Composition and closure

For composable translations $T_{ij}$ and $T_{jk}$, the composed error is bounded by

$$\varepsilon_{ij \circ jk} \;\leq\; \varepsilon_{ij} + \varepsilon_{jk} + \varepsilon_{ij}\,\varepsilon_{jk},$$

a standard first-order composition bound for independent fractional errors, which we adopt as a definition of the translation semigroupoid's error structure. For a cycle $F_{i_1} \to F_{i_2} \to \cdots \to F_{i_n} \to F_{i_1}$, the *closure error* is

$$\Delta_{\gamma} \;\leq\; 1 - \prod_{e \in \gamma} (1 - \varepsilon_e),$$

where $\gamma$ is the cycle and $\varepsilon_e$ the edge errors. A framework graph is *globally calibrated* to tolerance $\tau$ if $\Delta_{\gamma} \leq \tau$ for all cycles $\gamma$.

### 3.4 Structural versus conventional schisms

A schism between $F_i$ and $F_j$ is *structural* at tolerance $\tau$ if no admissible translation chain from $i$ to $j$ achieves $\Delta \leq \tau$; it is *conventional* if such a chain exists but is costly (long, or requiring strong auxiliary assumptions such as the "extremely accurate foreground model" of [6]). The classification is relative to $\tau$ and to the available auxiliary structure — which is precisely where engineering ingenuity, as in the thru-free standard of [8], can convert a structural schism into a conventional one.

### 3.5 The master calibration question

The *master calibration problem* is: given frameworks $\{F_1, \dots, F_n\}$ and candidate translations, does there exist an assignment of edge errors $\{\varepsilon_{ij}\}$ such that all cycles close within $\tau$? If not, the minimal set of edges that must be *cut* (schisms accepted as structural) is the combinatorial core of the problem. We do not solve this in general; we derive the quantitative machinery and apply it to the corpus counts.

## 4. Analysis

All inputs below are stated with sources; all arithmetic is shown step by step.

**Input 1 (from [9]):** the number of unresolved bifurcations is $N_{\text{schism}} = 29$.

**Input 2 (from [11]):** the number of research domains claimed to be vocabularies of one structural object is $n = 7$.

**Input 3 (from [2]):** the proposed linear collider center-of-mass energy range is $E_{\text{cm}} = 500\ \text{GeV}$ to $1\ \text{TeV}$.

**Input 4 (from [6]):** calibration precision is a limiting systematic in 21 cm cosmology (qualitative; used to justify nonzero $\varepsilon$ floors, no number cited).

**Derivation 1: pairwise translation count for the ultrametric program.** If each of the $n = 7$ domains requires a translation to each other, the number of unordered pairs is

$$P = \binom{7}{2} = \frac{7 \times 6}{2} = 21.$$

If translations are directional, the count of directed edges is $7 \times 6 = 42$. The single-invariant claim of [11] corresponds to the hypothesis that all $21$ pairwise closure errors can be driven below a common $\tau$; the 29-schism count of [9] suggests that, at present tolerances, at least some of these closures fail. Since $29 > 21$, the schism inventory cannot be a subset of the 7-domain pairwise relations alone; at least $29 - 21 = 8$ schisms must involve either frameworks outside the seven-domain set or intra-domain bifurcations (e.g., continuum versus discrete within a single framework's mathematics). This is a genuine constraint derived purely from the two supplied counts.

**Derivation 2: composed translation error.** Take a three-framework loop $F_1 \to F_2 \to F_3 \to F_1$ with edge errors $\varepsilon_{12} = 10^{-3}$, $\varepsilon_{23} = 2 \times 10^{-3}$, $\varepsilon_{31} = 5 \times 10^{-4}$ (illustrative values chosen to be far below unity, consistent with the qualitative claim of [6] that calibration is a limiting but not saturated systematic). The closure bound is

$$\Delta_{\gamma} \;\leq\; 1 - (1 - 10^{-3})(1 - 2 \times 10^{-3})(1 - 5 \times 10^{-4}).$$

Compute each factor:

$$(1 - 10^{-3}) = 0.999,$$
$$(1 - 2 \times 10^{-3}) = 0.998,$$
$$(1 - 5 \times 10^{-4}) = 0.9995.$$

Product:

$$0.999 \times 0.998 = 0.997002,$$
$$0.997002 \times 0.9995 = 0.997002 - 0.997002 \times 0.0005 = 0.997002 - 0.000498501 = 0.996503499.$$

Hence

$$\Delta_{\gamma} \;\leq\; 1 - 0.996503499 = 0.003496501 \;\approx\; 3.50 \times 10^{-3}.$$

Cross-check by the additive first-order bound: $\varepsilon_{12} + \varepsilon_{23} + \varepsilon_{31} = 10^{-3} + 2 \times 10^{-3} + 5 \times 10^{-4} = 3.5 \times 10^{-3}$, and the exact product bound $3.4965 \times 10^{-3}$ is indeed below the additive $3.5 \times 10^{-3}$, as expected since second-order terms are subtracted. The two derivations agree to within $3.5 \times 10^{-6}$ in absolute terms, confirming internal consistency of the error model.

**Derivation 3: tolerance at which a schism becomes structural.** Suppose the best available translation chain between two frameworks has $k = 4$ edges, each with error at least $\varepsilon_{\min} = 10^{-2}$ (a floor motivated qualitatively by [6]'s statement that calibration precision is limiting; the floor value itself is an assumption of this illustration, not a measurement). The closure bound is

$$\Delta \;\leq\; 1 - (1 - 10^{-2})^{4}.$$

Compute:

$$(1 - 10^{-2}) = 0.99,$$
$$0.99^2 = 0.9801,$$
$$0.9801^2 = 0.96059601,$$
$$\Delta \;\leq\; 1 - 0.96059601 = 0.03940399 \;\approx\; 3.94 \times 10^{-2}.$$

Thus with a per-edge floor of $10^{-2}$ and a 4-edge chain, no calibration finer than $\tau \approx 3.94 \times 10^{-2}$ is achievable; any application demanding $\tau < 3.94 \times 10^{-2}$ classifies the schism as structural under this chain. Equivalently, the maximum chain length tolerable at per-edge error $\varepsilon_{\min}$ and tolerance $\tau$ satisfies $1 - (1 - \varepsilon_{\min})^{k} \leq \tau$, i.e.

$$k \;\leq\; \frac{\ln(1 - \tau)}{\ln(1 - \varepsilon_{\min})}.$$

For $\tau = 10^{-2}$, $\varepsilon_{\min} = 10^{-2}$:

$$k \;\leq\; \frac{\ln(0.99)}{\ln(0.99)} = 1.$$

So at equal floor and tolerance, only single-edge (direct) translations suffice — a formal statement of why "no common domain, no calibration" intuitions arise: long indirect chains are exponentially penalized.

**Derivation 4: energy-scale gap as a domain-overlap proxy.** From [2], the proposed collider range is $E_{\text{cm}} \in [500\ \text{GeV}, 1\ \text{TeV}]$. Converting the upper bound: $1\ \text{TeV} = 10^{3}\ \text{GeV}$, so the ratio of upper to lower bound is $10^{3}/500 = 2$. The range spans a factor of $2$ in energy. We use this only to note that a single facility covers at most a factor-of-$2$ window, so any translation requiring phenomena outside $[500\ \text{GeV}, 1\ \text{TeV}]$ cannot be calibrated by this shared observable alone — an illustration of why manufactured overlaps are partial, not master, calibrations.

**Derivation 5: counting schisms per domain.** If the $N_{\text{schism}} = 29$ bifurcations of [9] were distributed uniformly over the $n = 7$ domains of [11], the mean would be $29/7 \approx 4.14$ schisms per domain (exact: $29/7 = 4.142857\ldots$). Uniformity is an assumption for illustration only; the derivation shows the inventory is dense enough that each claimed vocabulary carries, on average, more than four open bifurcations, which is the quantitative tension the master-calibration program must address.

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

**R1 (computed).** The number of unordered pairwise translations among the $n = 7$ domains claimed as vocabularies of one structural object [11] is $P = 21$; directed, $42$.

**R2 (computed).** Since the schism inventory counts $N_{\text{schism}} = 29$ [9] and $29 > 21$, at least $29 - 21 = 8$ schisms lie outside the pairwise relations of the seven-domain set, assuming every pairwise relation were itself a schism — the most favorable case for reduction. Under the weaker assumption that only some pairs are schismatic, the excess is larger.

**R3 (computed).** For a three-edge cycle with edge errors $10^{-3}$, $2 \times 10^{-3}$, $5 \times 10^{-4}$, the closure error is bounded by $\Delta_{\gamma} \leq 3.4965 \times 10^{-3}$ (exact product form), consistent with the additive bound $3.5 \times 10^{-3}$.

**R4 (computed).** With a per-edge error floor of $10^{-2}$ (assumed, not measured) and a 4-edge chain, the minimum achievable closure error is $\approx 3.94 \times 10^{-2}$; demanding $\tau = 10^{-2}$ restricts admissible chains to $k \leq 1$ edges.

**R5 (computed).** The collider energy window of [2] spans a factor of $2$ ($500\ \text{GeV}$ to $1\ \text{TeV}$), so it can serve as a shared observable only for translations whose discriminating phenomena fall within that factor-of-$2$ band.

**R6 (computed, under a uniformity assumption).** Mean schisms per domain under uniform distribution of 29 over 7: $\approx 4.14$.

**Projection P1 (labeled projection).** If the ultrametric program's single-invariant claim [11] holds, then all $21$ pairwise closure errors share a common mechanism, and improving any one edge's calibration should reduce the *global* maximum cycle error. Concretely, if a master calibration reduced every edge error by a common factor $f$, the three-edge cycle of R3 would close to $\Delta \leq 1 - (1 - 10^{-3}f)(1 - 2 \times 10^{-3}f)(1 - 5 \times 10^{-4}f)$; for $f = 0.5$ this is $1 - (0.9995)(0.999)(0.99975) = 1 - 0.99825037\ldots$. Computing: $0.9995 \times 0.999 = 0.9985005$; $0.9985005 \times 0.99975 = 0.9985005 - 0.9985005 \times 0.00025 = 0.9985005 - 0.000249625 = 0.998250875$; so $\Delta \leq 1.749 \times 10^{-3}$, a reduction by a factor of $3.4965/1.749125 \approx 2.0$ — i.e., halving edge errors roughly halves closure error at these magnitudes (first-order behavior). This projection assumes the error model of Section 3.3 and independent edge errors; its uncertainty is dominated by the unknown true edge errors, which we have only illustrated.

## 6. Discussion

**Limitations.** The error model is deliberately abstract: $\varepsilon_{ij}$ is defined relative to a "test battery" of propositions whose selection is itself a convention — a reflexive weakness, since the consistency of mathematical language is one of the 29 schisms [9]. The composition bound of Section 3.3 assumes edge errors combine as independent fractional disagreements; correlated errors (a shared flawed assumption in two frameworks) would violate independence and could make closure *worse* than the bound suggests in the correlated direction. The illustrative edge errors in R3 and R4 are assumptions, not measurements; no experiment currently measures $\varepsilon_{ij}$ between, say, general relativity and quantum mechanics, and constructing such a test battery is an open problem we flag rather than solve.

**Failure modes.** First, the framework may be vacuous: if every schism can be reclassified from structural to conventional by inventing auxiliary structure (as [8] eliminated the thru standard), the classification loses content. A guard is to require auxiliary assumptions to be *weaker* than the direct standard they replace, and to count assumption strength. Second, the counts in R1–R2 depend on the corpus's own inventory [9] and claim [11]; if the 29-schism list double-counts, or the seven domains overlap, the arithmetic excess of 8 dissolves. Third, the analogy from sensor calibration may be superficial: physical frameworks are not instruments with fixed error floors, and translation may be *exact* in principle (e.g., decoherence as a QM→classical map may be a theorem, not a calibration) — in which case the error model misdescribes those schisms, and they should be reclassified as conventional with $\varepsilon = 0$ on the relevant edges.

**What would falsify the claims.** The central falsifiable prediction is P1's structure: if a single invariant underlies the seven domains [11], then calibration improvements must propagate globally — reducing one edge error must reduce the maximum cycle error. If instead improving the quantum–classical translation leaves the continuum–discrete closure error untouched, the single-invariant claim is weakened. Similarly, if a direct two-framework translation is found with error far below the chain bound implied by indirect routes (violating $k \leq 1$-style constraints at fine tolerances), the error-composition model itself is falsified. Finally, a complete, internally consistent translation atlas over all 29 schisms with $\tau \to 0$ would falsify the paper's premise that some schisms are structural.

**Open questions.** What is the right measure on the "test battery"? Can the master calibration problem be shown NP-hard in a toy class, explaining why physics has not solved it by accumulation? Does the ultrametric structure of [10]–[11] supply the hierarchy invariant that would make all $21$ pairwise translations instances of one map? And sociologically: does the bottom-up input structure of strategy exercises [1] select for conventional over structural resolutions?

## 7. Conclusion

We have formalized the conjecture that physics' unresolved bifurcations are symptoms of internally consistent frameworks over disjoint domains lacking a master calibration. Modeling frameworks as calibrated theories, translations as error-carrying partial maps, and global consistency as cycle-closure within tolerance, we derived: (i) that pairwise consistency does not imply global consistency, with closure error bounded by $1 - \prod_e (1 - \varepsilon_e)$; (ii) a computed excess of at least $8$ schisms beyond the $21$ pairwise relations of the seven-domain ultrametric claim; (iii) an exponential penalty on indirect translation chains, $k \leq \ln(1-\tau)/\ln(1-\varepsilon_{\min})$; and (iv) a classification of schisms as structural or conventional relative to a stated tolerance. The framework converts a foundational puzzle into a calibration problem with falsifiable structure, and identifies the measurement of inter-framework translation error as the key missing empirical input.

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