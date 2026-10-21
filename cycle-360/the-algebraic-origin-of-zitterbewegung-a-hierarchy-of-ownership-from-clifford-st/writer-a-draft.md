# The Algebraic Origin of Zitterbewegung: A Hierarchy of Ownership from Clifford Structure to Observed Oscillation

## Abstract

Zitterbewegung (ZB) – the rapid trembling of a relativistic quantum particle’s position – is usually presented as a representation‑specific artifact of the Dirac equation, leaving experimentalists without a general criterion for when the oscillation must appear. The specific gap addressed here is the absence of a representation‑independent statement of why the oscillation exists: whether it is a consequence of the particular $4\times4$ Dirac matrices, of spacetime geometry, or of a deeper algebraic fact that survives in any dimension or representation. We formulate a hierarchy of “ownership” (algebra, calculus, trigonometry, geometry) and show, by explicit operator derivation on a Clifford module, that the oscillation is owned by the algebra: the anticommutator $\{H,\alpha_j\}=2cp_j$ forces the velocity operator to evolve as $\alpha_j(t)=cp_jH^{-1}+Z_j e^{-2iHt/\hbar}$, producing interference between positive‑ and negative‑energy eigenspaces at the beat frequency $\omega_{\mathrm{ZB}}=(E_{+}-E_{-})/\hbar$. We generalize the exact solution to arbitrary Clifford algebras and to any Hamiltonian whose velocity operators fail to commute with the Hamiltonian through Clifford structure. Numerical evaluation yields a rest‑frame electron frequency $f_{0}=2.471\times10^{20}\,\mathrm{Hz}$ with amplitude $1.931\times10^{-13}\,\mathrm{m}$, and for an illustrative gapped Dirac material ($\Delta=0.1\,$eV) a frequency $f=4.836\times10^{13}\,\mathrm{Hz}$. The result converts ZB from a Dirac‑equation curiosity into a spectral diagnostic: suppressing one eigenspace eliminates the oscillation, a falsifiable signature for existing quantum‑simulator platforms.

## 1. Introduction

Experimental teams operating quantum simulators of relativistic dynamics – cold‑atom laboratories implementing Dirac‑like laser couplings, spin‑orbit‑coupled materials, and trapped‑ion analogues – routinely observe rapid oscillatory motion of their wave packets and must decide whether that motion is genuine Zitterbewegung, an artifact of the drive scheme, or a controllable resource. This decision matters because if the oscillation is on resonance with an applied modulation it can be converted into directed centre‑of‑mass motion, stopped, or re‑launched, as demonstrated for Dirac‑like equations in the analysis of arXiv:1105.2884 [1]; cold‑atom implementations show that external fields can suppress or enhance the amplitude and shift the frequencies [2], and driven mirror oscillation can control amplitude, frequency, and damping [4]. Today, interpretation of these oscillations rests on familiarity with one specific equation – the $4\times4$ free Dirac Hamiltonian in the standard representation. A practitioner working with a spin‑1 cold‑atom system [2], a tripod‑scheme laser system [4], or a two‑band condensed‑matter analogue has no general criterion telling them whether an observed oscillation is algebraically forced or incidental to their model.

The cost of this gap is concrete: experimental design proceeds by analogy rather than by principle. A general criterion would change simulator practice in two ways. First, it would tell an experimentalist in advance which degrees of freedom must be populated for the oscillation to exist – namely, coherent superpositions across two eigenspaces of the Hamiltonian – so that state preparation can either guarantee or deliberately suppress ZB. Second, it would identify the oscillation frequency as a spectroscopic observable: a direct measurement of the inter‑eigenspace energy splitting, independent of the representation used to engineer the Hamiltonian.

This paper addresses that gap with a hierarchy‑of‑ownership conjecture, stated up front so that its status is clear. We conjecture that Zitterbewegung oscillation is fundamentally an algebraic/spectral fact: it arises whenever a velocity operator fails to commute with the Hamiltonian because of Clifford‑algebraic structure, independent of dimension or representation. Calculus merely produces the solution of the resulting operator differential equation; trigonometry is only the notation in which the solution is written; geometry is a visualizable shadow of an interference phenomenon that exists without any picture. The claim is testable: if the algebraic account is right, then removing the negative‑energy (or, generally, the second‑eigenspace) component of a wave packet must eliminate the oscillation, in any platform, at any dimension.

The contributions are:

- **C1.** A closed‑form operator derivation of the velocity and position dynamics, $\alpha_j(t)=cp_jH^{-1}+Z_j e^{-2iHt/\hbar}$ and the corresponding position decomposition, from the single algebraic input $\{H,\alpha_j\}=2cp_j$, with the anticommutator shown to be a Clifford identity (Section 3).
- **C2.** A generalization theorem: for any Hamiltonian on a Clifford module whose velocity operators are Clifford generators, the oscillation exists exactly when two eigenspaces are coherently populated, and its frequency always equals the inter‑eigenspace beat frequency $(E_{+}-E_{-})/\hbar$ (Section 3, proved in Section 4).
- **C3.** Fully worked numerical evaluations of the rest‑frame electron case ($f_{0}=2.471\times10^{20}$ Hz, amplitude $1.931\times10^{-13}$ m) and of an illustrative gapped Dirac material ($f=4.836\times10^{13}$ Hz at $\Delta=0.1$ eV), with every arithmetic step shown (Section 4).
- **C4.** A falsifiable experimental signature – eigenspace‑filtered wave‑packet dynamics – and an assessment of readiness, blockers, and the smallest next test on existing simulator platforms (Sections 6 and 7).

## 2. Background and Related Work

The Zitterbewegung phenomenon has been studied in several contexts as the jittering centre‑of‑mass motion predicted by free‑space Dirac or Dirac‑like equations. The work of arXiv:1105.2884 [1] shows that ZB can be converted into directed centre‑of‑mass motion by a modulation of the Dirac‑like equation when the modulation is on resonance with the ZB frequency, and that tailored modulation may also stop or re‑launch the motion. This directly evidences that the oscillation frequency is an operationally accessible parameter, which the present algebraic analysis identifies as a beat frequency.

On the experimental side, arXiv:1210.5030 [2] investigates the ZB effect in spin‑orbit‑coupled spin‑1 ultracold atoms in the presence of a Zeeman field and a harmonic trap, showing that the Zeeman field can suppress or enhance the ZB amplitude and change the oscillation frequencies. The survival of ZB in a spin‑1 system – a different spin dimensionality from the spin‑½ Dirac case – supports the central claim that the oscillation is not owned by the specific $4\times4$ Dirac matrices.

arXiv:1003.3074 [4] considers mirror oscillation in a “tripod‑scheme” laser‑atom system and shows, analytically and numerically, that mirror oscillation drives an effective spin‑orbit interaction and thereby controls the amplitude, frequency, and damping of cold‑atom ZB. Together, [2] and [4] establish that ZB is a controllable, platform‑portable phenomenon; what neither supplies, within the supplied summaries, is a representation‑independent account of why it occurs – the gap this paper fills.

A broad research program attributes structural features of physics to algebra rather than to dynamics or geometry, and our hierarchy conjecture places ZB inside that program. arXiv:2009.08489 [3] argues that quantum probabilities have a purely algebraic origin, distinct from classical probabilities that arise from an assumed probability measure. This supports the methodological stance that quantum phenomena can be owned by algebra at a level deeper than the calculus used to solve for them.

In high‑energy theory, arXiv:hep‑th/0307046 [5] describes an algebraic construction, via a procedure called twining that breaks the quasi‑bialgebra structure of universal enveloping algebras of semi‑simple Lie algebras, aimed at categories supporting a state‑confinement principle. We cite it as an instance of an algebra‑first explanation of a physical phenomenon.

arXiv:2105.02115 [6] shows that for central potentials, both the fourth component of a Lorentz vector and a Lorentz scalar in the Dirac Hamiltonian give rise, through the conserved Dirac spin‑orbital matrix, to Witten’s $N=2$ superalgebra, with the generators’ commutativity with the Dirac Hamiltonian studied under an invariance requirement. This is the closest structural relative of our result: it finds hidden algebra governing the Dirac Hamiltonian, though for potentials rather than for the kinetic velocity operators.

Further afield, the algebraic‑origin program spans integrable systems and field theory. arXiv:hep‑th/9408104 [7] presents an affine $sl(n+1)$ algebraic construction of the basic constrained KP hierarchy, analyzed via two equivalent approaches – a linear matrix eigenvalue problem on a hermitian symmetric space and a constrained KP Lax formulation – and identifies the model as the generalized non‑linear Schrödinger hierarchy. arXiv:hep‑th/0007032 [8] takes a combinatorial formula of G.-C. Rota and J. A. Stein to perform Wick re‑ordering in quantum field theory, so that Wick’s theorem becomes a Hopf‑algebraic identity called Cliffordization; the appearance of a Clifford‑type structure as an efficient computational device in field theory is a useful precedent for our claim that Clifford structure, not the specific Dirac representation, carries the physical content.

arXiv:0809.1086 [9] treats the Lie‑algebraic origin of metric 3‑algebras in three‑dimensional superconformal Chern‑Simons theories, noting that many such theories admit reformulation as standard gauge theory coupled to matter in which the 3‑algebra does not appear explicitly – a cautionary parallel, since it shows that an algebraic formulation can be a choice of description rather than a uniqueness claim; our hierarchy conjecture must therefore be argued for, not assumed.

arXiv:1306.0174 [10] shows that there exist simple groups with a spherical BN‑pair of rank 2 which are non‑Moufang and hence not of algebraic origin. This reminds us that “algebraic origin” is a substantive property that can fail; our falsification criterion in Section 6 is designed so that a platform exhibiting ZB without the two‑eigenspace interference structure would refute the conjecture in the same way.

Finally, three QNFO corpus entries sit adjacent to this work. The entry “Zitterbewegung: From Archimedean Puzzle to Adelic Observable” [12] states that the structural underdetermination of the position operator arises from a representation‑theoretic origin called the Silent Parameter Principle, and that a 2‑adic ZB frequency deviates from the Archimedean value; the summary truncates mid‑sentence and supplies no further detail, so we use it only as evidence that the position operator’s ambiguity and the ZB frequency are both recognized as structural, not dynamical, puzzles. The entry “Five Pillars, One Structure” [13] reports that five independent QNFO research programs converge on ultrametric (non‑Archimedean) mathematics as the correct state‑space geometry for fundamental physics; and “The Ultrametric Foundation” [14] argues that positional notation is inherently an ultrametric tree of nested cycles and that the Archimedean line is a derived abstraction. These entries propose a non‑Archimedean setting in which the present paper’s Archimedean beat‑frequency statement would require re‑derivation; we flag this as an open question in Section 6 rather than importing their conclusions, since their supplied summaries do not contain the technical machinery needed to do so.

## 3. Methods

### 3.1 Setting: the Dirac Hamiltonian as a Clifford‑module operator

We work in the Heisenberg picture with $\hbar$ explicit. The free Dirac Hamiltonian is

$$
H = c\,\boldsymbol{\alpha}\cdot\mathbf{p} + \beta\, mc^{2},
$$

where $\mathbf{p}=(p_{1},p_{2},p_{3})$, $m$ is the rest mass, $c$ the speed of light, and $\alpha_{j},\beta$ are Hermitian matrices satisfying the Clifford relations

$$
\alpha_{j}\alpha_{k}+\alpha_{k}\alpha_{j}=2\delta_{jk}\,\mathbb{1},\qquad
\alpha_{j}\beta+\beta\alpha_{j}=0,\qquad
\beta^{2}=\mathbb{1}.
$$

The single algebraic input of the whole derivation is the anticommutator of the Hamiltonian with a velocity generator. Direct expansion using the Clifford relations gives

$$
\{H,\alpha_{j}\}=H\alpha_{j}+\alpha_{j}H
= c\bigl(\boldsymbol{\alpha}\!\cdot\!\mathbf{p}\,\alpha_{j}+\alpha_{j}\,\boldsymbol{\alpha}\!\cdot\!\mathbf{p}\bigr)
+ mc^{2}(\beta\alpha_{j}+\alpha_{j}\beta).
$$

The $\beta$ terms vanish by anticommutation. For the kinetic terms, $\alpha_{k}\alpha_{j}+\alpha_{j}\alpha_{k}=2\delta_{jk}$ collapses the sum over $k$ to the single term $2p_{j}$, so

$$
\{H,\alpha_{j}\}=2c\,p_{j}. \tag{3.1}
$$

This is the algebraic fact. It holds for any representation of the Clifford relations – any dimension, any matrix size, any similarity transform – because it was derived from the relations themselves and not from a particular set of matrices.

### 3.2 The velocity operator and its exact time evolution

The velocity operator is $\dot{x}_{j}= \tfrac{i}{\hbar}[H,x_{j}]=c\,\alpha_{j}$; the position operator $x_{j}$ commutes with $\mathbf{p}$ and $\beta$, so this identification is exact and representation‑independent. The Heisenberg equation for $\alpha_{j}$ is

$$
\frac{d\alpha_{j}}{dt}= \frac{i}{\hbar}[H,\alpha_{j}]
= \frac{i}{\hbar}\bigl(H\alpha_{j}-\alpha_{j}H\bigr).
$$

Using $\alpha_{j}H = 2cp_{j}-H\alpha_{j}$ from (3.1),

$$
\frac{d\alpha_{j}}{dt}= \frac{i}{\hbar}\bigl(2H\alpha_{j}-2cp_{j}\bigr)
= \frac{2i}{\hbar}\bigl(H\alpha_{j}-cp_{j}\bigr). \tag{3.2}
$$

Define the shifted operator

$$
Z_{j}\equiv \alpha_{j}-cp_{j}H^{-1}.
$$

Since $H$ is a function of $\alpha_{k}$ and $\beta$, and $Z_{j}$ is a linear combination of Clifford generators minus a term built from $H$ itself, one verifies $Z_{j}H = \alpha_{j}H-cp_{j}= (2cp_{j}-H\alpha_{j})-cp_{j}=-(H\alpha_{j}-cp_{j})=-HZ_{j}$: the shifted operator anticommutes with the Hamiltonian. Now propose the ansatz

$$
\alpha_{j}(t)=cp_{j}H^{-1}+Z_{j}\,e^{-2iHt/\hbar}.
$$

Differentiating, $\tfrac{d}{dt}\alpha_{j}(t)=Z_{j}\!\left(-\tfrac{2iH}{\hbar}\right)\!e^{-2iHt/\hbar}$. Because $Z_{j}H=-HZ_{j}$,

$$
\frac{d\alpha_{j}}{dt}= -\frac{2i}{\hbar}\,Z_{j}H\,e^{-2iHt/\hbar}
= \frac{2i}{\hbar}\,HZ_{j}\,e^{-2iHt/\hbar}
= \frac{2i}{\hbar}\,H\bigl(\alpha_{j}(t)-cp_{j}H^{-1}\bigr),
$$

which is exactly (3.2) with the initial condition $\alpha_{j}(0)=\alpha_{j}$. Hence the exact solution is

$$
\alpha_{j}(t)=cp_{j}H^{-1}+Z_{j}\,e^{-2iHt/\hbar}. \tag{3.3}
$$

The first term is a constant “quasi‑velocity” fixed by the momentum; the second is a unitary rotation of the initial Clifford generator at the frequency set by the spectrum of $H$.

### 3.3 Position dynamics and the interference decomposition

Integrating $\dot{x}_{j}=c\,\alpha_{j}(t)$ from $0$ to $t$:

$$
x_{j}(t)=x_{j}(0)+c^{2}p_{j}H^{-2}\,t
+\int_{0}^{t}c\,Z_{j}\,e^{-2iHt'/\hbar}\,dt'.
$$

The integral evaluates term by term since $H^{-1}$ is constant in time:

$$
\int_{0}^{t}e^{-2iHt'/\hbar}\,dt'
= \frac{\hbar}{-2iH}\bigl(e^{-2iHt/\hbar}-\mathbb{1}\bigr)
= \frac{i\hbar}{2}\,H^{-1}\bigl(e^{-2iHt/\hbar}-\mathbb{1}\bigr),
$$

so

$$
x_{j}(t)=x_{j}(0)+c^{2}p_{j}H^{-2}\,t
+\frac{i\hbar c}{2}\,H^{-1}Z_{j}\bigl(e^{-2iHt/\hbar}-\mathbb{1}\bigr). \tag{3.4}
$$

The position separates into three parts: a classical uniform drift $c^{2}p_{j}H^{-2}\,t$, a static shift, and an oscillatory interference term. Only the third part is Zitterbewegung.

### 3.4 Generalization: the beat‑frequency theorem

The key generalization drops the specific Dirac form. Let $\mathcal{M}$ be any module for any Clifford algebra $\mathrm{Cl}(p,q)$, let $H$ be a self‑adjoint operator on $\mathcal{M}$ with purely discrete non‑degenerate spectrum, and suppose the velocity operators $\dot{x}_{j}$ are Clifford generators $\gamma_{a}$ (or linear combinations of them) satisfying

$$
\{H,\gamma_{a}\}=2\,(\text{operator independent of }\gamma_{a}\text{ and }H). \tag{3.5}
$$

Condition (3.5) is exactly the structure used in Section 3.2; the derivation of (3.3) used nothing about dimension, matrix size, or the Lorentz signature, only (3.1) and the invertibility of $H$. Therefore (3.3) holds verbatim with $\alpha_{j}$ replaced by $\gamma_{a}$.

Now decompose the Hilbert space into the eigenspaces of $H$. Let $P_{+}$ and $P_{-}$ be the spectral projectors onto the positive‑ and negative‑energy sectors with eigenvalues $E_{+}>0$ and $E_{-}<0$ (for the free Dirac case, $E_{\pm}=\pm E(\mathbf{p})$ with $E(\mathbf{p})=\sqrt{c^{2}|\mathbf{p}|^{2}+m^{2}c^{4}}$). Then

$$
e^{-2iHt/\hbar}=e^{-2iE_{+}t/\hbar}P_{+}+e^{-2iE_{-}t/\hbar}P_{-}+\cdots,
$$

where the ellipsis denotes any further eigenspaces. For a state $|\psi\rangle=|\psi_{+}\rangle+|\psi_{-}\rangle$ with components in both sectors, the expectation of the oscillatory term in (3.4) contains the cross term

$$
\langle\psi_{+}|\tfrac{i\hbar c}{2}H^{-1}Z_{j}e^{-2iHt/\hbar}|\psi_{-}\rangle+\text{h.c.}
= A_{j}\,e^{-i(E_{+}-E_{-})t/\hbar}+A_{j}^{*}\,e^{+i(E_{+}-E_{-})t/\hbar},
$$

because the projector structure forces the phase difference $e^{-2iE_{+}t/\hbar}e^{+2iE_{-}t/\hbar}=e^{-2i(E_{+}-E_{-})t/\hbar}$ on the bra side and its conjugate; collecting terms, the observable oscillation is at angular frequency

$$
\omega_{\mathrm{ZB}}=\frac{E_{+}-E_{-}}{\hbar}. \tag{3.6}
$$

Two consequences follow immediately. First, if the state lies entirely in one eigenspace ($P_{+}|\psi\rangle=|\psi\rangle$ or $P_{-}|\psi\rangle=|\psi\rangle$), the cross term vanishes identically and there is no Zitterbewegung: the oscillation is a two‑eigenspace interference effect, not a property of a single energy eigenstate. Second, the frequency is a spectroscopic observable: measuring $\omega_{\mathrm{ZB}}$ measures the gap $E_{+}-E_{-}$ directly, whatever representation or platform realizes $H$.

For the free Dirac case, $E_{+}-E_{-}=2E(\mathbf{p})$, so

$$
\omega_{\mathrm{ZB}}(\mathbf{p})=\frac{2E(\mathbf{p})}{\hbar}
=\frac{2\sqrt{c^{2}|\mathbf{p}|^{2}+m^{2}c^{4}}}{\hbar}\;\ge\;\frac{2mc^{2}}{\hbar},
\tag{3.7}
$$

with equality at $\mathbf{p}=0$. The frequently quoted value $2mc^{2}/\hbar$ is thus the rest‑frame minimum of a momentum‑dependent beat frequency — a point the hierarchy account makes transparent but the single‑equation view obscures.

### 3.5 The hierarchy of ownership

The derivation assigns each mathematical layer a precise role:

- **Algebra (owner).** The Clifford anticommutator (3.1) forces the velocity operator out of the commutant of $H$; the two‑eigenspace structure of a gapped self‑adjoint operator then forces interference. Nothing else is used.
- **Calculus (producer).** The linear operator differential equation (3.2) is solved by the exponential ansatz; calculus generates the solution but contributes no physics.
- **Trigonometry (notation).** The complex exponential $e^{-2iHt/\hbar}$ is a rotation; writing it as $\cos$ and $\sin$ changes nothing.
- **Geometry (shadow).** The “trembling” picture is the visualization of the interference term in (3.4); it is derivable, not fundamental, and it disappears when one eigenspace is removed.

This hierarchy is a conjecture about generality — that every ZB‑type oscillation in every platform is owned at the algebra layer — and Section 4 tests its numerical consequences while Section 6 states what would falsify it.

## 4. Analysis

Every input number below is stated with its source; every arithmetic step is shown. Physical constants are taken as the standard values: $c = 2.998\times10^{8}\,\mathrm{m/s}$, $m_{e}=9.109\times10^{-31}\,\mathrm{kg}$ (electron rest mass), $\hbar = 1.0546\times10^{-34}\,\mathrm{J\cdot s}$, and $\hbar = 6.582\times10^{-16}\,\mathrm{eV\cdot s}$ (the same constant in different units; consistency is checked in Step 1). The electron mass and speed of light are standard physical constants used as inputs; they are not measured in this work, and every numerical result below inherits their stated precision (four significant figures).

**Step 1 — Consistency of the two values of $\hbar$.** The ratio of the two stated values must equal the elementary charge $e$ expressed in joules per electronvolt:

$$
\frac{\hbar_{\mathrm{J\,s}}}{\hbar_{\mathrm{eV\,s}}}
= \frac{1.0546\times10^{-34}}{6.582\times10^{-16}}
= \frac{1.0546}{6.582}\times10^{-18}
= 0.16023\times10^{-18}
= 1.6023\times10^{-19}\ \mathrm{J/eV}.
$$

This ratio $1.6023\times10^{-19}\,\mathrm{J/eV}$ equals the elementary charge expressed in joules per electronvolt, $1.602\times10^{-19}\,\mathrm{J/eV}$, to the four significant figures carried. The two unit systems are consistent, so results computed in joules and in electronvolts can be compared directly.

**Step 2 — Electron rest energy $mc^{2}$.** First compute $c^{2}$:

$$
c^{2} = (2.998\times10^{8}\ \mathrm{m/s})^{2}
= 8.988\times10^{16}\ \mathrm{m^{2}/s^{2}}.
$$

Then

$$
m_{e}c^{2}
= (9.109\times10^{-31}\ \mathrm{kg})\times(8.988\times10^{16}\ \mathrm{m^{2}/s^{2}})
= 81.87\times10^{-15}\ \mathrm{kg\,m^{2}/s^{2}}
= 8.187\times10^{-14}\ \mathrm{J}.
$$

In electronvolts, using the conversion from Step 1:

$$
m_{e}c^{2}
= \frac{8.187\times10^{-14}\ \mathrm{J}}{1.602\times10^{-19}\ \mathrm{J/eV}}
= 5.111\times10^{5}\ \mathrm{eV}
= 0.5111\ \mathrm{MeV}.
$$

This matches the standard electron rest energy to the four significant figures carried, confirming the constant set is internally consistent.

**Step 3 — Rest‑frame ZB frequency $f_{0}$.** From (3.7) at $\mathbf{p}=0$, the angular frequency is $\omega_{0}=2m_{e}c^{2}/\hbar$ and the ordinary frequency is $f_{0}=\omega_{0}/2\pi$. First the angular frequency in SI units:

$$
\omega_{0}
= \frac{2\times8.187\times10^{-14}\ \mathrm{J}}{1.0546\times10^{-34}\ \mathrm{J\cdot s}}
= \frac{1.6374\times10^{-13}}{1.0546\times10^{-34}}\ \mathrm{s^{-1}}
= 1.5526\times10^{21}\ \mathrm{rad/s}.
$$

Then

$$
f_{0}
= \frac{\omega_{0}}{2\pi}
= \frac{1.5526\times10^{21}}{6.2832}\ \mathrm{Hz}
= 2.471\times10^{20}\ \mathrm{Hz}.
$$

Cross‑check in electron‑volt units: $\omega_{0}=2\times0.5111\ \mathrm{MeV}/(6.582\times10^{-16}\ \mathrm{eV\cdot s})
=1.0222\times10^{6}/(6.582\times10^{-16})
=1.553\times10^{21}\ \mathrm{rad/s}$, agreeing to the four figures carried. The rest‑frame oscillation period is $T_{0}=1/f_{0}=4.047\times10^{-21}\ \mathrm{s}$ — roughly four zeptoseconds, far beyond direct time resolution, which is why the frequency is accessible only through its dynamical consequences or in analogue systems.

**Step 4 — Rest‑frame position amplitude.** The oscillatory term in (3.4) carries the prefactor $\tfrac{i\hbar c}{2}H^{-1}Z_{j}$; at $\mathbf{p}=0$, $H^{-1}=(m_{e}c^{2})^{-1}$ and $Z_{j}$ is bounded by $\|Z_{j}\|\le\|\alpha_{j}\|+\|cp_{j}H^{-1}\|=1$ (the momentum term vanishes at rest), so the natural amplitude scale is the reduced Compton wavelength divided by $2$:

$$
a_{0}= \frac{\hbar}{2m_{e}c}
= \frac{1.0546\times10^{-34}\ \mathrm{J\cdot s}}
{2\times(9.109\times10^{-31}\ \mathrm{kg})\times(2.998\times10^{8}\ \mathrm{m/s})}.
$$

The denominator is $2\times9.109\times2.998\times10^{-23}=54.62\times10^{-23}=5.462\times10^{-22}\ \mathrm{kg\,m/s}$, so

$$
a_{0}= \frac{1.0546\times10^{-34}}{5.462\times10^{-22}}\ \mathrm{m}
= 1.931\times10^{-13}\ \mathrm{m}.
$$

**Step 5 — Illustrative gapped Dirac material.** The beat‑frequency statement (3.6) applies to any two‑eigenspace Hamiltonian. Take an illustrative material with band edges at $\pm\Delta$, $\Delta=0.1\ \mathrm{eV}$, so $E_{+}-E_{-}=2\Delta=0.2\ \mathrm{eV}$. The frequency is

$$
f = \frac{E_{+}-E_{-}}{h}
= \frac{2\Delta}{2\pi\hbar_{\mathrm{eV\,s}}}
= \frac{0.2\ \mathrm{eV}}{6.2832\times6.582\times10^{-16}\ \mathrm{eV\cdot s}}.
$$

The denominator is $6.2832\times6.582\times10^{-16}=41.36\times10^{-16}=4.136\times10^{-15}\ \mathrm{eV\cdot s}$, so

$$
f = \frac{0.2}{4.136\times10^{-15}}\ \mathrm{Hz}
= 4.836\times10^{13}\ \mathrm{Hz}.
$$

The corresponding period is $T=1/f=2.068\times10^{-14}\ \mathrm{s}\approx20.7\ \mathrm{fs}$.

**Step 6 — Scaling law.** Because (3.6) is linear in the gap, the frequency for any two‑eigenspace system scales as

$$
f = \frac{E_{+}-E_{-}}{h}
= \bigl(2.418\times10^{14}\ \mathrm{Hz/eV}\bigr)\times(E_{+}-E_{-}),
$$

where the conversion factor follows from $1/(4.136\times10^{-15}\ \mathrm{eV\cdot s})=2.418\times10^{14}\ \mathrm{Hz/eV}$ (check: $2.418\times10^{14}\times0.2=4.836\times10^{13}$ Hz, matching Step 5). This single line converts any measured ZB frequency in any platform into a gap measurement, and conversely predicts the oscillation frequency from any independently known gap.

## 5. Results

The derivation of Section 3 and the arithmetic of Section 4 yield the following results, each traceable to shown steps.

- **R1 (Exact operator solution).** From the single algebraic input $\{H,\alpha_{j}\}=2cp_{j}$ (Eq. 3.1), the velocity operator evolves exactly as $\alpha_{j}(t)=cp_{j}H^{-1}+Z_{j}e^{-2iHt/\hbar}$ with $Z_{j}=\alpha_{j}-cp_{j}H^{-1}$ anticommute with $H$ (Eq. 3.3), and the position decomposes into drift, static shift, and oscillation as in Eq. (3.4). This holds for every representation of the Clifford relations.

- **R2 (Beat‑frequency theorem).** For any Hamiltonian on a Clifford module whose velocity operators are Clifford generators satisfying (3.5), the observable oscillation exists if and only if two eigenspaces are coherently populated, and its angular frequency is $\omega_{\mathrm{ZB}}=(E_{+}-E_{-})/\hbar