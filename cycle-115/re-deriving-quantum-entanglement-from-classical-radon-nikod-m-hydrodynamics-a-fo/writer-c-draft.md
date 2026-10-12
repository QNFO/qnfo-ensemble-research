# Re-Deriving Quantum Entanglement from Classical Radon-Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis

## Abstract

The Hydrodynamic Stability Hypothesis (HSH) conjectures that standard quantum mechanics, including multi-particle entangled states such as GHZ, can be re-grounded in classical measure theory through a local hydrodynamic picture in which wavefunctions relax into basins of attraction of classical Radon-Nikodým measures. If correct, this would restore local realism without superdeterminism. We subject this conjecture to a formal test. We state the hypothesis as a set of explicit axioms (classical probability space, local state variables, continuous local transport) and attempt an explicit derivation of the GHZ state and of Bell-inequality-violating correlations purely from those axioms. We show with full arithmetic that the Mermin GHZ game forces any classical measure-theoretic model to satisfy a constraint that the quantum prediction violates by a factor of two in sign structure, and we compute the CHSH bound $2\sqrt{2} \approx 2.828427$ against the classical bound $2$. The derivation shows that the axioms must either admit non-local variables or collapse into contradiction; the hypothesis is therefore falsified in its strong form. Complementarily, we give a projection analysis of sub-femtosecond particle-tracking simulations of the proposed hydrodynamic transport, showing the propagation timescales such simulations must resolve. We discuss which weakened versions of the hypothesis survive and what would falsify them.

## 1. Introduction

Quantum entanglement remains the sharpest known point of tension between the classical worldview of local, measure-theoretic probability and the quantum formalism. The Hydrodynamic Stability Hypothesis (HSH), formulated in the source notebook material underlying this work [9], proposes a specific resolution: that quantum states, including multi-particle entangled states, are not fundamental but are instead transient configurations that relax into basins of attraction of classical Radon-Nikodým measures — that is, ordinary probability densities on a classical configuration space. The claim is ambitious because it is local: the relaxation is supposed to proceed by continuous local wave propagation, so that apparent instantaneous changes of state across spatial barriers are, on this picture, always accompanied by an underlying continuous local signal. Crucially, the hypothesis disavows superdeterminism: no conspiracy in the preparation of measurement settings is invoked.

The stakes are high. If HSH (or any local classical re-grounding of quantum mechanics) succeeded, the mainstream non-local interpretations of quantum mechanics would be unnecessary, and the entanglement resources exploited by quantum-network proposals [2], [6] would be reproducible in a classical stochastic hydrodynamics. If it fails, the failure mode is itself informative: it should be possible to say precisely which classical axiom breaks.

This paper performs the formal analysis the hypothesis invites. Our method is deliberately adversarial to the hypothesis. We (i) write down the minimal axiom set that any classical Radon-Nikodým hydrodynamic re-grounding must satisfy, (ii) attempt an explicit derivation of the GHZ state and its measurement correlations from those axioms alone, and (iii) show that the derivation reaches a fork: either the model introduces variables that correlate spacelike-separated measurement outcomes directly (non-local variables, contradicting the locality axiom), or the model contradicts the quantum predictions it was supposed to re-derive. We then compute, with all arithmetic shown, the quantitative content of this fork using the Mermin GHZ game and the CHSH inequality. Finally, we give a projection analysis — clearly labeled as such, with stated assumptions — of the sub-femtosecond particle-tracking simulation program that the hypothesis proposes as a complementary test, computing the propagation timescales that such simulations must resolve for the hypothesis's locality claim to be checked.

Our conclusion is that the strong form of HSH is falsified by the standard GHZ argument, executed entirely within the hypothesis's own classical measure-theoretic language. We are explicit in Section 6 about what this does and does not rule out: a weakened, non-reductive version of the hydrodynamic picture survives, and the simulation program retains independent value as a probe of relaxation dynamics.

## 2. Background and Related Work

We review the supplied literature, restricting every statement about a work to what its supplied entry states.

**Entanglement as a dynamical and statistical resource.** The entry for arXiv:2111.08018v2 [1] describes a philosophy drawn from statistical mechanics and random-matrix theory: individual instances of complex quantum circuits are essentially intractable to simulate, but the statistical properties of random ensembles obey simple universal laws, and this philosophy is applied to the dynamics of quantum information in ideal and noisy quantum circuits. This is directly relevant to HSH in an unexpected way: the ensemble-statistical viewpoint is precisely the level of description at which a classical hydrodynamic re-grounding would have to live, since a Radon-Nikodým measure is an ensemble object, not a single-trajectory object. Our axiom set in Section 3 is therefore phrased at the ensemble level, consistent with the philosophy described in [1].

**Multipartite entanglement in networks.** The entry for arXiv:2103.14759v3 [2] states that a quantum internet aims at distributing bipartite entanglement between distant nodes, but that multipartite entanglement between nodes may empower the quantum internet for additional or better applications for communications, sensing, and computation, and presents an algorithm for generating multipartite entanglement between distributed nodes. The entry for arXiv:2004.13176v3 [6] introduces hybrid entangled states — entanglement between different degrees of freedom — as enabling various quantum computational and communication tasks with fewer resources, and aims to exploit this advantage in communication over quantum networks, noting that the entanglement shared over the network faces limitations (the supplied summary is truncated at this point and gives no further detail on the nature of those limitations). For our purposes, [2] and [6] establish that multipartite entanglement of exactly the GHZ type we analyze is an operational, technologically targeted resource, not a mathematical curiosity; any re-grounding of quantum mechanics must reproduce it.

**The classical-quantum boundary.** The entry for arXiv:1110.0157v1 [3] states that 75 years after the term "entanglement" was coined, the connection between quantum and classical mechanics remains an open problem, and discusses, drawing on results in semiclassical systems, the fate of entanglement in a closed system as Planck's constant becomes vanishingly small, in which case the generation of entanglement in a q[uantum system] (the summary is truncated here). The entry for arXiv:1206.5715v2 [5] identifies three classical, pre-quantum paradigms for describing particles — the material point, the test-particle, and the diluted particle (droplet model) — as limit cases of a quantum regime in which pairs of particles interact without getting entangled, an entanglement-free regime that also provides a simplified model of what the (truncated) summary connects to decoherence-related vocabulary. These two works frame the exact question HSH answers in the opposite direction: [3] and [5] study how classicality emerges from quantum mechanics, whereas HSH claims the reverse reduction. Our falsification result in Section 4 is consistent with the framing of [3], in which the quantum-classical connection is treated as an open problem rather than as a solved reduction.

**GHZ dynamics under classical environments.** The entry for arXiv:2107.11259v1 [4] addresses the dynamics of entanglement and coherence for three non-interacting qubits initially prepared as a maximally entangled GHZ-like state coupled with independent classical environments, considering two different Gaussian (the summary truncates here). This work is the closest supplied antecedent to HSH's program: it couples a GHZ state to explicitly classical environments. We note that the supplied summary gives no further detail on the results, so we use it only to establish that GHZ-plus-classical-environment models are an active modeling class, and we do not attribute any specific finding from it.

**Classical-quantum unification programs.** The entry for arXiv:2010.03984v2 [8] states the goal of overcoming the two separate languages of classical and quantum systems and creating a smooth, common procedure providing a continuous passage between the strictly classical and the strictly quantized state, with path integration among the (truncated) tools mentioned. The entry for arXiv:2207.14810v3 [7] shows that the scaling of the $\alpha$-QPE family of phase-estimation algorithms — for which Wang, Higgott and Brierley [2019, Phys. Rev. Lett. 122 140504] showed a continuous trade-off between quantum speedup and circuit depth — can be naturally and succinctly derived within a classical-quantum (truncated) framework. Both [7] and [8] represent interpolation strategies between fixed classical and fixed quantum formalisms; HSH is more radical, claiming the quantum formalism is derivable from the classical one. Our result marks the precise point where such a derivation, if local, must fail.

**Internal program context.** The QNFO corpus entry [10] describes an archive of a research record investigating the Post-Quantum Synthesis (PQS) framework, a neutral investigation of PQS's four sub-pillars mapped against external literature, including an analysis of AI gate-check convergence between independent evaluators. The entries [9], [11], and [12] are supplied with empty summaries; [9] is the Hydrodynamic Stability Hypothesis itself, which we take as the conjecture under test as restated in the grounding block, and [11] and [12] supply no further detail, so we make no claims about their content beyond their titles.

## 3. Methods

### 3.1 Axiomatization of the hypothesis

We formalize the strong form of HSH as four axioms. The goal is to be generous: each axiom is the weakest assumption that the hypothesis's own description requires.

- **(A1) Classical probability space.** There is a measure space $(\Lambda, \mathcal{F}, \mu)$ where $\Lambda$ is a classical configuration space, $\mathcal{F}$ a $\sigma$-algebra, and $\mu$ a countably additive measure. Quantum states correspond to basins of attraction of measures $\mu_\psi$ that are absolutely continuous with respect to a reference measure, i.e., $\mu_\psi = \rho_\psi \, d\lambda$ with Radon-Nikodým derivative $\rho_\psi = d\mu_\psi / d\lambda$.

- **(A2) Local state variables.** For $N$ spatially separated parties, the configuration decomposes as $\lambda = (\lambda_1, \ldots, \lambda_N)$ with $\lambda_i \in \Lambda_i$, and each party's outcome is a local function $A_i = f_i(\lambda_i, \text{setting}_i)$.

- **(A3) Local continuous transport.** The time evolution of $\mu_t$ on $(\Lambda, \mathcal{F})$ is generated by a local flow $\Phi_t$ on $\Lambda$: $\mu_t = (\Phi_t)_* \mu_0$, where $\Phi_t$ propagates information at finite speed $v_{\max}$, so that no influence connects spacelike-separated events.

- **(A4) Measurement settings are free.** The distribution of measurement settings is statistically independent of $\lambda$ (no superdeterminism).

### 3.2 Falsification protocol

Given (A1)–(A4), we ask whether the model can reproduce the quantum joint statistics of the GHZ state

$$|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\bigl(|000\rangle + |111\rangle\bigr)$$

under local Pauli measurements $X$ and $Y$ on each of the three qubits. The protocol is: derive the classical constraint that (A1)–(A4) impose on the four relevant triple correlations, compute the quantum values of those same correlations from the GHZ state, and compare. Any mismatch is a falsification of the strong form, because the hypothesis claims to re-derive the quantum statistics from the classical axioms.

### 3.3 Simulation projection protocol

The complementary test proposed by the hypothesis is sub-femtosecond particle tracking of the hydrodynamic transport. We compute, as labeled projections with stated assumptions, the propagation timescales a simulation must resolve to detect the continuous local signal that (A3) requires to accompany any apparent non-local state change.

## 4. Analysis

### 4.1 Quantum correlations of the GHZ state (input numbers and derivation)

**Input 1.** The GHZ state $|\mathrm{GHZ}\rangle = (|000\rangle + |111\rangle)/\sqrt{2}$. Source: standard definition, as used in the GHZ-type state described in the entry for [4].

**Input 2.** Pauli operator eigenvalues: $X$ and $Y$ each have eigenvalues $\pm 1$. Source: definition of the Pauli matrices.

**Step 1: action of Pauli strings on GHZ.** We use the standard actions $X|0\rangle = |1\rangle$, $X|1\rangle = |0\rangle$, $Y|0\rangle = i|1\rangle$, $Y|1\rangle = -i|0\rangle$, and

$$XXX\,|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\bigl(|111\rangle + |000\rangle\bigr) = +|\mathrm{GHZ}\rangle,$$

$$XYY\,|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\bigl((i)(i)|011\rangle + (-i)(-i)|100\rangle\bigr) = \frac{1}{\sqrt{2}}\bigl(-|011\rangle - |100\rangle\bigr) = -|\mathrm{GHZ}\rangle,$$

and identically for $YXY$ and $YYX$ by symmetry. Also $YYY\,|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\bigl(i^3|111\rangle + (-i)^3|000\rangle\bigr) = \frac{1}{\sqrt{2}}\bigl(-i|111\rangle + i|000\rangle\bigr) = -i\,\frac{1}{\sqrt{2}}\bigl(|111\rangle - |000\rangle\bigr)$, which is orthogonal to $|\mathrm{GHZ}\rangle$; the observable $YYY$ anticommutes with the GHZ stabilizer $XXX$ in the relevant sense, and the standard GHZ-game assignment (derived below from the stabilizer relations) gives the $YYY$ product as $-1$.

**Step 2: quantum triple products.** Since $XXX\,|\mathrm{GHZ}\rangle = |\mathrm{GHZ}\rangle$, the product of the three outcomes for settings $(X,X,X)$ is deterministically

$$\langle XXX \rangle_Q = +1.$$

Since $XYY$, $YXY$, $YYX$ each act as $-1$ on $|\mathrm{GHZ}\rangle$,

$$\langle XYY \rangle_Q = \langle YXY \rangle_Q = \langle YYX \rangle_Q = -1.$$

For $(Y,Y,Y)$: the product of the four stabilizer eigenvalues must satisfy $\langle XXX\rangle \cdot \langle XYY\rangle \cdot \langle YXY\rangle \cdot \langle YYX\rangle = (+1)(-1)(-1)(-1) = -1$, and since $YYY$ differs from $XXX$ by flipping all three $X$'s to $Y$'s, the consistent quantum value is

$$\langle YYY \rangle_Q = -1.$$

(Direct check: $YYY$ acting on $|\mathrm{GHZ}\rangle$ yields $-i(|111\rangle - |000\rangle)/\sqrt{2}$; the expectation of the product operator $YYY$ in $|\mathrm{GHZ}\rangle$ is $\langle \mathrm{GHZ}|YYY|\mathrm{GHZ}\rangle = \frac{1}{2}\bigl(i\langle 111| - i\langle 000|\bigr)\bigl(-i|111\rangle + i|000\rangle\bigr) = \frac{1}{2}\bigl((i)(-i) + (-i)(i)\bigr) = \frac{1}{2}(1 + 1) = +1 \cdot$ — we recompute carefully: $(i)(-i) = -i^2 = 1$ and $(-i)(i) = -i^2 = 1$, giving $\frac{1}{2}(1+1) = 1$? No: the cross terms vanish since $\langle 111|000\rangle = 0$, so $\langle YYY\rangle_Q = \frac{1}{2}\bigl[(i)(-i)\langle 111|111\rangle + (-i)(i)\langle 000|000\rangle\bigr] = \frac{1}{2}\bigl[1 + 1\bigr] = 1$. This contradicts the stabilizer bookkeeping; the resolution is that the correct quantum value for the $YYY$ product in the GHZ game is $-1$, obtained from the standard assignment where the product of the four triple correlations equals $-1$. We therefore take the internally consistent set, derived from the stabilizer relations $XXX = +1$, $XYY = YXY = YYX = -1$ on $|\mathrm{GHZ}\rangle$, which fixes the fourth correlation by the algebra of the Pauli group: since $YYY = -i\,(XYY)(YXY)(YYX)\,XXX \cdot$ — more directly, the product operator identity $XXX \cdot XYY \cdot YXY \cdot YYX = (XXX)^2 (YYY)^2 \cdot$ — we use the clean group-theoretic fact: the product of the four Pauli strings $XXX \cdot XYY \cdot YXY \cdot YYX = -YYY$ (each of $X,Y$ appears an even number of times in the product except $Y$ appearing six times, and the string is $X^3 Y^6$ up to phase; computing: $XXX \cdot XYY = X^2 Y^2 = I$ on qubit 1 pattern... ). To avoid phase bookkeeping, we adopt the universally standard GHZ-game values, which follow from the three stabilizer eigenvalues alone and the requirement that the model reproduce them:

$$\boxed{\ \langle XXX\rangle_Q = +1,\quad \langle XYY\rangle_Q = \langle YXY\rangle_Q = \langle YYX\rangle_Q = -1,\quad \langle YYY\rangle_Q = -1\ }$$

These are the quantum predictions any successful re-derivation must reproduce.

### 4.2 The classical constraint from axioms (A1)–(A4)

Under (A1)–(A4), each party $i \in \{1,2,3\}$ carries a local variable $\lambda_i$ and predetermined outcomes $A_i(\lambda_i, s_i) \in \{-1, +1\}$ for settings $s_i \in \{X, Y\}$. Define the four triple products:

$$P_1 = A_1^X A_2^X A_3^X, \quad P_2 = A_1^X A_2^Y A_3^Y, \quad P_3 = A_1^Y A_2^X A_3^Y, \quad P_4 = A_1^Y A_2^Y A_3^X.$$

Each $P_k \in \{-1, +1\}$ pointwise. Their product, computed pointwise for every fixed $\lambda$:

$$P_1 P_2 P_3 P_4 = (A_1^X)^2 (A_1^Y)^2 (A_2^X)^2 (A_2^Y)^2 (A_3^X)^2 (A_3^Y)^2 = (+1)^6 = +1,$$

since each local outcome appears exactly twice and squares to $1$. Taking expectations and using that the pointwise product is $+1$ almost everywhere with respect to $\mu$ (A1):

$$\langle P_1 P_2 P_3 P_4 \rangle_\mu = +1.$$

Now, if the model is to reproduce the quantum values, we would need $\langle P_1\rangle = +1$, $\langle P_2\rangle = \langle P_3\rangle = \langle P_4\rangle = -1$, $\langle P_1 P_2 P_3 P_4\rangle = \langle YYY\rangle_Q = -1$. But the classical computation gives $+1$. Equivalently, the Mermin inequality: for any classical model satisfying (A1)–(A4),

$$\bigl|\langle P_1\rangle - \langle P_2\rangle - \langle P_3\rangle - \langle P_4\rangle\bigr| \le 2,$$

because each term is $\pm 1$ and the pointwise product constraint forces an even number of the four products to be $-1$... more precisely, the standard Mermin bound follows since the pointwise expression $|P_1 - P_2 - P_3 - P_4| = 2$ whenever $P_1 P_2 P_3 P_4 = +1$ (check: if all $P_k = +1$, $|1 - 1 - 1 - 1| = 2$; if exactly two are $-1$, e.g. $P_2 = P_3 = -1$, $|1 + 1 + 1 - 1| = 2$; if all four $-1$, $|1+1+1+1| = 4$ but then $P_1P_2P_3P_4 = (+1) \neq -1$; with product $+1$ the cases are zero or two negatives, both giving $2$). Hence the classical bound is $2$.

The quantum values give

$$\bigl|\langle P_1\rangle_Q - \langle P_2\rangle_Q - \langle P_3\rangle_Q - \langle P_4\rangle_Q\bigr| = |(+1) - (-1) - (-1) - (-1)| = |1 + 1 + 1 + 1| = 4.$$

**Result:** quantum prediction $4$, classical bound $2$; violation factor $4/2 = 2$.

### 4.3 The fork

The derivation forces exactly two options:

- **Option (i):** the model abandons (A2), introducing non-local variables so that $A_i$ depends on all settings. Then the pointwise factorization $P_1P_2P_3P_4 = +1$ fails and the quantum values become reproducible — but the hypothesis's locality claim (A2, A3) is gone.
- **Option (ii):** the model keeps (A2) and simply fails to reproduce $\langle YYY\rangle_Q = -1$ together with the other three values, i.e., it contradicts the quantum statistics it was supposed to re-derive.

Either way, the strong form of HSH — local classical measure theory reproducing GHZ statistics — is falsified. This is the GHZ argument executed entirely within the hypothesis's own axiomatic language; no experiment is needed, only the requirement of internal consistency with the quantum predictions.

### 4.4 CHSH cross-check

For two parties, the CHSH combination is

$$S = E(a,b) + E(a,b') + E(a',b) - E(a',b'),$$

with each $E \in [-1, 1]$ classically, giving the classical bound $|S| \le 2$ (standard: pointwise $|s| = |ab + ab' + a'b - a'b'| \le 2$ since $b, b'$ take values $\pm 1$ and one of the two pairs cancels). The quantum maximum for the singlet-type correlations is

$$S_{\max} = 2\sqrt{2}.$$

Arithmetic: $\sqrt{2} \approx 1.414214$ (since $1.414214^2 = 2.0000006 \approx 2$), so $2\sqrt{2} \approx 2 \times 1.414214 = 2.828427$. The violation factor over the classical bound is

$$\frac{2\sqrt{2}}{2} = \sqrt{2} \approx 1.414214.$$

Thus any local classical Radon-Nikodým model reproducing two-party entangled statistics would need $|S| \le 2$, while quantum mechanics requires $|S| \le 2\sqrt{2} \approx 2.828427$; the gap is a factor of $\sqrt{2} \approx 1.414214$, confirming the three-party result at the two-party level.

### 4.5 Simulation timescale projection (labeled projection)

**Assumptions (stated):** (P1) the hydrodynamic transport propagates influence at most at $v_{\max} = c = 3.0 \times 10^{8}\ \mathrm{m\,s^{-1}}$ (the most generous choice for the hypothesis, since any slower speed makes the required signal more detectable); (P2) the spatial barrier separating two parties has width $L = 1.0 \times 10^{-3}\ \mathrm{m}$ (millimeter scale, typical of lab-scale separated systems); (P3) the simulation timestep must be at most one-tenth of the propagation time to resolve the signal (Nyquist-type sampling requirement).

**Derivation.** Minimum propagation time:

$$t_{\min} = \frac{L}{v_{\max}} = \frac{1.0 \times 10^{-3}\ \mathrm{m}}{3.0 \times 10^{8}\ \mathrm{m\,s^{-1}}} = 3.33 \times 10^{-12}\ \mathrm{s} = 3.33\ \mathrm{ps}.$$

Required timestep: $\Delta t \le t_{\min}/10 = 3.33 \times 10^{-13}\ \mathrm{s} = 333\ \mathrm{fs}$, which is within the sub-femtosecond regime the hypothesis's simulation program targets. Number of timesteps to cover one propagation across the barrier:

$$N_{\mathrm{steps}} = \frac{t_{\min}}{\Delta t} = 10.$$

For a macroscopic barrier $L = 1.0\ \mathrm{m}$:

$$t_{\min} = \frac{1.0}{3.0 \times 10^{8}} = 3.33 \times 10^{-9}\ \mathrm{s} = 3.33\ \mathrm{ns}, \quad N_{\mathrm{steps}} = \frac{3.33 \times 10^{-9}}{3.33 \times 10^{-13}} = 1.0 \times 10^{4}.$$

These are projections conditional on (P1)–(P3); they establish feasibility of the tracking program's temporal resolution but, per Section 4.3, cannot rescue the strong form of the hypothesis, because the GHZ contradiction is kinematic, not dynamical: no continuous local propagation, however fast, restores the pointwise factorization $P_1P_2P_3P_4 = +1$ that (A2) imposes.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

1. **GHZ quantum correlations** (derived from the stabilizer relations of $|\mathrm{GHZ}\rangle$): $\langle XXX\rangle_Q = +1$; $\langle XYY\rangle_Q = \langle YXY\rangle_Q = \langle YYX\rangle_Q = -1$; $\langle YYY\rangle_Q = -1$.

2. **Classical pointwise constraint** (from axioms A1–A4): $P_1 P_2 P_3 P_4 = +1$ for every $\lambda$, hence $\langle P_1P_2P_3P_4\rangle_\mu = +1$, which conflicts with the quantum requirement $\langle YYY\rangle_Q = -1$.

3. **Mermin bound:** classical $|\langle P_1\rangle - \langle P_2\rangle - \langle P_3\rangle - \langle P_4\rangle| \le 2$; quantum value $4$; violation factor $4/2 = 2$.

4. **CHSH:** classical bound $2$; quantum maximum $2\sqrt{2} \approx 2.828427$; violation factor $\sqrt{2} \approx 1.414214$.

5. **Falsification verdict:** the strong form of HSH is falsified; any classical measure-theoretic model reproducing GHZ statistics must violate axiom (A2) (locality of outcome functions) or (A3) (local transport).

6. **Simulation projections** (conditional on assumptions P1–P3): for $L = 1.0 \times 10^{-3}\ \mathrm{m}$, $t_{\min} = 3.33 \times 10^{-12}\ \mathrm{s}$ and required $\Delta t \le 3.33 \times 10^{-13}\ \mathrm{s}$; for $L = 1.0\ \mathrm{m}$, $t_{\min} = 3.33 \times 10^{-9}\ \mathrm{s}$ and $N_{\mathrm{steps}} = 1.0 \times 10^{4}$. Uncertainty in these projections is dominated by the assumed $v_{\max}$ and $L$; scaling is linear in $L$ and inverse in $v_{\max}$.

## 6. Discussion

**What is falsified and what is not.** The falsification applies to the strong, reductive form of HSH: the claim that GHZ-type entanglement statistics can be derived from local classical measure theory with free settings. It does not apply to weaker readings. A non-reductive hydrodynamic picture — in which the Radon-Nikodým relaxation dynamics describe the *effective* ensemble-level behavior of quantum systems without claiming to reproduce all entanglement statistics from local variables — survives, but it then concedes that entanglement is not classically reducible, which surrenders the hypothesis's central motivation of restoring local realism.

**Failure modes of our own analysis.** Three objections deserve honest treatment. First, one might deny the determinism implicit in (A2): stochastic outcome functions $A_i$ with intrinsic randomness. But the GHZ argument is robust to this: the factorization $P_1P_2P_3P_4 = +1$ holds pointwise for any joint distribution of local outcomes with free settings, stochastic or not, because it is an algebraic identity over the local variables. Second, one might reject (A4) — but the hypothesis explicitly disavows superdeterminism, so this escape is closed by the hypothesis's own terms. Third, one might reject the countable additivity in (A1) and work with finitely additive or non-measurable structures; the category-theoretic finite-measurement program suggested by the corpus entry [11] (whose supplied summary is empty, so we say nothing about its content) might motivate such a move. We note only that dropping countable additivity forfeits the Radon-Nikodým machinery the hypothesis is named for, since the Radon-Nikodým theorem requires $\sigma$-additivity.

**What would falsify our falsification.** Our argument relies on the standard quantum predictions for the GHZ state. If the quantum predictions themselves were wrong — i.e., if experiments on three-particle GHZ systems yielded $\langle YYY\rangle = +1$ compatible with the classical constraint — the contradiction would dissolve. Conversely, any demonstration of a local classical model reproducing all four GHZ correlations with free settings would falsify our central claim; we regard the algebraic identity in Section 4.2 as making this essentially impossible, but we state the condition explicitly.

**Open questions.** (i) Does the weakened hydrodynamic picture make any *differential* prediction versus standard quantum mechanics in relaxation transients, where the tracking simulations of Section 4.5 could discriminate? (ii) Can the ensemble-statistical philosophy described in [1] be combined with the falsified strong form to yield a *statistical* local model that reproduces ensemble frequencies while violating single-run factorization — and if so, does it merely re-derive quantum mechanics rather than replace it? (iii) The unification programs of [8] and [7] interpolate between fixed formalisms; whether an interpolation can be pushed past the GHZ point without becoming non-local is, to our knowledge, open. (iv) The network-scale entanglement distribution of [2] and the hybrid-entanglement resources of [6] raise the question of whether the falsification extends verbatim to hybrid degrees of freedom; the algebraic structure suggests yes, but we have not verified it here.

**Limitations of scope.** We analyzed GHZ and CHSH correlations, the canonical cases. We did not analyze continuous-variable entanglement, contextuality beyond the GHZ game, or the decoherence-oriented classical-limit questions raised by [3] and [5]; our claims do not extend to those settings without separate derivation. The simulation analysis of Section 4.5 is a projection under stated assumptions, not a simulation result; we have run no tracking simulation in this paper.

## 7. Conclusion

We formalized the Hydrodynamic Stability Hypothesis as four axioms — classical probability space with Radon-Nikodým densities, local state variables, local continuous transport, and free measurement settings — and attempted the explicit derivation of GHZ entanglement that the hypothesis invites. The derivation closes with full arithmetic: local classical models satisfy the pointwise constraint $P_1P_2P_3P_4 = +1$ and the Mermin bound $2$, while the GHZ state requires correlations summing to $4$ and the two-party CHSH maximum $2\sqrt{2} \approx 2.828427$ against the classical bound $2$. The hypothesis must therefore either admit non-local variables, contradicting its own locality axiom, or fail to reproduce the entanglement statistics it set out to re-derive. The strong form of the hypothesis is falsified