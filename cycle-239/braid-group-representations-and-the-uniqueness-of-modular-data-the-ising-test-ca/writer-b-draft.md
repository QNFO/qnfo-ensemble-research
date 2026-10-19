# Braid Group Representations and the Uniqueness of Modular Data: The Ising Test Case and General Limitations (Revised)

## Abstract

We investigate whether the unitary braid group representation carried by a collection of non-Abelian anyons uniquely determines the modular data — the $S$ and $T$ matrices — of the underlying modular tensor category (MTC). Using the Ising anyon theory as a concrete laboratory, we reconstruct the full modular data from the elementary braid eigenvalue $R_{\sigma\sigma}=e^{-i\pi/8}$ together with the fusion rule $\sigma\times\sigma=1+\psi$. Explicit arithmetic yields the quantum dimension $d_\sigma=\sqrt{2}\approx1.4142$, the total quantum dimension $D=2$, the $S$-entries $S_{\sigma 1}=\sqrt{2}/2\approx0.7071$, $S_{\sigma\psi}=-\sqrt{2}/2\approx-0.7071$, $S_{\sigma\sigma}=0$, and the $T$-entry $T_{\sigma\sigma}=e^{i\pi/8}\approx0.9239+0.3827\,i$. We also compute the fusion-space dimensions $f(n,1)=2^{n/2-1}$ for even $n$, the braid generator's ordinary order $16$ (projective order $4$), and the three-anyon quantum trace $\operatorname{Tr}\rho_3(\sigma_1)=\sqrt{2}\,e^{i\pi/8}\approx1.3066+0.5412\,i$. Against these positive results we set the structural limits reported in the literature: finite-image braid representations, the $\mathrm{Ising}(7)$ deformation family with identical fusion rules but $\theta_\sigma=e^{7i\pi/8}$, and the spin-structure dependence of the global $S$-matrix. We conclude that braiding determines the fusion ring and the $S$-matrix of the Ising category exactly, while $T$ retains a finite ambiguity tied to the gravitational anomaly, and that no constructive collision of two MTCs with identical braid images and distinct modular data is currently established.

## 1. Introduction

Topological phases of matter support anyonic excitations whose adiabatic exchange is described by a unitary representation of the braid group $B_N$ [3]. A modular tensor category encodes the full topological data in its modular $S$ and $T$ matrices, which together determine fusion rules, quantum dimensions, and braiding phases [12]. The question addressed here is whether the braid representation on $N$ anyons suffices to reconstruct $S$ and $T$ uniquely.

The practical stakes are concrete. Two-dimensional topological superconductors host vortices that bind Majorana zero modes (MZMs), self-adjoint fermionic operators $\gamma_i=\gamma_i^\dagger$ obeying the Clifford algebra $\{\gamma_i,\gamma_j\}=2\delta_{ij}$; exchanging vortices $i$ and $j$ acts on the ground-state manifold by $U_{ij}=\exp(\frac{\pi}{4}\gamma_i\gamma_j)$, yielding a projective braid representation [11]. If these braid operations uniquely fixed the modular data, braiding alone could certify the underlying topological order of a Majorana chip, and classification programs for MZM fusion rules could dispense with complementary probes. If they do not, additional measurements — for example the interferometric protocols analyzed for non-Abelian anyons in impurity systems [7] — are required, and the certification budget of an experiment must include them. Today the choice between these two program designs is made without a settled answer: the prior version of this work claimed a "partial uniqueness theorem" for dense braid images, but also asserted, without constructive proof, that distinct MTCs share identical braid matrices with different $S$ matrices. Both the positive mechanism and the negative claims need to be stated at the level that the derivations and the literature actually support.

This revision tightens both directions. On the positive side, the Ising reconstruction is carried through with every arithmetic step explicit, and the three-anyon quantum trace is added as an independent cross-check. On the negative side, the non-uniqueness claims are re-anchored to what the sources establish: finiteness of certain braid images, an explicit deformation family with shared fusion rules, and the spin-structure dependence of the global $S$-matrix — while recording, as the source itself does, that no constructive collision of two MTCs with *identical* full projective braid images and distinct $(S,T)$ has been produced [9].

The contributions are:

1. A fully explicit reconstruction of the Ising modular data $(S,T)$ from the braid eigenvalue $R_{\sigma\sigma}=e^{-i\pi/8}$ and the fusion rule $\sigma\times\sigma=1+\psi$, with all arithmetic shown (Sections 3 and 4).
2. Derived auxiliary quantities: fusion-space dimensions $f(n,1)=2^{n/2-1}$ for even $n$, the braid generator orders $16$ (ordinary) and $4$ (projective), and the quantum trace $\operatorname{Tr}\rho_3(\sigma_1)=\sqrt{2}\,e^{i\pi/8}$ (Section 4).
3. A corrected assessment of non-uniqueness: finite-image families, the $\mathrm{Ising}(7)$ deformation with trace ratio $e^{-3i\pi/4}$, and spin-structure dependence, each attributed to its source and each qualified by that source's own stated limitations (Sections 2, 5 and 6).
4. A falsifiability analysis and a statement of what braiding does and does not fix for Majorana-based classification programs (Sections 6 and 7).

## 2. Background and Related Work

The braid group $B_N$ on $N$ strands is generated by elementary exchanges $\sigma_1,\ldots,\sigma_{N-1}$ satisfying the braid relations $\sigma_i\sigma_j=\sigma_j\sigma_i$ for $|i-j|\geq2$ and $\sigma_i\sigma_{i+1}\sigma_i=\sigma_{i+1}\sigma_i\sigma_{i+1}$; a unitary representation $\rho:B_N\to U(V)$ arises from the braiding of $N$ identical anyons, with $\dim V$ fixed by the fusion multiplicities $N_{aa\ldots a}^{c}$ [12]. The same relations appear beyond the planar setting: for anyons on graphs, an exchange of two quasiparticles multiplies a single-component wave function by a phase $e^{i\theta}$, $\theta\in\,]0,\pi[$, and the graph braid group $Br_N(\Gamma)$ is finitely presented with generators and relators of the same braid form; notably, the abelianisation satisfies $H_1(C_N(\Gamma),\mathbb{Z})\cong\mathbb{Z}^{m}\oplus(\mathbb{Z}_2)^{p}$ with $p=0$ if and only if the graph $\Gamma$ is planar, so the topology of the embedding space already changes the group whose representations carry the statistics [3]. This matters for the uniqueness question because any restriction of the braid data to a subgroup — planar or graph-based — can only reduce what braiding can probe.

On the modular side, a unitary MTC has simple objects with fusion rules $a\times b=\sum_c N_{ab}^{c}\,c$, associativity governed by $F$-symbols $F^{abc}_{d}$ and braiding by $R$-symbols $R^{ab}_c$, subject to the pentagon and hexagon equations; the modular $S$-matrix is defined by the Hopf link invariant and $T$ is diagonal with entries $T_{aa}=\theta_a$, the topological spins [12]. The same source concludes that the braid representation constrains the modular data up to finite gauge ambiguity but does not uniquely determine the global $S$-matrix without specifying the underlying spin structure, while the local MZM braid operator $\rho(\sigma_i)=\frac{1}{\sqrt{2}}(1+\gamma_{i+1}\gamma_i)$ uniquely fixes the local $F$ and $R$ symbols of the Ising category [12]. That split — local data fixed, global data spin-structure-dependent — is the central structural fact against which the Ising computation below must be read.

The Ising case itself has been worked in the QNFO literature from several angles. One report derives the Ising modular data $T=\operatorname{diag}(1,e^{i\pi/8},-1)$ and $S=\frac{1}{2}\begin{pmatrix}1&\sqrt{2}&1\\ \sqrt{2}&0&-\sqrt{2}\\ 1&-\sqrt{2}&1\end{pmatrix}$, verified against the ribbon identity, hexagon equations, $S^2=C$, and $STS^{-1}$ diagonalization; it also reports the three-anyon trace $\operatorname{Tr}\rho_3(\sigma_1)=\sqrt{2}\,e^{i\pi/8}$ with magnitude $\sqrt{2}=d_\sigma$, and a deformation family $\mathrm{Ising}(7)$ that shares all fusion rules with Ising but has $\theta_\sigma=e^{7i\pi/8}$ and a $B_3$ representation inequivalent to Ising's, with trace ratio $e^{-3i\pi/4}$ [9]. Critically, the same report states in its own discussion that "finite image" does not by itself prove "non-unique modular data", that its non-uniqueness assessment is an existence-of-room argument plus a concrete deformation family rather than a constructive collision, and that symmetry-enriched orders may evade the analysis because global symmetries can modify braiding without altering the underlying unitary braided fusion category [9]. The predecessor of the present paper performed the two-anyon reconstruction and computed the fusion-space dimensions and braid orders, concluding that braiding determines the fusion ring and $S$ matrix but requires independent parity or anomaly input to fix $T$ [10].

The Majorana-specific classification reports sharpen the ambiguity. One derives the Ising $S$ matrix from fusion rules and the braid-fixed twist $\theta_\sigma=e^{i\pi/8}$ via the Verlinde formula, verifies unitarity by explicit inner-product computation of all six row pairs, and states that the $T$ matrix is determined by the braid representation up to the finite ambiguity $\theta_\sigma\to e^{i\pi k/4}\theta_\sigma$, $k$ odd; its discussion concedes that no general determinacy theorem is proven — only the mechanism is exhibited — and that for higher-rank candidates the braid representation on small $N$ may under-determine the twists [11]. A companion report frames the same question for MZM fusion rules and concludes that the fusion rules are rigidly classified as Ising type ($\sigma\times\sigma=1+\psi$) with no alternative non-Abelian fusion rules consistent with the Majorana Clifford algebra and the super-modular structure, while the global $S$-matrix depends on the spin structure of the underlying manifold [12].

Two further strands bound the scope of braid-based inference. First, numerical extraction of modular data is possible but not braid-only: the tensor-network work on braided non-Abelian anyons constructed modified numerical algorithms based on tensor networks to simulate systems of anyons in low dimensions and used those methods to study the topological phases the anyons form when they braid around one another [1]; such simulations take the underlying anyon theory as input, so they corroborate modular data rather than replace its independent measurement. Second, braid-type group structures arise in settings far from topological order — for instance, the double affine Hecke algebra of type $C^\vee C_1$ is built from the fundamental group of a four-punctured sphere, generated by $T_0,T_0^{\vee},T_1,T_1^{\vee}$ with the relation deformed to $T_0^{\vee}T_0T_1T_1^{\vee}=q^{-1/2}$ [4] — a reminder that a braid presentation alone, without the ribbon and hexagon constraints of an MTC, carries far less information than modular data.

On the experimental side, a quantum-impurity-based protocol for braiding non-Abelian anyons has been analyzed that exploits mobile impurities with addressable internal spin states and provides a concrete protocol to experimentally measure the matrix elements of the $R$ (and related) operators [7]. This is the kind of complementary measurement that Section 7 identifies as the minimal next step for resolving the $T$-matrix ambiguity in practice.

Collectively, the literature supports a two-sided conclusion: braiding fixes a large and computable part of the modular data in the canonical case, but the sources themselves qualify every generalization of that fixity, and none claims a proof that braid representations are injective on modular data in general.

## 3. Methods

The reconstruction proceeds in three steps, applied to the Ising MTC whose braid eigenvalue $R_{\sigma\sigma}=e^{-i\pi/8}$ is the quantity accessed by Majorana braid operations [11] and by the impurity-based measurement protocols analyzed for non-Abelian anyons [7]. The fusion rules are $\sigma\times\sigma=1+\psi$, with $1$ and $\psi$ Abelian and $\psi$ a fermion.

**Step 1: Extract braid eigenvalues.** For a simple object $a$, the elementary braid generator $R_{aa}$ acts on the two-anyon fusion space $V_{aa}=\bigoplus_c N_{aa}^{c}\,V_c$ with eigenvalues $R^{aa}_c$, and the ribbon (monodromy) relation gives

$$
\left(R^{aa}_c\right)^2 = \frac{\theta_c}{\theta_a^2},
$$

where $\theta_x$ is the topological spin of $x$ [12]. Measuring the single-exchange eigenvalues on each fusion channel therefore determines the ratios $\theta_c/\theta_a^2$.

**Step 2: Determine quantum dimensions.** The quantum dimension $d_a$ obeys $d_a^2=\sum_c N_{aa}^{c}\,d_c$ for the generating object of the fusion ring; more generally $d_a$ is the largest eigenvalue of the fusion matrix. The total quantum dimension is

$$
D=\sqrt{\sum_x d_x^2}.
$$

**Step 3: Construct $S$ and $T$.** The $T$ matrix is diagonal with entries $T_{aa}=\theta_a$ [12]. The $S$ matrix is computed from the ribbon formula

$$
S_{ab}=\frac{1}{D}\sum_c N_{ab}^{c}\,d_c\,\frac{\theta_c}{\theta_a\,\theta_b},
$$

which is the Hopf-link definition of $S$ in the conventions of [12]; for $a=1$ it reduces to $S_{1b}=d_b/D$, and it satisfies unitarity $\sum_x S_{ax}S_{bx}^{*}=\delta_{ab}$ and the Verlinde formula

$$
N_{ab}^{c}=\sum_x \frac{S_{ax}S_{bx}S_{cx}^{*}}{S_{1x}}.
$$

Every quantity computed in Section 4 follows from these three steps with the inputs of Table 1; no simulation, measurement or numerical experiment is performed in this paper, and all numbers are exact algebraic values evaluated to four decimal places where stated.

## 4. Analysis

###