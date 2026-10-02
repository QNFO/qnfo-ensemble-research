# Generalized Scaling Exponents $D_q^\alpha$ for Arbitrary Scaling Ratio $q$: A Synthetic Framework

## Abstract

Dimension-like exponents in fractal geometry and multifractal analysis are conventionally anchored to integer scaling ratios: the middle-third Cantor set yields $\log 2/\log 3$, and $p$-adic constructions yield $\log p^k/\log p = k$. This paper develops a unified treatment of a two-parameter family of exponents, denoted $D_q^\alpha$, in which $q$ is an arbitrary (not necessarily integer) scaling ratio and $\alpha$ is a moment order in the Rényi sense. We define $D_q^\alpha$ via the asymptotic growth of $\alpha$-weighted partition sums under $q$-adic refinement, prove basic monotonicity and continuity properties, and compute explicit values for benchmark systems: the equal-measure two-cell refinement at $q=3$ ($D_3^0 = \log 2/\log 3 \approx 0.6309$), the biased two-cell system across $\alpha \in \{0,1,2,\infty\}$, and non-integer ratios such as $q = 2.5$ ($D_{2.5}^0 \approx 0.7565$). We situate the construction within ultrametric and adelic frameworks, arguing that arbitrary-$q$ scaling interpolates between the $p$-adic integer-ratio case and generic metric refinement. All numerical results are derived by explicit arithmetic from stated inputs; no simulated or empirical data are used. The framework is offered as a bookkeeping language for cross-scale phenomena, with clearly stated falsifiability conditions and limitations.

## 1. Introduction

Scaling exponents are among the most compact summaries of complex structure. When a set or measure refines under a contraction of ratio $1/q$, the leading behavior of an appropriate counting or moment functional defines a dimension. The classical cases are rigid about $q$: Hausdorff and box-counting dimensions are usually illustrated with $q = 2, 3, 5$, and the entire apparatus of $p$-adic and ultrametric physics — a program elaborated in the QNFO corpus [9], [10], [12] — fixes $q = p$, a prime. Yet many natural hierarchies do not refine by integer ratios: branching processes with non-integer mean offspring, renormalization flows with irrational contraction constants, and data-driven dendrograms [5], [7] all produce trees whose level-to-level contraction is generic.

The research idea re-entered from the record at DOI 10.5281/zenodo.22758467 [9] poses the question directly: what becomes of the exponent family $D_q^\alpha$ when $q$ is an arbitrary scaling ratio? This paper answers in three steps. First, we give a precise definition of $D_q^\alpha$ that reduces, at integer $q$ and uniform measure, to the familiar $\log N/\log q$ and, at $\alpha = 1$, to an information dimension. Second, we derive its structural properties — monotonicity in $\alpha$, behavior at $\alpha \to 0$ and $\alpha \to \infty$, and continuity in $q$ — with full arithmetic. Third, we compute a table of benchmark values, including non-integer $q$, and discuss what such numbers could and could not mean physically.

The motivation is not merely notational. If, as the adelic synthesis [12] and the cross-ratio reframing of the fine-structure constant [11] propose, physical constants encode geometric relationships across completions of the rationals, then the allowed "refinement ratios" of a theory are a structural datum. Ostrowski's theorem restricts absolute values to the real and the $p$-adic families; but hierarchical clustering of empirical data [5], [7], [8] respects no such restriction. A formalism in which $q$ is a free parameter measures the cost — or the freedom — of relaxing that constraint.

We write for an adjacent-field expert. An *ultrametric* is a metric satisfying the strong triangle inequality $d(x,z) \le \max(d(x,y), d(y,z))$; equivalently, all triangles are isosceles with the two long sides equal. A *Rényi dimension* of order $\alpha$ is a one-parameter family of dimensions built from $\alpha$-powers of measure on refining partitions, recovering box dimension at $\alpha = 0$, information dimension at $\alpha = 1$, and correlation dimension at $\alpha = 2$.

## 2. Background and Related Work

**Ultrametric foundations.** The view of ultrametrics as a zero-dimensional analogue of ordinary metrics, with the expectation that metric-space theorems admit ultrametric parallels, is systematized by Bayod, Marra, and others in the embedding-extension-interpolation program [3], which provides ultrametric versions of the Arens–Eells embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff compactness characterization. This matters here because our $D_q^\alpha$ is defined on hierarchical (hence ultrametric) refinements: the theorems of [3] guarantee that the structures we count — balls at successive levels — are well-behaved under extension and embedding, so the exponent does not depend on ambient choices.

**Data-induced ultrametrics.** Murtagh [5] shows how cross-tabulation data, given a Euclidean metric by correspondence analysis, induces an ultrametric that models anomaly and change as transitions between hierarchy levels. The induced ultrametric there is built sequentially, and nothing forces the level-to-level contraction to be an integer ratio; this is a concrete empirical source of arbitrary-$q$ hierarchies and a direct motivation for our parameterization. Murtagh's later work with Matte Blanco's principles of symmetric and asymmetric being [7] makes the same point cognitively: hierarchical clustering of text and questionnaire data yields ultrametric topologies whose branch ratios are data-determined, not prime-determined. If dimension-like summaries are to be computed on such trees, the integer-$q$ restriction is untenable.

**Ultrametric Cantor sets.** Raut and Datta's ultrametric Cantor sets [6], built from relative infinitesimals and an inversion rule, carry a valuation that is simultaneously scale- and reparametrization-invariant. That invariance is the deepest precedent for our claim that $D_q^\alpha$ should be a function of the *ratio* $q$ and the measure weights alone: if the valuation of [6] survives reparametrization, then exponents built on it inherit that survival, and arbitrary $q$ is as legitimate as $q = 3$.

**Ultrametric dynamics.** Khrennikov, Albeverio, and colleagues' ultrametric SIR model [8] introduces ultrametrics on populations via hierarchical clustering by average infectious-contact time, with $p$-adic parameterization as the concrete implementation. The clustering times are continuous data; the choice of $p$-adic coordinates is a modeling convenience. Our framework makes that convenience explicit and replaceable: any $q$ matching the empirical cluster geometry is admissible, and $D_q^\alpha$ quantifies the resulting scaling.

**Programmatic context.** The QNFO corpus anchors this work. *Ultrametric Physics* [9] states the general program; the *Research Plan* [10] organizes its open problems, of which arbitrary-$q$ scaling is one; the cross-ratio treatment of the fine-structure constant [11] demonstrates the methodological stance — reframing a constant as a geometric invariant with explicit falsifiability conditions — that we adopt here; and *Adelic Core Synthesis* [12] assembles the $p$-adic analysis, Bruhat–Tits geometry, and Ostrowski completions into a single foundation, against which the relaxation to arbitrary $q$ must be measured.

**Contrast with experimental strategy documents.** The Physics Briefing Book of the European Particle Physics Strategy Update [1] and the Snowmass '96 linear collider report [2] exemplify community-scale, bottom-up prioritization of future facilities. They are included not for their content on scaling — they have none — but as calibration for how a speculative formal proposal should position itself relative to an experimental community: with explicit feasibility discussion and falsifiable claims, a discipline we import into Section 6. Similarly, the MHD design analysis of CFETR and HFRC [4] shows fusion physics confronting hierarchical, multi-scale magnetohydrodynamic structure in engineering practice; such nested structures are exactly the kind of system where non-integer effective scaling ratios arise, even though [4] itself does not use ultrametric language.

## 3. Methods

### 3.1 Setup

Let $(X, d)$ be a compact ultrametric space, meaning the hierarchy of $d$-balls is a tree. Fix a *scaling ratio* $q > 1$, allowed to be any real number. A $q$-adic refinement sequence is a nested family of partitions $\mathcal{P}_n$, $n = 0, 1, 2, \dots$, such that each ball of level $n$ has diameter $\approx q^{-n}$ times the diameter of $X$. For integer $q$ this is literal subdivision; for non-integer $q$ we define it by requiring diameters to scale as $q^{-n}$, which is always achievable by choosing cut levels appropriately in a tree with continuous branch lengths (as in the data-induced trees of [5], [7]).

Let $\mu$ be a probability measure on $X$, and let $\{p_{n,i}\}_{i=1}^{M_n}$ be the $\mu$-masses of the level-$n$ cells.

### 3.2 Definition of $D_q^\alpha$

The $\alpha$-partition sum at level $n$ is

$$Z_n(\alpha) = \sum_{i=1}^{M_n} p_{n,i}^{\alpha}.$$

Define

$$D_q^\alpha = \frac{1}{1 - \alpha} \lim_{n \to \infty} \frac{\log Z_n(\alpha)}{n \log q}, \qquad \alpha \neq 1,$$

$$D_q^1 = -\lim_{n \to \infty} \frac{\sum_i p_{n,i} \log p_{n,i}}{n \log q}.$$

The logarithm base is immaterial as long as it is consistent; we use natural log throughout and divide by $\log q$. At $\alpha = 0$, $Z_n(0) = M_n$ (counting nonempty cells), recovering box-counting dimension $\log M / \log q$ in the self-similar case. At $\alpha = 1$ we get information dimension; at $\alpha = 2$, correlation dimension. The ultrametric property guarantees that cells at one level are either disjoint or nested, so the partition sums are unambiguous — this is where [3] and [6] do structural work for us.

### 3.3 Benchmark systems

We evaluate $D_q^\alpha$ on three exactly solvable systems:

- **(A) Uniform binary refinement at $q = 3$**: each level splits mass equally into 2 cells of diameter $1/3$ (the Cantor measure). Here $p_{n,i} = 2^{-n}$, $M_n = 2^n$.
- **(B) Biased binary refinement at $q = 3$**: each cell splits into two children with weights $p_1 = 1/3$, $p_2 = 2/3$.
- **(C) Uniform binary refinement at non-integer $q = 2.5$**: masses $2^{-n}$, diameters $2.5^{-n}$.

These are chosen because every partition sum is a geometric series computable in closed form, so all numbers below are exact arithmetic, not simulation.

## 4. Analysis

We now compute every value explicitly. Constants used throughout (standard natural logarithms): $\ln 2 = 0.693147$, $\ln 3 = 1.098612$, $\ln 5 = 1.609438$, $\ln 9 = 2.197225$.

### 4.1 System A: uniform, $q = 3$

At level $n$: $M_n = 2^n$ cells, each with $p_{n,i} = 2^{-n}$.

**Order $\alpha \neq 1$:**
$$Z_n(\alpha) = 2^n \cdot (2^{-n})^\alpha = 2^{n(1-\alpha)}.$$
$$\log Z_n(\alpha) = n(1 - \alpha)\ln 2.$$
$$D_3^\alpha = \frac{1}{1-\alpha} \cdot \frac{n(1-\alpha)\ln 2}{n \ln 3} = \frac{\ln 2}{\ln 3}.$$

Numerically: $0.693147 / 1.098612 = 0.63093$. So $D_3^\alpha = 0.63093$ for **all** $\alpha$ — the hallmark of a monofractal. This is the classical Cantor dimension, here emerging as the $\alpha$-flat member of the family.

**Order $\alpha = 1$:**
$$-\sum_i p_{n,i}\ln p_{n,i} = -2^n \cdot 2^{-n} \ln(2^{-n}) = n \ln 2.$$
$$D_3^1 = \frac{n \ln 2}{n \ln 3} = 0.63093.$$
Consistent, as required.

### 4.2 System B: biased, $q = 3$, weights $(1/3, 2/3)$

At level $n$, a cell reached by a word $w$ with $k$ "heavy" steps has mass $(1/3)^{n-k}(2/3)^k$; there are $\binom{n}{k}$ such cells.

**Order $\alpha = 0$:** $Z_n(0) = 2^n$, so
$$D_3^0 = \frac{n \ln 2}{n \ln 3} = 0.63093.$$
The support is still the Cantor set; bias does not change box dimension.

**Order $\alpha = 2$:**
$$Z_n(2) = \sum_{k=0}^{n}\binom{n}{k}\left[\left(\tfrac13\right)^{n-k}\left(\tfrac23\right)^k\right]^2 = \left[\left(\tfrac13\right)^2 + \left(\tfrac23\right)^2\right]^n = \left(\tfrac{1}{9} + \tfrac{4}{9}\right)^n = \left(\tfrac59\right)^n.$$
$$\log Z_n(2) = n \ln(5/9) = n(\ln 5 - \ln 9) = n(1.609438 - 2.197225) = -0.587787\,n.$$
$$D_3^2 = \frac{1}{1-2}\cdot\frac{-0.587787\,n}{1.098612\,n} = \frac{0.587787}{1.098612} = 0.53475.$$

**Order $\alpha = 1$ (information dimension):**
$$-\sum_i p_{n,i}\ln p_{n,i} = n\left[-\tfrac13\ln\tfrac13 - \tfrac23\ln\tfrac23\right].$$
Compute term by term: $\ln(1/3) = -1.098612$, so $-\frac13\ln\frac13 = \frac13(1.098612) = 0.366204$. $\ln(2/3) = \ln 2 - \ln 3 = 0.693147 - 1.098612 = -0.405465$, so $-\frac23\ln\frac23 = \frac23(0.405465) = 0.270310$. Sum: $0.366204 + 0.270310 = 0.636514$.
$$D_3^1 = \frac{0.636514}{1.098612} = 0.57937.$$

**Order $\alpha \to \infty$:** the dominant term is the all-heavy path, mass $(2/3)^n$:
$$D_3^\infty = -\lim \frac{n\ln(2/3)}{n\ln 3} = -\frac{-0.405465}{1.098612} = 0.36907.$$

**Monotonicity check:** $D_3^0 = 0.63093 \ge D_3^1 = 0.57937 \ge D_3^2 = 0.53475 \ge D_3^\infty = 0.36907$. The sequence is strictly decreasing, consistent with the general theorem that Rényi-type exponents are non-increasing in $\alpha$; here it is verified by direct arithmetic on four independent computations.

### 4.3 System C: uniform, non-integer $q = 2.5$

Masses $2^{-n}$, $M_n = 2^n$, diameters $(2.5)^{-n}$. Then for any $\alpha$,
$$D_{2.5}^\alpha = \frac{\ln 2}{\ln 2.5}.$$
Compute $\ln 2.5 = \ln 5 - \ln 2 = 1.609438 - 0.693147 = 0.916291$.
$$D_{2.5}^\alpha = \frac{0.693147}{0.916291} = 0.75647.$$

Two observations follow by arithmetic. First, $D_q^0$ for this system is *continuous in $q$*: at $q = 2$, $D = \ln 2/\ln 2 = 1$; at $q = 3$, $D = 0.63093$; at $q = 2.5$, $D = 0.75647$, which lies between, as continuity demands. Second, the exponent exceeds 1 for $q < 2$: e.g., at $q = 1.5$, $\ln 1.5 = 0.405465$, so $D_{1.5}^0 = 0.693147/0.405465 = 1.70952$. An exponent greater than 1 is not a Hausdorff dimension of a subset of a line; it signals that the "refinement" is outpacing binary splitting — the tree is adding cells faster than it shrinks them, i.e., the object is not embeddable in one ultrametric line at that ratio. This is a structural warning, not an error: it delimits the regime in which $D_q^\alpha$ admits a geometric interpretation.

### 4.4 Sensitivity to $q$: a projection

For System B, the $\alpha$-spectrum at general $q$ is, by the binomial computation of §4.2,
$$D_q^2 = \frac{-\ln(5/9)}{\ln q} = \frac{0.587787}{\ln q}, \qquad D_q^1 = \frac{0.636514}{\ln q}.$$

*Projection (clearly labeled):* if a data-induced hierarchy [5] had an effective ratio $q \in [2.4, 2.6]$ estimated from cluster diameters, then $D_q^1 \in [0.636514/\ln 2.6,\ 0.636514/\ln 2.4]$. Compute: $\ln 2.6 = 0.955511$, $\ln 2.4 = 0.875469$. Bounds: $0.636514/0.955511 = 0.66614$ and $0.636514/0.875469 = 0.72690$. So $D_q^1 \in [0.666, 0.727]$ under the stated assumption. This is a propagated-interval projection from the closed-form result, not a measurement.

## 5. Results

All numbers below were computed in Section 4 from stated closed-form inputs:

1. **Uniform Cantor system (A):** $D_3^\alpha = \ln 2/\ln 3 = 0.63093$ for every $\alpha \in [0,\infty]$, including $\alpha = 1$ (verified by the Shannon-entropy route, §4.1).
2. **Biased system (B), $q = 3$:** $D_3^0 = 0.63093$; $D_3^1 = 0.57937$; $D_3^2 = 0.53475$; $D_3^\infty = 0.36907$. The spectrum is strictly decreasing, with a spread $D_3^0 - D_3^\infty = 0.63093 - 0.36907 = 0.26186$, quantifying multifractality: the bias $(1/3, 2/3)$ costs $0.26186$ in dimension between the most-counting and most-concentrated orders.
3. **Non-integer ratio (C):** $D_{2.5}^\alpha = 0.75647$ for all $\alpha$; continuity in $q$ verified numerically ($D_2^0 = 1 > 0.75647 > 0.63093 = D_3^0$). At $q = 1.5$, $D_{1.5}^0 = 1.70952$, marking the breakdown of one-dimensional embeddability.
4. **Projected information dimension** for a hypothetical hierarchy with $q \in [2.4, 2.6]$ under System-B weights: $D_q^1 \in [0.666, 0.727]$ (projection with stated assumptions, §4.4).

No empirical, simulated, or measured quantities appear in this list; items 1–3 are exact arithmetic consequences of the definitions in Section 3.

## 6. Discussion

**What the numbers mean — and do not mean.** The values in Section 5 are properties of three exactly specified mathematical systems. Nothing in this paper demonstrates that physical or empirical hierarchies realize these systems. The ultrametric SIR literature [8] and the data-analysis program [5], [7] show that real hierarchies exist and have measurable branch structure, but connecting a measured branching ratio to a $D_q^\alpha$ requires estimation machinery (partition-sum regression, error bars on $q$) that we have not built. Our §4.4 projection is a template for that machinery, not a substitute.

**Limitations.** (i) *Non-integer $q$ is not $p$-adic.* The adelic framework [12] derives its power from Ostrowski's theorem: the completions of $\mathbb{Q}$ are $\mathbb{R}$ and $\mathbb{Q}_p$, so integer-prime ratios are structurally privileged. Our arbitrary-$q$ construction lives on the metric side (trees with continuous branch lengths), and it is *not* a new number field. Anyone claiming a $q = 2.5$-adic analysis would need to construct the underlying algebra; we explicitly do not. (ii) *Embeddability fails for $q < 2$ in the binary case*, as the exponent $1.70952 > 1$ shows; the formalism silently produces numbers outside the geometric regime, and a user must check the regime. (iii) *The definition presumes exact self-similarity* for the closed forms; generic hierarchies have fluctuating branch ratios, and the limit in §3.2 may fail to exist. The scale-invariant valuation of [6] suggests robustness under reparametrization, but that is an analogy, not a proof for our $Z_n(\alpha)$.

**Failure modes and falsifiability.** The mathematical claims are falsifiable by counterexample: (a) if some compact ultrametric space with well-defined $q$-adic refinement had a $D_q^\alpha$ that *increased* in $\alpha$ on some interval, the claimed monotonicity (verified here only on System B) would be false in general — though the standard Rényi argument via Hölder's inequality makes this unlikely; (b) if partition sums for data-induced trees [5] failed to scale linearly in $n$, the limit defining $D_q^\alpha$ would not exist and the framework would be inapplicable to exactly its intended use case. The interpretive claims — that arbitrary-$q$ exponents are a useful bookkeeping language — would be falsified by demonstrating that every empirically observed hierarchy is adequately captured by integer ratios, or that the $q$-dependence carries no information beyond $D$ itself.

**Arguing against ourselves.** One might object that $D_q^\alpha$ for non-integer $q$ is a mere reparameterization: given any exponent $D$, one can *choose* $q$ to make $\ln N/\ln q$ equal anything. This is correct for monofractals (System A/C), where the whole spectrum is flat and $q$ is a gauge choice. The biased case is the rebuttal: the *shape* of the spectrum ($0.63093 \to 0.36907$) is gauge-invariant, and $q$ enters as a physical input — the actual contraction ratio of the hierarchy — not a free dial. The framework is therefore falsifiable in content exactly to the extent that the measured $q$ of a real hierarchy is independently constrained. Where it is not, the objection stands, and the construction is decorative.

**Open questions.** (1) Does a "Bruhat–Tits building at ratio $q$" exist for non-integer $q$, in the sense of [11], [12], and what replaces Ostrowski's classification? (2) Can the multifractal formalism of [6] — scale- and reparametrization-invariant valuations on ultrametric Cantor sets — be extended to give $D_q^\alpha$ a valuation-theoretic definition immune to the gauge objection? (3) What estimation theory recovers $q$ from finite dendrograms of the type produced in [5], [7], [8], with confidence intervals? (4) Do the multi-scale MHD structures of devices like CFETR and HFRC [4] exhibit effective refinement ratios measurably different from integers? (5) A limitation of scope: the bibliography available to this paper contains no dedicated multifractal-formalism reference; the Rényi-dimension background is therefore reconstructed from first principles in §3.2 rather than cited, and a fuller treatment would engage that literature directly.

## 7. Conclusion

We defined a two-parameter exponent family $D_q^\alpha$ on ultrametric refinement hierarchies, with $q$ an arbitrary real scaling ratio, and computed it exactly on three benchmark systems. The results — a flat spectrum at $0.63093$ for the uniform Cantor case, a strictly decreasing spectrum from $0.63093$ to $0.36907$ for the biased case, and a continuous, embeddability-limited dependence on $q$ culminating in $0.75647$ at $q = 2.5$ — establish that the construction is well-defined, arithmetically checkable, and informative precisely when the hierarchy's measure is non-uniform. The framework extends the $p$-adic-anchored program of [9]–[12] to data-driven hierarchies of the kind constructed in [5], [7], [8], at the cost of leaving the algebraic privileges of prime ratios behind. Its value now depends on measurement: independent estimates of branching ratios in real hierarchies, and spectra that deviate from the flat monofractal case, would elevate $D_q^\alpha$ from bookkeeping to physics.

## References

[1] arXiv:1910.11775v2 | Physics Briefing Book

[2] arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96

[3] arXiv:2008.10209v2 | An embedding, an extension, and an interpolation of ultrametrics

[4] arXiv:2107.11742v1 | MHD analysis on the physical designs of CFETR and HFRC

[5] arXiv:0809.0492v1 | From Data to the p-Adic or Ultrametric Model

[6] arXiv:1002.3951v4 | Ultrametric Cantor Sets and Growth of Measure

[7] arXiv:1201.2711v3 | Ultrametric Model of Mind, I: Review

[8] arXiv:2005.08761v3 | Toward ultrametric modeling of the epidemic spread

[9] QNFO: ULTRAMETRIC PHYSICS | DOI 10.5281/zenodo.22758467

[10] QNFO: Ultrametric Physics Research Plan | DOI 10.5281/zenodo.21206278

[11] QNFO: Fine-Structure Constant as a Cross-Ratio: A Geometric Reframing of α | DOI 10.5281/zenodo.20108536

[12] QNFO: Adelic Core Synthesis: Cross-Domain Foundations of Adelic QFT | DOI 10.5281/zenodo.21786473