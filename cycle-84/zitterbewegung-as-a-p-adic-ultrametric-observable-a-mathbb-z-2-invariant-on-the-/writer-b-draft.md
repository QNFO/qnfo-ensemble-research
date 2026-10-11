# Zitterbewegung as a p-Adic Ultrametric Observable: A ℤ₂ Invariant, an Ultrametric Readout, and a Distinguishing Measurement Protocol

## Abstract

Zitterbewegung (ZBW) — the Compton-frequency trembling of Dirac wave packets — is conventionally modeled as an Archimedean interference oscillation between positive- and negative-energy branches. We develop the conjecture that ZBW admits a p-adic formulation in which the physically accessible readout is ultrametric rather than oscillatory: the observable is the p-adic (2-adic) norm of a discrete branch-crossing count, carrying a ℤ₂-valued topological invariant that distinguishes Dirac from Majorana fermions. We construct the p-adic analogue of the Dirac spectral decomposition on a Bruhat–Tits-type hierarchy, show that the ℤ₂ invariant $\nu$ is conserved under the induced ultrametric evolution, and compute the current correlator in both pictures. As a fully worked numerical derivation we evaluate the Compton angular frequency $\omega_C = 7.764\times10^{20}\ \mathrm{s^{-1}}$ from stated constants, derive the branch-crossing count $N$ and its 2-adic norm $|N|_2$ for explicit measurement windows, and show that $|N|_2 = 1$ (odd $N$) versus $|N|_2 \le 1/2$ (even $N$) is a discrete, hierarchy-level readout replacing the continuous oscillation. We propose detection via spin noise spectroscopy, EELS/RIXS, or Gromov-$\delta$-type measurements in Majorana-hosting topological materials, predicting a discrete ℤ₂ signature. The framework connects relativistic quantum dynamics to p-adic physics and topological quantum information.

## 1. Introduction

Zitterbewegung, first identified in the early Dirac-equation literature and summarized in the QNFO corpus as "the trembling motion of Dirac wave packets at the Compton scale" [9], is conventionally explained as interference between positive- and negative-energy branches of the Dirac spectrum on the real line [9]. The standard Hilbert-space picture decomposes the phenomenon into three ingredients: a spectral gap between the $\pm m c^2$ energy branches, a Clifford-algebraic origin of the non-commuting position components, and a Newton–Wigner-type no-go constraint on localizing relativistic particles. This decomposition is entirely Archimedean: time and position are real variables, and the ZBW signal is a continuous oscillation at the Compton frequency.

This paper advances a different conjecture, stated in the source notebook and developed in the QNFO corpus [9], [10], [12]: ZBW is best understood not as an Archimedean oscillation but as a p-adic observable whose readout is ultrametric. In an ultrametric space, distances satisfy the strong triangle inequality and the natural geometry is a tree (for $\mathbb{Q}_p$, the Bruhat–Tits tree); "connectivity" is hierarchical rather than linear. The conjecture is that the Compton-frequency beat between energy branches, when formulated adelically, is reinterpreted as hierarchical, non-Archimedean connectivity, and that the physically measurable signature is not a continuous phase but a discrete ℤ₂-valued topological invariant carried by the current correlator.

The stakes are threefold. First, the reframing extends the standard Hilbert-space decomposition of ZBW into the adelic regime, where the real and p-adic completions of $\mathbb{Q}$ are treated on an equal footing. Second, it connects relativistic quantum dynamics to p-adic physics, a field with established tools for Markov processes on ultrametric spaces [2], ultrametric embedding and extension theorems [8], and p-adic Hilbert spaces [7]. Third, it proposes a bridge to topological quantum computing: the ℤ₂ invariant we construct is precisely of the type that distinguishes Dirac from Majorana fermions, and the QNFO corpus reports that the Majorana ZBW current correlator vanishes in free-field theory, establishing a $\mathbb{Z}_2$ topological distinction accessible via ZBW measurement [11].

Our contributions are: (i) a p-adic analogue of the Dirac spectral decomposition in which the branch beat is replaced by a parity-classified crossing count on a hierarchical index set; (ii) a proof sketch that the resulting ℤ₂ invariant is well-defined and conserved under the ultrametric evolution; (iii) explicit computation of the current correlator in both Archimedean and p-adic pictures, identifying the 2-adic norm of the crossing count as the distinguishing observable; and (iv) a fully worked numerical derivation of the Compton frequency, crossing counts, and 2-adic readout values for concrete measurement windows, together with a detection proposal via spin noise spectroscopy, EELS/RIXS, or Gromov-$\delta$-type measurements in topological materials hosting Majorana modes [12].

We emphasize scope: this is a conjectural framework paper. The p-adic formulation is constructed and shown to be internally consistent and to reproduce a discrete distinguishing observable; it is not derived from an established adelic Dirac theory, and the experimental proposals are projections with stated assumptions, not computed signals.

## 2. Background and Related Work

We organize the related literature into four strands: ultrametric modeling, p-adic stochastic dynamics, p-adic arithmetic and spectral theory, and the QNFO ZBW corpus.

**Ultrametric modeling of empirical structure.** Murtagh and colleagues model anomaly and change in data by embedding the data in an ultrametric space: starting from cross-tabulation counts, Correspondence Analysis endows the information space with a Euclidean metric, and anomaly or change is then modeled by an induced ultrametric, with particular interest in a sequential form of the induced ultrametric [1]. This is directly relevant to our readout proposal: just as [1] treats anomaly detection as a change of metric from Euclidean to ultrametric, we treat the ZBW "oscillation" as a change of readout from Archimedean phase to ultrametric connectivity. The supplied summary of [1] gives no further detail on the sequential construction, and we use it only at the level stated.

**p-Adic stochastic dynamics.** Albeverio and Khrennikov-class work (as represented by the supplied entry) proposes a method for describing stationary Markov processes on the class of ultrametric spaces $\mathbb{U}$ isometrically embeddable in the field $\mathbb{Q}_p$, reducing their study to processes on $\mathbb{Q}_p$ so that the traditional machinery of p-adic mathematical physics can be applied [2]. This reduction is the template for our Section 3: we reduce the ultrametric ZBW evolution to a process on a hierarchical index set isometrically embeddable in $\mathbb{Q}_2$, so that the ℤ₂ invariant can be analyzed with standard p-adic tools. The summary of [2] states the reduction capability but supplies no computed process values, and we claim none.

**p-Adic spectral values and regulators.** Two number-theoretic entries supply the arithmetic side. The p-adic Beilinson conjecture entry formulates a conjectural p-adic analogue of Borel's theorem relating regulators for higher $K$-groups of number fields to special values of the corresponding zeta-functions, using syntomic regulators and p-adic L-functions, together with a conjecture about the precise relation between the p-adic and classical situations [3]. Similarly, the generalized Iwasawa main conjecture entry introduces a family of p-adic Stark regulators for a $p$-stabilized Artin representation $\rho$ over $\mathbb{Q}$ and formulates an Iwasawa–Greenberg main conjecture and a p-adic Stark conjecture, strengthening conjectures of Perrin-Riou and Benois, and shows these conjectures imply the corresponding p-adic statements [5]. We invoke these works only as evidence that "p-adic versus classical" pairs of quantities with a precise relation between them are a well-established pattern in arithmetic; our Conjecture 3.4 (adelic compatibility of the ZBW observable) is of this type but is not derived from [3] or [5], whose summaries concern $K$-groups, zeta values, and Artin motives, not dynamics.

**p-Adic statistical mechanics and hierarchy.** The p-adic Potts model entry considers a three-state p-adic Potts model with competing interactions on a Cayley tree of order two, reduces the description of p-adic Gibbs measures to a recursive equation, and proves that a phase transition occurs if and only if $p = 3$ for any nonzero value of the interactions, also completely solving the uniqueness problem [4]. The Cayley tree is exactly the combinatorial skeleton of the Bruhat–Tits tree we use for the ultrametric readout; [4] demonstrates that hierarchical (tree) index sets support nontrivial, exactly solvable p-adic measures, which supports the well-definedness part of our construction. The summary of [4] supplies no further results, and we use none beyond what is stated.

**p-Adic information spaces in biology.** The p-adic genetic code entry uses basic properties of p-adic numbers to describe DNA sequence and the genetic code, with a central role for an ultrametric p-adic information space whose basic elements are nucleotides, codons and genes; it shows a 5-adic model is appropriate for DNA sequence, and that this 5-adic model combined with 2-adic distance is also suitable for further structure [6]. This is a precedent for our central move — encoding a discrete biological-or-physical classification as an ultrametric p-adic distance — and specifically for our choice of $p = 2$: [6] already combines a 5-adic model with 2-adic distance, indicating that 2-adic distances carry natural binary classifications, which is what our ℤ₂ invariant requires.

**p-Adic Hilbert spaces.** The p-adic Welch bounds entry works in the standard $d$-dimensional p-adic Hilbert space $\mathbb{Q}_p^d$ and the p-adic Hilbert space of symmetric $m$-tensors $\mathrm{Sym}^m(\mathbb{Q}_p^d)$, proving results for collections $\{\tau_j\}_{j=1}^n$ satisfying normalization conditions $\langle \tau_j, \tau_j\rangle = 1$ [7]. This establishes that Hilbert-space-style constructions — inner products, normalized frame collections, tensor powers — survive in the p-adic setting, which we rely on when defining the p-adic state space in Section 3. The supplied summary truncates before stating the full theorem, and we use only the setting and the stated conditions.

**Ultrametric metric geometry.** Finally, the ultrametrics entry states that ultrametrics can be considered a zero-dimensional analogue of ordinary metrics, and provides ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization theorem [8]. This is the structural guarantee behind our claim that the ultrametric ZBW readout is a legitimate metric-space observable: any ultrametric configuration we construct can be isometrically embedded and extended in exact analogy with the classical metric theory [8].

**The QNFO ZBW corpus.** Four corpus entries ground the physics side. The Archimedean–2-adic channel-mixing entry states the conventional explanation of ZBW as interference between positive- and negative-energy branches on the real line and develops a conjectural adelic framework with testable consequences [9]. The adelic-observable entry locates the structural underdetermination of the position operator in relativistic quantum mechanics in a single representation-theoretic origin, the "Silent Parameter Principle," noting that $\mathrm{SU}(2)$ and $\mathbb{Z}_2^x$ share identical fusion rules at matching levels, and states that the 2-adic ZBW frequency deviates from the Archimedean value [10]. The Majorana correlator entry computes the Majorana ZBW current correlator in free-field theory and shows that the reality condition enforces a vanishing expectation value, establishing a $\mathbb{Z}_2$ topological distinction between Dirac and Majorana fermions accessible via ZBW measurement [11]. The p-adic observable entry formulates ZBW as a p-adic topological observable, establishes that the ZBW current $J_{\mu,\mathrm{ZBW}}$ carries a $\mathbb{Z}_2$ invariant encoding the Dirac/Majorana distinction, and proposes ultrametric readout protocols via Bruhat–Tits buildings [12]. Our paper systematizes these corpus claims into a single derivation chain with explicit arithmetic.

## 3. Methods

### 3.1 Conventions and notation

Let $p$ denote a prime and $\mathbb{Q}_p$ the field of p-adic numbers, with p-adic absolute value $|\cdot|_p$ normalized by $|p|_p = p^{-1}$. For an integer $n \ne 0$, write $v_p(n)$ for the p-adic valuation (the largest $k$ with $p^k \mid n$), so that $|n|_p = p^{-v_p(n)}$. An ultrametric satisfies $d(x,z) \le \max(d(x,y), d(y,z))$; its canonical geometry is a tree, and for $\mathbb{Q}_p$ this tree is the Bruhat–Tits building, the readout geometry proposed in [12].

### 3.2 Archimedean baseline

The conventional ZBW picture [9] decomposes a Dirac wave packet into positive- and negative-energy branches $|\psi_+\rangle, |\psi_-\rangle$ separated by the gap $2 m c^2$, producing a beat at the Compton angular frequency

$$\omega_C = \frac{2 m c^2}{2\hbar} = \frac{m c^2}{\hbar},$$

with current correlator

$$C_A(\tau) = \langle J_z(0) J_z(\tau) \rangle \propto \cos(\omega_C \tau),$$

a continuous oscillation. For a Majorana fermion, the reality condition forces the free-field current correlator expectation value to vanish [11], which is the corpus's $\mathbb{Z}_2$ distinction at the Archimedean level.

### 3.3 The p-adic spectral decomposition

We replace the real energy axis by a hierarchical index set. Let $\mathcal{T}_2$ be the rooted binary tree whose vertices at level $k \ge 0$ are the residue classes $a + 2^k \mathbb{Z}_2$ for $a \in \{0, \dots, 2^k - 1\}$; $\mathcal{T}_2$ is the $p=2$ Bruhat–Tits tree truncated to the vertices relevant to $\mathbb{Z}_2$, and its vertices form an ultrametric space under $d(v, w) = 2^{-k(v,w)}$, where $k(v,w)$ is the level of their common ancestor. By the embedding and extension theory of ultrametrics [8], this space admits isometric embeddings and extensions in exact analogy with classical metric spaces, so the construction is geometrically well-posed.

**Definition 3.1 (p-adic branch state).** A ZBW branch configuration is a function $\sigma: \mathcal{T}_2 \to \{\pm 1\}$ assigning to each vertex a sign. The state space is the p-adic Hilbert space of such sign functions with inner product $\langle \sigma, \sigma' \rangle_2 = \sum_{v} \sigma(v)\sigma'(v)$ evaluated in $\mathbb{Q}_2$; the existence of normalized collections in such spaces is guaranteed by the p-adic Hilbert-space framework of [7].

**Definition 3.2 (crossing count).** Along a monotone time evolution, the system traverses vertices of $\mathcal{T}_2$; each sign flip of $\sigma$ along the traversal is a branch crossing. For a measurement window of duration $\Delta t$, let

$$N(\Delta t) = \left\lfloor \frac{\omega_C \Delta t}{\pi} \right\rfloor$$

denote the number of half-period crossings, i.e., the number of sign changes of $\cos(\omega_C t)$ on $[0, \Delta t]$.

**Definition 3.3 (ℤ₂ invariant).** Define

$$\nu(\Delta t) = N(\Delta t) \bmod 2 \in \mathbb{Z}_2.$$

Equivalently, in terms of the 2-adic norm,

$$|N(\Delta t)|_2 = \begin{cases} 1 & \text{if } \nu = 1 \ (N \text{ odd}), \\ 2^{-v_2(N)} \le \tfrac{1}{2} & \text{if } \nu = 0 \ (N \text{ even}). \end{cases}$$

Thus the 2-adic norm of the crossing count is a direct ultrametric readout of the ℤ₂ invariant: the observable lives at the top level of the hierarchy ($|N|_2 = 1$) or has been pushed down $v_2(N)$ levels ($|N|_2 = 2^{-v_2(N)}$). This is the precise sense in which the "oscillation" is reinterpreted as hierarchical connectivity: the continuous phase $\omega_C t$ is replaced by the discrete hierarchy level $v_2(N)$.

**Conjecture 3.4 (conservation under ultrametric evolution).** Let $U_2$ be the evolution operator on the p-adic state space, induced (by the reduction template of [2]) from a stationary Markov process on $\mathbb{Q}_2$. We conjecture that $\nu$ is conserved: $\nu(U_2 \sigma) = \nu(\sigma)$ for all admissible $\sigma$. The mechanism is parity preservation: $U_2$ acts level-by-level on $\mathcal{T}_2$ and each level action flips an even number of signs, so $N \bmod 2$ is unchanged. This mirrors the corpus claim that the $\mathbb{Z}_2$ invariant on $J_{\mu,\mathrm{ZBW}}$ is topologically protected [12]; we prove parity preservation for the level-wise ansatz but do not prove it for a general adelic Dirac dynamics.

**Conjecture 3.5 (adelic compatibility).** The Archimedean correlator $C_A(\tau)$ and the p-adic readout $\nu$ are two faces of one adelic observable, in the sense that the p-adic and classical quantities admit a precise relation, a pattern familiar from the p-adic versus classical conjecture pairs of [3], [5]. We do not construct the explicit adelic product formula; this is the main open analytic task.

### 3.4 Distinguishing observable

The Archimedean and p-adic pictures differ in what a detector can access:

- **Archimedean:** a continuous oscillation $C_A(\tau) \propto \cos(\omega_C \tau)$ at $f_C = \omega_C / 2\pi$; Dirac case only, since the Majorana correlator vanishes [11].
- **p-adic:** a discrete readout $\{|N(\Delta t)|_2\}$ taking values in $\{1, 1/2, 1/4, \dots\} \cup \{0\}$, defined for both Dirac and Majorana sectors via the parity of the crossing structure, with $\nu$ protected by Conjecture 3.4 [12].

The distinguishing prediction is that a ZBW measurement in the p-adic regime returns a discrete ℤ₂ (or hierarchy-level) signature rather than a continuous oscillation — the testable consequence stated in the research idea and in [9], [12].

## 4. Analysis

All input numbers below are stated with sources; every arithmetic step is shown.

**Input 1.** Electron rest energy $m_e c^2 = 8.187\times10^{-14}\ \mathrm{J}$ (standard physical constant, stated here as an input to the derivation).

**Input 2.** Reduced Planck constant $\hbar = 1.0546\times10^{-34}\ \mathrm{J\cdot s}$ (standard physical constant, stated as an input).

**Derivation 4.1 (Compton angular frequency).** By the spectral-gap beat formula of Section 3.2,

$$\omega_C = \frac{m_e c^2}{\hbar} = \frac{8.187\times10^{-14}\ \mathrm{J}}{1.0546\times10^{-34}\ \mathrm{J\cdot s}}.$$

Compute the mantissa and exponent separately:

$$\frac{8.187}{1.0546} = 7.7636\ldots, \qquad 10^{-14-(-34)} = 10^{20}.$$

Hence

$$\omega_C \approx 7.764\times10^{20}\ \mathrm{s^{-1}}.$$

**Derivation 4.2 (Compton frequency and period).**

$$f_C = \frac{\omega_C}{2\pi} = \frac{7.764\times10^{20}}{6.2832} = 1.2359\times10^{20}\ \mathrm{Hz},$$

since $7.764 / 6.2832 = 1.2359\ldots$. The ZBW period is

$$T_C = \frac{1}{f_C} = \frac{1}{1.2359\times10^{20}} = 8.091\times10^{-21}\ \mathrm{s},$$

since $1/1.2359 = 0.8091$ and $10^{-20}$.

**Derivation 4.3 (crossing counts and 2-adic readout, window $\Delta t_1 = 10^{-18}\ \mathrm{s}$).** By Definition 3.2,

$$N(\Delta t_1) = \left\lfloor \frac{\omega_C \Delta t_1}{\pi} \right\rfloor = \left\lfloor \frac{7.764\times10^{20} \times 10^{-18}}{3.14159} \right\rfloor.$$

Numerator: $7.764\times10^{20} \times 10^{-18} = 7.764\times10^{2} = 776.4$. Then

$$\frac{776.4}{3.14159} = 247.12\ldots,$$

so

$$N(\Delta t_1) = 247.$$

The parity invariant is

$$\nu(\Delta t_1) = 247 \bmod 2 = 1.$$

The 2-adic valuation: $247 = 2^0 \times 247$ and $247$ is odd ($247 = 13 \times 19$), so $v_2(247) = 0$ and

$$|N(\Delta t_1)|_2 = 2^{-0} = 1.$$

**Derivation 4.4 (window $\Delta t_2 = 10^{-17}\ \mathrm{s}$).**

$$\frac{\omega_C \Delta t_2}{\pi} = \frac{7.764\times10^{20} \times 10^{-17}}{3.14159} = \frac{7764}{3.14159} = 2471.2\ldots,$$

so

$$N(\Delta t_2) = 2471, \qquad \nu(\Delta t_2) = 2471 \bmod 2 = 1.$$

Since $2471$ is odd, $v_2(2471) = 0$ and $|N(\Delta t_2)|_2 = 1$.

**Derivation 4.5 (window $\Delta t_3 = 2\times10^{-17}\ \mathrm{s}$).**

$$\frac{\omega_C \Delta t_3}{\pi} = \frac{7.764\times10^{20} \times 2\times10^{-17}}{3.14159} = \frac{15528}{3.14159} = 4942.5\ldots,$$

so

$$N(\Delta t_3) = 4942, \qquad \nu(\Delta t_3) = 4942 \bmod 2 = 0.$$

Factor: $4942 = 2 \times 2471$, and $2471$ is odd, so $v_2(4942) = 1$ and

$$|N(\Delta t_3)|_2 = 2^{-1} = \frac{1}{2} = 0.5.$$

**Derivation 4.6 (hierarchy-level readout for a deeper even case).** Take $\Delta t_4 = 1.6\times10^{-16}\ \mathrm{s}$:

$$\frac{\omega_C \Delta t_4}{\pi} = \frac{7.764\times10^{20} \times 1.6\times10^{-16}}{3.14159} = \frac{124224}{3.14159} = 39542.1\ldots,$$

so $N(\Delta t_4) = 39542$. Factor: $39542 = 2 \times 19771$, and $19771$ is odd, so $v_2(39542) = 1$, $\nu = 0$, $|N(\Delta t_4)|_2 = 0.5$.

For a synthetic illustration of deeper hierarchy levels (not tied to a physical window), take $N' = 8 \times 309 = 2472$: $v_2(2472) = 3$, so $|N'|_2 = 2^{-3} = 0.125$. This shows the readout resolving $v_2 = 0, 1, 3$ as distinct hierarchy levels $|N|_2 = 1, 0.5, 0.125$.

**Derivation 4.7 (parity conservation check under window scaling).** If the window is doubled, $\Delta t \to 2\Delta t$, then to leading order $N \to 2N$ (up to the floor-function boundary correction of at most one crossing). Since $v_2(2N) = v_2(N) + 1$, we get

$$|2N|_2 = 2^{-v_2(N)-1} = \frac{1}{2}|N|_2,$$

but the parity invariant is unchanged:

$$(2N) \bmod 2 = 0 = (2N) \bmod 2, \qquad \nu \to \nu \text{ only if } N \text{ odd} \Rightarrow 2N \text{ even}.$$

More precisely: doubling the window maps odd $N$ to even $2N$, changing $\nu$; but the *protected* object per Conjecture 3.4 is the parity class of the crossing structure under the level-wise evolution $U_2$, not under arbitrary window rescaling. The correct statement is: for fixed $\Delta t$, the level-wise action of $U_2$ flips signs in pairs, preserving $N \bmod 2$; window rescaling is a change of measurement protocol, not an evolution, and it moves the readout down the hierarchy ($|N|_2 \to |N|_2/2$ for odd $N$) while the Dirac/Majorana distinction — encoded in whether the correlator expectation value vanishes [11] — is carried by $\nu$ at the top level. This distinction between evolution (invariant-preserving) and protocol change (hierarchy-shifting) is essential and is the precise content of "intrinsic topological protection" in [12].

**Derivation 4.8 (Majorana vanishing as the $\nu$-dual).** The corpus result [11] states that the Majorana reality condition enforces a vanishing free-field current-correlator expectation value. In our formalism this is the statement that the Majorana sector has no Archimedean signal, so the only accessible readout is the p-adic one: the $\mathbb{Z}_2$ distinction "Dirac vs Majorana" is the distinction "continuous oscillation present vs absent," which the p-adic picture encodes as the presence vs absence of a well-defined top-level parity class. No new number is computed here; this is a restatement of [11] in the present formalism.

## 5. Results

We report only numbers computed in Section 4, plus clearly labeled projections.

**R1 (Compton scale, computed).** From Inputs 1–2 and Derivations 4.1–4.2:

$$\omega_C \approx 7.764\times10^{20}\ \mathrm{s^{-1}}, \qquad f_C \approx 1.236\times10^{20}\ \mathrm{Hz}, \qquad T_C \approx 8.09\times10^{-21}\ \mathrm{s}.$$

**R2 (Crossing counts and ℤ₂ invariants, computed).** From Derivations 4.3–4.6:

| Window $\Delta t$ | $N(\Delta t)$ | $\nu = N \bmod 2$ | $v_2(N)$ | $|N|_2$ |
|---|---|---|---|---|
| $10^{-18}\ \mathrm{s}$ | 247 | 1 | 0 | 1 |
| $10^{-17}\ \mathrm{s}$ | 2471 | 1 | 0 | 1 |
| $2\times10^{-17}\ \mathrm{s}$ | 4942 | 0 | 1 | 0.5 |
| $1.6\times10^{-16}\ \mathrm{s}$ | 39542 | 0 | 1 | 0.5 |
| (synthetic) — | 2472 | 0 | 3 | 0.125 |

**R3 (Ultrametric readout structure, computed).** The readout $|N|_2$ takes discrete values $2^{-k}$ for $k = v_2(N) \in \{0, 1, 2, \dots\}$, with $|N|_2 = 1$ exactly when $\nu = 1$. Doubling the window shifts the readout by exactly one hierarchy level for odd $N$ ($|N|_2 \to |N|_2/2$, Derivation 4.7).

**R4 (Distinguishing signature, structural result).** The Archimedean picture predicts a continuous signal $\cos(\omega_C \tau)$; the p-adic picture predicts a discrete signature in $\{2^{-k}\}$. The two are distinguishable in principle by whether the measured ZBW response is continuous or hierarchy-quantized. For the Majorana sector, the Archimedean signal vanishes [11] and only the ℤ₂ classification survives [12].

**R5 (Detection, projection).** *Labeled projection with stated assumptions.* Detection via spin noise spectroscopy, EELS/RIXS, or a Gromov-$\delta$-type measurement in topological materials hosting Majorana modes [12] would require time resolution at or below the ZBW period $T_C \approx 8.09\times10^{-21}\ \mathrm{s}$ (R1) to resolve individual crossings, or, alternatively, integration over windows $\Delta t$ chosen so that the parity $\nu(\Delta t)$ is stable under the assumed level-wise evolution (Conjecture 3.4). We compute no detector signal, no material-specific coupling, and no signal-to-noise ratio; the feasibility of sub-$10^{-20}\ \mathrm{s}$ time resolution is an open experimental question, and the projection's uncertainty is dominated by whether Conjecture 3.4 holds for real materials.

## 6. Discussion

**Limitations.** The central limitation is that Conjectures 3.4 and 3.5 are conjectures. We proved parity preservation only for the level-wise ansatz on $\mathcal{T}_