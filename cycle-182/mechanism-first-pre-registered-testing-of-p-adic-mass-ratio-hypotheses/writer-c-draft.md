# Mechanism-First Pre-Registered Testing of p-Adic Mass-Ratio Hypotheses: Converting Numerology into Falsifiable Physics

## Abstract

Prior attempts to derive the Standard Model particle mass spectrum from p-adic and adelic structures — j-invariant matching, cross-ratios on Bruhat–Tits trees, and 5-smooth semigroup fits — have produced claims that statistical audits reclassify as look-elsewhere artifacts. We argue that the failure is methodological, not mathematical: pattern-matching over a large search space without a derivable mechanism cannot distinguish signal from coincidence. We propose a mechanism mandate: any viable non-anthropocentric natural-units account of the mass spectrum must be grounded in a derivable dynamical mechanism, such as renormalization-group (RG) flow from a UV Yukawa boundary condition, anomaly-cancellation constraints, or moduli-stabilization symmetries, and must yield pre-registered predictions of specific mass ratios or Compton-spectrum structure with locked statistical thresholds. We formalize the protocol: mechanism selection, pre-registration of infrared (IR) predictions, generation of independent surrogate spectra, and full null-distribution reporting. As worked examples we compute the look-elsewhere probability for a 100-candidate search, quantify the evidential weight of a reported $9138\sigma$ deviation, and give a one-loop RG projection for Yukawa running. We situate the program against the p-adic literature, distinguishing rigorous p-adic arithmetic results from speculative p-adic physics, and conclude that a mechanism mandate is the minimal conversion of adelic numerology into testable physics.

## 1. Introduction

The Standard Model (SM) mass spectrum — the set of fermion masses, mixing angles, and coupling ratios — remains unexplained within the SM itself: Yukawa couplings are free parameters fitted to data. This vacuum has repeatedly attracted proposals that the spectrum encodes hidden arithmetic structure. Among the most persistent are p-adic and adelic proposals, in which the real-valued mass ratios are conjectured to be shadowed by structure over the p-adic numbers $\mathbb{Q}_p$ (numbers equipped with a norm in which divisibility by a prime $p$ measures size, so that "closeness" means congruence modulo growing powers of $p$).

The historical record of these proposals, as documented in the QNFO programme corpus, is sobering. The Adelic Cross-Domain Program matched SM particle masses to elliptic-curve $j$-invariants using decimal data from the Particle Data Group; its v3.2 corrections record arithmetic errors in mass-ratio triplets, of which only 5 of 9 verified independently, and acknowledge a "semigroup density epistemological risk" [11]. A statistical audit of the related 5-smooth semigroup mass-ratio claim returned the verdict CONSISTENT WITH LOOK-ELSEWHERE ARTIFACT, with a global p-value $p_{\text{global}} = 0.116$, two arithmetic errors in the claimed fit, five non-optimal triples, and precise ratios deviating by $4$ to $9138$ standard deviations from the claimed values [10]. A pre-registered search for adelic structure in Compton-frequency cross-ratios on Bruhat–Tits trees (the combinatorial trees on which buildings over p-adic groups are modeled) represents the current state of the programme and explicitly retreats from the earlier "Adelic Theory of Everything" matching approach [9].

The common failure mode is clear: in each case, a large space of candidate numerical coincidences was searched, a match was found, and the match was reported without accounting for the search itself. This is the look-elsewhere effect, and it is not a defect of p-adic mathematics but of the absence of a mechanism. A mechanism — a derivable dynamical statement of the form "UV boundary condition $X$, evolved through documented dynamics $Y$, necessarily produces IR ratio $Z$" — changes the epistemic situation qualitatively. It restricts the search space before looking, it produces predictions rather than postdictions, and it can be falsified.

This paper makes three contributions. First, we articulate the mechanism mandate as a formal criterion for adelic/p-adic mass-spectrum proposals (Section 3). Second, we specify a complete pre-registered testing protocol, including independent surrogate generation and locked thresholds (Section 3). Third, we provide explicit quantitative illustrations: the look-elsewhere arithmetic that explains the failures in [10, 11], the evidential content of extreme sigma claims, and a one-loop RG projection showing what a mechanism-based prediction would look like in practice (Section 4). Throughout, we distinguish what the p-adic literature rigorously establishes from what remains conjectural or speculative (Section 2).

## 2. Background and Related Work

We review the supplied bibliography in its given order, separating rigorous p-adic arithmetic, p-adic statistical mechanics, p-adic physics proposals, and the QNFO programme documents.

**Rigorous p-adic arithmetic and L-functions.** The p-adic Beilinson conjecture work [1] formulates a conjectural p-adic analogue of Borel's theorem, relating regulators for higher $K$-groups of number fields to special values of the corresponding zeta-functions, using syntomic regulators and p-adic $L$-functions, and states a conjecture about the precise relation between the p-adic and classical situations. This is representative of the mainstream p-adic arithmetic tradition: deep, structural conjectures connecting p-adic invariants to classical special values, with the p-adic–classical relation itself made an object of study. Our mechanism mandate imports exactly this standard of precision: a p-adic account of masses should state the p-adic–real correspondence as precisely as [1] states its regulator–zeta relation, not leave it as an aesthetic analogy.

The supersingular Birch–Swinnerton-Dyer formulation [2] constructs p-adic analogues of the BSD conjecture for an elliptic curve $E$ at a prime $p$ of good supersingular reduction, using a pair of Iwasawa functions $L^\sharp(E,T)$ and $L^\flat(E,T)$, proves equivalence to the conjectures of Perrin-Riou and Bernardi, and generalizes work of Kurihara and Pollack to give a criterion for positive rank in terms of the value of the (truncated summary supplies no further detail on that criterion). The relevance to our program is structural: [2] shows how a p-adic object ($L^\sharp$, $L^\flat$) can carry physical-type content (rank, order of vanishing) with equivalent classical formulations. Any p-adic mass proposal should aspire to an equivalence theorem of this type — a demonstration that the p-adic formulation and a real formulation agree on all testable content.

Generalized Iwasawa main conjectures and p-adic Stark conjectures for Artin motives [4] introduce, for an odd prime $p$ and a $p$-stabilized Artin representation $\rho$ over $\mathbb{Q}$, a family of p-adic Stark regulators and formulate an Iwasawa–Greenberg main conjecture and a p-adic Stark conjecture, described as an explicit strengthening of conjectures by Perrin-Riou and Benois; the entry further states that these conjectures imply the p-pa... (truncated). Again the pattern is: conjectures with precise regulator objects and stated implications. The p-adic multiple $L$-functions paper [8] constructs $p$-adic multiple $L$-functions in several variables, generalizing the classical Kubota–Leopoldt $p$-adic $L$-functions, via a specific $p$-adic measure, and establishes fundamental properties and evaluation of special values from the p-adic analytic side. Multi-variable p-adic $L$-functions are the natural analytic home for multi-ratio spectra: if a mass-ratio vector is ever to be predicted by a p-adic mechanism, an object of the type constructed in [8] is a plausible carrier of the arithmetic side.

**p-Adic statistical mechanics.** The Potts model work [3] considers a three-state p-adic Potts model with competing interactions on a Cayley tree of order two, reduces the description of p-adic Gibbs measures to a recursive equation, and proves that a phase transition occurs if and only if $p=3$ for any nonzero value of the interactions, additionally solving the uniqueness problem. This is instructive for two reasons. First, it is a case where p-adic structure yields a sharp, provable, parameter-free dichotomy ($p=3$ or not) — precisely the shape of result a mechanism should produce. Second, it shows that p-adic models can have genuine phase structure, i.e., that p-adic statistical systems are not mere curiosities but support nontrivial collective behavior.

The p-adic equiangular lines paper [5] introduces p-adic equiangular lines and derives the first fundamental relation between common angle, dimension, and number of lines: if $\{\tau_j\}_{j=1}^n$ are p-adic $\gamma$-equiangular lines in $\mathbb{Q}_p^d$, then

$$|n|^2 \leq |d|\,\max\{|n|, \gamma^2\},$$

called the p-adic van Lint–Seidel relative bound. Equiangular lines are the p-adic analogue of structures used in quantum information for mutually unbiased bases; the existence of a p-adic relative bound shows that p-adic geometry supports the same kind of packing/angle constraints that organize real Hilbert-space structure. For our purposes this is a template for how a p-adic constraint could bound a spectrum: a mechanism that derives an inequality of the form (1) for mass ratios would be falsifiable without any free parameter.

**p-Adic physics proposals.** The Topological GeometroDynamics (TGD) Higgs-mechanism paper [6] is the first in a series devoted to calculating the particle mass spectrum in TGD. Its stated logic is that the TGD universe is critical at quantum level, that conformal invariance is an attractive realization of criticality, and that ordinary real numbers do not allow this — but if, in long length scales, p-adic topology replaces real topology as the effective topology, the situation changes (the supplied summary truncates at this point). This is the closest antecedent to a "mechanism-first" p-adic mass program: it names a mechanism (criticality realized through p-adic effective topology) rather than a numerological match. However, the summary supplied gives no further detail on the calculated spectrum, so we cannot assess from the entry whether the mechanism produced falsifiable numbers; our mandate is designed to force exactly that disclosure.

The companion mathematical paper [7] describes the mathematical basis of the p-adic Higgs mechanism of the series hep-th 9410058–62: the basic properties of p-adic numbers, their algebraic extensions, and the so-called canonical identification between positive real numbers and p-adic numbers, which induces p-adic topology and a differentiable structure on the real axis (summary truncated). The canonical identification is the crucial device: it is the map by which p-adic quantities acquire real readings, and therefore the point where any p-adic mass prediction must commit to an explicit, non-anthropocentric convention. The QNFO corpus notes that Version 1.0 of the Compton-frequency programme "established that physical quantities can be formulated without anthropocentric conventions" [9]; the canonical identification of [7] is the mathematical tool for making such a formulation precise.

**The QNFO programme documents.** The Compton-frequency cross-ratio programme [9] documents the trajectory: Version 1.0 established convention-free formulation; its extension into an "Adelic Theory of Everything" attempted to match SM particle masses to CM $j$-invariants via decimal PDG data — "an approach we now recogni[se as flawed]" (truncated). The statistical audit [10] supplies the quantitative verdict quoted in Section 1: $p_{\text{global}} = 0.116$, two claimed-fit arithmetic errors, five non-optimal triples, precise ratios deviating $4$–$9138\sigma$, and a pre-registered neutrino prediction that "trivially passes" — i.e., a prediction so weak that passing it carries no evidential weight. The Adelic Cross-Domain Program document [11] records the v3.2 corrections of 2026-07-25: arithmetic errors in mass-ratio triplets corrected (5 of 9 verified independently), the Efimov lambda derivation replaced with an "honest structural correspondence," a constraining literature section added, and the semigroup density epistemological risk acknowledged. Together [9, 10, 11] constitute an unusually candid self-audit trail, and they motivate the present paper: the programme has already conceded that pattern-matching fails; the remaining question is what replaces it.

## 3. Methods

### 3.1 The mechanism mandate

We define a **mechanism** for a mass-spectrum account as a triple $\mathcal{M} = (B, D, \Phi)$:

- $B$ (boundary data): a finite, explicitly stated set of UV or high-scale inputs, e.g., a Yukawa boundary condition $y_i(M_{\text{UV}})$, a gauge group with anomaly-cancellation constraints, or a moduli-stabilization vacuum with fixed symmetries.
- $D$ (dynamics): a derivable evolution law taking $B$ to IR observables, e.g., RG equations $\frac{d y_i}{d \ln \mu} = \beta_i(\{y_j\}, \{g_a\})$.
- $\Phi$ (prediction map): a rule producing specific numerical IR predictions — mass ratios $r_k = m_k / m_{k'}$, or Compton-frequency ratios $\nu_k / \nu_{k'}$ where $\nu_k = m_k c^2 / h$ is the Compton frequency of a particle of mass $m_k$.

A proposal satisfies the mandate iff $\Phi(B, D)$ outputs numbers before comparison with data, with no free post-hoc fitting. Pattern-matching proposals — including the $j$-invariant matching of [11] and the 5-smooth semigroup fits audited in [10] — have empty $D$: they search a discrete candidate set for coincidences with data, which is precisely the configuration that generates look-elsewhere artifacts.

### 3.2 Pre-registered testing protocol

Given a candidate mechanism $\mathcal{M}$:

1. **Pre-registration.** Before any data comparison, publish: the predicted IR ratios $\{r_k^{\text{pred}}\}_{k=1}^{K}$ with uncertainties $\{\sigma_k^{\text{pred}}\}$, the statistical threshold $\alpha$ (locked, e.g., $\alpha = 0.05$ family-wise), the test statistic, and the number of independent tests $K$.
2. **Independent surrogates.** Generate surrogate spectra that preserve the known symmetries and marginal statistics of the data but are *not* permutations or rescalings of the model output. The null distribution $H_0$ is built from these surrogates, not assumed Gaussian.
3. **Full null reporting.** Report the entire null distribution of the test statistic $T$, the realized $T_{\text{obs}}$, and the p-value $p = \Pr(T \geq T_{\text{obs}} \mid H_0)$, alongside the family-wise correction.
4. **Mechanism ablation.** Re-run with each element of $B$ and $D$ perturbed within its stated uncertainty; a mechanism that survives only at its tuned point is rejected.

### 3.3 Candidate mechanism class

As the concrete exemplar we take 2-loop RG running of SO(10) Yukawa unification: boundary condition $y_t(M_{\text{UV}}) = y_b(M_{\text{UV}}) = y_\tau(M_{\text{UV}})$ from unified representation structure, evolved through the 2-loop RG to the IR, predicting ratios such as $r_{b/\tau} = m_b / m_\tau$ and $r_{\tau/\mu} = m_\tau / m_\mu$. The methodological analysis below does not depend on whether this particular mechanism succeeds; it depends only on the mechanism having nonempty $D$.

## 4. Analysis

All arithmetic in this section is shown step by step. Input numbers are stated with their sources.

### 4.1 Look-elsewhere arithmetic for unstructured searches

**Input 1.** The audit [10] reports $p_{\text{global}} = 0.116$ for the 5-smooth semigroup claim. **Input 2.** The audit reports deviations of $4\sigma$ to $9138\sigma$ for precise ratios. **Input 3.** We posit, as a stated assumption for illustration, a search over $N_c = 100$ independent candidate ratios (the corpus documents of [10, 11] describe searches over many candidate triples; $N_c = 100$ is an illustrative order of magnitude, not a measured count).

The probability of at least one "match" at per-candidate threshold $p_0$ in $N_c$ independent trials is

$$P_{\geq 1} = 1 - (1 - p_0)^{N_c}.$$

For $p_0 = 0.05$, $N_c = 100$:

$$(1-p_0)^{N_c} = 0.95^{100} = e^{100 \ln 0.95} = e^{100 \times (-0.051293)} = e^{-5.1293} = 0.005916,$$

$$P_{\geq 1} = 1 - 0.005916 = 0.994084.$$

So a 100-candidate search at the conventional $5\%$ threshold yields at least one "significant" match with probability $\approx 0.9941$ — a near-certainty of false positive. This is the quantitative explanation of the verdict in [10]: with an empty $D$, the search space itself manufactures significance.

For the global p-value: the audit's $p_{\text{global}} = 0.116$ exceeds $\alpha = 0.05$, so the claim is not significant even before search-space correction is debated; we compute the odds ratio against the alternative as $0.116 / (1 - 0.116) = 0.116 / 0.884 = 0.1312$, i.e., the null is favored by a factor $1/0.1312 = 7.62$.

### 4.2 Evidential weight of extreme sigma claims

The audit [10] reports precise ratios deviating up to $9138\sigma$ from claimed values. Under a Gaussian null, the two-sided p-value for a $z\sigma$ deviation is

$$p(z) = \operatorname{erfc}\!\left(\frac{z}{\sqrt{2}}\right) \approx \sqrt{\frac{2}{\pi}} \frac{e^{-z^2/2}}{z}.$$

For $z = 9138$:

$$z^2 = 9138^2 = 83{,}503{,}044, \qquad \frac{z^2}{2} = 41{,}751{,}522,$$

$$p \approx \sqrt{\frac{2}{\pi}} \cdot \frac{e^{-41{,}751{,}522}}{9138} \approx 0.7979 \times \frac{e^{-41{,}751{,}522}}{9138}.$$

In base-10: $e^{-41{,}751{,}522} = 10^{-41{,}751{,}522 / \ln 10} = 10^{-41{,}751{,}522 / 2.302585} = 10^{-1.8134 \times 10^{7}}$. The deviation is therefore astronomically inconsistent with the claimed fit — which is the audit's point: the "precise" ratios were not merely unlucky, they were arithmetically wrong (consistent with the two claimed-fit arithmetic errors and five non-optimal triples also reported in [10]). The lesson for the mandate: a mechanism's predictions must be checked for internal arithmetic consistency *before* statistical comparison, since a $9138\sigma$ discrepancy signals broken bookkeeping, not new physics.

At the other end, the smallest reported deviation, $4\sigma$, gives

$$\frac{z^2}{2} = \frac{16}{2} = 8, \qquad p \approx 0.7979 \times \frac{e^{-8}}{4} = 0.7979 \times \frac{3.3546 \times 10^{-4}}{4} = 6.692 \times 10^{-5}.$$

Even the mildest reported deviation is individually decisive against the claimed ratios — reinforcing that the failures in [10, 11] were arithmetic, not statistical subtlety.

### 4.3 One-loop RG projection for a mechanism-based prediction

**Stated assumptions (projection, not measurement).** We illustrate what a mechanism prediction looks like using a one-loop Yukawa RG step. Assumptions: (i) UV scale $M_{\text{UV}} = 1.22 \times 10^{19}\ \text{GeV}$ (a stated convention for the reduced Planck scale, chosen here purely for illustration); (ii) IR scale $M_{\text{IR}} = 125.1\ \text{GeV}$ (Higgs mass scale as reference); (iii) one-loop running $\frac{dy}{d\ln\mu} = \frac{y^3}{16\pi^2}$, giving

$$\frac{\Delta y}{y} \approx \frac{y^2}{16\pi^2} \ln\!\frac{M_{\text{UV}}}{M_{\text{IR}}}.$$

Compute the log:

$$\frac{M_{\text{UV}}}{M_{\text{IR}}} = \frac{1.22 \times 10^{19}}{125.1} = 9.752 \times 10^{16},$$

$$\ln\!\frac{M_{\text{UV}}}{M_{\text{IR}}} = \ln(9.752) + 16 \ln 10 = 2.2775 + 36.8414 = 39.119.$$

Then for a unified Yukawa $y = 1$ (stated assumption):

$$\frac{\Delta y}{y} = \frac{1}{16\pi^2} \times 39.119 = \frac{39.119}{157.914} = 0.2477.$$

So a one-loop mechanism with $y(M_{\text{UV}}) = 1$ shifts the Yukawa by $\approx 24.8\%$ over the full Planck-to-electroweak run — a $25\%$-level prediction that is falsifiable at achievable precision. For $y = 0.1$ (stated assumption):

$$\frac{\Delta y}{y} = 0.01 \times 0.2477 = 2.477 \times 10^{-3},$$

i.e., light Yukawas run slowly, so mechanism-based predictions for $r_{\tau/\mu}$-type ratios would need 2-loop and threshold effects — which is why the exemplar mechanism of Section 3.3 specifies 2-loop running. This projection illustrates the *form* of a mechanism prediction: a number with stated inputs, derivable by anyone, falsifiable by anyone.

### 4.4 Threshold design for the pre-registered test

With $K$ pre-registered predictions and family-wise error rate $\alpha_{\text{FWER}}$, the Šidák-type per-test threshold (assuming independence, stated assumption) is

$$\alpha_{\text{per}} = 1 - (1 - \alpha_{\text{FWER}})^{1/K}.$$

For $\alpha_{\text{FWER}} = 0.05$, $K = 5$:

$$\alpha_{\text{per}} = 1 - 0.95^{0.2} = 1 - e^{0.2 \ln 0.95} = 1 - e^{-0.010259} = 1 - 0.98979 = 0.01021.$$

So five pre-registered predictions each require $p < 0.0102$ to keep the family-wise false-positive rate at $5\%$ — a locked threshold that removes post-hoc discretion.

## 5. Results

We report only quantities computed in Section 4, plus the labeled projection of Section 4.3.

1. **Look-elsewhere saturation (computed).** For a 100-candidate independent search at per-candidate $p_0 = 0.05$, the probability of at least one match is $P_{\geq 1} = 0.994084$ (Section 4.1). Unstructured searches essentially guarantee false positives; this reproduces, in expectation, the look-elsewhere verdict of [10].
2. **Global significance of the audited claim (computed).** With $p_{\text{global}} = 0.116$ from [10], the null is favored over the alternative by a factor $7.62$ (odds $0.1312$ against signal); the claim fails a locked $\alpha = 0.05$ threshold.
3. **Evidential weight of reported deviations (computed).** The reported $9138\sigma$ deviation corresponds to $p \approx 10^{-1.8134 \times 10^{7}}$; even the smallest reported deviation, $4\sigma$, gives $p \approx 6.692 \times 10^{-5}$. Both are decisive against the claimed ratios, indicating arithmetic failure rather than statistical fluctuation.
4. **One-loop RG projection (labeled projection; assumptions in Section 4.3).** With $M_{\text{UV}} = 1.22 \times 10^{19}\ \text{GeV}$, $M_{\text{IR}} = 125.1\ \text{GeV}$, and $y(M_{\text{UV}}) = 1$, the one-loop shift is $\Delta y / y = 0.2477$; for $y(M_{\text{UV}}) = 0.1$, $\Delta y / y = 2.477 \times 10^{-3}$. Uncertainty: these are illustrative one-loop values; 2-loop terms and threshold corrections are of order the omitted $\mathcal{O}(y^4/(16\pi^2)^2)$ terms and are not quantified here.
5. **Locked threshold (computed).** For $K = 5$ pre-registered predictions at $\alpha_{\text{FWER}} = 0.05$, the per-test threshold is $\alpha_{\text{per}} = 0.01021$.

No empirical measurement of any particle mass ratio is performed or claimed in this paper; the RG numbers are projections under stated assumptions, and all other numbers derive from inputs supplied by [10] or stated assumptions.

## 6. Discussion

**Limitations.** The mechanism mandate is a criterion, not a guarantee: a mechanism can be derivable and still wrong, and the RG exemplar of Section 3.3 is chosen for methodological clarity, not because the supplied corpus establishes its success. The look-elsewhere computation of Section 4.1 assumes independence of candidate ratios; correlated candidates (e.g., ratios sharing a mass) reduce the effective $N_c$, so $P_{\geq 1} = 0.994$ is an upper bound under that assumption — though the qualitative conclusion (saturation) is robust for any $N_c \gtrsim 10$. The one-loop projection ignores 2-loop, threshold, and mixing effects that are essential for the light Yukawas, as the $y = 0.1$ case shows ($\Delta y/y \approx 2.5 \times 10^{-3}$, below current spectroscopic relevance for many ratios). The illustrative scales $M_{\text{UV}}$ and $M_{\text{IR}}$ are conventions; a non-anthropocentric account, in the spirit of the convention-free formulation of [9] and the canonical identification of [7], would need to justify its scale choices structurally rather than by convention — a tension we do not resolve here.

**Failure modes of the mandate itself.** (i) *Mechanism laundering*: a "mechanism" whose boundary data $B$ secretly encodes the answer (e.g., a UV condition fixed by fitting the IR masses) is pattern-matching in disguise; the ablation step of Section 3.2 is the defense, but it is not foolproof. (ii) *Surrogate contamination*: if surrogates are generated using the model's own output statistics, the null is biased toward acceptance; the requirement that surrogates not be permutations of model output is necessary but its enforcement is procedural. (iii) *Threshold rigidity*: locked thresholds can reject a correct mechanism whose uncertainty estimate was optimistic; the protocol should therefore pre-register the uncertainty model, not only the threshold. (iv) *Truncated evidence*: as the truncated summaries in [2, 4, 6, 7, 9] illustrate, published claims often cannot be fully assessed from abstracts alone; our assessment of the TGD mechanism [6], for instance, is limited to what its supplied entry states, and the entry gives no calculated spectrum.

**What would falsify our claims.** The central methodological claim — that empty-$D$ searches produce look-elsewhere artifacts — would be weakened if a pre-registered, search-corrected, empty-$D$ match survived scrutiny with $p < \alpha_{\text{per}}$ and reproduced across independent data. Conversely, the claim that mechanism-based predictions are achievable at testable precision would be falsified if all candidate mechanisms (RG, anomaly, moduli) produced IR predictions whose intrinsic uncertainties exceed the measured ratios' precision by orders of magnitude. The specific one-loop projection of Section 4.3 is falsified by any demonstration that 2-loop corrections to it exceed $\pm 0.25$ in $\Delta y / y$ for $y = 1$.

**Open questions.** Can the p-adic machinery of [1, 2, 4, 8] — regulators, $L^\sharp/L^\flat$ pairs, multiple $L$-functions — be adapted to carry a *dynamical* p-adic mechanism rather than a static correspondence? The phase-transition dichotomy of [3] ($p = 3$ iff transition) and the p-adic van Lint–Seidel bound of [5] show that p-adic structures can yield parameter-free, falsifiable statements; whether any such statement can be connected to mass ratios through a canonical identification of the type described in [7] remains open. Whether the Compton-frequency cross-ratio search of [9] finds structure above its pre-registered thresholds is an empirical question this paper does not answer.

## 7. Conclusion

The audit trail of the adelic mass-spectrum programme — arithmetic errors, non-optimal triples, a global p-value of $0.116$, and deviations up to $9138\sigma$ — establishes that pattern-matching over p-adic and adelic candidate structures does not yield physics. We have argued that the remedy is structural: a mechanism mandate requiring a derivable dynamics $(B, D, \Phi)$, pre-registered IR predictions, independent surrogates, locked thresholds, and full null reporting. The quantitative illustrations — look-elsewhere saturation at $P_{\geq 1} = 0.994$ for a 100-candidate search, a per-test threshold of $0.0102$ for five pre-registered predictions, and a one-loop RG shift of $0.248$ for a unit unified Yukawa — show concretely how the mandate converts numerology into falsifiable predictions. The rigorous p-adic literature demonstrates that p-adic mathematics can produce sharp, parameter-free, provable statements; the task for p-adic physics is to reach that standard through mechanism, not coincidence.

## References

[1] arXiv:0707.3682v2 | On the p-adic Beilinson conjecture for number fields

[2] arXiv:1512.09362v1 | A formulation for p-adic versions of the Birch and Swinnerton-Dyer conjectures in the supersingular case

[3] arXiv:math-ph/0512018v2 | On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree

[4] arXiv:2103.06864v4 | On generalized Iwasawa main conjectures and $p$-adic Stark conjectures for Artin motives

[5] arXiv:2408.00810v3 | p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound

[6] arXiv:hep-th/9410058v3 | p-Adic description of Higgs mechanism I: p-Adic square root and p-adic light cone

[7] arXiv:hep-th/9506097v2 | p-Adic TGD: Mathematical Ideas

[8] arXiv:1508.07185v2 | Fundamentals of p-adic multiple L-functions and evaluation of their special values

[9] QNFO: Compton Frequency Cross-Ratios on Bruhat-Tits Trees: A Pre-Registered Search for Adelic Structure in the Standard Model Mass Spectrum (Version 2.3)

[10] QNFO: Statistical Audit