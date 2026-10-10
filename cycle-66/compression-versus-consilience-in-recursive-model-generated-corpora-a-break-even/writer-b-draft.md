# Compression Versus Consilience in Recursive Model-Generated Corpora: An Information-Theoretic Crossover Analysis

## Abstract

Training machine learning models on model-generated (synthetic) data is often modeled as lossy compression of real-world structure: each recursive fine-tuning generation should shrink tail entropy and effective dimensionality, producing progressively "shallower" inference. Yet practitioners of large-scale synthetic corpora report novel cross-disciplinary link structure that no comparably sized human effort would surface. We formalize this tension in a minimal stochastic model. Per generation, tail entropy and effective dimensionality decay geometrically with retention factor $\rho$; meanwhile corpus size grows with factor $\beta$, so the expected count of cross-domain consilience links scales as $(\beta^{2}\rho)^{g}$. We derive the exact crossover condition $\beta^{2}\rho > 1$ for consilience growth to outrun compression, and a saturation generation $g^{\ast}$ at which the link space fills. Under the reference parameterization ($\rho = 0.95$, $\beta = 1.5$, $N_0 = 10^{4}$, $\pi_0 = 10^{-6}$, link capacity $K = 10^{6}$), expected consilience links grow by a factor $2.1375$ per generation, tail entropy falls from $4.0$ to $1.434$ bits by generation $20$, and consilience novelty halves near generation $g^{\ast} \approx 11.7$. Periodic re-anchoring every $r$ generations bounds tail entropy below at $H_t^{(0)}\rho^{r}$; for $r = 5$ this floor is $3.095$ bits. The analysis yields falsifiable predictions and identifies diversity enforcement and re-anchoring as the levers that determine whether consilience gains can offset compression losses.

## 1. Introduction

A growing fraction of the data used to train machine learning models is itself produced by machine learning models. If such synthetic data is a lossy compression of high-dimensional real-world structure — a view supported by the dataset-distillation literature, which explicitly treats synthetic corpora as compressed encodings of original datasets [5], [8] — then recursive training on model-generated data should compound that loss: each generation should discard tail events, reduce effective dimensionality, and narrow the distribution of inferable content. Call this the **compression conjecture**. It predicts monotone decay of tail entropy $H_t$ and effective dimensionality $d_{\text{eff}}$ across generations of model-on-model training.

Against this stands an **emergent-consilience conjecture**, motivated by the observation that very large synthetic corpora — for example, a corpus of more than 800 model-written research papers — can still exhibit cross-disciplinary link structure that a human-scale research effort would be unlikely to find. Consilience here means the density of unexpected but valid cross-domain associations, measurable in embedding or citation-graph space. The precondition for such associations is shared vocabulary across disciplines, and this precondition is empirically scarce: a quantitative audit of cross-domain vocabulary found that $97.2\%$ of external technical vocabulary occurs in exactly one discipline [14]. If bridge terms are so rare, synthetic corpora that recombine content at machine scale might surface bridges that human literature never formed — precisely because machines can enumerate combinations humans do not attempt.

The research question is then sharp: **can emergent cross-domain link structure compensate for per-sample compression, or does compression inevitably dominate?** This paper answers with a conditional, not a verdict. We build a minimal information-theoretic model of recursive synthetic-data training (Section 3), derive closed-form decay laws for tail entropy and effective dimensionality, a growth law for expected consilience links, an exact crossover condition, and a saturation generation (Section 4). We then compute all headline numbers under a single stated reference parameterization (Sections 4–5), compare pure synthetic against re-anchored hybrid pipelines, and state the conditions under which each conjecture wins (Section 6). The contribution is not an empirical measurement but a derivable structure of predictions that any simulation or corpus study can falsify.

## 2. Background and Related Work

The compression view of synthetic data has direct antecedents in several literatures.

**Bayesian data compression.** The Bayesian data compression (BDC) algorithm compresses a dataset while conserving its posterior structure, with minimal information loss given prior knowledge, in the context of signal reconstruction [1]. This is the closest formal analogue to our setting: the question "what information survives compression?" is answered there by posterior conservation. Our tail-entropy decay law (Section 4.1) is the recursive-corpus analogue of BDC's single-step information budget: if each generation preserves only a fraction $\rho$ of tail information, recursion turns a single-step loss into geometric decay.

**Compression for control.** In data-driven robust control, an optimal-transport-based method compresses a large dataset of input/output pairs into a smaller synthetic dataset of representative behaviours, to alleviate computational cost while retaining controller utility [2]. The "representative behaviours" framing is exactly the compression conjecture in miniature: compression keeps the typical and discards the atypical. Our model makes the cost of discarding the atypical explicit as tail-entropy loss, and asks when recombination of the retained mass regenerates value.

**Adaptive trade-offs in storage systems.** An adaptive column compressor for self-driving databases offers a new trade-off point between memory footprint and query speed, noting that compression often reduces query speed [3]. This is a systems-level echo of our central trade-off: compression buys efficiency at the price of a performance dimension (there query latency, here inferential depth). The entry's summary gives no further quantitative detail, so we use it only as evidence that compression-utility trade-offs are treated as first-class design objects across fields.

**Landmark encoding of time series.** Peak-nadir encoding reduces dense continuous glucose monitoring profiles to a compact set of landmark points while maintaining fidelity in reconstructed signals and derived glycemic metrics [4]. The relevant lesson is that downstream metrics can be preserved under aggressive compression when the encoding targets the structure that the downstream task reads. This motivates our hybrid-pipeline question: does re-anchoring on real data preserve exactly the tail structure that consilience metrics read?

**Dataset distillation as compression.** Dataset distillation compresses an original dataset into a small set of synthetic samples while preserving its full utility; existing methods either maximize performance under fixed storage or fix performance and minimize storage, and the rate-utility perspective frames this as a compression problem [5]. A companion mechanistic study notes that distillation is a training-aware data compression technique whose mechanisms — how task-relevant information is extracted and encoded into synthetic points — remain largely empirical [8]. These two works supply the per-generation compression step of our model: distillation is the deliberate, optimized version of what recursive synthetic training does inadvertently. Our decay factor $\rho$ is the un-optimized counterpart of their rate-utility frontier.

**Compression as clustering.** Spatial regionalization based on optimal information compression extracts natural regions without user-specified region counts or similarity measures, using information compression as the clustering principle [6]. This supports our treatment of emergent structure: compression itself can reveal structure (regions, clusters) that was not annotated in advance — the optimistic reading under which synthetic corpora might reveal cross-domain structure rather than merely lose it.

**Latent-space compression.** A quantum variational autoencoder with regularized mixed-state latent representations addresses the problem that large real-world datasets exceed scarce quantum hardware, using low-dimensional representations that preserve essential information for downstream analysis [7]. The entry's summary is truncated, but its framing — low-dimensional representations preserving essential information — is the same effective-dimensionality reduction our model predicts for recursive corpora, here as a design goal rather than a side effect.

**Tensor compression.** A modified Levenberg–Marquardt algorithm for tensor canonical polyadic (CP) decomposition, formulated as nonlinear least squares, is applied to image compression and reconstruction [11]. CP decomposition is a concrete instantiation of effective-dimensionality reduction: a high-dimensional object is represented by a low-rank factorization. Our $d_{\text{eff}}$ decay law is the corpus-level analogue of rank reduction.

**Synthetic data privacy.** A survey of privacy measurement in tabular synthetic data reports that there is no standard for quantifying the degree of privacy protection of synthetic data and discusses proposed quantification approaches [10]. We cite this as a cautionary parallel: synthetic-data evaluation currently lacks agreed metrics, which is also true of consilience measurement; our Section 3 therefore defines its metrics explicitly rather than importing them.

**Domain illustration.** Constraints on dark energy from H II starburst galaxy apparent magnitude versus redshift data were found to be generally consistent with those from other datasets but not as restrictive as the tightest available constraints [9]. We use this only as an example of cross-dataset consilience in science: agreement across independent data sources is the classical form of the consilience our metric generalizes to cross-domain link density.

Finally, the QNFO audit of cross-domain vocabulary measures the precondition of consilience — shared vocabulary — and finds that $97.2\%$ of external technical vocabulary occurs in exactly one discipline, with bridge terms massively enriched in method-level vocabulary [14]. This number enters our model as motivation for small baseline cross-domain association probability $\pi_0$.

## 3. Methods

### 3.1 Model of a recursive synthetic corpus

Let generation $g \in \{0, 1, 2, \dots\}$ denote a corpus $\mathcal{D}_g$ of $N_g$ samples, where $\mathcal{D}_0$ is human-anchored (real) data and $\mathcal{D}_{g+1}$ is generated by a model trained on $\mathcal{D}_g$ (possibly mixed with fresh real data; Section 4.4). Each sample is a point in a high-dimensional semantic space; we summarize it by two statistics:

- **Tail entropy** $H_t$: the Shannon entropy carried by the tail of the sample-topic distribution, i.e., the entropy mass outside the head of topics covering $1 - \epsilon$ of probability mass. Formally, if $p_g(k)$ is the topic distribution of $\mathcal{D}_g$ and $\mathcal{H}_\epsilon(g)$ the head set, then
$$H_t^{(g)} = -\sum_{k \notin \mathcal{H}_\epsilon(g)} p_g(k) \log_2 p_g(k).$$
- **Effective dimensionality** $d_{\text{eff}}^{(g)}$: the participation ratio of the embedding covariance spectrum $\{\lambda_i^{(g)}\}$,
$$d_{\text{eff}}^{(g)} = \frac{\left(\sum_i \lambda_i^{(g)}\right)^{2}}{\sum_i \left(\lambda_i^{(g)}\right)^{2}}.$$

### 3.2 Compression step

Each generation applies a lossy compression operator $\mathcal{C}$ to the corpus. We assume $\mathcal{C}$ acts as a contraction on both statistics with a single retention factor $\rho \in (0,1)$:
$$H_t^{(g+1)} = \rho\, H_t^{(g)}, \qquad d_{\text{eff}}^{(g+1)} = \rho\, d_{\text{eff}}^{(g)}.$$
This is the strong form of the compression conjecture; Section 6 discusses when it fails. The factor $\rho$ is the free parameter of the model; it is not measured here but treated parametrically, with all results given as functions of $\rho$ and instantiated at a reference value.

### 3.3 Consilience metric

Define a **cross-domain link** as a pair of samples $(x_i, x_j)$ from different disciplines whose embedding similarity or citation-graph co-occurrence exceeds a threshold, and which is not derivable from the head vocabulary of either discipline. Let $\pi_g$ be the per-pair probability of such a link in $\mathcal{D}_g$. Because genuine cross-domain bridges live in the tail (rare vocabulary; cf. the $97.2\%$ single-discipline share of external technical vocabulary [14]), we set
$$\pi_g = \pi_0\, \rho^{\gamma g},$$
with tail-concentration exponent $\gamma \geq 0$: $\gamma = 0$ means link probability is compression-neutral, $\gamma = 1$ means it decays exactly with tail mass. Corpus size grows as
$$N_g = N_0\, \beta^{g}, \qquad \beta > 1.$$
The expected number of cross-domain links is
$$E_g = \binom{N_g}{2} \pi_0\, \rho^{\gamma g}.$$

### 3.4 Novelty and saturation

Links repeat. Let $K$ be the capacity of the link-type space (the number of distinguishable cross-domain link types). With cumulative expected links $S_g = \sum_{k=0}^{g} E_k$, the fraction of generation-$g$ links that are **novel** (of a type not previously instantiated) is modeled as
$$\nu_g = \exp\!\left(-\frac{S_{g-1}}{K}\right).$$
The expected count of novel consilience links is then $E_g^{\text{nov}} = E_g\, \nu_g$. The **saturation generation** $g^{\ast}$ is where $\nu_g = 1/2$, i.e., $S_{g-1} = K \ln 2$.

### 3.5 Hybrid re-anchoring

In a hybrid pipeline, a fraction of each generation's training mixture is fresh real data. We model the simplest regime: full re-anchoring every $r$ generations, which resets the compression operator. Tail entropy then obeys a sawtooth bounded below by
$$H_{t,\min} = H_t^{(0)} \rho^{r}.$$

All symbols: $g$ generation index; $\rho$ per-generation retention; $\beta$ corpus growth factor; $N_0$ initial corpus size; $\pi_0$ baseline cross-domain link probability; $\gamma$ tail-concentration exponent; $K$ link-type capacity; $r$ re-anchoring period; $H_t^{(0)}$ initial tail entropy; $d_0$ initial effective dimensionality.

## 4. Analysis

Every input number below is either a model parameter declared in Section 3 or derived here. The reference parameterization, used for all concrete numbers, is:

$$\rho = 0.95,\quad \beta = 1.5,\quad N_0 = 10^{4},\quad \pi_0 = 10^{-6},\quad \gamma = 1,\quad K = 10^{6},\quad H_t^{(0)} = 4.0\ \text{bits},\quad d_0 = 128.$$

These values are assumptions, not measurements; $\rho = 0.95$ represents mild per-generation loss, $\beta = 1.5$ moderate corpus growth, and $\pi_0 = 10^{-6}$ a rare bridge event consistent in spirit with the near-total single-discipline confinement of technical vocabulary reported in [14] (that work reports $97.2\%$ of external technical vocabulary in one discipline; we do not convert this into $\pi_0$, we only use it to justify treating $\pi_0$ as small).

### 4.1 Tail-entropy and effective-dimensionality decay

From the recursion $H_t^{(g)} = \rho\, H_t^{(g-1)}$ with $H_t^{(0)} = 4.0$:
$$H_t^{(g)} = H_t^{(0)} \rho^{g} = 4.0 \times 0.95^{g}.$$
Compute $0.95^{20}$: $\ln 0.95 = -0.0512933$, so $20 \ln 0.95 = -1.0258655$, and $e^{-1.0258655} = 0.358486$. Hence
$$H_t^{(20)} = 4.0 \times 0.358486 = 1.433944 \approx 1.434\ \text{bits}.$$
Similarly $d_{\text{eff}}^{(20)} = 128 \times 0.358486 = 45.886 \approx 45.9$.

Half-life of tail entropy: $0.95^{g} = 0.5 \Rightarrow g = \ln 0.5 / \ln 0.95 = (-0.693147)/(-0.0512933) = 13.513$. So tail entropy halves every $\approx 13.5$ generations.

### 4.2 Consilience growth and the crossover condition

With $\gamma = 1$,
$$E_g = \binom{N_0 \beta^{g}}{2}\, \pi_0\, \rho^{g} \approx \frac{N_0^{2}\pi_0}{2}\, \beta^{2g} \rho^{g} = E_0\, (\beta^{2}\rho)^{g},$$
where $E_0 = \binom{N_0}{2}\pi_0$. Compute $E_0$: $\binom{10^{4}}{2} = \frac{10^{4} \times 9999}{2} = 49{,}995{,}000$, so
$$E_0 = 49{,}995{,}000 \times 10^{-6} = 49.995.$$
Growth factor per generation:
$$\beta^{2}\rho = 1.5^{2} \times 0.95 = 2.25 \times 0.95 = 2.1375.$$
Since $2.1375 > 1$, expected consilience links **grow** under this parameterization. The exact crossover condition is
$$\beta^{2}\rho^{\gamma} > 1 \quad \Longleftrightarrow \quad \rho > \beta^{-2/\gamma}.$$
For $\gamma = 1$: $\rho > \beta^{-2} = 1/2.25 = 0.4444$. For $\gamma = 2$ (links concentrated twice as strongly in the tail): $\rho > \beta^{-1} = 0.6667$. Compression dominates consilience whenever $\rho$ falls below these thresholds.

Concrete growth check: $E_{10} = 49.995 \times 2.1375^{10}$. Compute $2.1375^{10}$: $\ln 2.1375 = 0.759757$, so $10 \times 0.759757 = 7.59757$, and $e^{7.59757} = 1990.6$. Hence
$$E_{10} = 49.995 \times 1990.6 = 99{,}524.$$

### 4.3 Saturation generation

Cumulative links $S_g = E_0 \sum_{k=0}^{g} (\beta^{2}\rho)^{k} = E_0\, \frac{(\beta^{2}\rho)^{g+1} - 1}{\beta^{2}\rho - 1} = 49.995 \times \frac{2.1375^{g+1} - 1}{1.1375}.$

Saturation at $\nu_g = 1/2$ requires $S_{g-1} = K \ln 2 = 10^{6} \times 0.693147 = 693{,}147$. Solve:
$$49.995 \times \frac{2.1375^{g} - 1}{1.1375} = 693{,}147$$
$$2.1375^{g} - 1 = \frac{693{,}147 \times 1.1375}{49.995} = \frac{788{,}455}{49.995} = 15{,}771$$
$$2.1375^{g} = 15{,}772 \Rightarrow g = \frac{\ln 15{,}772}{\ln 2.1375} = \frac{9.6661}{0.759757} = 12.72.$$
So $g^{\ast} \approx 12.7$: under the reference parameterization, roughly half of cross-domain links at generation $13$ are repeats of types already instantiated.

Novelty at generation $10$: $S_9 = 49.995 \times \frac{2.1375^{10} - 1}{1.1375} = 49.995 \times \frac{1989.6}{1.1375} = 49.995 \times 1748.9 = 87{,}437$. Then
$$\nu_{10} = e^{-87{,}437/10^{6}} = e^{-0.087437} = 0.9163.$$
So at generation $10$, $91.6\%$ of consilience links are still novel — consilience and compression coexist through the mid-range.

### 4.4 Re-anchoring floor

With full re-anchoring every $r$ generations, tail entropy is bounded below by $H_{t,\min} = H_t^{(0)}\rho^{r}$. For $r = 5$: $0.95^{5} = e^{-0.2564665} = 0.773781$, so
$$H_{t,\min} = 4.0 \times 0.773781 = 3.095\ \text{bits}.$$
For $r = 10$: $0.95^{10} = e^{-0.512933} = 0.598737$, giving $H_{t,\min} = 2.395$ bits. Re-anchoring converts unbounded geometric decay into a controlled floor, at the cost of real-data acquisition per cycle.

### 4.5 Effective dimensionality under the same law

$d_{\text{eff}}^{(g)} = 128 \times 0.95^{g}$. At the saturation generation $g^{\ast} = 12.7$: $0.95^{12.7} = e^{-0.651425} = 0.5214$, so $d_{\text{eff}}^{(g^{\ast})} = 128 \times 0.5214 = 66.7$. At the moment consilience novelty halves, effective dimensionality has fallen to about $52\%$ of its initial value — both phenomena are simultaneously active, which is the paper's central quantitative finding.

## 5. Results

All numbers below are computed in Section 4 from the declared reference parameterization ($\rho = 0.95$, $\beta = 1.5$, $N_0 = 10^{4}$, $\pi_0 = 10^{-6}$, $\gamma = 1$, $K = 10^{6}$, $H_t^{(0)} = 4.0$ bits, $d_0 = 128$); they are model outputs, not empirical measurements.

**R1 (Decay law).** Tail entropy and effective dimensionality decay geometrically: $H_t^{(g)} = 4.0 \times 0.95^{g}$ bits and $d_{\text{eff}}^{(g)} = 128 \times 0.95^{g}$. At $g = 20$: $H_t^{(20)} = 1.434$ bits, $d_{\text{eff}}^{(20)} = 45.9$. Tail-entropy half-life: $13.5$ generations.

**R2 (Crossover condition).** Expected consilience links grow iff $\beta^{2}\rho^{\gamma} > 1$. Under the reference parameterization the per-generation growth factor is $2.1375$, so consilience grows. The critical retention thresholds are $\rho > 0.4444$ for $\gamma = 1$ and $\rho > 0.6667$ for $\gamma = 2$.

**R3 (Growth magnitude).** $E_0 = 49.995$ expected cross-domain links at generation $0$; $E_{10} = 99{,}524$ at generation $10$.

**R4 (Saturation).** The novelty fraction at generation $10$ is $\nu_{10} = 0.9163$ ($91.6\%$ novel). The saturation generation is $g^{\ast} \approx 12.7$, beyond which consilience growth is increasingly recycled rather than novel.

**R5 (Coexistence window).** At $g^{\ast} \approx 12.7$, $d_{\text{eff}} = 66.7$ ($52.1\%$ of $d_0$) and $H_t = 4.0 \times 0.5214 = 2.086$ bits ($52.1\%$ of $H_t^{(0)}$). Consilience growth and compression decay coexist over a window of at least $\sim 12$ generations under these parameters.

**R6 (Re-anchoring).** Re-anchoring every $r = 5$ generations bounds tail entropy at $H_{t,\min} = 3.095$ bits; every $r = 10$ generations, at $2.395$ bits. Hybrid pipelines trade real-data cost for a compression floor, and by R2 they do not change the consilience growth condition (which depends on $\beta$, $\rho$, $\gamma$) but they prevent the late-generation collapse of $H_t$ that would eventually starve $\pi_g$.

**R7 (Conditional answer).** Compression does **not** inevitably dominate: for $\rho > \beta^{-2/\gamma}$, machine-scale corpus growth ($\beta^{2}$ pair-scaling) outruns per-sample tail loss ($\rho^{\gamma}$). But consilience is finite: the link space saturates at $g^{\ast} \approx 12.7$ generations under the reference parameters, after which the emergent-consilience mechanism exhausts itself unless $K$ or $\beta$ grows.

## 6. Discussion

**Limitations of the model.** The single-factor contraction $H_t^{(g+1)} = \rho H_t^{(g)}$ is the model's strongest assumption. Real recursive training may exhibit superlinear collapse (mode collapse amplifying across generations) or sublinear loss (regularization and sampling temperature preserving tails). If $\rho$ is generation-dependent, e.g., $\rho_g = \rho_{\infty} + (\rho_0 - \rho_{\infty})\delta^{g}$, all closed forms become products $\prod_k \rho_k$ and the crossover condition changes; our results then describe only the asymptotic-$\rho$ regime.

**The $\gamma$ exponent is the crux.** The entire answer pivots on how strongly consilience lives in the tail. If cross-domain bridges are head phenomena — method-level vocabulary shared across fields, as the bridge-term enrichment reported in [14] suggests — then $\gamma$ is small and consilience is robust to compression. If bridges are irreducibly rare-tail events, $\gamma \to 1$ or higher and compression bites. Measuring $\gamma$ on a real recursive corpus is the single most valuable empirical follow-up.

**What would falsify the claims.** (i) A recursive fine-tuning study measuring $H_t$ and $d_{\text{eff}}$ per generation that finds non-geometric decay (e.g., plateauing above $H_t^{(0)}\rho^{g}$) falsifies the contraction model. (ii) A corpus study finding consilience-link density *decaying* while $\beta^{2}\rho > 1$ holds would falsify the multiplicative link model — implying links are not independent pair events but require head-mass co-activation. (iii) Finding saturation far earlier than $g^{\ast} \approx 12.7$ under comparable $N_0$, $\pi_0$, $K$ would falsify the Poisson-style novelty model $\nu_g = e^{-S_{g-1}/K}$, which assumes uniform link-type usage; real link types are surely heterogeneous, and a Zipf-type capacity distribution would lower the effective $K$ and accelerate saturation.

**Failure modes of the hybrid prescription.** Re-anchoring bounds $H_t$ but does not guarantee consilience: if real anchor data is drawn from the same narrow disciplines that dominate the corpus, re-anchoring preserves entropy without adding bridge mass. Diversity enforcement (deliberately sampling anchor data from underrepresented domains) is the lever the model points to but does not formalize; formal verification of generated claims, mentioned in the research program, would raise the *precision* of consilience links, which our recall-style metric ignores entirely.

**Against the emergent-consilience conjecture.** A skeptic should note that our consilience count $E_g$ counts *candidate* links, not validated ones. If the per-link validity rate also decays with $\rho$ — plausible if tail samples are precisely the ones the generator fabricates least reliably — then the effective growth factor is $\beta^{2}\rho\,\kappa$ with $\kappa < 1$ a validity retention, and the crossover condition tightens to $\rho > (\beta^{2}\kappa)^{-1/\gamma}$. For $\kappa = 0.5$, $\gamma = 1$: $\rho > 1/1.125 = 0.8889$ — barely satisfied at $\rho = 0.95$. The consilience-optimal conclusion is therefore fragile to validity decay, and the honest summary is that the sign of the answer is an empirical quantity, not a theorem.

**Open questions.** (1) Measure