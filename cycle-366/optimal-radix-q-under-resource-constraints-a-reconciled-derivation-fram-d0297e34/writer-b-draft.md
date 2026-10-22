# Optimal Radix $q$ under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies

## Abstract

Hierarchical (ultrametric) representations organize $N$ items in a $q$-ary tree of depth $n=\lceil\ln N/\ln q\rceil$, and the branching factor $q$ determines storage, interconnection, and traversal costs. Existing treatments treat $q$ as a fixed parameter inherited from convention rather than a design variable, leaving no systematic selection rule under resource constraints. We formalize three resource functionals—pointer storage $S(q)=qN(1-q^{-n})/(q-1)$, traversal cost $T(q)=q\lceil\ln N/\ln q\rceil$, and interconnection degree $D(q)=q+1$—and minimize a weighted composite $F_{\alpha,\beta}(q)=\alpha\,S(q)/N+\beta\,T(q)/T_{\mathrm{ref}}$ with $T_{\mathrm{ref}}=\ln N$. The continuous relaxation places the traversal-only optimum at $q=e\approx2.718$. Exact evaluation for $N=10^{6}$ gives $F_{1,1}(4)=4.2289$, $F_{1,1}(3)=4.3227$, and a traversal-weight threshold $\beta^{*}=2.286$ at which $q=3$ overtakes $q=4$; padded storage leaves $q=4$ optimal with $F^{\mathrm{pad}}_{1,1}(4)=4.2937$. This revision corrects the asymptotic composite calculation: the derivative of the asymptotic composite changes sign between $q=3$ ($-0.1683$) and $q=4$ ($+0.0899$), and linear interpolation gives the root $q=3+0.1683/0.2582=3.6518\approx3.65$, replacing the previously reported intermediate value $3.4956$, which was arithmetically wrong. The results give designers of hierarchical indexes a quantitative selection rule, a weight-sensitivity threshold, and an explicit falsification condition.

## 1. Introduction

Large-scale nested collections—genomic resource ecosystems, virtual-observatory registries, library indexes—must decide how their catalog hierarchy branches, yet the decision is usually made by convention (binary trees, $p$-adic models) rather than by calculation. The operators who face this decision are the maintainers of metadata registries and resource catalogs: the NHGRI resources ecosystem study [5] documents that genomic resource projects identify metadata tools, data curation, and identifier schemes as their key operational challenges, and the IVOA resource-metadata recommendation [6] exists precisely so that registry users can find and use data collections, which requires a queryable hierarchical organization underneath. For $N=10^{6}$ items the branching factor $q$ moves the tree depth between $10$ and $20$ levels, moves pointer storage per item between $1.25$ and $2.00$ units (a factor of $1.6$ between the extremes computed in Section 4.3), and alters the worst-case comparison count per lookup by up to $12.5\%$ across $q\in\{2,3,4,5\}$; at registry scale these differences translate directly into memory footprint, lookup latency, and interconnection fan-out, and a wrong choice is expensive to reverse once data and tooling are built.

If a defensible selection rule existed, a designer could input the item count and a weighting of storage versus traversal, obtain the radix that minimizes the composite cost, quantify the savings over the binary default, and know how far the weighting must move before a different radix wins. This paper provides that rule, together with a sensitivity map that states when the recommendation would be falsified. The paper is a post-publication revision of the predecessor framework [9]: it keeps every result of [9] that its derivations support, corrects the one arithmetic error found in its asymptotic analysis (Section 4.6 here), and strengthens the literature grounding.

**Contributions**

1. A corrected closed-form and numerical derivation of the asymptotic composite optimum: the derivative of $\alpha\,q/(q-1)+\beta\,q/\ln q$ equals $-0.1683$ at $q=3$ and $+0.0899$ at $q=4$, and linear interpolation gives the root $q\approx3.6518\approx3.65$; the previously published intermediate value $3.4956$ is shown to be an arithmetic error (Section 4.6).
2. Exact integer-radix comparison for $N=10^{6}$ with shown arithmetic: $q=4$ is optimal under equal weights ($F_{1,1}(4)=4.2289$) and under padded storage ($F^{\mathrm{pad}}_{1,1}(4)=4.2937$), $q=3$ becomes optimal only when the traversal weight exceeds $\beta^{*}=2.286$, and $q=2$ is never optimal for any $\beta>0$ (Sections 4.3–4.5).
3. A methodological embedding that imports the multi-metric optimization lesson of reversible-circuit synthesis [2] and the uncertainty-quantification framing of re-entry breakup studies [8], and a falsification map that specifies the conditions under which the $q=4$ recommendation would fail (Sections 2 and 6).

## 2. Background and Related Work

**Radar-based re-entry prediction for GOCE [1].** The study uses accurate GPS and attitude measurements to compute a precise reference orbit for three weeks of GOCE decay and to extrapolate the ballistic-coefficient evolution of the object; its main result is that radar-based orbit determination with sparse tracking, even from a single EISCAT UHF site, estimates the average evolution of the ballistic coefficient effectively compared to continuous GPS [1]. This supplies the methodological template for the present revision: a well-instrumented reference derivation (the exact integer evaluation of Section 4.3) followed by extrapolation of a small parameter set (the asymptotic root of Section 4.6) into a regime where direct evaluation is not performed. The sparse-tracking-versus-continuous-observation contrast in [1] also motivates stating explicitly which quantities are derived exactly and which are interpolated.

**Synthesis of reversible functions beyond gate count and quantum cost [2].** The paper argues that physically realizable reversible and quantum hardware faces constraints beyond the simple metrics of gate count and quantum cost, and demonstrates concretely that for benchmark circuits the BDD-based synthesis approach appears best if only gate count and quantum cost are used, while the judgement changes when further cost metrics such as nearest-neighbor cost, depth, and transfer cost are considered; it further reports synthesis-flow improvements that reduce quantum cost by up to $83\%$ ($56\%$ on average) without affecting NNC-optimality [2]. This is the direct precedent for the composite objective used here: a single metric (depth alone, or storage alone) can rank radices differently from a weighted composite, so the ranking must be reported as a function of the weights, which Section 4.5 does.

**InstructLayout [3].** The work integrates a semantic graph prior and a layout decoder to improve controllability and fidelity of 2D and 3D layout synthesis, and measures controllability with an instruction-recall metric that requires all three elements of a subject-relation-object triplet to occur in the synthesized scene [3]. The relevance is structural: an explicit prior over the output space (there a semantic graph, here a $q$-ary ultrametric tree) is what makes the design variable controllable and auditable. Treating the radix as an explicit, declared parameter of the hierarchy—rather than an implicit consequence of the representation—mirrors the role the semantic graph prior plays in [3].

**Synth-by-Reg [4].** The paper introduces a registration loss for weakly supervised image translation that does not require perfectly aligned training data, converting inter-modality registration into an intra-modality task, and reports landmark-error reductions of $11\%$, $9\%$, and $7\%$ against cGAN, RoT, and NMIw on the Allen dataset and $23\%$ and $33\%$ against cGAN and RoT on the BigBrain dataset [4]. The lesson imported here is that an objective must be a faithful proxy for the quantity of interest: the composite $F_{\alpha,\beta}$ is useful only insofar as its storage and traversal terms proxy real memory and latency, which is why Section 6 treats the proxy quality of $T(q)=q\,n(q)$ as a first-class limitation rather than an afterthought.

**Text-to-speech synthesis techniques for MIDI-to-audio synthesis [7].** The study builds piano MIDI-to-audio systems from Tacotron and neural source-filter waveform models and finds that training Tacotron with MIDI filter bank spectrograms as output reduced alignment errors from $21\%$ with Mel spectrograms to $3\%$ [7]; it validates system quality with a crowdsourced listening test collecting mean-opinion-score ratings from 224 unique listeners over 20 systems [7]. The transferable point is the pairing of an objective architectural substitution (one feature representation for another) with a measured, comparable evaluation protocol; Section 7 proposes the analogous minimal measurement protocol for radix selection, in which two radix implementations of the same index are compared under a fixed composite definition.

**Uncertainty quantification study of a re-entry breakup [8].** The work models a breakup-recorder capsule during atmospheric re-entry as a rigid body undergoing collisions, using binary-search time-of-impact calculation, PGS-LCP collision resolution, and split-impulse stabilisation, and concludes from the chaotic behaviour of the REBR capsule during the ATV3 re-entry that a bouncing-inside-the-bay hypothesis is feasible [8]. Its method—propagating severe input uncertainty through a model to obtain a map of outcomes rather than a single prediction—is the template for the weight-sensitivity analysis of Section 4.5, which propagates uncertainty in the weight $\beta$ into a precise switching threshold $\beta^{*}=2.286$ instead of a single point recommendation.

**The predecessor framework [9].** The predecessor paper states the same resource functionals and reports the continuous traversal-only optimum $q=e\approx2.718$, the exact integer optimum $q=4$ with $F_{1,1}(4)=4.2289$ for $N=10^{6}$ under equal weights, the padded-storage confirmation $F^{\mathrm{pad}}_{1,1}(4)=4.2937$, the threshold $\beta^{*}=2.286$, and an asymptotic composite optimum quoted as $q\approx3.65$ [9]. The present revision reproduces every one of those numbers by shown arithmetic and corrects the asymptotic derivation, whose published intermediate value $3.4956$ does not follow from the derivative values the paper itself reports (Section 4.6).

**Positional notation as an intrinsic ultrametric valuation [10].** The work formalizes the $b$-adic valuation and ultrametric distance carried by digit strings, enumerates exact distance frequencies for decimal integers up to three digits, and computes for two-digit decimals a total of $4{,}950$ unordered pairs of which $450$ share the same last digit, with the ratio of the ultrametric mean distance $\bar d_{10}=101/110\approx0.918$ to the normalized Euclidean mean $\bar d_{\mathrm{Euc}}=101/297\approx0.340$ equal to $2.70$ [10]. This establishes that the tree hierarchy underlying a radix choice is intrinsic to positional representation rather than an artifact, which is the mathematical reason the radix $q$ is a genuine design variable: changing $q$ changes the intrinsic ultrametric geometry of the collection, not merely an implementation detail. [10] also poses, as an open question, whether the $b$-adic ultrametric can be leveraged for radix trees with provable performance guarantees; the present paper answers a restricted version of that question for the specific cost functionals of Section 3.

**Factoring, adelic complexity, and the silent-radix principle [11].** The paper develops the observation that no positional numeral specifies its own base—the silent radix—into a hidden-modulus cryptographic program, and reports experimental verification in which the GCD-based modulus-recovery rate falls from $1.00$ at noise level $t=0$ to $0.07$ at $t=1$ and $0.00$ at $t\geq2$, with archimedean noise $\approx2^{80}$ against ultrametric noise $p^{-4}\approx2^{-80}$ at $t=4$ [11]. Two points carry over. First, the radix is a silent parameter of any positional system, so it must be fixed by explicit analysis of the kind performed here rather than read off the data. Second, [11] demonstrates the pattern of validating each analytic claim by a targeted computational check at toy scale; the falsification experiment proposed in Section 7(c) follows that pattern for the radix-selection rule.

**Functoriality as a transform [12].** The paper computes, for a finite adelic toy register with $S=\{2,3,5\}$ and $k_p=4$, a structured stage count $C_{\mathrm{str}}=2888$ against a dense non-recursive baseline $C_{\mathrm{naive}}=6.561\times10^{11}$, a separation factor $\approx2.27\times10^{8}$, and states explicitly that these are theorems about a toy model while the claim that the structured transform reproduces Hecke eigenvalues is a conjecture with a stated falsification condition [12]. This is the closest methodological sibling to the present paper: both compare a structured hierarchical cost against a baseline on exactly computable models, both keep the claims narrow, and both attach a falsification condition to the headline number. The separation-factor style of reporting (structured cost divided by baseline cost) is echoed here in the ratio $F_{1,1}(2)/F_{1,1}(4)=4.8956/4.2289\approx1.158$ computed in Section 4.3, which quantifies the penalty of the binary default.

## 3. Methods

### 3.1 Setup

Let $N$ be the number of items to organize, and let the ultrametric representation be a rooted $q$-ary tree with all leaves at depth $n$. The depth is

$$
n(q)=\left\lceil\frac{\ln N}{\ln q}\right\rceil .
$$

Internal nodes at level $k$ (root at $k=0$) number $N/q^{\,n-k}$; summing over levels gives

$$
\begin{aligned}
I(q) &=\sum_{k=0}^{n-1}\frac{N}{q^{\,n-k}}
      =N\sum_{j=1}^{n}\frac{1}{q^{\,j}}
      =N\,\frac{q^{-1}\bigl(1-q^{-n}\bigr)}{1-q^{-1}}
      =\frac{N\bigl(1-q^{-n}\bigr)}{q-1}
      \le\frac{N}{q-1},
\end{aligned}
$$

where the inequality holds because $q^{-n}>0$.

### 3.2 Resource functionals

1. **Storage.** Each internal node stores $q$ child pointers, so total pointer storage is

$$
S(q)=q\,I(q)=\frac{qN\bigl(1-q^{-n}\bigr)}{q-1}.
$$

2. **Traversal.** A lookup descends $n$ levels, comparing up to $q$ children at each level, giving the worst-case comparison count

$$
T(q)=q\,n(q)=q\left\lceil\frac{\ln N}{\ln q}\right\rceil .
$$

3. **Interconnection.** Each internal node has $q$ child links plus one parent link, so the maximum node degree is

$$
D(q)=q+1 .
$$

### 3.3 Composite objective

We minimize the weighted, normalized composite

$$
F_{\alpha,\beta}(q)=\alpha\,\frac{S(q)}{N}+\beta\,\frac{T(q)}{T_{\mathrm{ref}}},
$$

where $T_{\mathrm{ref}}=\ln N$ normalizes traversal cost. The monotone increase of $D(q)$ with $q$ is folded into the storage term: a node of degree $q+1$ must at minimum address its $q$ children, so storage and fan-out move together and a single weight $\alpha$ covers both, an assumption listed in Section 6.

### 3.4 Continuous relaxation

Dropping the ceiling, the traversal term reduces to $q/\ln q$. Minimizing

$$
f(q)=\frac{q}{\ln q},\qquad q>1,
$$

gives

$$
f'(q)=\frac{\ln q-1}{(\ln q)^{2}}=0\;\Longrightarrow\;\ln q=1\;\Longrightarrow\;q=e\approx2.718 .
$$

Since $f''(e)=1/e>0$, $q=e$ is the unique minimum of the traversal component alone.

### 3.5 Method summary

The method is purely analytical: (i) closed-form derivation of the continuous traversal-only optimum; (ii) exact integer evaluation of $F_{\alpha,\beta}(q)$ for $q\in\{2,3,4,5\}$ at $N=10^{6}$; (iii) solution of weight-equality conditions to locate optimum-switch thresholds; and (iv) an asymptotic composite optimum check, in which the derivative of the relaxed composite is evaluated at $q=3$ and $q=4$ and the root is located by linear interpolation, with the interpolation arithmetic shown in full and cross-checked. No experiment, measurement, or simulation is performed; every number in Section 4 follows from the stated inputs by shown arithmetic.

## 4. Analysis

All input numbers are stated with their source; every arithmetic step is shown.

### 4.1 Input numbers

- $N=10^{6}$ (reference workload, an assumption of the analysis).
- $\ln 2=0.693147$, $\ln 3=1.098612$, $\ln 4=1.386294$, $\ln 5=1.609438$, $\ln 10^{6}=13.815511$ (standard logarithm values to six decimals).
- Reference weights $\alpha=1$, $\beta=1$ (equal weighting, an assumption).
- $T_{\mathrm{ref}}=\ln N=13.815511$.

### 4.2 Depth and traversal for each integer radix

Compute the raw ratio $\ln N/\ln q$:

$$
\begin{aligned}
\frac{13.815511}{0.693147}&=19.931574 &&(q=2),\\
\frac{13.815511}{1.098612}&=12.575423 &&(q=3),\\
\frac{13.815511}{1.386294}&=9.965787 &&(q=4),\\
\frac{13.815511}{1.609438}&=8.584059 &&(q=5).
\end{aligned}
$$

Applying the ceiling:

$$
n(2)=20,\qquad n(3)=13,\qquad n(4)=10,\qquad n(5)=9 .
$$

Traversal costs $T(q)=q\,n(q)$:

$$
T(2)=2\times20=40,\quad
T(3)=3\times13=39,\quad
T(4)=4\times10=40,\quad
T(5)=5\times9=45 .
$$

Normalized traversal $T(q)/T_{\mathrm{ref}}$:

$$
\frac{40}{13.815511}=2.8956,\qquad
\frac{39}{13.815511}=2.8227,\qquad
\frac{45}{13.815511}=3.2575 .
$$

(The $q=2$ and $q=4$ values are identical because $T(2)=T(4)=40$.)

### 4.3 Storage and composite score (unpadded)

Compute $q^{-n}$ using $q^{-n}=e^{-n\ln q}$ and the logarithms of Section 4.1:

$$
\begin{aligned}
2^{-20}&=e^{-20\times0.693147}=e^{-13.862940}\approx9.54\times10^{-7},\\
3^{-13}&=e^{-13\times1.098612}=e^{-14.281956}\approx6.27\times10^{-7},\\
4^{-10}&=e^{-10\times1.386294}=e^{-13.862940}\approx9.54\times10^{-7},\\
5^{-9}&=e^{-9\times1.609438}=e^{-14.484942}\approx5.12\times10^{-7}.
\end{aligned}
$$

Because each $q^{-n}<10^{-6}$, the factor $1-q^{-n}$ exceeds $0.999999$ and does not affect the fourth decimal place. Inserting into the storage-per-item expression $S(q)/N=q(1-q^{-n})/(q-1)$:

$$
\begin{aligned}
\frac{S(2)}{N}&=\frac{2(1-9.54\times10^{-7})}{1}=2.0000,\\
\frac{S(3)}{N}&=\frac{3(1-6.27\times10^{-7})}{2}=1.5000,\\
\frac{S(4)}{N}&=\frac{4(1-9.54\times10^{-7})}{3}=1.3333,\\
\frac{S(5)}{N}&=\frac{5(1-5.12\times10^{-7})}{4}=1.2500.
\end{aligned}
$$

Composite $F_{1,1}(q)=S(q)/N+T(q)/T_{\mathrm{ref}}$:

$$
\begin{aligned}
F_{1,1}(2)&=2.0000+2.8956=4.8956,\\
F_{1,1}(3)&=1.5000+2.8227=4.3227,\\
F_{1,1}(4)&=1.3333+2.8956=4.2289,\\
F_{1,1}(5)&=1.2500+3.2575=4.5075.
\end{aligned}
$$

**Result:** $q=4$ minimizes $F_{1,1}$ under equal weighting. The binary default carries a penalty factor of $F_{1,1}(2)/F_{1,1}(4)=4.8956/4.2289=1.1576$, i.e. about $15.8\%$ higher composite cost than the optimum.

### 4.4 Padding overhead

The tree must contain $q^{n}$ leaves; the padding fraction is

$$
\phi(q)=\frac{q^{n}-N}{N}.
$$

Compute $q^{n}$:

$$
\begin{aligned}
2^{20}&=1{,}048{,}576 \;\Rightarrow\; \phi(2)=\frac{1{,}048{,}576-1{,}000{,}000}{10^{6}}=0.048576,\\
3^{13}&=1{,}594{,}323 \;\Rightarrow\; \phi(3)=\frac{1{,}594{,}323-1{,}000{,}000}{10^{6}}=0.594323,\\
4^{10}&=1{,}048{,}576 \;\Rightarrow\; \phi(4)=0.048576,\\
5^{9}&=1{,}953{,}125 \;\Rightarrow\; \phi(5)=0.953125.
\end{aligned}
$$

Effective storage with padding counts all $q^{n}$ leaves, giving

$$
\frac{S_{\mathrm{eff}}(q)}{N}= \frac{q\,q^{n}}{N\,(q-1)}.
$$

Evaluating:

$$
\begin{aligned}
\frac{S_{\mathrm{eff}}(2)}{N}&=\frac{2\times1{,}048{,}576}{10^{6}\times1}=2.097152,\\
\frac{S_{\mathrm{eff}}(3)}{N}&=\frac{3\times1{,}594{,}323}{10^{6}\times2}=2.391485,\\
\frac{S_{\mathrm{eff}}(4)}{N}&=\frac{4\times1{,}048{,}576}{10^{6}\times3}=1.398101,\\
\frac{S_{\mathrm{eff}}(5)}{N}&=\frac{5\times1{,}953{,}125}{10^{6}\times4}=2.441406.
\end{aligned}
$$

Padded composite $F^{\mathrm{pad}}_{1,1}(q)=S_{\mathrm{eff}}(q)/N+T(q)/T_{\mathrm{ref}}$:

$$
\begin{aligned}
F^{\mathrm{pad}}_{1,1}(2)&=2.0972+2.8956=4.9928,\\
F^{\mathrm{pad}}_{1,1}(3)&=2.3915+2.8227=5.2142,\\
F^{\mathrm{pad}}_{1,1}(4)&=1.3981+2.8956=4.2937,\\
F^{\mathrm{pad}}_{1,1}(5)&=2.4414+3.2575=5.6989.
\end{aligned}
$$

**Result:** $q=4$ remains optimal under padded storage, with $F^{\mathrm{pad}}_{1,1}(4)=4.2937$.

### 4.5 Weight sensitivity ("breakup map")

Set $\alpha=1$ and solve $F_{1,\beta}(3)=F_{1,\beta}(4)$:

$$
\begin{aligned}
1.5000+\beta\cdot2.8227 &= 1.3333+\beta\cdot2.8956\\
1.5000-1.3333 &= \beta\,(2.8956-2.8227)\\
0.1667 &= 0.0729\,\beta\\
\beta^{*} &= \frac{0.1667}{0.0729}=2.286 .
\end{aligned}
$$

Thus:

- $\beta<2.286$: $q=4$ optimal.
- $\beta>2.286$: $q=3$ optimal.

Comparisons against $q=2$, using the unpadded values of Section 4.3:

$$
\begin{aligned}
F(2)-F(3)&=(2.0000-1.5000)+\beta\,(2.8956-2.8227)=0.5000+0.0729\,\beta>0\quad\forall\,\beta>0,\\
F(2)-F(4)&=(2.0000-1.3333)+\beta\,(2.8956-2.8956)=0.6667>0\quad\forall\,\beta,\\
F(2)-F(5)&=(2.0000-1.2500)+\beta\,(2.8956-3.2575)=0.7500-0.3619\,\beta>0\;\text{iff}\;\beta<2.072 .
\end{aligned}
$$

Hence $q=2$ is never optimal for any $\beta>0$: it is dominated by $q=3$ and $q=4$ at every positive traversal weight, and by $q=5$ once $\beta$ exceeds $2.072$.

### 4.6 Asymptotic composite optimum (corrected)

For large $N$, the ceiling vanishes and $T(q)/\ln N\to q/\ln q$, while $S(q)/N\to q/(q-1)$. The composite derivative is

$$
\frac{d}{dq}\!\left[\alpha\frac{q}{q-1}+\beta\frac{q}{\ln q}\right]
= -\frac{\alpha}{(q-1)^{2}}+\beta\,\frac{\ln q-1}{(\ln q)^{2}} .
$$

Setting $\alpha=\beta=1$ and solving $-\frac{1}{(q-1)^{2}}+\frac{\ln q-1}{(\ln q)^{2}}=0$ yields a root between $3$ and $4$. Evaluating the derivative at $q=3$ and $q=4$ with the logarithms of Section 4.1:

$$
\begin{aligned}
\text{At }q=3:&\quad -\frac{1}{(3-1)^{2}}+\frac{1.098612-1}{(1.098612)^{2}}
= -0.250000+ \frac{0.098612}{1.206948}\\
&\quad= -0.250000+0.081710=-0.168290,\\[4pt]
\text