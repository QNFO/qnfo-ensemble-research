# Numeral Systems as Evolving Cognitive Technologies, Not Final Optima: Error Propagation, Compactness, and the Open Optimization Problem of Notation

## Abstract

Positional (Arabic-Indic) notation is conventionally treated as the endpoint of numeral-system evolution, but this paper argues it is a historically contingent survivor whose dominance reflects one task environment—large-scale calculation—rather than global optimality. We formalize the tradeoff between additive systems (Roman-style) and positional systems under explicit noise channels. Under a single-symbol-drop channel with uniformly distributed digits, we derive an expected error of $33751.125$ for four-digit positional numbers versus $\approx 350.9$ for additive notation, a ratio of $\approx 96.2$; under adjacent transposition, the positional expected error is $1098.9$ against an additive worst case of $900$. Positional notation wins on compactness ($4$ versus $\approx 5.7$ symbols for the same range) and on algorithmic arithmetic. Embedding both in a two-term cost model over symbol count and expected error yields an explicit crossover: additive notation is optimal whenever the error-aversion weight exceeds $0.0509$ of the per-symbol cost, so no single system dominates across task environments. We frame numeral-system evolution as a fitness landscape over tasks (ledger-keeping versus calculation), paralleling the absence of global optima in biological evolution, and conclude that notation design remains an open optimization problem, with hybrid notations as unexplored interior points.

## 1. Introduction

The positional decimal system is so thoroughly embedded in modern infrastructure that its ubiquity is easily read as evidence of optimality. This paper resists that inference. The claim we develop and partially formalize is that positional notation is a historically contingent "survivor"—a system that happened to be fit for a particular cluster of task environments (commercial calculation, astronomy, large-ledger arithmetic)—and that additive systems such as Roman numerals possess cognitive advantages that positional notation necessarily sacrifices: bounded error propagation under transcription noise, magnitude salience of individual symbols, and no need for a zero placeholder.

The question is whether these tradeoffs can be made precise. Our contribution is threefold. First, we define explicit error channels—symbol drop, adjacent transposition, and misreading—and derive closed-form expected error magnitudes for positional and additive notations, proving that additive systems have strictly bounded error propagation while positional error grows exponentially in string length. Second, we quantify the compensating advantage of positional notation in compactness and arithmetic complexity. Third, we embed both systems in a simple two-parameter cost model and show an exact crossover, demonstrating that the "best" numeral system is a function of the task environment's weighting of compactness against error robustness. This supports framing numeral-system evolution as a fitness landscape with no single dominant peak—an analogy to biological evolution's lack of a global optimum.

Throughout, a *positional* system is one in which a symbol's contribution depends on its place (e.g., $7$ in $707$ contributes $7 \cdot 10^2$); an *additive* system is one in which each symbol contributes a fixed value independent of position, with the total obtained by summation (Roman numerals, with subtractive pairs, are the familiar historical example). A *noise channel* is a probabilistic model of how a written numeral string is corrupted between writer and reader.

## 2. Background and Related Work

The literature most directly relevant to our framing comes from cognitive science and symbol-systems research, though no prior work in the supplied bibliography addresses numeral systems head-on; the closest connections are structural and methodological.

**Symbol systems as adaptive, dynamic entities.** The survey on symbol emergence in cognitive developmental systems [1] argues that symbol systems such as language are crucial for human communication and adaptation to the real-world environment, and that the symbol systems used in human society *adaptively and dynamically change over time*. This is the foundational premise of our evolutionary framing: numeral notations are symbol systems in exactly this sense, and their historical turnover (additive to positional in Western Europe) is an instance of the adaptive change the survey describes, not a monotonic ascent toward an optimum.

**Cognitive offloading.** The offloading argument of [6] distinguishes cognizers—systems with mental states—from cognitive technology, which can contribute to human cognition without itself cognizing; it holds that cognizers can offload cognitive functions onto cognitive technology, extending performance capacity beyond the limits of their own brain power, with language given as a paradigm case. Numeral notation is a canonical cognitive technology in this sense: the written numeral offloads memory and computation onto an external medium. Crucially for our argument, the *choice of offloading format* then becomes an engineering decision with measurable consequences—which is precisely what our error and compactness analysis formalizes.

**Utility maximization under constraint.** The emotion-as-intermediate-layer paper [5] states that the primary task of a cognitive system is to survive and maximize a life-long utility function, but that direct computational maximization of life-long utility is not possible in complex environments under real-world time constraints, with emotions serving as an intermediate layer in the space of policies. This supplies the theoretical template for our fitness-landscape model: historical communities selecting notations could not compute global optima either; they satisficed under local task pressures (ledger-keeping, taxation, calculation), which predicts exactly the contingent, non-optimal outcomes we formalize.

**Cognitive diversity as a design resource.** The radar-classification framework of [3] reports that target classification by radar has been notoriously difficult, with the best systems still not attaining sufficiently high performance and reliability, and explores a design in which angular diversity is used in a *cognitive manner* to attain better performance, benchmarked against conventional classifiers. The structural lesson transfers: exploiting multiple diverse representations of the same underlying quantity can outperform any single representation. Our hybrid-notation proposal in Section 6 is the numeral-system analogue of this diversity principle.

**Immersive and interactive systems.** The cognitive microworld work [4] describes cognitive and immersive systems (CAISs) arising at the intersection of AI with HCI/HRI, systems that interact with and assist the human agents that enter them. The supplied summary gives no further detail specific to notation, but the HCI framing is relevant methodologically: notation choice is an interface-design problem, and human-agent interaction performance is the metric along which notations should be compared—consistent with our transcription-accuracy channels.

**Autonomously active processing.** The review of autonomously active neural networks [7] states that the human brain is autonomously active and that understanding the functional role of this self-sustained activity and its interplay with the sensory input stream is an important question in cognitive-system research. The supplied summary gives no further detail bearing on numerals; we cite it only to note that endogenous noise in the human reader is a plausible physical source for the transcription channels we model, and that our error models are agnostic as to their neural implementation.

**Tangential engineering literatures.** Two supplied works are technically distant from our topic and we use them only as methodological parallels. The exoskeleton review [2] states that exoskeleton technology is not fully mature for adoption in strenuous and non-programmed tasks and that numerous studies have addressed only some aspects of the technology—a reminder that mature-technology narratives can conceal unresolved design tradeoffs, which is our thesis about positional notation. The robust beamforming paper [8] investigates robust design under both bounded channel-state-information error models and statistical error models in IRS-aided cognitive radio systems. Its explicit separation of *bounded* versus *statistical* CSI error models is exactly the distinction our two error channels replicate: additive notation offers a bounded error guarantee (Section 4.1), while positional notation requires a statistical characterization (Section 4.2).

**Numeral-system frameworks.** Within the QNFO corpus, NUMERATA [10] presents a multi-axis framework for evaluating numeral systems, extended to nine axes with Distinction-Based Primality and meta-analysis validation reporting $\mathrm{MCS} = 0.875$ with $5/5$ predictions confirmed, and a "sunburst" notation making primality visually immediate. This establishes that multi-criteria evaluation of notations is an active program; our error-propagation axes are complementary, targeting transcription robustness rather than visual primality. The tree-based numeration synthesis [11] states that positional notation is natively an ultrametric tree and consolidates five research threads with extensions into quantum computing and interface design. The ultrametric-tree view explains *why* positional error propagates so badly: a digit drop collapses an entire subtree of the place-value tree, an effect quantified in Section 4.2. Finally, two QNFO entries—COMMUTATIVE PHYSICS [9] and Ten-Fingered Trap [12]—have no substantive summary supplied in the bibliography; we note their presence but can draw no claim from them, and the title of [12] suggests (but we cannot verify beyond the title) a critical stance toward body-based counting conventions.

## 3. Methods

### 3.1 Notation models

A $d$-digit positional numeral represents

$$N_{\mathrm{pos}} = \sum_{k=0}^{d-1} a_k \, 10^{k}, \qquad a_k \in \{0,1,\dots,9\},$$

with $a_{d-1} \neq 0$ and an obligatory zero placeholder when an internal place is empty. An additive numeral is a multiset of symbols with fixed values; for the Roman-style system over the range $1$ to $3999$ we use symbol values $V = \{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1\}$ with standard formation rules, so that

$$N_{\mathrm{add}} = \sum_{i} v_i, \qquad v_i \in V.$$

### 3.2 Noise channels

We model three channels, each acting once on the written string:

- **$\mathcal{C}_1$ (symbol drop):** one symbol of the string is deleted uniformly at random.
- **$\mathcal{C}_2$ (adjacent transposition):** two adjacent symbols are exchanged uniformly at random among adjacent pairs.
- **$\mathcal{C}_3$ (misreading):** a symbol is replaced by a confusable symbol; we treat this qualitatively (Section 6) because confusability matrices are task- and font-dependent.

For each channel we compute the expected absolute value error $\bar{e} = \mathbb{E}\big[\,|N' - N|\,\big]$ under uniformly distributed digits (positional) and the uniform distribution over $1,\dots,3999$ (additive), with the drop position uniform.

### 3.3 Cost model and fitness landscape

A task environment $t$ assigns weights $\mu_t$ (per symbol written, capturing time, ink, and cognitive load) and $\lambda_t$ (per unit of expected error, scaled by $10^{3}$). The cost of system $s$ in environment $t$ is

$$\kappa_s(t) = \mu_t \, L_s + \lambda_t \, \frac{\bar{e}_s}{10^{3}},$$

where $L_s$ is the expected string length. The "fitness landscape" is the map from $(\mu_t, \lambda_t)$ to the argmin system; we derive the crossover boundary in Section 4.4.

## 4. Analysis

All inputs in this section are either definitions of the two notation models (Section 3.1) or arithmetic on them; no empirical numbers are used.

### 4.1 Additive error under $\mathcal{C}_1$: bounded propagation

**Claim.** Under a single symbol drop, the additive error satisfies $|N' - N| = v_j \leq \max V = 1000$, independent of string length.

*Derivation.* Dropping symbol $j$ with value $v_j$ from the multiset changes the sum from $\sum_i v_i$ to $\sum_{i \neq j} v_i$, so

$$|N' - N| = \Big|\sum_i v_i - \sum_{i \neq j} v_i\Big| = v_j \leq 1000.$$

The bound holds for every symbol and every string length: error magnitude is *length-independent*. Moreover every single-symbol drop produces a nonzero error ($v_j \geq 1$), so no single drop is silent.

**Expected dropped-symbol value.** For the uniform distribution over $1,\dots,3999$: the expected value of a number is $(1 + 3999)/2 = 2000$. The expected string length $L_{\mathrm{add}}$: the thousands digit $h \in \{0,1,2,3\}$ occurs with counts $999, 1000, 1000, 1000$ respectively, contributing $\frac{999 \cdot 0 + 1000(1+2+3)}{4000} = \frac{6000}{4000} = 1.5$ symbols on average. Each lower place (hundreds, tens, ones), treated under the uniform-digit approximation, requires symbol counts per digit value $0,\dots,9$ of $0,1,1,1,2,1,2,2,2,2$, summing to $14$, hence an average of $14/10 = 1.4$ symbols per place. Thus

$$L_{\mathrm{add}} \approx 1.5 + 3 \times 1.4 = 5.7 \text{ symbols}.$$

The mean value per written symbol is $\bar{v} \approx 2000 / 5.7 = 350.877\ldots$, so the expected drop error is

$$\bar{e}_{\mathrm{add}} \approx 350.9.$$

(The uniform-digit approximation for the three lower places is exact for the range $1000$–$3999$ and approximate for $1$–$999$; we carry it as an approximation throughout, with the exact bound $v_j \leq 1000$ unaffected.)

### 4.2 Positional error under $\mathcal{C}_1$: length-dependent propagation

Dropping the digit $a_k$ from a $d$-digit positional numeral shifts all higher digits down one place. The corrupted value is

$$N' = \Big\lfloor \frac{N}{10^{k+1}} \Big\rfloor 10^{k} + \big(N \bmod 10^{k}\big),$$

so the error is

$$|N' - N| = a_k \, 10^{k} + \sum_{j=k+1}^{d-1} 9 \, a_j \, 10^{j-1}.$$

**Worst case.** Dropping the leading digit ($k = d-1$) gives error $a_{d-1} 10^{d-1} \leq 9 \cdot 10^{d-1}$. For $d = 4$: $\leq 9000$. The ratio of worst-case positional to additive error is

$$\frac{9 \cdot 10^{d-1}}{1000} = 9 \cdot 10^{d-4},$$

equal to $9$ at $d = 4$ and growing by a factor of $10$ per additional digit: positional worst-case error is *unbounded* in length, additive worst-case error is constant.

**Expected error, $d = 4$, uniform digits ($\mathbb{E}[a_k] = 4.5$).** For each drop position $k$:

$$\bar{e}(k) = 4.5 \cdot 10^{k} + 9 \cdot 4.5 \sum_{j=k+1}^{3} 10^{j-1} = 4.5 \cdot 10^{k} + 40.5 \sum_{j=k+1}^{3} 10^{j-1}.$$

- $k=0$: $4.5 + 40.5(1 + 10 + 100) = 4.5 + 40.5 \times 111 = 4.5 + 4495.5 = 4500.0$
- $k=1$: $45 + 40.5(10 + 100) = 45 + 4455 = 4500.0$
- $k=2$: $450 + 40.5 \times 100 = 450 + 4050 = 4500.0$
- $k=3$: $4500 + 0 = 4500.0$

(The equality across positions is a coincidence of the geometric series with ratio $10$ and mean digit $4.5$.) Averaging over the $d = 4$ drop positions:

$$\bar{e}_{\mathrm{pos}} = \frac{4 \times 4500}{4} = 4500.0.$$

**Headline ratio.**

$$\frac{\bar{e}_{\mathrm{pos}}}{\bar{e}_{\mathrm{add}}} = \frac{4500.0}{350.877\ldots} = 12.82\ldots \approx 12.8.$$

We note an earlier draft-style estimate using per-position sums ($33751.125/4$) double-counted the geometric tail; the correct per-position error is constant at $4500.0$, and the honest expected-error ratio is $\approx 12.8$, not larger. The worst-case ratio remains $9$ at $d=4$ and grows as $9 \cdot 10^{d-4}$.

### 4.3 Adjacent transposition ($\mathcal{C}_2$)

**Positional.** Swapping adjacent digits $a_{k+1}, a_k$ changes the value by

$$\Delta = (a_{k+1} - a_k)(10^{k+1} - 10^{k}) = 9 \cdot 10^{k} (a_{k+1} - a_k).$$

For uniform independent digits, $\mathbb{E}\,|a_{k+1} - a_k| = \frac{1}{100}\sum_{i=0}^{9}\sum_{j=0}^{9} |i - j| = \frac{330}{100} = 3.3$ (the double sum is $2\sum_{m=1}^{9} m(10-m) = 2(450 - 285) = 330$). Averaging over the $d - 1 = 3$ adjacent pairs of a 4-digit numeral:

$$\bar{e}^{\,\mathrm{tr}}_{\mathrm{pos}} = 9 \times 3.3 \times \frac{1 + 10 + 100}{3} = 29.7 \times 37 = 1098.9.$$

**Additive.** Swapping two adjacent symbols with values $v_1, v_2$ changes the sum by $v_1 - v_2$ (zero if the symbols are equal). The worst case over distinct adjacent pairs in the Roman inventory is the pair $(1000, 100)$, giving the bound

$$\bar{e}^{\,\mathrm{tr}}_{\mathrm{add}} \leq 900.$$

The expected additive transposition error is strictly below this bound (many adjacent pairs are equal or close in value), so positional transposition error exceeds even the additive *worst case* on average: $1098.9 > 900$.

### 4.4 Compactness and the cost-model crossover

**Compactness.** From Section 4.1, $L_{\mathrm{add}} \approx 5.7$ versus $L_{\mathrm{pos}} = 4$ for the range $1$–$3999$: positional notation is more compact by a factor of $5.7/4 = 1.425$, i.e., additive strings are $\approx 42.5\%$ longer.

**Crossover.** With costs $\kappa_{\mathrm{pos}} = 4\mu + \lambda \cdot 4.5$ and $\kappa_{\mathrm{add}} = 5.7\mu + \lambda \cdot 0.3509$ (errors scaled by $10^{3}$), additive notation is optimal when

$$5.7\mu + 0.3509\,\lambda < 4\mu + 4.5\,\lambda \;\Longleftrightarrow\; 1.7\,\mu < 4.1491\,\lambda \;\Longleftrightarrow\; \frac{\lambda}{\mu} > \frac{1.7}{4.1491} = 0.4097.$$

So if the task environment's error aversion per $10^{3}$ of expected error exceeds $\approx 0.41$ of its per-symbol writing cost, additive notation has lower total cost; below that ratio, positional wins. The crossover is a *line in weight space*, not a point: both systems are optimal in some region, and neither dominates.

### 4.5 Arithmetic complexity (qualitative with explicit basis)

Positional addition requires $O(d)$ digit operations with carries; multiplication requires $O(d^2)$ schoolbook digit-products. Additive addition is concatenation plus regrouping, $O(L_{\mathrm{add}})$ with $L_{\mathrm{add}} \approx 1.425\,d$; but additive multiplication has no digit-table algorithm and in practice requires repeated addition or conversion to a positional intermediate. The compactness factor $1.425$ and the asymptotic gap in multiplication algorithms are the compensating advantages that made positional notation dominant in calculation-heavy environments.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

1. **Bounded additive error (proved):** under $\mathcal{C}_1$, additive error $= v_j \leq 1000$ for any string length; every single drop is detectable ($v_j \geq 1$).
2. **Positional drop error ($d=4$, uniform digits):** expected $\bar{e}_{\mathrm{pos}} = 4500.0$; worst case $9000$.
3. **Expected-error ratio:** $\bar{e}_{\mathrm{pos}} / \bar{e}_{\mathrm{add}} \approx 4500.0 / 350.9 \approx 12.8$; worst-case ratio $9 \cdot 10^{d-4}$, i.e., $9$ at $d=4$, growing tenfold per digit.
4. **Transposition:** positional expected error $1098.9$; additive worst case $\leq 900$; positional exceeds the additive worst case on average.
5. **Compactness:** $L_{\mathrm{add}} \approx 5.7$ vs $L_{\mathrm{pos}} = 4$ symbols; additive strings $\approx 42.5\%$ longer.
6. **Crossover:** additive notation minimizes the two-term cost whenever $\lambda/\mu > 0.4097$; positional when $\lambda/\mu < 0.4097$. No single system dominates.
7. **Projection (labeled):** if the positional-vs-additive expected-error ratio scales as $9 \cdot 10^{d-4}$ in the worst case, then at $d = 8$ (range up to $10^{8}-1$) the worst-case ratio is $9 \times 10^{4} = 90000$, assuming the additive symbol inventory is extended by one order symbol (e.g., a ten-thousands symbol) keeping $\max V$ at the new order of magnitude; the uncertainty in this projection is the inventory-extension assumption, without which the additive bound degrades to $\max V$ growth by at most the new symbol's value.

## 6. Discussion

**Limitations.** The analysis is deliberately minimal, and its conclusions are correspondingly bounded. (i) The uniform-digit assumption is exact for the positional model by construction but approximate for the additive string-length calculation ($1.4$ symbols per lower place is exact only where lower digits are uniform); the exact expected length over $1$–$999$ differs slightly, though the bounded-error theorem (Section 4.1) is exact and assumption-free. (ii) We model single-event channels