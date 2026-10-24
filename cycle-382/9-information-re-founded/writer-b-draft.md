# Information Censorship: A Layered Account of Which Distinctions Count, Propagate, and Get Suppressed

## Abstract

Every scientific community, indexing system, and communication channel decides which differences count as information and which are silently dropped; this filtering, which we call information censorship, blocks research questions, skews citation visibility, and caps what any physical region can record. The specific gap is that existing accounts treat such filtering either as a purely syntactic channel property, as a purely social phenomenon, or as a metaphysical claim about information being fundamental, without a single framework that connects all three. We develop a four-layer model — distinction, pattern, relational significance, semantic content — in which a difference is *censored* when it exists at one layer but fails to propagate to the next, and we instantiate the model quantitatively. For a binary symmetric channel with crossover probability $p = 0.1$ we derive a censorship ratio $C = 1 - I(X;Y)/H(X) = 0.468996$, meaning 46.9% of source distinctions fail to reach a receiver intact. Applying the holographic entropy bound, a region of boundary area $A = 1\ \mathrm{cm}^2$ can carry at most $1.38049 \times 10^{65}$ bits, so any distinction beyond that budget is censored by physics itself. The framework reclassifies neglected research questions, uncited publications, and formal-methods narrowing as instances of one mechanism, and it supplies a falsifiable criterion for when a filtering process destroys information rather than merely delaying it.

## 1. Introduction

Researchers, funders, journal editors, indexing systems, and ultimately the laws of physics all face the same operational problem: an unbounded supply of candidate distinctions — differences in data, in hypotheses, in citation patterns, in physical states — must be reduced to what can be transmitted, stored, reviewed, and acted upon. The filtering is unavoidable, but it has costs that are currently paid invisibly. Research questions that fall outside a field's accepted standards are neglected or left unfunded even when they deserve exploration; the phenomenon has been named "undone science" in social research and extended to computer science precisely because entire problem classes are relegated to informal hallway conversations rather than to the published record [6]. In computer science the publication record itself is severely skewed: acceptance rates at selective conferences range between 10% and 20%, and the citation distribution is so right-skewed that only a small number of articles are cited near or above the mean while a significant share of papers sleep uncited [7]. At the physical extreme, the entropy of any finite region is bounded by its boundary area, so distinctions beyond that budget cannot exist as recordable information at all [13].

What would change if these three filters — social, infrastructural, and physical — were recognized as instances of one mechanism? A funder could ask not "is this topic interesting?" but "at which layer does the relevant distinction currently fail to propagate, and can that layer be opened?" An index designer could measure how much of a field's distinction supply its mapping tools actually carry. A physicist could state, with a number, how much information a region can hold before nature itself censors the rest. Today no shared vocabulary supports these questions: Shannon theory measures transmission but deliberately excludes meaning; semantic theories incorporate meaning but struggle with observer-dependency; ontological proposals such as "it from bit" leave the status of information before observation unclear [12].

This paper develops that vocabulary. We define information censorship as the failure of a distinction that exists at one layer of an information hierarchy to propagate to the next layer, and we give the hierarchy a precise, checkable form. The contributions are:

- A four-layer model of information — distinction, pattern, relational significance, semantic content — with an explicit censorship criterion at each boundary, derived in Section 3.
- A quantitative censorship ratio for a binary symmetric channel, $C = 1 - I(X;Y)/H(X)$, computed in full for $p = 0.1$ in Section 4.
- A physical censorship budget: the maximum number of bits a $1\ \mathrm{cm}^2$ region can carry, derived from the holographic bound in Section 4.
- A mapping of sociotechnical filtering — undone research questions, skewed citation visibility, term-selection in field maps, and formalization-driven narrowing — onto the same censorship criterion, argued from the primary literature in Sections 2 and 5.

## 2. Background and Related Work

The paper under revision, the autaxic chapter on information, advances the thesis that information is neither a fundamental independent substance nor a subjective construct, but emerges from objective generated distinctions that acquire relational significance through participation in complex interacting systems, with spontaneous symmetry breaking generating the initial distinctions and conservation of distinguishability giving them persistence [12]. We keep that layered architecture, because it is what allows social, infrastructural, and physical filtering to be compared at all; but we strip its dependence on a speculative generative substrate and rebuild each layer on results that the cited literature actually establishes.

The physical anchor for the lowest layer is spontaneous symmetry breaking. In statistical physics, a system whose dynamics is invariant under a continuous symmetry may, below a critical temperature, enter an ordered phase in which the symmetry is reduced; the breaking is always discontinuous at the transition point even when order parameters set in continuously, and the ferromagnetic transition illustrates ground state degeneracy together with the appearance of a massless mode and a massive mode [8]. In relativistic quantum field theory the same mechanism was introduced by Nambu in analogy with the BCS theory of superconductivity: chiral symmetry is broken by a fermion condensate $\langle\bar{\psi}\psi\rangle \neq 0$, which yields a fermion mass through a self-consistency equation $g = f(m/\Lambda)$ [8]. This matters for our model because it shows that "distinction generation" is not a metaphor: symmetry breaking is the established physical process by which a degenerate, undifferentiated state becomes a set of differentiated alternatives, and the degeneracy itself — many equally valid ground states — is the raw supply of distinctions from which any recordable pattern must be selected.

The statistical-physics literature also shows what happens when the distinction supply is computationally inaccessible. In the spin glass, interactions $J_{ij}$ drawn from a symmetric distribution with zero mean and unit variance produce a ground state whose degeneracy is exponentially large in the number of spins $N$, giving a finite ground state entropy; algorithms from computer science "broke the size barrier" for the two-dimensional spin glass and the random field model, yet with the genetic algorithm available at the time one could study only of order $10^3$ spins [2]. Here censorship is computational: exponentially many ground-state distinctions exist, but only those reachable by feasible algorithms ever enter the scientific record. The same paper notes that such cross-disciplinary application works best as a collaboration between computer scientists and physicists [2], which is itself a statement about which channels for carrying distinctions between communities are reliable.

At the layer of relational significance, theories of semantic information require that a difference make a difference to something. The sociotechnical literature supplies concrete instances of that "something" failing. The concept of undone science, which emerged in the 2010s at the intersection of social movement studies and science and technology studies, names research questions that are neglected, ignored, or left unfunded even though they deserve exploration; applying it to computer science surfaces problems "relegated to informal 'hallway track' discussions at conferences, because they were not considered legitimate according to that research field's own standards" [6]. That passage is a censorship statement in our sense: the distinctions exist, are expressible, and would change the field's state if received, but the field's acceptance standards block propagation. The same source records Gilles Dowek's classification of computer science as "a posteriori analytical knowledge" — its properties are intrinsic and independent of the laws of nature, yet their validation requires interaction with a physical machine, which is a form of experimentation [6] — a duality we use in Section 5 to explain why purely formal filtering and purely empirical filtering both operate on the same discipline.

Visibility infrastructure determines which distinctions can propagate at scale. The Maps of Computer Science system builds field maps from DBLP paper titles: multi-word terms are extracted using NLTK part-of-speech tags, ranked by term frequency and related measures, and positioned by co-occurrence similarity, with heatmaps showing temporal evolution [3]. The design choices are censorship choices in our framework: terms that fail extraction or ranking never become "cities," so the distinctions they name cannot appear on the map that researchers use to explore the field. The authors themselves note that the system's modularity makes it possible to experiment with different approaches to the subproblems [3], which is exactly the openness a censorship audit would require.

Publication channels add a second, quantitative filter. Acceptance rates at selective computer science conferences run between 10% and 20% — in 2007–2008, ICSE 13%, OPOSLA-era OOPSLA 19%, POPL 18% — and the resulting citation distribution is severely skewed, so that the mean is not an appropriate measure of central tendency: only a small number of articles are cited near or above the mean, the great majority are endorsed less than average, and a significant share of papers sleep uncited [7]. The same work derives a theoretical model of these distributions and observes a two-leveled citational hierarchy, of venues and of articles within venues [7]. In our terms, the acceptance filter censors at submission and the citation dynamics censor again after publication; the skewness statistic (the third standardized central moment, positive for right skew [7]) is a measurable censorship index.

Formal methods illustrate deliberate, productive narrowing. The Lean computer science library CSLib bundles abstract reduction systems and labelled transition systems into shared structures, from which multistep reduction, reachable states, and properties such as confluence and the diamond property are automatically derived, and it maintains these through a continuous-integration pipeline aligned with Mathlib [4]. Formalization censors ambiguity: a labelled transition system admits only the distinctions its transition relation encodes. The payoff is verification at scale — formalization and verification of real-life theorems is no longer just an in-principle possibility but is done on an increasing scale, and large areas of computer science such as automated reasoning, automated verification, and type inference make essential use of logical formalisms [11]. CSLib's own conclusion is that there had not previously been a monolithic library of computer science in Lean offering cross-cutting abstractions [4], which marks the moment a previously informal distinction supply (programming-language folklore) was partially admitted into a formal channel.

Which formalisms get admitted is itself historically contingent. The mutual influence of mathematical logic and computer science since the 1950s is traced through four areas — computability, model theory, proof theory, and set theory — with computability having had the strongest impact on the younger discipline, while model theory received relatively little and set theory almost nothing explicitly [5]. A survey of the relationship around the year 2000 covers five areas: descriptive complexity, logic as a database query language, type theory, reasoning about knowledge, and one further area [5]. The uneven allocation is a censorship pattern: distinctions expressible in set-theoretic terms propagated poorly into computing practice, while computability-theoretic distinctions propagated well. Proof theory shows the boundary is still moving: one recent analysis asks whether open problems in computational complexity can be solved by advanced proof-theoretic techniques and reports proofs of the equalities $\mathbf{NP} = \mathbf{coNP} = \mathbf{PSPACE}$ obtained by tree-to-dag compressing techniques applied to a minimal-logic natural-deduction calculus with an added separation rule [10]. Whether or not those proofs survive scrutiny, the episode demonstrates that the channel between proof theory and complexity theory was narrow enough that a claimed crossing of it is noteworthy — and that a community's standards determine which claimed distinctions are even examined.

Finally, community composition gates who can feed distinctions into the channels. Science and technology are viewed differently by individuals, communities, and societies, and which viewpoints prevail depends on socioeconomic capabilities [1]. Workforce programs address the resulting gatekeeping directly: education and support programs aimed at underrepresented students teach skills, inform students of career options, and grow students' networks in computer science, and studies demonstrate these programs' effectiveness with respect to changes in affective outcomes [9]. In our framework, such programs widen the set of distinctions that ever enter the field's channels; their measured effect on affective outcomes is an effect on the willingness to transmit, which is a propagation parameter, not a source property.

Two adjacent axiomatic programs sharpen what our framework is not. The informational-universe synthesis distinguishes three readings of "the universe is informational" — epistemic, nomological, and ontological — adopts the nomological reading (physical law constrained by information-theoretic bounds) as its core framework, explicitly tags the ontological reading as the least supported, and states a precise falsification condition: the claim fails if entanglement entropy in a region of boundary area $A$ is shown to exceed $A/4\ell_P^2$ in Planck units [13]. We adopt the same discipline: our physical-layer claims are bound-based and carry that falsification condition. The Infomatics framework instead treats information as the fundamental substrate axiomatically, deriving a fine-structure constant $\alpha = 1/137$ and a $p$-adic correction with parameter $c_1 = 5$ that it reports as matching to 0.0014% [14]. We treat such substrate claims as outside our scope: our model needs only that distinctions, once generated, are countable and bounded, which the holographic bound supplies without any ontological commitment [13].

## 3. Methods

The method of this paper is conceptual reconstruction plus quantitative instantiation. We take the four-layer hierarchy articulated in the paper under revision — primordial distinctions, stabilized patterns, relational information, functional or semantic information [12] — and restate each layer so that membership is decidable and the transition between layers is a measurable propagation event. No experiment, simulation, or survey is performed; all numbers are either derived here from stated inputs or quoted from the cited works.

**Layer 1: Distinctions.** A distinction is a binary differentiation: pattern $A$ is not pattern $B$. Physically, such differentiations arise by spontaneous symmetry breaking, which converts a degenerate symmetric state into ordered alternatives with ground-state degeneracy [8]. We require only that distinctions be countable; the count is bounded at Layer 4 below.

**Layer 2: Patterns.** Distinctions become patterns when stabilized into reproducible configurations. In physics this is the formation of ordered phases with persistent order parameters [8]; in a literature system it is a term that recurs across a corpus and can be extracted and ranked, as in the DBLP title analysis where terms are extracted with part-of-speech tagging and ranked by frequency-based functions [3].

**Layer 3: Relational significance.** A pattern acquires significance when its state makes a discernible difference to the state of other patterns — the operational content of "a difference which makes a difference" as reinterpreted in the source chapter [12]. Formally, for a source distinction $d$ and a receiver state variable $Y$, $d$ has relational significance in a channel if

$$P\big(Y \text{ changes} \mid d \text{ present}\big) \neq P\big(Y \text{ changes} \mid d \text{ absent}\big).$$

**Layer 4: Semantic/functional content.** Significance becomes semantic content when the receiving system's response depends on the pattern's role in the system's own maintenance or goals. We do not formalize goals; we only require that Layer 4 presupposes Layer 3, which presupposes Layer 2, which presupposes Layer 1.

**Censorship criterion.** Given the hierarchy, we define information censorship operationally:

> A distinction is *censored at the boundary between Layer $k$ and Layer $k+1$* if it exists at Layer $k$ but the propagation condition for Layer $k+1$ is not met — that is, its presence does not change any Layer-$(k+1)$ state variable, or the channel to Layer $k+1$ is closed to it by cost, standard, algorithmic infeasibility, or physical bound.

This definition is deliberately neutral about *why* propagation fails. A dropped conference submission [7], a term excluded by a part-of-speech tagger [3], a ground state unreachable by any feasible algorithm [2], and a distinction beyond the holographic budget [13] are all censored in the same sense, at different layers and by different mechanisms. The definition is also falsifiable per instance: to refute a censorship claim about a specific distinction, one exhibits a receiver whose state the distinction changes.

**Quantitative instantiation.** For a discrete memoryless channel with input $X$ and output $Y$, we define the censorship ratio

$$C \;=\; 1 - \frac{I(X;Y)}{H(X)},$$

where $H(X)$ is the source entropy and $I(X;Y) = H(X) - H(Y \mid X)$ the mutual information. $C = 0$ means every source distinction propagates; $C = 1$ means none does. For the physical layer we use the holographic bound as stated in the informational-universe synthesis: entanglement entropy in a finite region is bounded by the region's boundary area, $S \leq A/(4\ell_P^2)$, with the Hilbert-space dimension bounded by $\exp(A/4\ell_P^2)$ [13]. Assumptions specific to each computation are stated where the computation is performed.

## 4. Analysis

**4.1 Censorship ratio for a binary symmetric channel.**

Take a binary symmetric channel (BSC) with crossover probability $p$: each transmitted bit is flipped independently with probability $p$. Input distribution uniform, so

$$H(X) = 1 \text{ bit}.$$

The conditional entropy is the binary entropy function of $p$:

$$H(Y \mid X) = H_2(p) = -p\log_2 p - (1-p)\log_2(1-p).$$

We assume $p = 0.1$ (a stated assumption; no source supplies it). Compute each term:

$$\log_2 0.1 = \frac{\ln 0.1}{\ln 2} = \frac{-2.302585}{0.693147} = -3.321928,$$

$$\log_2 0.9 = \frac{\ln 0.9}{\ln 2} = \frac{-0.105361}{0.693147} = -0.152003.$$

Then

$$H_2(0.1) = 0.1 \times 3.321928 + 0.9 \times 0.152003 = 0.3321928 + 0.1368027 = 0.4689955 \text{ bits}.$$

Mutual information:

$$I(X;Y) = H(X) - H(Y \mid X) = 1 - 0.4689955 = 0.5310045 \text{ bits}.$$

Censorship ratio:

$$C = 1 - \frac{0.5310045}{1} = 0.4689955.$$

So with a 10% crossover probability, 46.9% of the source's distinction content fails to reach the receiver intact. The interpretation in our framework: each flipped bit is a Layer-1 distinction that exists at the source but whose Layer-3 significance is destroyed — the receiver's state is the same as if the complementary bit had been sent, so the distinction "this bit was 0 rather than 1" has lost its discriminating power for 10% of symbols, and the aggregate loss, weighted by the entropy geometry above, is 0.469 bits per symbol.

Sensitivity check, same arithmetic at $p = 0.01$: $\log_2 0.01 = -6.643856$, $\log_2 0.99 = -0.014500$ (since $\ln 0.99 = -0.010050$, divided by $0.693147$ gives $-0.014500$). Then $H_2(0.01) = 0.01 \times 6.643856 + 0.99 \times 0.014500 = 0.0664386 + 0.0143545 = 0.0807931$ bits, and $C = 0.0807931$. The censorship ratio falls by a factor of $0.4689955 / 0.0807931 = 5.805$ when $p$ falls by a factor of 10: near $p = 0$ the ratio is superlinear in $p$, so small improvements in channel fidelity buy disproportionately large reductions in censorship.

**4.2 The physical censorship budget of a $1\ \mathrm{cm}^2$ region.**

The holographic bound states $S \leq A/(4\ell_P^2)$ for a region of boundary area $A$, with Hilbert-space dimension bounded by $\exp(A/4\ell_P^2)$ [13]. We assume $A = 1\ \mathrm{cm}^2 = 10^{-4}\ \mathrm{m}^2$ and use the Planck length $\ell_P = 1.616255 \times 10^{-35}\ \mathrm{m}$ (a stated assumption for the numerical constant; the bound itself is from [13]).

Step 1 — Planck area:

$$\ell_P^2 = (1.616255 \times 10^{-35})^2 = 2.612280 \times 10^{-70}\ \mathrm{m}^2.$$

Step 2 — the bound in natural units:

$$\frac{A}{4\ell_P^2} = \frac{10^{-4}}{4 \times 2.612280 \times 10^{-70}} = \frac{10^{-4}}{1.044912 \times 10^{-69}} = 9.57016 \times 10^{64}.$$

Step 3 — convert to bits ($1$ nat $= \log_2 e = 1.442695$ bits):

$$S_{\max} = 9.57016 \times 10^{64} \times 1.442695 = 1.38049 \times 10^{65} \text{ bits}.$$

Step 4 — the dimension bound:

$$\dim \mathcal{H} \leq \exp\!\left(9.57016 \times 10^{64}\right) = 10^{\,9.57016 \times 10^{64} / \ln 10} = 10^{\,9.57016 \times 10^{64} / 2.302585} = 10^{\,4.15646 \times 10^{64}}.$$

Interpretation: a region the size of a postage stamp can carry at most $1.38049 \times 10^{65}$ bits of entanglement entropy. Any distinction a physical process in that region might generate beyond this budget is censored by physics — it cannot be recorded, in principle, by anything confined to the region. This is the hard floor under every social and infrastructural filter discussed above. The falsification condition travels with the bound: if entanglement entropy in a region of boundary area $A$ were shown to exceed $A/4\ell_P^2$ in Planck units, the physical censorship budget would be refuted [13].

**4.3 Computational censorship in the spin glass.**

The spin glass with $\pm J$ interactions has a number of ground states that is exponentially large in the number of spins $N$, giving a finite ground-state entropy [2]. Suppose, for illustration only and as a labeled assumption, that the degeneracy is of order $2^{N/2}$ (the source states "exponentially large" without a base; we assume base $2^{1/2}$ per spin). Then at the reported practical limit of the genetic algorithm, $N \approx 10^3$ [2], the reachable fraction of ground states, even if the algorithm enumerated one distinct ground state per run at a rate of one per second, is bounded by

$$\frac{10^3 \text{ states/s} \times 3.15 \times 10^7 \text{ s/yr} \times 1 \text{ yr}}{2^{500}} = \frac{3.15 \times 10^{10}}{3.27 \times 10^{150}} = 9.63 \times 10^{-141}.$$

Here $2^{500} = 10^{500 \log_{10} 2} = 10^{500 \times 0.301030} = 10^{150.515} = 3.27 \times 10^{150}$. The reachable fraction is below $10^{-140}$: the overwhelming majority of ground-state distinctions are computationally censored — they exist, are physically real alternatives, and can never enter the scientific record through any feasible algorithmic channel. The exponent is the point, not the precise coefficient; the assumption on the degeneracy base changes the exponent by a constant factor, not its order.

**4.4 Publication-channel censorship.**

The acceptance rates reported for selective computer science conferences are 13% (ICSE), 19% (OOPSLA), and 18% (POPL) in 2007–2008 [7]. Taking the range midpoint as a labeled assumption, $a = 0.167$, the per-submission survival probability through one conference is $a$, and through a sequence of $n$ independent submissions to such venues it is $a^n$. For $n = 3$:

$$a^3 = 0.167^3 = 0.00466.$$

A distinction carried by a manuscript rejected three times has a survival probability of about $0.5\%$ through that channel sequence — before any citation dynamics are applied. The citation layer then compounds the filtering: because the distribution is severely skewed, the great majority of published articles are cited less than the average and a