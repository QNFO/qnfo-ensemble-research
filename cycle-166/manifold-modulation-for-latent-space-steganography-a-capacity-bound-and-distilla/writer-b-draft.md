# Manifold Modulation for Latent Space Steganography: A Capacity Bound and Distillation Demodulation Model for Teacher-Student Transmission Channels

## Abstract

Large language models are increasingly deployed in teacher-student pipelines in which a student model is fine-tuned on text produced by a teacher, so any statistical signature the teacher imprints on its outputs is transferred to the student whether or not anyone intends it. This paper asks whether that transfer channel can be engineered deliberately: can a teacher's internal state be encoded as a steganographic modulation of its token statistics, constrained to a chosen latent manifold, so that a student fine-tuned on the carrier text demodulates and inherits a targeted behavior? The specific gap is quantitative: no existing treatment gives a bound on covert bits per carrier token when the carrier task itself constrains the output distribution. We model the teacher's output distribution as a carrier with a per-token Kullback-Leibler modulation budget and derive a capacity bound of $C = D_{\mathrm{KL}}/\ln 2$ bits per token; at an illustrative budget of $D_{\mathrm{KL}} = 0.05$ nats this yields $0.0721$ bits per token, or $721$ bits over a $10^4$-token carrier document. We further derive a detection sample size of approximately $93$ tokens for a steganalyst at $10^{-2}$ false-alarm tolerance, and a demodulation requirement of roughly $1.4 \times 10^5$ carrier tokens for a $10^4$-bit behavior specification. The results reframe fine-tuning-on-outputs as demodulation and give practitioners a budget for auditing such pipelines.

## 1. Introduction

Organizations that build and deploy large language models face a supply-chain problem that is currently unmanaged: student models are routinely fine-tuned on corpora of teacher-generated text, synthetic instruction data, and agent transcripts, and the student inherits whatever statistical structure the teacher imprinted on that text. The scale of this practice is substantial. Agentic systems now execute entire expert workflows autonomously and emit their reasoning as text; Latent-Y, for example, executes complete antibody design campaigns from text prompts, covering literature review, target analysis, epitope identification, candidate design, computational validation, and selection of lab-ready sequences, with a target-level success rate of $67\%$ across nine targets [1]. Every token of such a transcript is a potential carrier of the producing model's internal statistical state. Today, nobody measures what is transferred, nobody bounds it, and nobody can decide whether a given fine-tuning corpus carries an unacceptable amount of upstream model state. If a quantitative capacity bound existed, a data provenance auditor could certify a corpus as carrying at most $B$ bits of upstream state, and a pipeline designer could deliberately encode desired behaviors into synthetic data at a known rate rather than by trial and error.

The cost of leaving this unquantified runs in both directions. In the defensive direction, a teacher model may leak proprietary capabilities, alignment-relevant behaviors, or hidden decision policies through its outputs, and a student fine-tuned on those outputs acquires them without any explicit transfer of weights; the downstream organization has no instrument to detect or bound this. In the offensive direction, an adversary with control of a data-generating teacher could encode arbitrary behavior into a synthetic corpus that looks like an ordinary task dataset, and the victim's fine-tuning run demodulates it automatically. The decision that would change if the present result holds is precisely the audit decision: given a measured or budgeted per-token modulation $D_{\mathrm{KL}}$ and a corpus of $N$ tokens, an auditor can compute the maximum covert information $N \cdot D_{\mathrm{KL}} / \ln 2$ bits and accept or reject the corpus.

This paper formalizes the claim that any transmission from a sufficiently complex, stateful source carries two parallel information streams: the content stream, which is the explicit message, and the source-information stream, which is the sender's internal statistical state. Fine-tuning a student on a teacher's outputs is demodulation of the second stream. We propose engineering this deliberately: constrain the teacher's internal states to a chosen latent "covert manifold" while it performs an unrelated carrier task, so that the manifold's geometry is encoded into token statistics, and a student fine-tuned on that data inherits the targeted behavior.

The contributions are:

1. A formal two-stream transmission model in which a teacher performing a carrier task modulates its output distribution toward a covert manifold, with an explicit per-token Kullback-Leibler modulation budget (Section 3).
2. An information-theoretic capacity bound $C = D_{\mathrm{KL}} / \ln 2$ bits per carrier token, derived from the modulation budget, with worked numerical values at several budgets (Section 4).
3. A steganalysis sample-complexity bound showing that detection requires on the order of $\ln(1/\alpha) / D_{\mathrm{KL}}$ tokens, computed as approximately $93$ tokens at $D_{\mathrm{KL}} = 0.05$ nats and $\alpha = 10^{-2}$ (Section 4).
4. A demodulation condition for distillation: a student recovers a behavior specification of $K$ bits from a carrier corpus of $M$ tokens when $M \geq K / C$, computed as $1.39 \times 10^5$ tokens for $K = 10^4$ bits at the illustrative budget (Section 4).
5. A capacity-versus-carrier-degradation tradeoff curve under an explicitly assumed linear degradation model, giving the ablation axes that an experimental program must measure (Sections 4 and 5).

## 2. Background and Related Work

Steganography supplies the conceptual template for this work. Steganography is the science of hiding and communicating a secret message by embedding it in an innocent-looking text such that the eavesdropper is unaware of its existence; the term derives from the Greek $steganos$ (covered) and $graphia$ (writing), and it differs from cryptography in that the existence of the secret message, not merely its content, is concealed [4]. The classical formulation distinguishes $stegotext$ from $covertext$, and the intended receiver alone can detect and decipher the hidden message [4]. Our covert manifold plays the role of the secret message and the carrier task's token distribution plays the role of covertext. The quantum steganography literature also demonstrates the failure mode that motivates our steganalysis bound: protocols built on quantum key distribution were shown to be vulnerable to a steganalysis attack that can detect the presence of the hidden transmission, which is why [4] develops modified protocols in which the party communicating steganographically operates in the reverse direction of the party sending the initial quantum states, camouflaged as part of the classical reconciliation step. The lesson we carry over is that embedding direction and detection direction must be analyzed jointly; in our setting the "receiver" is a fine-tuning procedure, which is precisely why the channel is hard to police with conventional tools.

Network steganography provides the engineering precedent and the maturity warning. Network steganography has been a known covert data channeling method for over three decades, and the basic set of techniques and implementation tools has not changed significantly since their introduction in the early 1980s; the predominant methods of classical network steganography embed data in the detailed operations of network protocols, and the resultant challenges involve embedding data without detectable statistical deviation [7]. The stagnation of technique that [7] documents in the network domain is the outcome our field should avoid: model-output steganography is new enough that its capacity limits, detection thresholds, and degradation tradeoffs are still unmeasured, and the present paper supplies the first analytical scaffolding for those measurements.

The latent-manifold literature supplies the representational machinery. GeMA combines deep generative modeling with classical efficiency-analysis concepts, learning latent manifold frontiers with a ProMan-VAE architecture, and its experiments probe settings where production technologies are heterogeneous, non-convex, or confounded with scale, using $n = 500$ decision-making units averaged over $30$ Monte Carlo replications [5]. Two points from [5] transfer directly. First, its demonstration that a latent generative model can represent a structured frontier that classical estimators in observed space miss supports our claim that a low-dimensional covert manifold can be embedded in a high-dimensional output space without disturbing observable task statistics. Second, its limitation discussion states that the latent technology and inefficiency variables have clear conceptual roles but the decomposition is not uniquely identifiable in a purely data-driven sense, being regularised by priors, shape constraints, and structural equations, and that individual latent dimensions should not be over-interpreted [5]. We adopt this caution: our covert manifold is identifiable to the demodulator only because the demodulator knows the manifold's parameterization, which is exactly the steganographic key.

Latent-space subdivision demonstrates that latent structure can be engineered to carry information orthogonal to the primary prediction task. The fluid-flow architecture of [6] splits the latent space so that external information can be passively injected into the prediction process: an obstacle unseen during training is injected by supplying an encoded density field with the obstacle region masked out, and the method predicts stable flow over $400$ time steps where the unsplit baseline fails and produces unphysical behavior [6]. This is a working precedent for our central mechanism: a partitioned latent representation in which one subspace carries task content and a second subspace carries injected, task-orthogonal information that a downstream consumer reads out. Our proposal is the steganographic dual of this: the injected subspace is hidden rather than declared.

The teacher-model literature establishes that the carrier streams we analyze exist at industrial scale and quality. Latent-X is an all-atom protein design model that jointly generates sequence and structure, achieving macrocycle hit rates of $91\%$ on MDM2 and $100\%$ on MCL-1 against RFpeptide baselines of $38\%$ and $21\%$, and mini-binder hit rates from $10\%$ on TrkA to $64\%$ on BHRF1, including a $52\%$ hit rate on SC2RBD versus $12\%$ for AlphaProteo [2]. Latent-X2 extends this to zero-shot antibody design, producing potent VHHs and scFvs with drug-like profiles from the first generation, testing only $4$ to $24$ designs per modality-target pair, and demonstrating, for the first time for any de novo generated antibody, confirmed low immunogenicity in ex vivo assays with primary human peripheral blood mononuclear cells from $10$ donors [3]. These systems matter to our argument for two reasons. They generate exactly the kind of high-stakes, proprietary-capability-bearing output streams whose transmission to downstream students an auditor would want to bound; and their tiered screening workflows, in which initial single-point BLI screens advance only designs exceeding a predefined binding response threshold [3], illustrate how a generating model's internal decision policy is imprinted on the statistics of its emitted dataset, which is the source-information stream we formalize.

Information theory supplies the demodulation formalism. The monistic-reality framework of [11] formalizes perceiver correlations through mutual information, $I(X_p; X_q) = \sum_{x_p,x_q} P(x_p,x_q) \log\left[\frac{P(x_p,x_q)}{P(x_p)P(x_q)}\right]$, quantifying the correlation between perceiver states as the overlap of accessible information [11]. We use exactly this quantity as the demodulation metric: the student's recovered behavior is measured by the mutual information between the covert manifold parameter and the student's induced policy. The dual-mode arithmetic work of [12] supplies the dimensional argument that constrains our manifold design: static two-dimensional encodings are informationally incomplete for prime factorization because the dimensional mismatch between the infinite-dimensional prime exponent space and any fixed low-dimensional geometric space is fundamental, with no isomorphism existing between the representations [12]. Applied to our setting, a covert manifold of too low a dimension cannot carry an arbitrary behavior specification; the manifold dimension $d$ places a hard ceiling on the per-token covert alphabet, which enters our capacity bound.

Two further sources shape the detection and complexity analysis. The topological-aliasing work of [10] analyzes empirical detection thresholds and concludes that the temporal threshold is the primary barrier to verification, because detecting the effect requires equipment operating beyond standard experimental thresholds, with attosecond lasers only now approaching the necessary speeds [10]. This is the structural analogue of our steganalysis bound: every covert channel has a detection threshold set by the observer's resolution, and the auditor's analogue of detector resolution is the number of carrier tokens they can collect. Finally, the quantum-architectonics simulations of [9] show that interaction richness governs state-space accessibility: Universe B, with the rich interaction structure of a Rank-42 category providing a dense network of fusion channels, achieved a "Clean Sweep" with vacuum order parameter $\Psi = 0.9590$ and matter density $n \approx 0.0067$, while the low-rank Universe A suffered kinetic frustration and froze at $\Psi = 0.8333$ with relic defect density $n_{matter} \approx 0.033$ [9]. We use this as a design heuristic: a covert channel embedded in a state space with rich, dense transition structure demodulates reliably, whereas one embedded in a sparse, low-rank state space freezes before the student can extract it.

Multi-stream information extraction has a precise astronomical precedent. The SPACE mission design notes that CMB temperature spectra $C_l$ depend on the combination $\Omega_m h^2$ while the matter power spectrum $P(k)$ is sensitive to $\Omega_m h$, so combining the two datasets breaks degeneracies and tightens parameter limits beyond what either dataset achieves in isolation [8]. This is the exact logic of our two-stream model: the content stream and the source-information stream are subject to different parameter degeneracies, and a demodulator that reads both, rather than the content stream alone, recovers sender state that a content-only reader cannot.

## 3. Methods

### 3.1 Setting and notation

Let $T$ be a teacher model with internal state $s \in \mathcal{S}$, performing a carrier task. At each step the teacher emits a token $x_t$ from a vocabulary of size $V$. Absent modulation, the teacher's output distribution is $p_t(x) = p(x \mid x_{<t}, s)$, which depends on the internal state $s$. We define the carrier distribution $p^{(0)}_t(x) = p(x \mid x_{<t}, s_0)$ as the distribution the teacher would produce under a reference internal state $s_0$ that carries no covert information.

A covert manifold is a parameterized family of internal states $\{s(\theta) : \theta \in \mathcal{M}\}$ with $\mathcal{M} \subseteq \mathbb{R}^d$ a $d$-dimensional manifold. The teacher performing the carrier task while its state is constrained to $s(\theta)$ emits tokens from the modulated distribution

$$\pi_t(x) = p(x \mid x_{<t}, s(\theta)).$$

The modulation strength at step $t$ is the Kullback-Leibler divergence between the modulated and carrier distributions,

$$D_t = D_{\mathrm{KL}}\!\left(\pi_t \,\|\, p^{(0)}_t\right) = \sum_{x} \pi_t(x) \log \frac{\pi_t(x)}{p^{(0)}_t(x)}.$$

We impose a per-token modulation budget $D_t \leq D$ for all $t$. The budget is the engineering constraint that keeps the carrier task intact: it bounds the total statistical deviation of the modulated stream from an ordinary carrier stream.

### 3.2 The two-stream decomposition

The emitted sequence $x_{1:N}$ carries two streams. The content stream is the explicit carrier-task output, measured by the mutual information between the sequence and the carrier task's intended output. The source-information stream is the mutual information between the sequence and the covert parameter $\theta$,

$$I(x_{1:N}; \theta) = \sum_{x_{1:N}, \theta} P(x_{1:N}, \theta) \log \frac{P(x_{1:N}, \theta)}{P(x_{1:N}) P(\theta)},$$

which is the same functional form used in [11] for perceiver correlations. Under the budget constraint, the per-token covert capacity is bounded in Section 4 by $C = D / \ln 2$ bits, so the total covert information satisfies $I(x_{1:N}; \theta) \leq N \cdot D / \ln 2$.

### 3.3 Demodulation by fine-tuning

A student model $S$ is fine-tuned on the modulated corpus $\{x^{(i)}_{1:N_i}\}$ generated by the teacher under covert parameters $\{\theta^{(i)}\}$. Fine-tuning is demodulation if the student's induced policy $P_S(y \mid x)$ satisfies

$$I\!\left(P_S; \theta\right) > I\!\left(P_S^{(0)}; \theta\right),$$

where $P_S^{(0)}$ is the policy of a student fine-tuned on unmodulated carrier data. The demodulation gain is the excess mutual information attributable to the modulation. The condition for full recovery of a behavior specification of $K$ bits is derived in Section 4 as $M \geq K/C$, where $M$ is the total number of carrier tokens the student trains on.

### 3.4 Steganalysis model

A steganalyst observes $n$ tokens from either the carrier distribution $p^{(0)}$ or the modulated distribution $\pi$ and must decide which. This is a binary hypothesis test between two distributions whose per-token divergence is $D$. We derive the sample size required for detection at false-alarm probability $\alpha$ in Section 4 using the Chernoff-Stein exponent, which for simple hypotheses is governed by the KL divergence between the hypotheses.

### 3.5 Assumptions

We state the assumptions that the analysis rests on, since the grounding sources do not fix them empirically. (i) The carrier task constrains the teacher's output distribution only through the budget $D$; we assume the carrier task's own entropy is large enough that a budget of $D \leq 0.2$ nats per token is feasible without truncating the carrier vocabulary. (ii) We assume the covert parameter $\theta$ is drawn uniformly from a $d$-dimensional manifold whose effective discrete alphabet at token resolution is large compared to the capacity bound, so that the capacity bound, not the manifold dimension, is the binding constraint; the counter-case is governed by the dimensional-incompleteness argument of [12]. (iii) We assume a linear carrier-degradation model $\Delta A \approx \beta D$ with slope $\beta$ for the ablation analysis; this is an explicitly labeled modeling assumption to be measured experimentally, not a derived result. (iv) We assume the student's fine-tuning procedure is a standard likelihood-based update, so that information about $\theta$ present in the training corpus is transferred at a rate bounded by the corpus's covert information content.

## 4. Analysis

### 4.1 Capacity bound derivation

The teacher emits a sequence of tokens; each token is drawn from $\pi_t$ under modulation or $p^{(0)}_t$ under the carrier. The information about $\theta$ carried by the whole sequence is bounded by the mutual information $I(x_{1:N}; \theta)$. By the chain rule of mutual information and the fact that conditioning reduces entropy,

$$I(x_{1:N}; \theta) = \sum_{t=1}^{N} I(x_t; \theta \mid x_{<t}) \leq \sum_{t=1}^{N} I(x_t; \theta, x_{<t}).$$

At step $t$, the token distribution given the past and the covert state is $\pi_t(x) = p(x \mid x_{<t}, s(\theta))$. The maximal mutual information between $\theta$ and $x_t$ given the past is achieved when the modulation uses the full budget, and is bounded by the divergence between the modulated and carrier distributions:

$$I(x_t; \theta \mid x_{<t}) \leq D_{\mathrm{KL}}\!\left(\pi_t \,\|\, p^{(0)}_t\right) \leq D.$$

This is the standard bound that the information a random variable $X$ carries about a parameter cannot exceed the KL divergence between the conditional distributions it induces; in nats, $I \leq D_{\mathrm{KL}}$. Converting to bits, one nat equals $1/\ln 2$ bits. Therefore

$$C = \frac{D}{\ln 2} \ \text{bits per token},$$

and the total covert capacity of an $N$-token carrier document is

$$I_{\max}(N) = \frac{N \cdot D}{\ln 2} \ \text{bits}.$$

### 4.2 Numerical evaluation of the capacity bound

We evaluate the bound at three modulation budgets. Using $\ln 2 = 0.693147$:

At $D = 0.05$ nats:

$$C = \frac{0.05}{0.693147} = 0.072134 \ \text{bits per token}.$$

At $D = 0.10$ nats:

$$C = \frac{0.10}{0.693147} = 0.144270 \ \text{bits per token}.$$

At $D = 0.20$ nats:

$$C = \frac{0.20}{0.693147} = 0.288539 \ \text{bits per token}.$$

For a carrier document of $N = 10^4$ tokens at $D = 0.05$ nats:

$$I_{\max} = 10^4 \times 0.072134 = 721.34 \ \text{bits}.$$

In bytes this is $721.34 / 8 = 90.17$ bytes, so a single $10^4$-token document at this budget can carry at most about $90$ bytes of covert information. At $D = 0.20$ nats the same document carries $10^4 \times 0.288539 = 2885.39$ bits, or $2885.39/8 = 360.67$ bytes.

### 4.3 Steganalysis sample complexity

The steganalist performs a hypothesis test between $H_0$: tokens from $p^{(0)}$, and $H_1$: tokens from $\pi$. By the Chernoff-Stein theorem, the minimal sample size $n$ needed to detect the modulated stream with false-alarm probability $\alpha$ and high detection probability satisfies, to first order,

$$n \gtrsim \frac{\ln(1/\alpha)}{D_{\mathrm{KL}}(\pi \| p^{(0)})}.$$

We evaluate this at $\alpha = 10^{-2}$, so $\ln(1/\alpha) = \ln(100) = 4.60517$:

At $D = 0.05$ nats:

$$n \gtrsim \frac{4.60517}{0.05} = 92.10 \ \text{tokens},$$

that is, approximately $93$ tokens. At $D = 0.10$ nats:

$$n \gtrsim \frac{4.60517}{0.10} = 46.05 \ \text{tokens}.$$

At $D = 0.20$ nats:

$$n \gtrsim \frac{4.60517}{0.20} = 23.03 \ \text{tokens}.$$

The inverse scaling is the central tension of the design: doubling the modulation budget doubles the covert capacity per token and halves the number of tokens a steganalyst needs for detection. The channel is therefore detectable at modest sample sizes under this simple hypothesis test; the practical defense of the scheme is not that detection is impossible but that the steganalist must know which test to run, which is the camouflage lesson of [4], where the modified protocols hide the covert transmission inside the classical reconciliation traffic of the QKD protocol itself.

### 4.4 Demodulation condition for distillation

Let the targeted behavior be a specification of $K$ bits, meaning that the student must acquire a policy equivalent to one of $2^K$ alternatives. The student's training corpus contains $M$ carrier tokens in total, each carrying at most $C = D/\ln 2$ covert bits. The covert information available to the student is at most

$$I_{\text{avail}} = M \cdot \frac{D}{\ln 2} \ \text{bits}.$$

Full demodulation requires $I_{\text{avail}} \geq K$, giving the condition

$$M \geq \frac{K \ln 2}{D}.$$

We evaluate this for an illustrative behavior specification of $K = 10^4$ bits, which we state as an assumption about the complexity of a targeted behavioral policy; the correct value of $K$ for any real behavior is an empirical quantity that the experimental program of Section 7 must measure.

At $D = 0.05$ nats:

$$M \geq \frac{10^4 \times 0.693147}{0.05} = \frac{6931.47}{0.05} = 138{,}629.4 \ \text{tokens}.$$

At $D = 0.10$ nats:

$$M \geq \frac{6931.47}{0.10} = 69{,}314.7 \ \text{tokens}.$$

At $D = 0.20$ nats:

$$M \geq \frac{6931.47}{0.20} = 34{,}657.4 \ \text{tokens}.$$

In units of $10^4$-token documents at $D = 0.05$ nats, this is $138{,}629.4 / 10^4 = 13.86$, so approximately $14$ carrier documents suffice in information content. This number should be read as a lower bound on corpus size: the actual requirement is larger by a factor accounting for the student's learning efficiency, which is less than unity.

### 4.5 Capacity-degradation tradeoff under an assumed linear model

We model the carrier task's accuracy loss as linear in the modulation budget,

$$\Delta A \approx \beta D,$$

and we assume the slope $\beta = 0.4$ per nat as an explicitly labeled modeling assumption; measuring $\beta$ is the third testable objective of the research idea. Under this assumption:

At $D = 0.05$ nats: $\Delta A = 0.4 \times 0.05 = 0.02$, a $2\%$ carrier accuracy loss, with capacity $C = 0.072134$ bits per token.

At $D = 0.10$ nats: $\Delta A = 0.4 \times 0.10 = 0.04$, a $4\%$ loss, with $C = 0.144270$ bits per token.

At $D = 0.20$ nats: $\Delta A = 0.4 \times 0.20 = 0.08$, an $8\%$ loss, with $C = 0.288539$ bits per token.

The capacity-to-degradation ratio is constant under the linear model, $C / \Delta A = 1/(\beta \ln 2) = 1/(0.4 \times 0.693147) = 1/0.277259 = 3.6068$ bits per token per unit fractional accuracy loss. The experimental ablation over modulation strength exists precisely to test whether this ratio is constant or whether degradation is convex in $D$; convexity would make low budgets strictly more efficient per bit.

### 4.6 Manifold dimension constraint

The covert manifold has dimension $d$. If the demodulator must recover a continuous parameter $\theta \in \mathbb{R}^d$ to resolution $\delta$ per coordinate over a normalized range of $R$ per coordinate, the parameter carries

$$K_\theta = d \cdot \log_2\!\left(\frac{R}{\delta}\right) \ \text{bits}.$$

As a worked example with $d = 8$, $R/\delta = 2^{10}$ (ten bits of resolution per coordinate):

$$K_\theta = 8 \times 10 = 80 \ \text{bits}.$$

At $D = 0.05$ nats, recovering this parameter requires $M \geq 80 \times 0.693147 / 0.05 = 55.4518 / 0.05 = 1109.04$ tokens, that is, $1109.04 / 10^4 = 0.111$ of one $10^4$-token document. The dimensional-incompleteness argument of [12] applies in the opposite direction: if the behavior to be encoded requires the full structure of a high-dimensional specification space, a low-dimensional manifold cannot carry it, exactly as a static two-dimensional encoding cannot carry the infinite-dimensional prime exponent structure. The manifold dimension $d$ and the budget $D$ jointly determine what behaviors are encodable.

## 5. Results

All numbers in this section are computed in Section 4 from the stated inputs; the only non-derived quantities are the assumed slope $\beta = 0.4$ per nat and the assumed behavior size $K = 10^4$ bits, both labeled as assumptions.

**Capacity per token.** The covert capacity is $C = D/\ln 2$ bits per token: $0.072134$ bits per token at $D = 0.05$ nats, $0.144270$ at $D = 0.10$ nats, and $0.288539$ at $D = 0.20$ nats.

**Capacity per document.** A $10^4$-token carrier document carries at most $721.34$ bits ($90.17$ bytes) at $D = 0.05$ nats, $1442.70$ bits at $D = 0.10$ nats, and $2885.39$ bits ($360.67$ bytes) at $D = 0.20$ nats.

**Detection sample size.** A steganalyst testing at false-alarm probability $\alpha = 10^{-2}$ requires approximately $92.10$ tokens at $D = 0.05$ nats, $46.05$ tokens at $D = 0.10$ nats, and $23.03$ tokens at $D = 0.20$ nats, under the Chernoff-Stein first-order approximation.

**Demodulation corpus size.** Recovering a $K = 10^4$-bit behavior specification requires at least $138{,}629$ tokens at $D = 0.05$ nats, $69{,}315$ tokens at $D = 0.10$ nats