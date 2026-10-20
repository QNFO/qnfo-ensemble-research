## 6. Discussion

The quantitative analysis presented in Sections 4 and 5 establishes two complementary perspectives on the master‑calibration problem.  The **combinatorial perspective** (Derivations 1 and 2) shows that the 29 unresolved bifurcations listed in the inventory [10] generate 406 unordered pairwise translation maps and 3 654 independent composition constraints, giving an exact constraint‑to‑map ratio of  

$$\frac{3654}{406}=9.0.$$  

The **error‑budget perspective** (Derivations 3–9) quantifies how edge‑wise translation errors propagate around cycles and how mediating domains increase the effective error.  Together these results answer the two research questions posed in the Introduction: (i) a master calibration can exist only for families whose pairwise‑map capacity exceeds the number of schisms, and (ii) even when this capacity condition holds, the error budget must be tight enough that every cycle closes within a prescribed tolerance $\tau$.

### 6.1  Falsifiability criterion

A concrete falsification experiment follows directly from the closure‑error bound derived in Derivation 3.  Consider a three‑framework loop with edge errors  

$$\varepsilon_{12}=10^{-3},\qquad \varepsilon_{23}=2\times10^{-3},\qquad \varepsilon_{31}=5\times10^{-4}$$  

as used for Result R3.  A study would **assemble** three physical subsystems (e.g., a quantum‑optical platform, a classical interferometer, and a microwave resonator) that implement the translations $\tau_{12}$, $\tau_{23}$ and $\tau_{31}$, **measure** each $\varepsilon_{ij}$ on a common test battery, **compute** the closure error  

$$\Delta_{\gamma}=1-(1-\varepsilon_{12})(1-\varepsilon_{23})(1-\varepsilon_{31})$$  

and **compare** the result to the bound $3.4965\times10^{-3}$ obtained in R3.  Observation of $\Delta_{\gamma}>3.5\times10^{-3}$ would falsify the first‑order composition model assumed throughout the paper and would invalidate the genericity projection (Derivation 5) that treats each square constraint as an independent Bernoulli trial with probability $p=0.9$.

### 6.2  Limitations

- **assumes** independent translation errors on each edge (Definition 3.2); correlated systematic drifts would increase $\Delta_{\gamma}$ beyond the product bound.  
- **neglects** higher‑order cycles (four or more frameworks); the constraint‑to‑map ratio of 9.0 only counts unordered triples (Derivation 1).  
- **relies** on the one‑schism‑per‑pair assumption (Derivation 2); if multiple schisms can share a single unordered pair, the combinatorial overdetermination is relaxed but the analysis of unassigned bifurcations (the “8 schisms” in R2) no longer applies.  
- **uses** a uniform error floor $\varepsilon_{\min}=10^{-2}$ motivated by the limiting systematic in 21 cm cosmology [6]; other domains may have lower or higher intrinsic floors, altering the structural‑vs‑conventional classification (Derivation 4).  
- **adopts** a tolerance $\tau$ that is not tied to a specific experimental requirement; choosing $\tau=10^{-3}$ (Derivation 9) yields a per‑edge error requirement of $3.33\times10^{-4}$, but different applications (e.g., collider precision measurements) may demand tighter tolerances, which would further restrict feasible families.  

Sensitivity analysis (Derivation 8) shows that halving all edge errors reduces the closure bound from $3.4965\times10^{-3}$ to $1.749\times10^{-3}$, confirming approximate linearity.  However, the same scaling does not hold once mediated domains are introduced: Derivation 7 demonstrates that replacing a single edge of error $\varepsilon=10^{-2}$ with a two‑edge mediated chain raises the effective error to $1-(1-\varepsilon)^{2}=0.0199$, i.e. almost a factor of two increase.  This non‑linear penalty limits the usefulness of mediating domains unless the direct edge error can be reduced substantially.

### 6.3  Open questions

1. **Higher‑order cycle behavior.**  The product bound $\Delta_{\gamma}\le1-\prod_{e\in\gamma}(1-\varepsilon_{e})$ is exact for any cycle, but the combinatorial explosion of constraints for $|\gamma|\ge4$ has not been enumerated.  Determining the exact constraint‑to‑map ratio for larger loops would clarify whether the ratio 9.0 is a worst‑case or typical value.  
2. **Correlation structures.**  Empirical calibration studies such as the road‑marking mediated calibration in [3] report positional accuracy of $0.02\ \mathrm{m}$ and angular accuracy of $0.086^{\circ}$, suggesting that translation errors may be spatially correlated.  Incorporating a covariance model into the error‑propagation formalism could tighten or relax the closure bound.  
3. **Alternative error metrics.**  The analysis uses a fractional disagreement metric $\varepsilon_{ij}\in[0,1)$.  Other metrics (e.g., Kullback–Leibler divergence between probability distributions of test‑battery outcomes) might better capture the information loss in quantum‑to‑classical decoherence maps.  
4. **Dynamic schism allocation.**  The one‑schism‑per‑pair assumption treats each bifurcation as a static resource.  In practice, a single translation map may resolve multiple related schisms (e.g., a decoherence map that simultaneously bridges the Heisenberg cut and the quantum‑gravity interface).  Formalizing a “schism‑sharing” factor could reduce the effective $N_{\mathrm{schism}}$ in the combinatorial count.  

### 6.4  Implications for the structural‑vs‑conventional classification

Derivation 4 shows that a chain of $k=4$ edges each with floor $\varepsilon_{\min}=10^{-2}$ yields a closure error of $3.94\times10^{-2}$.  Since the oblique‑parameter precision expected at future $e^{+}e^{-}$ colliders is $\sim1\%$ (Section 3.5, citing [1]), any translation chain whose closure error exceeds $10^{-2}$ classifies the associated schism as **structural** for that application.  Conversely, if a direct translation with $\varepsilon=10^{-2}$ can be achieved, the schism is **conventional** because the error budget meets the tolerance.  This dichotomy provides a quantitative decision rule for allocating engineering effort: invest in improving the direct translation (e.g., better decoherence control) before introducing mediating domains, whose price is quantified in Derivation 7.  

### 6.5  Summary of quantitative findings

| Identifier | Statement | Computation |
|------------|-----------|-------------|
| **R1** | Pairwise maps = 406; composition constraints = 3 654; ratio = 9.0. | $\binom{29}{2}=406$, $\binom{29}{3}=3654$, $3654/406=9.0$ (Derivation 1). |
| **R2** | For $n=7$, unordered pairs = 21; at least 8 schisms remain unassigned under one‑schism‑per‑pair. | $\binom{7}{2}=21$, $29-21=8$ (Derivation 2). |
| **R3** | Closure bound for edge errors $10^{-3},2\times10^{-3},5\times10^{-4}$ is $3.4965\times10^{-3}$. | $1-0.999\times0.998\times0.9995=3.4965\times10^{-3}$ (Derivation 3). |
| **R4** | Chain of four edges with $\varepsilon_{\min}=10^{-2}$ yields $\Delta=3.94\times10^{-2}$. | $1-(0.99)^{4}=3.94\times10^{-2}$ (Derivation 4). |
| **R5** | Energy‑window factor = 2 (abstract) and = 3 (preface). | $1\ \mathrm{TeV}/500\ \mathrm{GeV}=2$, $1.5\ \mathrm{TeV}/0.5\ \mathrm{TeV}=3$ (Derivation 6). |
| **R6** | Mean schisms per domain = 4.14 (uniform assumption). | $29/7=4.142857\approx4.14$ (Derivation 6). |
| **R7** | Feynman‑Shor bifurcation ($m=2$) yields no composition constraint. | $\binom{2}{3}=0$ (Derivation 2′). |
| **P1** | Random family success probability with $p=0.9$ is $6.34\times10^{-168}$; $n_{\max}=7$ for $>1\%$ success. | $p^{3654}=6.34\times10^{-168}$, $\binom{7}{3}=35\le43.7<\binom{8}{3}$ (Derivation 5). |
| **P2** | Halving all edge errors halves the closure bound to $1.749\times10^{-3}$. | Re‑compute with $f=0.5$ (Derivation 8). |
| **P3** | Mediated translation doubles error from $10^{-2}$ to $0.0199$. | $1-(1-0.01)^{2}=0.0199$ (Derivation 7). |

These numbers are the sole quantitative basis for the conclusions drawn in the paper.  No additional empirical data have been introduced, and every claim is either a direct computation (as shown above) or a projection that explicitly states its assumptions (e.g., independence of square constraints in P1).