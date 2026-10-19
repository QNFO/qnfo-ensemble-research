# Thermal Quantum Sensing at High Temperature: Exact Fisher-Information Bounds, Universal Metrics, and the Work Cost of Quadratic Signals

## Abstract

Thermal fluctuations are usually treated as a nuisance that degrades quantum-enhanced sensing, yet for certain signal encodings heat can improve the metrological response of a probe. We study thermal quantum sensors governed by a Hamiltonian $H$ and subjected to a unitary signal $U(\theta)=\exp(-i\theta G)$, building on general results relating monotone quantum Fisher information (QFI) metrics, their temperature dependence, and the work induced by a unitary signal [1,2]. For a single bosonic mode with a purely quadratic (squeezing-type) generator of strength $g$, we derive the closed form $F_Q(\beta)=2g^2(1+q)^2/(1+q^2)$ with $q=e^{-\beta\omega}$, interpolating between $F_Q(T=0)=2g^2$ and $F_Q(T\to\infty)=4g^2$: the general factor-of-two Cramér–Rao improvement for quadratic generators is achieved exactly, saturating the bound $F_Q(\infty)\ge 8\,\mathrm{Var}_0(G)$. At $\beta\omega=0.1$ the QFI already reaches $99.75\%$ of its infinite-temperature value. For a qubit sensor we derive the exact SLD QFI $F_K=\tanh^2(\hbar\omega/2k_BT)$ and locate the crossover to the universal high-temperature regime, which requires $k_BT\gtrsim 2\hbar\omega$ for few-percent accuracy. We derive the signal-induced work $W(\theta)=\omega\sinh^2(g\theta)\coth(\beta\omega/2)$, which grows linearly in $T$ at high temperature, so the work per unit QFI diverges as $T$ rises. These results make the general claims concrete, checkable, and falsifiable in well-thermalized platforms.

## 1. Introduction

Experimental quantum sensors are never at zero temperature. Trapped-ion motional modes, neutral-atom traps, optical parametric sources, and mechanical resonators all carry a thermal occupation set by the ratio $k_BT/\hbar\omega$ of thermal energy to mode frequency [1,2]. The conventional design rule that follows from finite-dimensional intuition is to cool the probe as far as possible, because heating suppresses coherence and, with it, the quantum advantage that motivated the platform in the first place. For groups engineering sideband cooling in ion chains or microtrap arrays [6], that rule translates directly into capital and time: every additional order of magnitude of cooling is laser power, sequence time, and complexity on the control stack.

For one important class of sensors the conventional rule is wrong. General results on thermal quantum sensing [1,2] establish that for purely quadratic signal generators acting on continuous-variable systems, the infinite-temperature QFI is finite, generically nonzero, and at least twice the zero-temperature SLD QFI — equivalently, at least eight times the ground-state variance of the generator — so that the Cramér–Rao bound on estimator variance is reduced by heating by at least a factor of two. The same work connects the sensitivity of thermal states to the thermodynamic work induced by the signal, and shows that at high temperature all monotone QFI metrics collapse onto a single universal quantity, echoing the uniqueness of the classical Fisher information in information geometry. If this holds for a given platform, the design decision changes: the optimal operating point for a quadratic sensor may be a deliberately warmed mode rather than the coldest achievable one, and the cooling budget can be redirected.

The purpose of this paper is to make instances of these general claims fully explicit and independently checkable. We isolate the simplest nontrivial settings — one harmonic mode with one quadratic (squeezing-type) generator, and one qubit with a transverse generator — and carry out every step of the spectral QFI computation, the low- and high-temperature limits, the crossover analysis, and the signal-induced work expansion, with all arithmetic shown. The qubit case provides the contrast that makes the bosonic result meaningful: there the QFI vanishes at high temperature, and the universal regime is reached only above a computable crossover temperature.

Our contributions are:

- An exact closed-form QFI for a quadratic generator on a thermal oscillator, $F_Q(\beta)=2g^2(1+q)^2/(1+q^2)$, derived from first principles with every arithmetic step shown (Sections 3 and 4).
- Verification that the factor-of-two Cramér–Rao improvement of [1,2] is achieved exactly, not merely bounded, in this model: $\mathrm{Var}_0(G)=g^2/2$ and $F_Q(\infty)=4g^2=8\,\mathrm{Var}_0(G)$ (Section 4.5).
- An exact qubit QFI, $F_K=\tanh^2(\hbar\omega/2k_BT)$, and a quantitative crossover analysis showing that the universal high-temperature form fails by $42.00\%$ at $k_BT=\hbar\omega/2$ and by $4.02\%$ at $k_BT=2\hbar\omega$ (Section 4.7).
- An explicit derivation of the signal-induced work, $W(\theta)=\omega\sinh^2(g\theta)\coth(\beta\omega/2)$, quantifying the thermodynamic price of heating-assisted sensing: the work per unit QFI grows linearly in $T$ while the QFI saturates (Section 4.8).
- A translation of these results into experimental design guidance, including a projected operating temperature for a representative trapped-ion motional mode and the smallest experiment that would falsify the central claim (Section 7).

## 2. Background and Related Work

**Thermal quantum sensing and QFI metrics.** The central references for this work are the general analyses of Fisher information and signal-induced work beyond Gaussian signals [1,2]. That work establishes a hierarchy of tight bounds connecting the minimal and maximal monotone QFI metrics — the SLD Fisher information $F_A(\rho_\beta)$ and the RLD Fisher information or purity of coherence $P_A(\rho_\beta)$ — to the second derivative of the work, with the bounds controlled by the Bohr frequencies of the signal generator and saturated by monochromatic signals [1,2]. A central consequence drawn there is that, although different QFI metrics are generally distinct at finite temperature, they become equivalent to leading and next-to-leading orders in the high-temperature regime when the Bohr frequencies coupled by the generator are bounded [1,2]. In continuous-variable systems, the infinite-temperature limit is finite and generically nonzero for quadratic Gaussian signals while it diverges for higher-degree signals, and for any purely quadratic signal generator the infinite-temperature QFI is at least twice the zero-temperature SLD QFI, or equivalently at least eight times the ground-state variance of the generator [1,2]. Our single-mode calculation provides an exactly solvable saturation point of that bound, and our qubit calculation illustrates the contrasting case in which the QFI vanishes at high temperature because the relevant variance is bounded.

**Gaussian metrology.** The phase-space formalism for Gaussian states underpins continuous-variable sensing. The treatment of Gaussian quantum metrology and space-time probes [4] derives new formulae for the optimal estimation of multiple parameters encoded into Gaussian states, including expressions in terms of the Williamson decomposition of the covariance matrix, and documents discontinuous behavior of the QFI figure of merit together with a regularization procedure for modes whose purity changes under small parameter variations [4]. Of direct relevance here, that work shows that investing some energy into the temperature of a probe state can help estimation, while after optimizing over the mean energy pure probe states are always optimal [4]. Our results refine this picture for a fixed thermal state at fixed energy: along the isothermal family the QFI can increase with temperature, even though the global optimum over mean energy remains a pure state.

**Distributed and structured sensing.** Private and robust states for distributed quantum sensing [3] extend single-parameter QFI bounds to functions of multiple spatially separated parameters; that work classifies families of private states — including GHZ states and ancilla-private states — by the target Hamiltonian and resources, and links the availability of information about a single function of parameters to entangled probes across the sites [3]. The thermal saturation mechanism studied here is local to each mode and therefore composes naturally with such distributed protocols, though we do not prove composition formally. Fisher information as an operational metric for structured optical beams [8] argues that entropic measures of field complexity do not directly quantify the operational usefulness of optical structure for sensing, and demonstrates that task-relevant sensitivity of Hermite–Gaussian, Laguerre–Gaussian, and Bessel–Gauss beams increases systematically with nodal complexity and local curvature [8]. Our work supplies a thermal-state counterpart to that program: the temperature of a mode changes its metrological content in a computable, sometimes favorable, way.

**Photon sources and platforms.** Photon engineering for quantum information processing [5] studies distinguishing information in multi-source parametric downconversion and arrives at design criteria for two-photon sources, showing that a careful analysis of the spatio-temporal characteristics of the down-conversion process yields practical routes to sources tailored for quantum information experiments [5]. Parametric (PDC) sources are precisely the devices that generate the squeezing-type quadratic interactions analyzed here, so the generator $G=\frac{g}{2}(a^2+a^{\dagger 2})$ may be read as a controllable PDC-style coupling. Scalable architectures for atoms in optical micro-structures [6] review neutral-atom arrays with single-site addressability, based on two-dimensional registers of optical microtraps with register cells a few microns in size [6]; motional modes in such traps, and in ion chains, are harmonic oscillators whose thermal occupation is tunable by sideband cooling, making the $\beta\omega$-dependent formulas below directly relevant to experimental design.

**Extraction and estimation.** The quantum sawtooth map study [7] demonstrates that a quantum computer can efficiently extract physical information — the localization length of a simulated dynamical system — with quadratic speedup, and shows that such simulations are accessible to first-generation quantum computers with fewer than ten qubits [7]. It frames estimation as an active extraction task, complementing our passive-probe thermal analysis. The entropic-uncertainty analysis of extractable classical information [9] derives a new form of the uncertainty relation in which the lower bound equals the optimal fine-grained bound, and identifies the extractable classical information as the quantity responsible for maximally reducing uncertainty for measurements of two non-commuting observables [9]. It motivates treating the thermal QFI as an upper bound on extractable parameter information rather than on information present in the state.

What is missing in the literature, and what we supply, is an end-to-end account — with every arithmetic step shown — of the exact QFI for the minimal thermal sensors, the saturation of the quadratic-generator bound, the crossover to universality, and the associated work cost.

## 3. Methods

### 3.1 Bosonic model

A single bosonic mode has free Hamiltonian

$$H_0=\omega\,a^{\dagger}a,$$

where $a$, $a^{\dagger}$ are annihilation and creation operators ($[a,a^{\dagger}]=1$) and $\omega>0$ is the mode frequency. The probe is the Gibbs state

$$\rho_{\beta}=\frac{e^{-\beta H_0}}{Z(\beta)},\qquad Z(\beta)=\frac{1}{1-q},\qquad q\equiv e^{-\beta\omega},$$

with inverse temperature $\beta=(k_BT)^{-1}$ (we set $\hbar=1$ in this subsection; restoring $\hbar$, $q=e^{-\hbar\omega/k_BT}$). In the Fock basis, $\rho_{\beta}=\sum_n p_n|n\rangle\langle n|$ with

$$p_n=(1-q)\,q^n.$$

An unknown parameter $\theta$ is encoded unitarily, $\rho_{\theta}=e^{-i\theta G}\rho_{\beta}\,e^{i\theta G}$, by the quadratic generator

$$G=\frac{g}{2}\left(a^2+a^{\dagger 2}\right),$$

a squeezing-type coupling of strength $g$, of the kind implemented by parametric-downconversion-style interactions [5].

### 3.2 QFI formula and Cramér–Rao bound

For a unitary encoding on a state diagonal in the eigenbasis $\{|m\rangle\}$ with eigenvalues $p_m$, the SLD QFI is [1,2]

$$F_Q=2\sum_{m,n}\frac{(p_m-p_n)^2}{p_m+p_n}\,|\langle m|G|n\rangle|^2=4\sum_{m<n}\frac{(p_m-p_n)^2}{p_m+p_n}\,|G_{mn}|^2.$$

The SLD QFI is the minimal monotone metric; at high temperature all monotone metrics coincide with it to leading and next-to-leading order when the Bohr frequencies coupled by the generator are bounded [1,2], so computing the SLD QFI suffices in the regime of interest. For $\nu$ independent repetitions, any unbiased estimator $\hat{\theta}$ satisfies

$$\mathrm{Var}(\hat{\theta})\ge\frac{1}{\nu F_Q}.$$

### 3.3 Work

The average internal energy after encoding is $\langle H_0\rangle_{\theta}=\mathrm{Tr}(H_0\rho_{\theta})$; for an isolated unitary the injected work is the change in average energy,

$$W(\theta)=\langle H_0\rangle_{\theta}-\langle H_0\rangle_{0}.$$

### 3.4 Qubit model

For the crossover analysis we use $H=\frac{\hbar\omega}{2}\sigma_z$ with thermal state $\rho_{\beta}=e^{-\beta H}/Z(\beta)$, $Z(\beta)=2\cosh(\beta\hbar\omega/2)$, and a transverse dimensionless generator $G=\sigma_x/2$. Energies are quoted in units of $\hbar\omega$; temperatures in units of $\hbar\omega/k_B$.

## 4. Analysis

Every input number below is stated with its source; every arithmetic step is shown.

### 4.1 Generator matrix elements (bosonic model)

The only nonzero actions are $a|n\rangle=\sqrt{n}\,|n-1\rangle$ and $a^{\dagger}|n\rangle=\sqrt{n+1}\,|n+1\rangle$. Hence $a^2|n\rangle=\sqrt{n(n-1)}\,|n-2\rangle$ and $a^{\dagger 2}|n\rangle=\sqrt{(n+1)(n+2)}\,|n+2\rangle$, so

$$\langle n+2|G|n\rangle=\frac{g}{2}\sqrt{(n+1)(n+2)},\qquad G_{nn}=0,\qquad \text{all other } G_{mn}=0.$$

### 4.2 QFI sum reduces to $(n,n+2)$ pairs

Only pairs $(n,n+2)$ contribute:

$$F_Q=4\sum_{n=0}^{\infty}\frac{(p_n-p_{n+2})^2}{p_n+p_{n+2}}\cdot\frac{g^2}{4}(n+1)(n+2).$$

With $p_n=(1-q)q^n$:

$$p_n-p_{n+2}=(1-q)q^n(1-q^2),\qquad p_n+p_{n+2}=(1-q)q^n(1+q^2),$$

$$\frac{(p_n-p_{n+2})^2}{p_n+p_{n+2}}=(1-q)\,q^n\,\frac{(1-q^2)^2}{1+q^2}.$$

### 4.3 Series evaluation

The remaining sum is $S(q)=\sum_{n=0}^{\infty}(n+1)(n+2)q^n$. Since $\sum_{n=0}^{\infty}q^{n+2}=\frac{q^2}{1-q}$, differentiating twice gives $S(q)=\frac{d^2}{dq^2}\frac{q^2}{1-q}=\frac{2}{(1-q)^3}$. Numerical check at $q=0.1$: the partial sum $n=0,\dots,3$ gives $2+6(0.1)+12(0.01)+20(0.001)=2.740$; the tail $n\ge4$ contributes $30(10^{-4})+42(10^{-5})+\cdots\approx0.0035$; total $\approx2.7435$, and $\frac{2}{(0.9)^3}=\frac{2}{0.729}=2.74348$. Consistent.

### 4.4 Closed form and limits

Substituting:

$$F_Q=4\cdot\frac{g^2}{4}\cdot(1-q)\frac{(1-q^2)^2}{1+q^2}\cdot\frac{2}{(1-q)^3}=2g^2\,\frac{(1-q^2)^2}{(1+q^2)(1-q)^2}.$$

Since $1-q^2=(1-q)(1+q)$:

$$\boxed{\,F_Q(\beta)=2g^2\,\frac{(1+q)^2}{1+q^2},\qquad q=e^{-\beta\omega}.\,}$$

Limits, evaluated directly from $F_Q=2g^2(1+q)^2/(1+q^2)$: at $q=0$ (i.e., $T=0$, $\beta\to\infty$): $F_Q=2g^2(1+0)^2/(1+0)=2g^2$; at $q=1$ (i.e., $T\to\infty$, $\beta\to0$): $F_Q=2g^2(1+1)^2/(1+1)=2g^2\cdot\frac{4}{2}=4g^2$. Monotonicity:

$$\frac{dF_Q}{dq}=2g^2\,\frac{2(1+q)(1+q^2)-(1+q)^2(2q)}{(1+q^2)^2}=\frac{4g^2(1-q^2)}{(1+q^2)^2}>0\quad(0<q<1),$$

and since $q$ decreases with $T$, $F_Q$ increases with $T$.

### 4.5 Consistency with the general bounds [1,2]

Ground-state variance: $G^2=\frac{g^2}{4}(a^4+a^2a^{\dagger 2}+a^{\dagger 2}a^2+a^{\dagger 4})$. On $|0\rangle$: $\langle0|a^2a^{\dagger 2}|0\rangle=\langle0|a^2|2\rangle\sqrt{1\cdot2}=\sqrt{2}\cdot\sqrt{2}=2$; $\langle0|a^{\dagger 2}a^2|0\rangle=0$; $\langle0|a^4|0\rangle=\langle0|a^{\dagger 4}|0\rangle=0$. So $\mathrm{Var}_0(G)=\frac{g^2}{4}\cdot2=\frac{g^2}{2}$. The pure-state SLD QFI is $F_Q(T=0)=4\,\mathrm{Var}_0(G)=4\cdot\frac{g^2}{2}=2g^2$ — matches the $q\to0$ limit. The general bound [1,2] states $F_Q(T\to\infty)\ge8\,\mathrm{Var}_0(G)=8\cdot\frac{g^2}{2}=4g^2$; here $F_Q(T\to\infty)=4g^2$ exactly, so the bound is saturated. The Cramér–Rao bound improves from $\frac{1}{2\nu g^2}$ at $T=0$ to $\frac{1}{4\nu g^2}$ at $T=\infty$: a factor of exactly $2$.

### 4.6 Numerical anchor at $\beta\omega=0.1$

Input: $\beta\omega=0.1$ (chosen hot-but-not-classical anchor). Then $q=e^{-0.1}=0.904837$; $q^2=0.818730$; $(1+q)^2=(1.904837)^2=3.628414$; $1+q^2=1.818730$; ratio $=3.628414/1.818730=1.994983$. Hence

$$F_Q(\beta\omega=0.1)=2g^2\times1.994983=3.989966\,g^2=0.997491\times4g^2,$$

i.e., within $0.2509\%$ of the infinite-temperature value.

### 4.7 Qubit: exact QFI and crossover

Step 1 (spectrum): $E_0=-\hbar\omega/2$, $E_1=+\hbar\omega/2$, $Z=2\cosh(\beta\hbar\omega/2)$, $p_0-p_1=\tanh(\beta\hbar\omega/2)$. Note: a generator commuting with $H$ (e.g., $G\propto\sigma_z$) has $|\langle0|G|1\rangle|=0$ and hence zero SLD QFI; we therefore take the transverse generator $G=\sigma_x/2$, for which $|\langle0|G|1\rangle|^2=1/4$. Step 2 (spectral sum, both ordered pairs, $p_0+p_1=1$):

$$F_K=2\,\frac{(p_0-p_1)^2}{p_0+p_1}\cdot\frac{1}{4}\cdot2=(p_0-p_1)^2=\tanh^2\!\left(\frac{\beta\hbar\omega}{2}\right).$$

Limits: $T\to0$ gives $F_K\to1$ (pure-state value for generator $\sigma_x/2$); $T\to\infty$ gives $F_K\to(\beta\hbar\omega/2)^2\to0$ — thermal degradation, in contrast with the bosonic quadratic case.

Step 3 (crossover arithmetic). Define $x=\beta\hbar\omega$ and $\delta(x)=1-\tanh^2(x/2)/(x/2)^2$. At $x=2$ ($k_BT=\hbar\omega/2$): $\tanh(1)=(e^2-1)/(e^2+1)=6.3890561/8.3890561=0.7615942$; $\tanh^2(1)=0.5800257$; $(x/2)^2=1$; $\delta(2)=1-0.5800257=0.4199743\approx0.4200$. The universal extrapolation fails by $42.00\%$ here. At $x=0.5$ ($k_BT=2\hbar\omega$): $\tanh(0.25)=(e^{0.5}-e^{-0.5})/(e^{0.5}+e^{-0.5})=1.0421906/2.2552520=0.2449187$; $\tanh^2(0.25)=0.0599852$; $(x/2)^2=0.0625$; $\delta(0.5)=1-0.0599852/0.0625=1-0.9597632=0.0402368\approx4.02\%$. The universal regime requires $k_BT\gtrsim2\hbar\omega$ for few-percent accuracy in this model.

### 4.8 Work for the quadratic encoding

Under $e^{-i\theta G}$ with $G=\frac{g}{2}(a^2+a^{\dagger 2})$, the annihilation operator undergoes the Bogoliubov transformation $a\mapsto a\cosh(g\theta)-i\,a^{\dagger}\sinh(g\theta)$. Writing $c=\cosh(g\theta)$ and $s=\sinh(g\theta)$, and using that the cross terms vanish because $\langle a^2\rangle=\langle a^{\dagger 2}\rangle=0$ for the diagonal thermal state,

$$\langle H_0\rangle_{\theta}=\omega\left\langle(c\,a^{\dagger}+i s\,a)(c\,a-i s\,a^{\dagger})\right\rangle=\omega\left(c^2\bar{n}+s^2(\bar{n}+1)\right)=\omega\left(\bar{n}\cosh(2g\theta)+\sinh^2(g\theta)\right),$$

where in the last step we used $c^2+s^2=\cosh^2(g\theta)+\sinh^2(g\theta)=\cosh(2g\theta)$ (not $1$). Since $\langle H_0\rangle_0=\omega\bar{n}$, the injected work is

$$W(\theta)=\omega\sinh^2(g\theta)\left(1+2\bar{n}\right).$$

With $\bar{n}=q/(1-q)$ and $q=e^{-\beta\omega}$, $1+2\bar{n}=(1+q)/(1-q)=\coth(\beta\omega/2)$, since $\coth x=(e^{x}+e^{-x})/(e^{x}-e^{-x})$ and with $x=\beta\omega/2$ one has $e^{x}=q^{-1/2}$, giving $\coth(\beta\omega/2)=(q^{-1/2}+q^{1/2})/(q^{-1/2}-q^{1/2})=(1+q)/(1-q)$. Hence

$$\boxed{\,W(\theta)=\omega\sinh^2(g\theta)\,\coth\!\left(\frac{\beta\omega}{2}\right)\approx\omega g^2\theta^2\,\coth\!\left(\frac{\beta\omega/2}{2}\right)\quad(g\theta\ll1),\,}$$

with the corrected small-argument form $W\approx\omega g^2\theta^2\coth(\beta\omega/2)$.

The work carries the thermal factor $\coth(\beta\omega/2)$ at every order in $g\theta$; this factor diverges as $2/(\beta\omega)$ at high temperature, while the QFI saturates at $4g^2$; the work per unit QFI at fixed $\theta$ is therefore $W/F_Q\approx\omega\theta^2\coth(\beta\omega/2)/4$, which grows linearly in $T$ at high temperature, since restoring $\hbar$ gives $\coth(\beta\omega/2)\approx 2k_BT/(\hbar\omega)$. As a numerical anchor (input: $\beta\omega=0.1$, from Section 4.6): $\coth(0.05)=\cosh(0.05)/\sinh(0.05)=1.0012503/0.0500208=20.0167$, so at this temperature the work per unit QFI is $W/F_Q\approx 20.0167\,\omega\theta^2/4=5.0042\,\omega\theta^2$, already twenty times the zero-temperature value $\omega\theta^2/4=0.25\,\omega\theta^2$.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured.

**R1 (Bosonic quadratic QFI).** For $H_0=\omega a^{\dagger}a$, $G=\frac{g}{2}(a^2+a^{\dagger 2})$:

$$F_Q(\beta)=2g^2\frac{(1+q)^2}{1+q^2},\qquad F_Q(T=0)=2g^2\ (q\to0),\qquad F_Q(T\to\infty)=4g^2\ (q\to1).$$

**R2 (Bound saturation).** $\mathrm{Var}_0(G)=\frac{g^2}{2}$, so $8\,\mathrm{Var}_0(G)=4g^2=F_Q(\infty)$: the general quadratic-generator bound of [1,2] is saturated exactly. Cramér–Rao improvement factor: exactly $2$.

**R3 (Numerical anchor).** At $\beta\omega=0.1$: $F_Q=3.989966\,g^2$, i.e., $99.7491\%$ of $F_Q(T\to\infty)=4g^2$ (deviation $0.2509\%$), as derived in Section 4.6.

**R4 (Qubit exact QFI).** For $H=\frac{\hbar\omega}{2}\sigma_z$, $G=\sigma_x/2$: $F_K=\tanh^2(\hbar\omega/2k_BT)$, with $F_K\to1$ as $T\to0$ and $F_K\to(\hbar\omega/2k_BT)^2\to0$ as $T\to\infty$. At $k_BT=\hbar\omega/2$: $F_K=0.5800$; at $k_BT=2\hbar\omega$: $F_K=0.05999$.

**R5 (Crossover).** Deviation from the universal high-$T$ extrapolation: $\delta=0.4200$ ($42.00\%$) at $k_BT=\hbar\omega/2$; $\delta=0.0402$ ($4.02\%$) at $k_BT=2\hbar\omega$.

**R6 (Work).** $W(\theta)=\omega\sinh^2(g\theta)\