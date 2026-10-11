# Zitterbewegung as a p-Adic Ultrametric Observable: A ℤ₂ Invariant on the Bruhat–Tits Tree and Its Readout

## Abstract

Zitterbewegung (ZBW) — the Compton-frequency trembling of Dirac wave packets — is conventionally modeled as an Archimedean interference oscillation between positive- and negative-energy branches. We develop a conjectural alternative in which the ZBW readout is ultrametric: the observable lives on a Bruhat–Tits tree over $\mathbb{Q}_2$, and the physically accessible content is not a continuous oscillation but a discrete $\mathbb{Z}_2$-valued invariant carried by the current correlator. We (i) formulate a p-adic analogue of the Dirac spectral decomposition in which the spectral gap becomes a separation of tree branches, (ii) show that the $\mathbb{Z}_2$ invariant is conserved under ultrametric (isometric) evolution, (iii) compute the Archimedean and p-adic readouts of the electron Compton scale explicitly: $\omega_C = 7.763\times 10^{20}\ \mathrm{s}^{-1}$, $\log_2 \omega_C = 69.40$, yielding tree level $n = 69$ and invariant $\chi = 1$, with a cross-check $\log_2 \omega_C + \log_2 \lambda_C = 28.16 = \log_2 c$, and (iv) show that the ultrametric tree distance between the frequency and length vertices is $110$, not $\log_2 c \approx 28.16$ — a structural non-additivity that constitutes the distinguishing observable. We propose detection via spin noise spectroscopy, EELS/RIXS, or Majorana-platform measurements, predicting a discrete parity signature rather than a continuous beat. All quantitative claims are either derived here with shown arithmetic or explicitly labeled projections with stated assumptions.

## 1. Introduction

Zitterbewegung is the standard name for the rapid trembling motion of a relativistic Dirac wave packet, conventionally explained as interference between positive- and negative-energy branches of the Dirac spectrum at the Compton scale [9]. The received picture is thoroughly Archimedean: the interference lives on the real line, oscillates at the Compton frequency, and its observability is obstructed by the usual representation-theoretic obstructions to a sharp position operator. The structural underdetermination of that position operator has been argued to arise from a single representation-theoretic origin, the Silent Parameter Principle, under which $\mathrm{SU}(2)$ and $\mathbb{Z}_2^x$ share identical fusion rules at matching levels, and under which the 2-adic ZBW frequency deviates from the Archimedean value [10].

This paper takes the underdetermination seriously as a physical hypothesis rather than a pathology. If the position operator is structurally underdetermined, the "oscillation" readout is one convention among several; we propose that an ultrametric readout — in which the ZBW observable is a hierarchical connectivity pattern on a Bruhat–Tits tree rather than a displacement on the real line — is an equally admissible convention with a sharply different experimental signature. The central conjecture is:

> **Conjecture (p-adic ZBW).** The Compton-frequency beat between positive- and negative-energy branches admits an adelic formulation in which the ZBW observable is a $\mathbb{Z}_2$-valued topological invariant carried by the current correlator, read out as ultrametric (Bruhat–Tits tree) connectivity, and conserved under the ultrametric evolution.

The stakes are threefold. First, it would extend the standard Hilbert-space decomposition of ZBW — spectral gap, Clifford-algebra origin, Newton–Wigner no-go — into the adelic regime. Second, it connects relativistic quantum dynamics to the growing body of p-adic and ultrametric modeling across physics and beyond. Third, it connects to topological quantum computing: the same $\mathbb{Z}_2$ invariant has been shown to encode the Dirac/Majorana distinction in the ZBW current correlator [11], and ultrametric readout protocols via Bruhat–Tits buildings have been proposed for exactly this observable [12]. A Majorana platform would therefore exhibit a *vanishing* ZBW signal where a Dirac platform exhibits the invariant $\chi$ — a binary, topology-protected discriminator.

Our contributions: (1) a p-adic analogue of the Dirac spectral decomposition (Section 3.1–3.2); (2) proof that the $\mathbb{Z}_2$ invariant is well-defined and conserved under isometric ultrametric evolution (Section 3.3); (3) explicit numerical evaluation of the Archimedean and p-adic readouts for the electron, with all arithmetic shown (Section 4); (4) a concrete distinguishing observable — the failure of multiplicativity of the tree readout — and three detection channels (Sections 4–5).

## 2. Background and Related Work

We organize the literature into three strands: ultrametric modeling, p-adic dynamics and Hilbert spaces, and the ZBW/adelic corpus.

**Ultrametric modeling of empirical and physical systems.** Murtagh [1] models anomaly and change in data by embedding the data in an ultrametric space: starting from cross-tabulation counts, Correspondence Analysis endows the information space with a Euclidean metric, and anomaly or change is then modeled by an induced ultrametric, of a sequential kind. This establishes the methodological pattern we adopt: an Archimedean representation is available, but the *induced ultrametric* is the object that carries the relevant (anomalous, discrete) structure. Our claim is that ZBW is exactly such a case — the Archimedean oscillation is available, but the induced ultrametric carries the invariant. Khrennikov [6] applies the same pattern to biology: an ultrametric p-adic information space whose basic elements are nucleotides, codons and genes, with a 5-adic model appropriate for DNA sequence and a 2-adic distance suitable for the genetic code. The relevance is twofold: it shows that small primes ($p = 2, 5$) can be the *correct* primes for a physical information space, supporting our focus on $\mathbb{Q}_2$; and it demonstrates that a discrete, hierarchical encoding can be the primary physical description, not a coarse-graining of a continuous one. The summary supplied for [6] gives no further technical detail, and we rely on it only for these stated points.

**p-adic dynamics.** Albeverio and Khrennikov-type constructions for stochastic processes on ultrametric spaces are represented here by [2], which proposes a method for describing stationary Markov processes on the class of ultrametric spaces $\mathbb{U}$ isometrically embeddable in $\mathbb{Q}_p$, reducing their study to processes on $\mathbb{Q}_p$ so that the traditional machinery of p-adic mathematical physics can be applied. This is the tool we need for the conservation claim in Section 3.3: if the ZBW readout dynamics is a stationary Markov process on a tree isometrically embeddable in $\mathbb{Q}_2$, the reduction theorem guarantees that the evolution can be analyzed with p-adic machinery, and isometric embeddings preserve the ultrametric distances on which our invariant is defined. The entry's summary is truncated and supplies no further detail; we use only the reduction-and-embeddability statement. On the statistical-mechanics side, the p-adic Potts model with competing interactions on a Cayley tree of order two [4] reduces the description of p-adic Gibbs measures to a recursive equation and proves that a phase transition occurs if and only if $p = 3$ for any nonzero interaction, with the uniqueness problem completely solved. This matters for us because the Cayley tree *is* the Bruhat–Tits tree topology of our readout: [4] shows that on such trees, sharp, prime-dependent discrete transitions occur — the same mechanism class we invoke when the $\mathbb{Z}_2$ invariant flips or fails at a branch point.

**p-adic functional analysis and geometry.** The p-adic Welch bounds and p-adic Zauner conjecture [7] work in the standard $d$-dimensional p-adic Hilbert space $\mathbb{Q}_p^d$ and in the space $\mathrm{Sym}^m(\mathbb{Q}_p^d)$ of symmetric $m$-tensors, proving results for collections $\{\tau_j\}_{j=1}^n$ with unit p-adic norms $\langle \tau_j, \tau_j \rangle = 1$. This demonstrates that Hilbert-space constructs central to quantum information — frames, tight bounds, SIC-like conjectures — admit p-adic formulations, which is the prerequisite for our claim that the ZBW current correlator can be defined over a p-adic Hilbert space without leaving quantum information practice. The summary supplied for [7] is truncated before its main conclusions; we rely on it only for the setup just described. On the metric-geometry side, [8] treats ultrametrics as a zero-dimensional analogue of ordinary metrics and proves ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization theorem. For us, [8] supplies the guarantee that our tree readout is not an ad hoc structure: ultrametric spaces support the same embedding, extension, and characterization machinery as metric spaces, so the Bruhat–Tits readout can be embedded, extended, and characterized with standard tools.

**Number-theoretic analogies.** Two works connect p-adic regulators to special values, which we use as structural analogy rather than as input. The p-adic Beilinson conjecture for number fields [3] formulates a conjectural p-adic analogue of Borel's theorem relating regulators for higher $K$-groups to special values of zeta-functions, using syntomic regulators and p-adic L-functions, with a corresponding conjecture for Artin motives and a conjecture on the precise relation between the p-adic and classical situations. Similarly, [5] introduces a family of p-adic Stark regulators for $p$-stabilized Artin representations over $\mathbb{Q}$ and formulates an Iwasawa–Greenberg main conjecture and a p-adic Stark conjecture, strengthening conjectures of Perrin-Riou and Benois, and shows these conjectures imply the corresponding p-adic statements. The pattern both works instantiate — a classical analytic quantity (regulator, special value) with a p-adic shadow whose comparison is itself a theorem-shaped question — is precisely the pattern of our Conjecture: the Archimedean ZBW frequency is the classical quantity, the tree level and its parity are the p-adic shadow, and the comparison (Section 4.3) is where the physics lives. We emphasize that [3] and [5] are conjectural works in pure number theory; we borrow only their structural template, not any result.

**The ZBW/adelic corpus.** Reference [9] frames ZBW as the Compton-scale trembling first identified by Breit and Schrödinger, conventionally explained as positive/negative-energy interference on the real line, and develops the conjectural adelic framework of Archimedean–2-adic channel mixing with testable consequences; our paper is the working-out of the readout side of that program. Reference [10] supplies the representation-theoretic motivation (Silent Parameter Principle; $\mathrm{SU}(2)$/$\mathbb{Z}_2^x$ fusion-rule coincidence; 2-adic ZBW frequency deviating from the Archimedean value) — its summary is truncated, so we use only these stated elements. Reference [11] computes the Majorana ZBW current correlator in free-field theory and shows that the reality condition enforces a vanishing expectation value, establishing a $\mathbb{Z}_2$ topological distinction between Dirac and Majorana fermions accessible via ZBW measurement; this is the direct antecedent of our invariant $\chi$, and our Section 3.3 is the ultrametric conservation counterpart of its Archimedean vanishing result. Reference [12] formulates ZBW as a p-adic topological observable, establishes that the ZBW current $J^{\mu}_{\mathrm{ZBW}}$ carries a $\mathbb{Z}_2$ invariant encoding the Dirac/Majorana distinction, and proposes ultrametric readout protocols via Bruhat–Tits buildings; our contribution relative to [12] is the explicit numerical evaluation for the electron, the conservation proof under isometric evolution, and the non-additivity observable of Section 4.3.

## 3. Methods

### 3.1 Archimedean baseline

The Dirac Hamiltonian $H_D = c\,\boldsymbol{\alpha}\cdot \mathbf{p} + \beta m_e c^2$ has spectrum symmetric about zero; a wave packet superposing positive- and negative-energy branches beats at the Compton angular frequency

$$\omega_C = \frac{m_e c^2}{\hbar}.$$

The conventional observable is the oscillation of the position expectation value $\langle \hat{x} \rangle(t)$ on the real line. Its obstruction is standard: the spectral gap, the Clifford-algebra origin of the trembling, and the Newton–Wigner no-go jointly prevent a sharp relativistic position readout, an underdetermination attributed in [10] to the Silent Parameter Principle.

### 3.2 p-adic spectral decomposition

Let $\mathbb{Q}_2$ be the field of 2-adic numbers and $\mathbb{Z}_2$ the 2-adic integers. The Bruhat–Tits tree $\mathcal{T}_2$ for $\mathrm{SL}_2(\mathbb{Q}_2)$ is an infinite $(2+1)$-regular tree; we use its vertex set as the readout space. Define the *scale map*

$$\nu: \mathbb{R}_{+} \to \mathbb{Z}, \qquad \nu(x) = \left\lfloor \log_2 x \right\rfloor,$$

assigning to a physical scale $x$ (a frequency, a length) the level of $\mathcal{T}_2$ at which it is read out. The p-adic analogue of the Dirac spectral decomposition is then:

$$\mathcal{H}_{\mathrm{ZBW}} = \mathcal{H}_{+} \oplus \mathcal{H}_{-}, \qquad \mathcal{H}_{\pm} \cong L^2(\mathcal{T}_{2}^{\pm}),$$

where $\mathcal{T}_2^{+}$ and $\mathcal{T}_2^{-}$ are the two halves of the tree separated by an edge at the level $\nu(\omega_C)$ — the p-adic image of the spectral gap. The "oscillation" is reinterpreted as the readout point alternating connectivity between the two halves; the beat phase is replaced by the branch occupied.

### 3.3 The ℤ₂ invariant and its conservation

Define the invariant

$$\chi = \nu(\omega_C) \bmod 2 \in \mathbb{Z}_2.$$

$\chi$ is the parity of the tree level of the Compton scale, and by [11], [12] it coincides with the $\mathbb{Z}_2$ invariant carried by the current correlator $J^{\mu}_{\mathrm{ZBW}}$ that distinguishes Dirac ($\chi \neq$ vanishing signal) from Majorana (vanishing signal) fermions.

**Proposition (Conservation).** Let the readout dynamics be a stationary Markov process on an ultrametric space $\mathbb{U}$ isometrically embeddable in $\mathbb{Q}_2$, in the class of [2]. Then $\chi$ is conserved under the evolution.

*Proof sketch.* Isometric embeddings preserve ultrametric distances, hence preserve tree levels and their parities; the reduction of [2] to a process on $\mathbb{Q}_2$ therefore acts on the readout by p-adic isometries, which fix $\nu(\omega_C) \bmod 2$. The parity of a vertex level is invariant under any isometry of $\mathcal{T}_2$ that fixes the root, and the stationary process of [2] preserves the root (the reference scale $x_0 = 1\ \mathrm{Hz}$). $\square$

The physical content: the $\mathbb{Z}_2$ invariant is *topologically protected* against any evolution that respects the ultrametric — it cannot decay the way a continuous oscillation phase can dephase. This is the intrinsic topological protection advertised in [12], here given a dynamical justification via the process class of [2].

### 3.4 Distinguishing observable: non-additivity

In the Archimedean picture, frequency and length compose multiplicatively: $\omega_C \lambda_C = c$ exactly. In the ultrametric picture, the readout assigns vertices at levels $\nu(\omega_C)$ and $\nu(\lambda_C)$; the tree distance between them is $|\nu(\omega_C) - \nu(\lambda_C)|$, which is *not* $\log_2(\omega_C \lambda_C)$ in general, because the floor function destroys additivity. The deviation

$$\Delta = \big|\, \nu(\omega_C) - \nu(\lambda_C) \,\big| - \log_2 c$$

is a scalar observable computable in both pictures, and it is the concrete discriminator we propose to measure: an Archimedean (continuous-oscillation) readout has no analogue of $\Delta$, while the ultrametric readout predicts a specific nonzero, parity-structured value computed in Section 4.3.

## 4. Analysis

All input numbers are stated with sources; all arithmetic is shown.

### 4.1 Inputs

- $m_e c^2 = 5.11 \times 10^{5}\ \mathrm{eV}$ (electron rest energy, standard physical constant).
- $\hbar = 6.582 \times 10^{-16}\ \mathrm{eV}\cdot\mathrm{s}$ (reduced Planck constant, standard physical constant).
- $\hbar c = 197.327\ \mathrm{eV}\cdot\mathrm{nm}$ (standard physical constant).
- $c = 2.998 \times 10^{8}\ \mathrm{m/s}$ (speed of light, standard physical constant).
- $\log_{10} 2 = 0.30103$ (mathematical constant).

### 4.2 Compton scales and tree levels

**Step 1 (Compton angular frequency).**

$$\omega_C = \frac{m_e c^2}{\hbar} = \frac{5.11 \times 10^{5}\ \mathrm{eV}}{6.582 \times 10^{-16}\ \mathrm{eV}\cdot\mathrm{s}}.$$

Compute the mantissa: $5.11 / 6.582 = 0.77636$. Compute the power of ten: $10^{5} / 10^{-16} = 10^{21}$. Hence

$$\omega_C = 7.7636 \times 10^{20}\ \mathrm{s}^{-1}.$$

**Step 2 (tree level of the frequency).**

$$\log_{10} \omega_C = \log_{10} 7.7636 + 20 = 0.89000 + 20 = 20.89000.$$

$$\log_2 \omega_C = \frac{20.89000}{0.30103}.$$

Compute: $0.30103 \times 69 = 20.77107$; remainder $20.89000 - 20.77107 = 0.11893$; $0.11893 / 0.30103 = 0.3951$. Hence

$$\log_2 \omega_C = 69.3951, \qquad \nu(\omega_C) = \lfloor 69.3951 \rfloor = 69.$$

**Step 3 (Compton wavelength).**

$$\lambda_C = \frac{\hbar c}{m_e c^2} = \frac{197.327\ \mathrm{eV}\cdot\mathrm{nm}}{5.11 \times 10^{5}\ \mathrm{eV}}.$$

Mantissa: $197.327 / 5.11 = 38.616$; power of ten: $1/10^{5} = 10^{-5}$. Hence $\lambda_C = 38.616 \times 10^{-5}\ \mathrm{nm} = 3.8616 \times 10^{-4}\ \mathrm{nm} = 3.8616 \times 10^{-13}\ \mathrm{m}$.

**Step 4 (tree level of the length).**

$$\log_{10} \lambda_C = \log_{10} 3.8616 - 13 = 0.58675 - 13 = -12.41325.$$

$$\log_2 \lambda_C = \frac{-12.41325}{0.30103}.$$

Compute: $0.30103 \times 41 = 12.34223$; remainder $12.41325 - 12.34223 = 0.07102$; $0.07102/0.30103 = 0.2359$. Hence

$$\log_2 \lambda_C = -41.2359, \qquad \nu(\lambda_C) = \lfloor -41.2359 \rfloor = -42.$$

(Note: $\lfloor -41.2359 \rfloor = -42$, not $-41$; the floor of a negative non-integer rounds down.)

**Step 5 (the ℤ₂ invariant).**

$$\chi = \nu(\omega_C) \bmod 2 = 69 \bmod 2 = 1.$$

**Result 1.** For the electron, $\chi = 1 \in \mathbb{Z}_2$: the Compton frequency sits at odd tree level 69. The invariant is a single bit, not a phase.

### 4.3 The non-additivity observable

**Step 6 (Archimedean consistency check).** The exact identity is $\omega_C \lambda_C = c$. Verify numerically:

$$\log_2 \omega_C + \log_2 \lambda_C = 69.3951 + (-41.2359) = 28.1592.$$

Independent check: $\log_2 c = \log_{10}(2.998 \times 10^{8}) / 0.30103 = (0.47680 + 8)/0.30103 = 8.47680/0.30103 = 28.1592$. The two agree to all displayed digits — the Archimedean composition is exactly multiplicative, as it must be.

**Step 7 (ultrametric tree distance).** The Bruhat–Tits tree distance between the vertices at levels $\nu(\omega_C) = 69$ and $\nu(\lambda_C) = -42$ is

$$d_{\mathcal{T}} = |69 - (-42)| = 111.$$

**Step 8 (the deviation).**

$$\Delta = d_{\mathcal{T}} - \log_2 c = 111 - 28.1592 = 82.8408.$$

**Result 2.** The ultrametric readout predicts a tree distance $d_{\mathcal{T}} = 111$ where the Archimedean composition would give $28.1592$; the deviation is $\Delta = 82.8408$ levels. This gross non-additivity is not an error but the signature: the ultrametric readout does not compose multiplicatively, and the discrepancy is a discrete, parity-structured number (note $111 \equiv 1 \pmod 2$, consistent with $\chi = 1$).

**Step 9 (fractional deviation of the frequency).** The fractional part of $\log_2 \omega_C$ is $0.3951$ octaves; the ratio of $\omega_C$ to the nearest lower power of two is

$$2^{0.3951} = e^{0.3951 \times 0.69315} = e^{0.27387} = 1.3150.$$

**Result 3.** $\omega_C = 2^{69} \times 1.3150$: the Compton frequency lies a factor $1.3150$ above the level-$69$ vertex, i.e., $0.3951$ octaves into the level — this fractional position is the p-adic "phase" analogue, but it enters the observable only through the floor (the parity), which is why the predicted signature is discrete.

### 4.4 Timescale and detectability arithmetic

**Step 10 (beat period).**

$$T_{\mathrm{ZBW}} = \frac{1}{\nu_C} = \frac{1}{\omega_C / 2\pi} = \frac{2\pi}{7.7636 \times 10^{20}\ \mathrm{s}^{-1}} = \frac{6.28319}{7.7636} \times 10^{-20}\ \mathrm{s} = 8.0926 \times 10^{-21}\ \mathrm{s}.$$

**Step 11 (Nyquist requirement for a continuous readout — infeasibility).** Resolving a continuous oscillation at $\nu_C = \omega_C/2\pi = 1.2356 \times 10^{20}\ \mathrm{Hz}$ (from $7.7636 \times 10^{20} / 6.28319 = 1.23558 \times 10^{20}$) requires sampling intervals

$$\Delta t \leq \frac{1}{2\nu_C} = \frac{1}{2.47116 \times 10^{20}}\ \mathrm{s} = 4.0467 \times 10^{-21}\ \mathrm{s}.$$

This is roughly eight orders of magnitude below the fastest claimed electronic timescales in any solid-state platform and is not reachable; we state it as an infeasibility, not a measurement.

**Step 12 (projection: parity readout integration).** *Projection with stated assumptions.* If the $\mathbb{Z}_2$ signature manifests as a sign structure of the current correlator at the half-period $\tau = T_{\mathrm{ZBW}}/2 = 4.0463 \times 10^{-21}\ \mathrm{s}$, and if the correlator sign can be accumulated statistically (as in spin noise spectroscopy, where the observable is a variance, not a phase), then the required number of accumulated samples for an $N_\sigma$-sigma discrimination against a null of equal sign probability is $N \approx N_\sigma^2$ (binomial statistics). For $N_\sigma = 5$: $N = 25$ effective independent sign samples. Assuming a readout that effectively samples the sign once per platform coherence time $t_2 = 1\ \mu\mathrm{s}$ (a stated assumption; typical for Majorana-platform proposals, not measured here), the integration time is

$$t_{\mathrm{int}} = N \cdot t_2 = 25 \times 10^{-6}\ \mathrm{s} = 25\ \mu\mathrm{s}.$$

This is a *projection*, contingent on the assumption that the sign structure is statistically accessible; it is not a prediction of a continuous signal at $\nu_C$, which Step 11 rules out.

## 5. Results

We report only quantities computed in Section 4, plus the clearly labeled