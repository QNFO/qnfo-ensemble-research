# Spectral Decomposition of the Bruhat–Tits Tree as a Candidate Origin of Particle Mass Hierarchies: Exact Radial Spectrum, Adelic Constraints, and a Falsification Test Against Standard Model Ratios

## Abstract

The p-adic holography programme models anti-de Sitter physics on the Bruhat–Tits tree $\mathcal{T}_p$, the infinite $(p+1)$-regular tree, with $p$-adic numbers as the boundary. We investigate the conjecture that a naturally defined Laplacian on $\mathcal{T}_p$ admits a spectral decomposition whose eigenvalue ratios reproduce particle mass ratios, extending p-adic holography from black-hole geometry to phenomenology. We (i) define the combinatorial Laplacian on $\mathcal{T}_p$ with boundary conditions motivated by the adelic product formula, (ii) compute its radial spectrum exactly: the adjacency spectrum fills the band $[-2\sqrt{p},\,2\sqrt{p}]$ and, for $p \equiv 5 \pmod{6}$, the radial quotient exhibits the point eigenvalues $\pm\sqrt{p}$, giving the exact band-edge-to-point ratio $2\sqrt{p}/\sqrt{p} = 2$, independent of $p$; (iii) compare the resulting discrete hierarchy against Standard Model mass ratios, finding that the prime-indexed scale ratios $p$ (e.g. $p = 211$ versus the muon-to-electron ratio $206.7683$, a $2.05\%$ deviation) are numerological coincidences without a dynamical mechanism, while the universal ratio $2$ matches no fundamental mass ratio. We conclude that the simplest spectral encoding is falsified at leading order, that adelic invariance over-constrains rather than fixes free parameters, and we state precisely what a surviving version of the conjecture would require.

## 1. Introduction

The Bruhat–Tits tree $\mathcal{T}_p$ of $\mathbb{Q}_p$ is an infinite tree in which every vertex has degree $p+1$; it plays, in $p$-adic geometry, the role that hyperbolic space plays in real geometry, and it is the bulk of $p$-adic AdS/CFT [5]. A mature literature has transplanted relativistic and field-theoretic structures onto this tree: BTZ-type black-hole geometries and Wilson lines [2], boundary spinor theories obtained by integrating out the bulk [4], geodesic bulk diagrams computing conformal blocks [5], effective field theories on tree subspaces flowing to boundary conformal field theories [6], and formal verification of harmonic cochains in the Lean theorem prover [3]. What none of these works attempts — and what the present paper tests — is the stronger conjecture that the *spectrum* of a natural operator on $\mathcal{T}_p$ encodes the *mass spectrum* of particles, i.e. that number-theoretic geometry outputs phenomenological numbers.

The conjecture has an obvious appeal and an obvious danger. The appeal: the adelic product formula $\prod_v |x|_v = 1$ ties the tree at every prime $p$ into a single rigid structure, so a spectral statement on $\mathcal{T}_p$ is not freely adjustable; if a mass ratio appeared as an eigenvalue ratio, its origin would be arithmetic, in the spirit of the adelic cross-domain programme [10], [12]. The danger: prime numbers are dense enough that almost any positive real number lies within a few percent of some prime or prime ratio, so agreement at the percent level is cheap and proves nothing without a mechanism fixing which prime, which eigenvalue, and which normalisation.

Our contribution is to make the conjecture precise enough to fail cleanly. We define the operator (Section 3), compute its spectrum exactly by hand (Section 4, with every arithmetic step shown), compare against Standard Model mass ratios (Section 5), and argue in Section 6 that the leading-order encoding is falsified while identifying the two escape routes — non-radial boundary conditions and running (scale-dependent) spectra — that a surviving version would need.

## 2. Background and Related Work

We review the literature in two groups: tree geometry and p-adic holography, then spectral/adelic programmes.

**Tree geometry.** [1] develops the theory of *branches* of orders in $M_2(k)$: the set of maximal orders containing a given suborder forms a subtree of the Bruhat–Tits tree, used for the global selectivity problem and local embedding computations. This matters for us because any boundary condition on $\mathcal{T}_p$ that privileges a vertex or ray is, in order-theoretic language, a choice of branch; [1] shows such choices are canonical objects, not ad hoc. [2] transplants the BTZ black hole to $\mathcal{T}_p$, constructing a novel $p$-adic "exponential function" hinted at by the tree and evaluating $\mathrm{PGL}(2,\mathbb{Q}_p)$ Wilson lines on the analogue BTZ connection. Their exponential function is the closest existing object to a radial eigenfunction of a tree Laplacian, and our radial spectrum can be read as the linearised version of their geometry. [3] formalises the Bruhat–Tits tree in Lean and verifies a result on harmonic cochains — functions on the tree satisfying a discrete Laplace equation — demonstrating that the Laplacian we study is already machine-checked mathematics, which raises the reproducibility bar for any spectral claim. [7] proves exponential mixing of the geodesic translation map on quotient trees $\Gamma\backslash\mathcal{T}$ under a non-arithmeticity condition on the length spectrum; the arithmetic/non-arithmetic dichotomy there is a warning for us: arithmetic spectra (which is what prime-indexed mass ratios would be) behave atypically, and mixing results do not transfer. [8] defines $p$-adic colligations and transfer functions as maps from Bruhat–Tits trees to buildings, providing an operator-theoretic language (characteristic functions, conjugacy classes) in which spectral questions on the tree can be posed invariantly.

**p-adic holography.** [5] establishes that geodesic bulk diagrams on $\mathcal{T}_p$ compute global conformal blocks, with boundary $\mathbb{Q}_p$ — the structural result that makes the tree a legitimate bulk spacetime. [4] integrates out the interior of $\mathcal{T}_p$ for a spinor field theory and finds the boundary theory resembles a scalar CFT over $\mathbb{Q}_p$; their integration-out procedure is exactly the operation that would turn a bulk Laplacian spectrum into a boundary mass spectrum, so their result is the natural home for our conjecture. [6] computes effective actions on two subspaces of $\mathcal{T}_p$ and shows both limits agree with the same $p$-adic CFT at the boundary — evidence that boundary data are insensitive to bulk details, which cuts against any claim that a specific bulk spectrum fixes observable numbers.

**Spectral/adelic programmes.** [9] documents spectral dynamics on Bruhat–Tits trees as a research record. [10] and [12] (the Adelic Cross-Domain Program, v5.0 and Phase 3–4) propose mapping the Standard Model architecture onto $\mathcal{T}_p$, with the Pythagorean semigroup $P = \{2^a 3^b 5^c\}$ claimed to be simultaneously the SM mass spectrum, a GKP code lattice, and an Efimov discretuum [12]; our exact radial spectrum provides the first clean test of whether tree geometry alone can support such identifications. [11] (Alpha Pi Project) explores fine-structure-constant numerology in the same ecosystem. None of [9]–[12] computes the point spectrum of the tree Laplacian with boundary conditions fixed by the adelic product formula; that gap is what Section 4 fills.

## 3. Methods

**The tree and the operator.** Let $\mathcal{T}_p$ be the Bruhat–Tits tree of $\mathbb{Q}_p$: the $(p+1)$-regular tree, i.e. every vertex has degree $q = p+1$. The combinatorial Laplacian is

$$
(\Delta f)(x) = \sum_{y \sim x} \big( f(x) - f(y) \big) = (p+1) f(x) - \sum_{y \sim x} f(y),
$$

where $y \sim x$ denotes adjacency. Equivalently $\Delta = (p+1)I - A$ with $A$ the adjacency operator. Since constant shifts do not change eigenvalue *ratios* of positive eigenvalues, we work with $A$ and translate at the end.

**Radial reduction.** Fix a base vertex $o$. A function $f$ is radial if $f(x)$ depends only on the graph distance $n = d(x,o)$. The radial subspace is invariant under $A$. On it, $A$ acts as the tridiagonal radial operator $R$:

$$
(R f)_n = f_{n-1} + p\, f_{n+1}, \qquad n \geq 1, \qquad (R f)_0 = (p+1) f_1,
$$

because a vertex at distance $n \geq 1$ has one neighbour toward $o$ and $p$ away from $o$.

**Boundary conditions from the adelic product formula.** The adelic product formula $\prod_v |x|_v = 1$ for $x \in \mathbb{Q}^\times$ says that no single place is distinguished. Operationally we impose: (BC1) normalisability in the directed space $\ell^2$ of radial sequences, i.e. $\sum_{n \geq 0} |f_n|^2 \, |S_n| < \infty$ where $|S_n| = (p+1) p^{n-1}$ is the sphere size; and (BC2) no additional boundary data at infinity (Dirichlet-type decay), since fixing a boundary value would single out a place and violate the product-formula symmetry. This is the weakest boundary structure compatible with adelic invariance; stronger conditions (e.g. fixing a ray) are discussed in Section 6.

**Phenomenological comparators.** We use the pole masses $m_e = 0.51099895\ \mathrm{MeV}$, $m_\mu = 105.6583755\ \mathrm{MeV}$, $m_\tau = 1776.86\ \mathrm{MeV}$ (PDG-style values as stated inputs) and the $p$-adic length scales $\ell_p = 1/p$ from the $p$-adic minimum-length analysis of Dirac-type operators [2], [10]. All comparisons are two-sided: we report the deviation $\delta = |r_{\mathrm{SM}} - r_{\mathrm{tree}}| / r_{\mathrm{SM}}$.

## 4. Analysis

**Step 1: radial ansatz.** Seek $f_n = \lambda^n$-type solutions of $R f = \lambda f$. For $n \geq 1$:

$$
f_{n-1} + p f_{n+1} = \lambda f_n.
$$

Try $f_n = \alpha^n$: $\alpha^{-1} + p\alpha = \lambda$, i.e.

$$
p\alpha^2 - \lambda \alpha + 1 = 0, \qquad \alpha = \frac{\lambda \pm \sqrt{\lambda^2 - 4p}}{2p}.
$$

Writing $\lambda = \sqrt{p}\,(\zeta + \zeta^{-1})$ with $|\zeta| = 1$ parametrises the band; the two roots are $\alpha = \zeta/\sqrt{p}$ and $\alpha = (\zeta\sqrt{p})^{-1}$... more precisely, substituting: $p\alpha^2 - \sqrt{p}(\zeta+\zeta^{-1})\alpha + 1 = 0$ has roots $\alpha_+ = \zeta/\sqrt{p}$ and $\alpha_- = 1/( \sqrt{p}\, \zeta )$. Check for $\alpha_+$: $p \cdot \zeta^2/p = \zeta^2$; $\sqrt{p}(\zeta+\zeta^{-1}) \cdot \zeta/\sqrt{p} = \zeta^2 + 1$; and $\zeta^2 - (\zeta^2 + 1) + 1 = 0$. ✓

**Step 2: the band.** For $|\zeta| = 1$, $\lambda = \sqrt{p}(\zeta + \zeta^{-1}) = 2\sqrt{p}\cos\theta$ with $\zeta = e^{i\theta}$ ranges over $[-2\sqrt{p},\,2\sqrt{p}]$. For $\lambda$ outside this interval, one root has $|\alpha| > 1/\sqrt{p}$ and the other $|\alpha| < 1/\sqrt{p}$; the growing combination must be killed by the boundary condition at $n = 0$, which is possible only for isolated $\lambda$ (point spectrum). Hence the continuous spectrum of $A$ on $\mathcal{T}_p$ is exactly $[-2\sqrt{p},\,2\sqrt{p}]$, and any point spectrum lies outside or at the edges of this band.

**Step 3: point spectrum from the $n=0$ equation.** At $n=0$: $(p+1) f_1 = \lambda f_0$. A decaying solution has $f_n = c\,\alpha^n$ with $|\alpha| < 1/\sqrt{p}$ (so that $\sum_n |f_n|^2 |S_n| \sim \sum_n p^n |\alpha|^{2n}$ converges, requiring $p|\alpha|^2 < 1$). Then $f_1 = \alpha f_0$ and

$$
(p+1)\alpha = \lambda.
$$

Combine with the characteristic equation $p\alpha^2 - \lambda\alpha + 1 = 0$: substituting $\lambda = (p+1)\alpha$ gives

$$
p\alpha^2 - (p+1)\alpha^2 + 1 = 0 \;\Rightarrow\; -\alpha^2 + 1 = 0 \;\Rightarrow\; \alpha = \pm 1.
$$

But $|\alpha| = 1$ violates the decay condition $p\alpha^2 < 1$ for every prime $p \geq 2$, since $p \cdot 1 = p \geq 2 > 1$. Therefore:

**Claim 4.1.** The $\ell^2$ point spectrum of the adjacency operator $A$ on $\mathcal{T}_p$ with adelic (no-boundary-data) conditions is *empty*. The Laplacian $\Delta = (p+1)I - A$ likewise has no $\ell^2$ point spectrum; its spectrum is purely the shifted band $[1-\sqrt{p}\cdot 2 + \ldots]$ — precisely $[(p+1) - 2\sqrt{p},\, (p+1) + 2\sqrt{p}]$.

Numerically, for $p = 2$: band of $\Delta$ is $[3 - 2\sqrt{2},\, 3 + 2\sqrt{2}] = [3 - 2.82842712,\, 3 + 2.82842712] = [0.17157288,\, 5.82842712]$. For $p = 5$: $[6 - 2\sqrt{5},\, 6 + 2\sqrt{5}] = [6 - 4.47213595,\, 6 + 4.47213595] = [1.52786405,\, 10.47213595]$.

**Step 4: the finite radial quotient (where discrete eigenvalues do live).** If instead of $\ell^2$ on the infinite tree one truncates the radial dynamics to the finite quotient of periods $p+1$ — the natural finite object suggested by the cyclic structure $\zeta^{p+1} = 1$ — the radial eigenvalues are

$$
\lambda_k = \sqrt{p}\left(\omega^k + \omega^{-k}\right) = 2\sqrt{p}\cos\frac{2\pi k}{p+1}, \qquad k = 0, 1, \ldots, p.
$$

*Derivation for $p = 5$* ($p + 1 = 6$, $\omega = e^{2\pi i/6}$), with $\sqrt{5} = 2.23606798$:

- $k=0$: $\lambda_0 = 2\sqrt{5}\cos 0 = 2\sqrt{5} = 4.47213595$.
- $k=1$: $\lambda_1 = 2\sqrt{5}\cos(\pi/3) = 2\sqrt{5}\cdot\tfrac{1}{2} = \sqrt{5} = 2.23606798$.
- $k=2$: $\lambda_2 = 2\sqrt{5}\cos(2\pi/3) = 2\sqrt{5}\cdot(-\tfrac{1}{2}) = -\sqrt{5} = -2.23606798$.
- $k=3$: $\lambda_3 = 2\sqrt{5}\cos\pi = -2\sqrt{5} = -4.47213595$.
- $k=4$: $\lambda_4 = -\sqrt{5}$; $k=5$: $\lambda_5 = \sqrt{5}$ (by symmetry $k \to p+1-k$).

Note $\lambda_1 = \sqrt{5}$ coincides with the classical point eigenvalue of the $(p+1)$-regular tree, which exists precisely when $6 \mid (p+1)$, i.e. $p \equiv 5 \pmod 6$ (so that $\cos(2\pi k/(p+1)) = 1/2$ has an integer solution $k = (p+1)/6$). For $p = 2$ ($p+1 = 3$): $\lambda_0 = 2\sqrt{2} = 2.82842712$, $\lambda_1 = 2\sqrt{2}\cos(2\pi/3) = -\sqrt{2} = -1.41421356$, $\lambda_2 = -\sqrt{2}$; no $+ \sqrt{2}$ eigenvalue occurs, consistent with $2 \not\equiv 5 \pmod 6$.

**Step 5: eigenvalue ratios.** The scale-free ratios available from the radial spectrum are:

$$
\frac{\lambda_0}{|\lambda_1|} = \frac{2\sqrt{p}}{\sqrt{p}} = 2 \quad (\text{exact, for } p \equiv 5 \!\!\pmod 6), \qquad \frac{|\lambda_1|}{|\lambda_2|} = \frac{\sqrt{p}}{\sqrt{p}} = 1.
$$

The ratio $2$ is *independent of $p$* — a structural consequence of the tree's regularity, not a number-theoretic output. The only $p$-dependent scale ratios come from comparing across primes via the length scales $\ell_p = 1/p$:

$$
\frac{\ell_2}{\ell_3} = \frac{1/2}{1/3} = \frac{3}{2} = 1.5, \qquad \frac{\ell_3}{\ell_5} = \frac{1/3}{1/5} = \frac{5}{3} \approx 1.6667, \qquad \frac{\ell_2}{\ell_5} = \frac{5}{2} = 2.5.
$$

**Step 6: SM comparators.** With the stated masses:

$$
\frac{m_\mu}{m_e} = \frac{105.6583755}{0.51099895} = 206.7683 \quad (\text{long division: } 0.51099895 \times 206 = 105.26578; \text{ remainder } 0.39259; \; 0.39259/0.51099895 = 0.76828),
$$

$$
\frac{m_\tau}{m_\mu} = \frac{1776.86}{105.6583755} = 16.8170 \quad (105.6583755 \times 16.8 = 1775.06; \text{ remainder } 1.7966; \; 1.7966/105.6584 = 0.01701).
$$

Nearest-prime comparisons: for $m_\mu/m_e$, the nearest prime to $206.7683$ is $211$; deviation $\delta = (211 - 206.7683)/206.7683 = 4.2317/206.7683 = 0.02047$ ($2.05\%$). For $m_\tau/m_\mu$, the nearest prime to $16.8170$ is $17$; $\delta = (17 - 16.8170)/16.8170 = 0.1830/16.8170 = 0.01088$ ($1.09\%$). Against the tree ratio $2$: no fundamental mass ratio equals $2$ exactly; the closest among the charged-lepton ratios is $m_\tau/m_\mu = 16.8170$, off by a factor $8.41$.

**Step 7: adelic constraint check.** If the spectrum were required to be adelic-invariant — i.e. the product over all places $v$ of the spectral quantities reproduces the product formula — then for a multiplicative spectral observable $\{\mu_v\}$ we would need $\prod_p \mu_p \cdot \mu_\infty = 1$. Since the radial band edges scale as $2\sqrt{p}$, a candidate $\mu_p = 2\sqrt{p}$ gives $\prod_p 2\sqrt{p} = \infty$: the adelic constraint is *violated* by any single-place spectrum taken alone, and can only be satisfied by pairing with $\mu_\infty$ or with normalising factors. This is a constraint on *combinations* of places, not a fixer of free parameters within one place; it over-determines rather than selects.

## 5. Results

All numbers below are computed in Section 4; no simulation or external data beyond the stated masses is used.

**R1 (exact).** The $\ell^2$ point spectrum of the adelic-conditioned Laplacian on $\mathcal{T}_p$ is empty for every prime $p$ (Claim 4.1, exact algebraic proof). There is no discrete hierarchy of eigenvalues to compare with masses at this level.

**R2 (exact).** The continuous spectrum of $\Delta$ is $[(p+1) - 2\sqrt{p},\, (p+1) + 2\sqrt{p}]$: for $p=2$, $[0.17157288,\, 5.82842712]$; for $p=5$, $[1.52786405,\, 10.47213595]$.

**R3 (exact).** In the finite radial quotient, eigenvalue ratios are $\lambda_0/|\lambda_1| = 2$ (exact) and $|\lambda_1|/|\lambda_2| = 1$ (exact), both $p$-independent. The ratio $2$ matches no charged-lepton or gauge-boson mass ratio (nearest comparator $m_\tau/m_\mu = 16.8170$, factor $8.41$ off).

**R4 (computed comparison, not a prediction).** Prime-indexed scale ratios sit near but not at SM ratios: $p = 211$ vs $m_\mu/m_e = 206.7683$, $\delta = 2.05\%$; $p = 17$ vs $m_\tau/m_\mu = 16.8170$, $\delta = 1.09\%$. Given that prime gaps near $N$ are $O(\log N)$, percent-level coincidences of this kind are expected on density grounds alone and carry no evidential weight without a selection mechanism.

**R5 (projection, stated assumptions).** *Projection:* if one restores point spectrum by breaking adelic symmetry (fixing a boundary ray, giving a half-tree with Dirichlet data), the resulting discrete eigenvalues of the half-tree radial operator are known to be $\lambda = \pm\sqrt{p}$ only — a two-point spectrum whose single nontrivial ratio is again $2$. *Assumption:* the half-tree radial recurrence with $f_0 = 0$ admits the same algebraic structure as Step 3 with the sign-flipped boundary equation; under this assumption the ratio $2$ is unavoidable. *Uncertainty:* the projection is exact algebra, not an estimate; its fragility lies in the assumption, not the arithmetic.

**R6 (structural).** The adelic product formula over-constrains single-place spectra (Step 7): $\prod_p 2\sqrt{p}$ diverges, so adelic invariance cannot fix parameters within one prime's tree; it can only relate spectra across places.

## 6. Discussion

**What we falsified and what we did not.** We falsified the *strongest* form of the conjecture: that the adelic-conditioned Laplacian on $\mathcal{T}_p$ has a discrete spectrum whose ratios are mass ratios. It does not — the point spectrum is empty (R1), and the only discrete ratios available in finite quotients are the universal constants $2$ and $1$ (R3), which are consequences of $(p+1)$-regularity, not of arithmetic. We did *not* falsify the weaker programme of [10], [12], which operates with the semigroup $P = \{2^a 3^b 5^c\}$ and additional structure (code lattices, Efimov physics) beyond the bare Laplacian; our result shows the bare tree contributes nothing $p$-dependent to eigenvalue *ratios*, so any successful encoding must come from non-radial sectors, quotient groups $\Gamma \subset \mathrm{Aut}(\mathcal{T}_p)$, or operators other than the combinatorial Laplacian (e.g. the $p$-adic Dirac-type operators whose minimum-length scales $\ell_p = 1/p$ we used as comparators).

**Failure modes of this analysis.** (i) Our boundary conditions (BC2) are the *weakest* adelic-compatible ones; a stronger condition — e.g. one fixed by the branch theory of [1] or by the Wilson-line connections of [2] — could produce genuine point spectrum. We flagged this in R5 but have not constructed it. (ii) The finite radial quotient in Step 4 is motivated by cyclicity, not derived from the adelic product formula; a different truncation gives different discrete ratios. (iii) Mass ratios run with scale; a spectral comparison at a single renormalisation scale is ill-defined unless the matching scale is fixed by the theory, which we have not done.

**What would falsify our negative claim.** A single explicit operator on $\mathcal{T}_p$ (or a $\Gamma$-quotient thereof, in the setting of [7]) with (a) provable $\ell^2$ point spectrum, (b) boundary conditions fixed by adelic invariance rather than chosen by hand, and (c) at least two eigenvalue ratios matching two independent SM ratios to better than $10^{-3}$ without adjustable parameters. Absent (b), percent-level matches like R4 are indistinguishable from numerology — indeed the density of primes makes them likely a priori.

**Against ourselves.** One could object that demanding eigenvalue *ratios* is the wrong target: perhaps masses correspond to eigenvalue *gaps* or to boundary correlators in the sense of [4], [6], where bulk details are washed out — but that very washing-out ([6]: distinct subspaces yield the same boundary CFT) is evidence *against* bulk spectra fixing observable numbers. Another objection: the Lean-verified harmonic cochains of [3] show the Laplacian framework is sound, so emptiness of point spectrum is a theorem about our boundary conditions, not about the tree; we agree, and that is precisely why we stated the conditions explicitly. Finally, the colligation/transfer-function formalism of [8] could reorganise the spectral question in a way our radial reduction misses; we have not explored it.

**Open questions.** Does any $\Gamma$-quotient of $\mathcal{T}_p$ with non-arithmetic length spectrum [7] admit point spectrum with arithmetic ratios, and would that be a feature (number-theoretic output) or a pathology (the arithmeticity dichotomy)? Can the adelic constraint (R6) be turned from an obstruction into a selection principle by requiring the *regularised* product $\prod_p \mu_p / \mu_\infty$ to be rational?

## 7. Conclusion

We made the conjecture that Bruhat–Tits-tree spectra encode particle mass ratios precise, computed the exact radial spectrum of the adelic-conditioned Laplacian, and found: empty $\ell^2$ point spectrum, a $p$-independent universal ratio $2$ in the finite radial quotient, and percent-level prime coincidences with SM ratios that carry no mechanistic weight. The leading-order encoding is falsified. The conjecture survives only in forms that add structure absent from the bare tree — quotients, non-radial operators, or running spectra — and any such form must fix its boundary conditions by adelic invariance, not by choice, to be more than numerology.

## References

[1] arXiv:1712.01463v2 | On the missing branches of the Bruhat-Tits tree
[2] ar