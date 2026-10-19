# Thermal Quantum Sensing at High Temperature: Exact Fisher‑Information Bounds, Universal Metrics, and the Work Cost of Quadratic Signals

## Abstract

Thermal fluctuations are usually treated as a nuisance that degrades quantum‑enhanced sensing, yet for certain signal encodings heat can improve the metrological response of a probe. We study thermal quantum sensors governed by a Hamiltonian $H$ and subjected to a unitary signal $U(\theta)=\exp(-i\theta G)$. Building on recent general results relating monotone quantum Fisher information (QFI) metrics, their temperature dependence, and the work induced by a unitary signal, we make the central claims fully explicit and independently checkable in two exactly solvable models. For a single bosonic mode with a purely quadratic (squeezing‑type) generator of strength $g$, we derive the closed form
$$
F_Q(\beta)=\frac{2g^{2}(1+q)^{2}}{1+q^{2}},\qquad q=e^{-\beta\omega},
$$
interpolating between the zero‑temperature value $F_Q(T=0)=2g^{2}$ (limit $q\to0$) and the infinite‑temperature value $F_Q(T\!\to\!\infty)=4g^{2}$ (limit $q\to1$): the general factor‑of‑two Cramér–Rao improvement for quadratic generators is achieved exactly, saturating the bound $F_Q(\infty)\ge8\,\mathrm{Var}_{0}(G)$. At $\beta\omega=0.1$ the QFI already reaches $99.7491\%$ of its infinite‑temperature value. For a qubit sensor we derive the exact SLD QFI $F_K=\tanh^{2}(\hbar\omega/2k_{B}T)$ and locate the crossover to the universal high‑temperature regime. We derive the signal‑induced work
$$
W(\theta)=\omega\sinh^{2}(g\theta)\coth\!\left(\frac{\beta\omega}{2}\right)
\approx\omega g^{2}\theta^{2}\coth\!\left(\frac{\beta\omega}{2}\right),
$$
which is temperature‑independent only at $T=0$ and grows linearly in $T$ at high temperature, and discuss the work–information trade‑off, limitations, and falsifiability.

## 1. Introduction

Quantum metrology promises estimator variances below classical limits by exploiting non‑classical probe states [1,2,4]. In practice, probes are never at zero temperature: trapped‑ion motional modes, optical parametric sources, and mechanical resonators all carry thermal occupation that is conventionally assumed to wash out quantum advantage. A recent general analysis of thermal quantum sensing [1,2] overturns the naive expectation in an important class of cases: for *purely quadratic* signal generators acting on continuous‑variable systems, the infinite‑temperature QFI is finite, generically non‑zero, and at least twice the zero‑temperature SLD QFI — equivalently at least eight times the ground‑state variance of the generator — so that the Cramér–Rao bound on estimator variance is *reduced* by heating by at least a factor of two. The same work connects the sensitivity of thermal states to the thermodynamic work induced by the signal, and shows that at high temperature all monotone QFI metrics collapse onto a single universal quantity, echoing the uniqueness of the classical Fisher information in information geometry.

The purpose of this paper is to make instances of these general claims fully explicit and independently checkable. We isolate the simplest nontrivial settings — one harmonic mode with one quadratic (squeezing‑type) generator, and one qubit with a transverse generator — and carry out every step of the spectral QFI computation, the low‑ and high‑temperature limits, the crossover analysis, and the signal‑induced work expansion, with all arithmetic shown.

Our contributions are:
* (i) an exact closed‑form QFI for a quadratic generator on a thermal oscillator, derived from first principles;
* (ii) verification that the factor‑of‑two Cramér–Rao improvement is achieved exactly (not merely bounded) in this model;
* (iii) an exact qubit QFI and a quantitative crossover analysis showing where the universal high‑temperature form fails; and
* (iv) an explicit derivation of the signal‑induced work for the quadratic encoding, quantifying the thermodynamic price of heating‑assisted sensing.

## 2. Background and Related Work

**Thermal quantum sensing and QFI metrics.** The central references for this work are the general analysis of Fisher information and signal‑induced work beyond Gaussian signals [1,2]. Those papers establish three results we build on: (i) monotone QFI metrics (SLD, RLD, Kubo–Mori and the wider operator‑monotone family) obey a temperature‑dependent hierarchy; (ii) at high temperature all monotone QFI metrics coincide to leading order with a universal variance‑like quantity; and (iii) for any purely quadratic signal generator the infinite‑temperature QFI is at least twice the zero‑temperature SLD QFI, equivalently at least eight times the ground‑state variance of the generator. The present bosonic calculation provides an exactly solvable saturation point of that bound, and the qubit calculation illustrates the contrasting case in which the QFI *vanishes* at high temperature because the relevant variance is bounded.

**Gaussian metrology.** The phase‑space formalism for Gaussian states underpins continuous‑variable sensing. The treatment of Gaussian quantum metrology and space‑time probes [4] derives optimal multi‑parameter estimation formulae for Gaussian states and documents discontinuous behavior of the QFI figure of merit — a reminder that QFI can be non‑smooth in parameters, which is why we work with an exactly solvable spectral formula rather than perturbative expansions.

**Distributed and structured sensing.** Private and robust states for distributed quantum sensing [3] extend single‑parameter QFI bounds to functions of multiple spatially separated parameters; the introduction of [3] notes that quantum metrology can surpass classical bounds and that distributed protocols are a natural extension of single‑parameter sensing. The thermal saturation mechanism studied here is local and therefore composes naturally with such distributed protocols, although we do not prove composition formally.

**Photon sources and platforms.** Photon engineering for quantum information processing [5] studies distinguishing information in multi‑source parametric‑down‑conversion (PDC) devices and emphasizes that PDC sources generate squeezing‑type quadratic interactions. Our generator $G=\frac{g}{2}(a^{2}+a^{\dagger2})$ may be read as a controllable PDC‑style coupling, linking the abstract model to experimentally available nonlinear optics.

**Scalable atom arrays.** Scalable architectures for atoms in optical micro‑structures [6] review neutral‑atom arrays with single‑site addressability. Motional modes in such traps, and in ion chains, are harmonic oscillators whose thermal occupation is tunable by sideband cooling, making the $\beta\omega$‑dependent formulas below directly relevant to experimental design.

**Extraction and estimation.** The quantum sawtooth map study [7] demonstrates that a quantum computer can extract physical information (e.g., localization lengths) from a simulated dynamical system with quadratic speedup; it frames estimation as an active extraction task, complementing our passive‑probe thermal analysis.

**Operational FI for structured beams.** Fisher information as an operational metric for structured optical beams [8] argues that Fisher information, not entropic complexity measures, quantifies the metrological content of a field mode; our work supplies a thermal‑state counterpart: the *temperature* of a mode changes its metrological content in a computable, sometimes favorable, way.

**Extractable classical information.** The entropic‑uncertainty analysis of extractable classical information [9] bounds how much classical information measurements can extract in the presence of correlations beyond entanglement; it motivates treating the thermal QFI as an upper bound on *extractable* parameter information rather than on information present in the state.

What is missing in the literature, and what we supply, is an end‑to‑end account — with every arithmetic step shown — of the exact QFI for the minimal thermal sensors, the saturation of the quadratic‑generator bound, the crossover to universality, and the associated work cost.

## 3. Methods

### 3.1 Bosonic model

A single bosonic mode with free Hamiltonian
$$
H_{0}=\omega\,a^{\dagger}a,
$$
where $a$, $a^{\dagger}$ satisfy $[a,a^{\dagger}]=1$ and $\omega>0$ is the mode frequency. The probe is the Gibbs state
$$
\rho_{\beta}=\frac{e^{-\beta H_{0}}}{Z(\beta)},\qquad Z(\beta)=\frac{1}{1-q},\qquad q\equiv e^{-\beta\omega},
$$
with inverse temperature $\beta=(k_{B}T)^{-1}$ (we set $\hbar=1$ in this subsection; restoring $\hbar$, $q=e^{-\hbar\omega/k_{B}T}$). In the Fock basis, $\rho_{\beta}=\sum_{n}p_{n}|n\rangle\langle n|$ with $p_{n}=(1-q)q^{n}$.

An unknown parameter $\theta$ is encoded unitarily, $\rho_{\theta}=e^{-i\theta G}\rho_{\beta}e^{i\theta G}$, by the quadratic generator
$$
G=\frac{g}{2}\bigl(a^{2}+a^{\dagger2}\bigr),
$$
a squeezing‑type coupling of strength $g$, of the kind implemented by parametric‑down‑conversion‑style interactions [5].

### 3.2 QFI formula and Cramér–Rao bound

For a unitary encoding on a state diagonal in the eigenbasis $\{|m\rangle\}$ with eigenvalues $p_{m}$, the SLD QFI is [1,2]
$$
F_{Q}=2\sum_{m,n}\frac{(p_{m}-p_{n})^{2}}{p_{m}+p_{n}}\,|\langle m|G|n\rangle|^{2}
=4\sum_{m<n}\frac{(p_{m}-p_{n})^{2}}{p_{m}+p_{n}}\,|G_{mn}|^{2}.
$$
The SLD QFI is the standard monotone metric; at high temperature all monotone metrics coincide with it to leading order [1,2], so computing the SLD QFI suffices in the regime of interest. For $\nu$ independent repetitions, any unbiased estimator $\hat{\theta}$ satisfies
$$
\mathrm{Var}(\hat{\theta})\ge\frac{1}{\nu F_{Q}}.
$$

### 3.3 Work

The average internal energy after encoding is $\langle H_{0}\rangle_{\theta}=\mathrm{Tr}(H_{0}\rho_{\theta})$; for an isolated unitary the injected work is the change in average energy,
$$
W(\theta)=\langle H_{0}\rangle_{\theta}-\langle H_{0}\rangle_{0}.
$$

### 3.4 Qubit model

For the crossover analysis we use $H=\frac{\hbar\omega}{2}\sigma_{z}$ with thermal state $\rho_{\beta}=e^{-\beta H}/Z(\beta)$, $Z(\beta)=2\cosh(\beta\hbar\omega/2)$, and a transverse dimensionless generator $G=\sigma_{x}/2$. Energies are quoted in units of $\hbar\omega$; temperatures in units of $\hbar\omega/k_{B}$.

## 4. Analysis

Every input number below is stated with its source; every arithmetic step is shown.

### 4.1 Generator matrix elements (bosonic model)

The only nonzero actions are $a|n\rangle=\sqrt{n}\,|n-1\rangle$ and $a^{\dagger}|n\rangle=\sqrt{n+1}\,|n+1\rangle$. Hence $a^{2}|n\rangle=\sqrt{n(n-1)}\,|n-2\rangle$ and $a^{\dagger2}|n\rangle=\sqrt{(n+1)(n+2)}\,|n+2\rangle$, so
$$
\langle n+2|G|n\rangle=\frac{g}{2}\sqrt{(n+1)(n+2)},\qquad G_{nn}=0,\qquad \text{all other }G_{mn}=0.
$$

### 4.2 QFI sum reduces to $(n,n+2)$ pairs

Only pairs $(n,n+2)$ contribute:
$$
F_{Q}=4\sum_{n=0}^{\infty}\frac{(p_{n}-p_{n+2})^{2}}{p_{n}+p_{n+2}}\cdot\frac{g^{2}}{4}(n+1)(n+2).
$$
With $p_{n}=(1-q)q^{n}$:
\begin{align*}
p_{n}-p_{n+2}&=(1-q)q^{n}(1-q^{2}),\\
p_{n}+p_{n+2}&=(1-q)q^{n}(1+q^{2}),
\end{align*}
\[
\frac{(p_{n}-p_{n+2})^{2}}{p_{n}+p_{n+2}}=(1-q)\,q^{n}\,\frac{(1-q^{2})^{2}}{1+q^{2}}.
\]

### 4.3 Series evaluation

The remaining sum is $S(q)=\sum_{n=0}^{\infty}(n+1)(n+2)q^{n}$. Since $\sum_{n=0}^{\infty}q^{n+2}=q^{2}/(1-q)$, differentiating twice gives
$$
S(q)=\frac{d^{2}}{dq^{2}}\frac{q^{2}}{1-q}=\frac{2}{(1-q)^{3}}.
$$
Numerical check at $q=0.1$: the partial sum $n=0,\dots,3$ gives $2+6(0.1)+12(0.01)+20(0.001)=2.740$; the tail $n\ge4$ contributes $30(10^{-4})+42(10^{-5})+\cdots\approx0.0035$; total $\approx2.7435$, and $\frac{2}{(0.9)^{3}}=2.74348$. Consistent.

### 4.4 Closed form and limits

Substituting:
\begin{align*}
F_{Q}&=4\cdot\frac{g^{2}}{4}\cdot(1-q)\frac{(1-q^{2})^{2}}{1+q^{2}}\cdot\frac{2}{(1-q)^{3}}\\[4pt]
&=2g^{2}\,\frac{(1-q^{2})^{2}}{(1+q^{2})(1-q)^{2}}.
\end{align*}
Since $1-q^{2}=(1-q)(1+q)$,
$$
\boxed{F_{Q}(\beta)=2g^{2}\,\frac{(1+q)^{2}}{1+q^{2}},\qquad q=e^{-\beta\omega}.}
$$
Limits, evaluated directly from $F_{Q}=2g^{2}(1+q)^{2}/(1+q^{2})$:
\begin{itemize}
\item $q=0$ ($T=0$, $\beta\!\to\!\infty$): $F_{Q}=2g^{2}$.
\item $q=1$ ($T\!\to\!\infty$, $\beta\!\to\!0$): $F_{Q}=4g^{2}$.
\end{itemize}
Monotonicity:
$$
\frac{dF_{Q}}{dq}=2g^{2}\,\frac{2(1+q)(1+q^{2})-(1+q)^{2}(2q)}{(1+q^{2})^{2}}
=\frac{4g^{2}(1-q^{2})}{(1+q^{2})^{2}}>0\quad(0<q<1),
$$
and since $q$ decreases with $T$, $F_{Q}$ increases with $T$.

### 4.5 Consistency with the general bounds [1,2]

Ground‑state variance: $G^{2}=\frac{g^{2}}{4}(a^{4}+a^{2}a^{\dagger2}+a^{\dagger2}a^{2}+a^{\dagger4})$. On $|0\rangle$,
\begin{align*}
\langle0|a^{2}a^{\dagger2}|0\rangle&=2,\\
\langle0|a^{\dagger2}a^{2}|0\rangle&=0,\\
\langle0|a^{4}|0\rangle&=\langle0|a^{\dagger4}|0\rangle=0,
\end{align*}
so $\mathrm{Var}_{0}(G)=\frac{g^{2}}{2}$. The pure‑state SLD QFI is $F_{Q}(T=0)=4\,\mathrm{Var}_{0}(G)=2g^{2}$ — matches the $q\to0$ limit. The general bound [1,2] states $F_{Q}(T\!\to\!\infty)\ge8\,\mathrm{Var}_{0}(G)=4g^{2}$; here $F_{Q}(T\!\to\!\infty)=4g^{2}$ exactly, so the bound is *saturated*. The Cramér–Rao bound improves from $\frac{1}{2\nu g^{2}}$ at $T=0$ to $\frac{1}{4\nu g^{2}}$ at $T=\infty$: a factor of exactly $2$.

### 4.6 Numerical anchor at $\beta\omega=0.1$

Input: $\beta\omega=0.1$ (chosen hot‑but‑not‑classical anchor). Then $q=e^{-0.1}=0.904837$; $q^{2}=0.818730$; $(1+q)^{2}=3.628414$; $1+q^{2}=1.818730$; ratio $=3.628414/1.818730=1.994983$. Hence
$$
F_{Q}(\beta\omega=0.1)=2g^{2}\times1.994983=3.989966\,g^{2}=0.997491\times4g^{2},
$$
i.e. within $0.2509\%$ of the infinite‑temperature value.

### 4.7 Qubit: exact QFI and crossover

Step 1 (spectrum): $E_{0}=-\hbar\omega/2$, $E_{1}=+\hbar\omega/2$, $Z=2\cosh(\beta\hbar\omega/2)$, $p_{0}-p_{1}=\tanh(\beta\hbar\omega/2)$. For the transverse generator $G=\sigma_{x}/2$, $|\langle0|G|1\rangle|^{2}=1/4$. Step 2 (spectral sum, both ordered pairs, $p_{0}+p_{1}=1$):
$$
F_{K}=2\,\frac{(p_{0}-p_{1})^{2}}{p_{0}+p_{1}}\cdot\frac{1}{4}\cdot2=(p_{0}-p_{1})^{2}
=\tanh^{2}\!\left(\frac{\beta\hbar\omega}{2}\right).
$$
Limits: $T\to0$ gives $F_{K}\to1$; $T\to\infty$ gives $F_{K}\to(\beta\hbar\omega/2)^{2}\to0$.

Step 3 (crossover arithmetic). Define $x=\beta\hbar\omega$ and $\delta(x)=1-\tanh^{2}(x/2)/(x/2)^{2}$.
* At $x=2$ ($k_{B}T=\hbar\omega/2$): $\tanh(1)=0.7615942$, $\tanh^{2}(1)=0.5800257$, $(x/2)^{2}=1$, $\delta(2)=1-0.5800257=0.4199743\approx0.4200$ (42.00 % deviation).
* At $x=0.5$ ($k_{B}T=2\hbar\omega$): $\tanh(0.25)=0.2449187$, $\tanh^{2}(0.25)=0.0599852$, $(x/2)^{2}=0.0625$, $\delta(0.5)=1-0.0599852/0.0625=0.0402368\approx4.02\%$.

Thus the universal high‑$T$ extrapolation requires $k_{B}T\gtrsim2\hbar\omega$ for few‑percent accuracy.

### 4.8 Work for the quadratic encoding

Under $e^{-i\theta G}$ with $G=\frac{g}{2}(a^{2}+a^{\dagger2})$, the annihilation operator undergoes the Bogoliubov transformation $a\mapsto a\cosh(g\theta)-i\,a^{\dagger}\sinh(g\theta)$. Then
\begin{align*}
\langle H_{0}\rangle_{\theta}
&=\omega\Bigl\langle\bigl(c\,a^{\dagger}+i s\,a\bigr)\bigl(c\,a-i s\,a^{\dagger}\bigr)\Bigr\rangle\\
&=\omega\bigl(c^{2}\bar{n}+s^{2}(\bar{n}+1)\bigr)\\
&=\omega\bigl(\bar{n}\cosh(2g\theta)+\sinh^{2}(g\theta)\bigr),
\end{align*}
where $c=\cosh(g\theta)$, $s=\sinh(g\theta)$, and $\bar{n}=q/(1-q)$. Since $\langle H_{0}\rangle_{0}=\omega\bar{n}$, the injected work is
$$
W(\theta)=\omega\sinh^{2}(g\theta)\bigl(1+2\bar{n}\bigr).
$$
Using $1+2\bar{n}=(1+q)/(1-q)=\coth(\beta\omega/2)$ (the identity follows from $q=e^{-\beta\omega}$), we obtain
$$
\boxed{W(\theta)=\omega\sinh^{2}(g\theta)\,\coth\!\left(\frac{\beta\omega}{2}\right)
\approx\omega g^{2}\theta^{2}\,\coth\!\left(\frac{\beta\omega}{2}\right)\quad(g\theta\ll1).}
$$
The work carries the thermal factor $\coth(\beta\omega/2)$ at every order in $g\theta$; this factor diverges as $2/(\beta\omega)$ at high temperature, while the QFI saturates at $4g^{2}$. Consequently the work per unit QFI at fixed $\theta$ is
$$
\frac{W}{F_{Q}}\approx\frac{\omega\theta^{2}\coth(\beta\omega/2)}{4},
$$
which grows linearly in $T$ at high temperature (restoring $\hbar$, $\coth(\beta\omega/2)\approx2k_{B}T/(\hbar\omega)$).

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured.

* **R1 (Bosonic quadratic QFI).** For $H_{0}=\omega a^{\dagger}a$, $G=\frac{g}{2}(a^{2}+a^{\dagger2})$:
$$
F_{Q}(\beta)=2g^{2}\frac{(1+q)^{2}}{1+q^{2}},\qquad
F_{Q}(T=0)=2g^{2},\qquad
F_{Q}(T\!\to\!\infty)=4g^{2}.
$$

* **R2 (Bound saturation).** $\mathrm{Var}_{0}(G)=\frac{g^{2}}{2}$, so $8\,\mathrm{Var}_{0}(G)=4g^{2}=F_{Q}(\infty)$: the general quadratic‑generator bound of [1,2] is saturated exactly. Cramér–Rao improvement factor: exactly $2$.

* **R3 (Numerical anchor).** At $\beta\omega=0.1$: $F_{Q}=3.989966\,g^{2}=0.997491\times4g^{2}$, i.e. $99.7491\%$ of the infinite‑temperature value (deviation $0.2509\%$).

* **R4 (Qubit exact QFI).** For $H=\frac{\hbar\omega}{2}\sigma_{z}$, $G=\sigma_{x}/2$:
$$
F_{K}=\tanh^{2}\!\left(\frac{\hbar\omega}{2k_{B}T}\right),
$$
with $F_{K}\to1$ as $T\to0$ and $F_{K}\to(\hbar\omega/2k_{B}T)^{2}\to0$ as $T\to\infty$.

* **R5 (Crossover).** Deviation from the universal high‑$T$ extrapolation: $\delta=0.4200$ (42.00 %) at $k_{B}T=\hbar\omega/2$; $\delta=0.0402$ (4.02 %) at $k_{B}T=2\hbar\omega$.

* **R6 (Work).** $W(\theta)=\omega\sinh^{2}(g\theta)\coth(\beta\omega/2)\approx\omega g^{2}\theta^{2}\coth(\beta\omega/2)$ for $g\theta\ll1$; at $T=0$ this reduces to $\omega g^{2}\theta^{2}$, while at high temperature $W\approx2g^{2}\theta^{2}k_{B}T/\hbar$, and the work per unit QFI $W/F_{Q}\approx\omega\theta^{2}\coth(\beta\omega/2)/4$ grows linearly in $T$.

* **R7 (Projection).** For an $N$‑sensor uncorrelated array of qubit sensors, $\mathcal{F}^{(N)}=N\,F_{K}$ by standard additivity for product probes. *Projection assumptions:* independent sensors, no cross‑correlations, identical temperature. Under these assumptions, at $k_{B}T=2\hbar\omega$, $\mathcal{F}^{(N)}=0.05999\,N$; matching one ground‑state sensor ($\mathcal{F}=1$) requires $N\approx17$ warm sensors.

## 6. Discussion

**Limitations.** The bosonic result R1 assumes an ideal thermal Gibbs state of $H_{0}$, exact unitary encoding, and no decoherence; strong system–bath coupling producing non‑Gibbs steady states invalidates the spectral derivation. The factor‑of‑two statement is proven (and here saturated) only for *purely quadratic* generators; linear generators on qubits can violate the analogous inequality, and higher‑degree generators cause the high‑temperature QFI to diverge rather than saturate [1,2]. The qubit result R4 is restricted to a transverse generator: for commuting generators the SLD QFI vanishes identically, a nontrivial warning that generator geometry, not temperature, can be the dominant design variable near the commuting boundary.

**Failure modes and falsifiability.** R1 is directly falsifiable: any experiment on a well‑thermalized bosonic mode measuring phase‑estimation variance $\mathrm{Var}(\hat{\theta})\ge1/(\nu F_{Q})$ that finds $F_{Q}(\infty)<2F_{Q}(0)$ within experimental uncertainty would falsify the derivation (which relies only on the spectral form of $\rho_{\beta}$ and the SLD definition), indicating unaccounted noise, a non‑thermal state, or a misidentified generator order. Similarly, observing work scaling different from $W\propto\omega g^{2}\theta^{2