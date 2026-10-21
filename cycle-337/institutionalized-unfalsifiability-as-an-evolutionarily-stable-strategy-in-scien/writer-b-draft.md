# Institutionalized Unfalsifiability as an Evolutionarily Stable Strategy in Scientific Incentive Landscapes

## Abstract

Funding agencies, journals, tenure committees, and citation markets reward novelty, narrative coherence, and impact, yet no formal criterion prices the risk a claim carries of failing a prospective test. This gap makes it impossible to quantify whether research incentives systematically favor unfalsifiable work over risky, testable predictions. We model knowledge production as a two-strategy evolutionary game: agents choose between a Falsifiable strategy, which publishes a testable prediction that succeeds with probability $p$, and a Post-hoc strategy, which publishes a flexible narrative fitted to existing evidence for a certain reward $s$. Payoffs depend on a confirmed-prediction reward $b$ and a failure cost $c$. Under the explicitly assumed values $b=2$, $c=1$, $s=1$, $p=0.6$, we derive the rationality threshold $p^{*}=(s+c)/(b+c)=2/3\approx0.6667$; because $p=0.6<p^{*}$, the Post-hoc payoff $\pi_P=1.0$ exceeds the Falsifiable payoff $\pi_F=0.8$, the replicator dynamics $\dot{x}=-0.2\,x(1-x)$ drive the falsifiable share from $0.5$ to $0.1$ in approximately $10.99$ generations, and the all-Post-hoc state is a strict Nash equilibrium and therefore an evolutionarily stable strategy. Solving $\pi_F=\pi_P$ yields a flip point $b_{\text{flip}}=7/3\approx2.3333$: a modest increase in the confirmed-prediction reward reverses the equilibrium without changing reviewer judgment or researcher ability. The result converts demarcation into a computable property of incentive configurations and supplies funding agencies and journal editors with a quantitative lever, testable by a registered-prediction pilot.

## 1. Introduction

Researchers, journal editors, funding agencies, tenure committees, and citation markets together form a knowledge-production ecosystem that decides which scientific claims receive resources, prestige, and careers. Today this ecosystem often rewards unfalsifiable narratives: a paper that weaves a compelling story around existing data can accumulate citations, media attention, and promotions, while a risky theory that makes bold predictions is penalized when those predictions fail. The cost is concrete. Institutions fund research programs that cannot be proven wrong and therefore cannot be corrected; talented forecasters with moderate accuracy rationally stop making predictions; and public trust erodes when celebrated narratives repeatedly fail retrospective checks. The problem is faced directly by program officers who must score proposals, editors who must select among submissions, and designers of automated research pipelines whose outputs inherit the same scoring rules.

Two observations sharpen the stakes. First, unfalsifiable content is not a marginal phenomenon confined to science: computational work on social media shows that posts expressing unfalsifiable claims are ill-suited to fact-checking pipelines precisely because no pipeline can settle them, motivating methods that distill such content into narrative clusters rather than verified facts [1]. Second, the reward for narrative cohesion is measurable in human communities: a large-scale computational study of Palestinian refugee oral histories finds that narrative similarity is systematically higher among interviewees sharing origin or residence, demonstrating that shared narratives cohere through social continuity rather than through independent verification [7]. If the same cohesion-seeking incentives operate inside science, the ecosystem may select for narratives over predictions.

The historical record contains cautionary cases in both directions. Programs that made expensive, falsifiable bets — a decade-long sky survey designed to measure weak-lensing shear at the level of $\lesssim 1\%$ against a intrinsic ellipticity dispersion of roughly $0.36$ [2], or an X-ray spectroscopy mission rebuilt to recover the science lost when its predecessor failed approximately one month after launch in 2016 [6] — show that falsifiable science is achievable but costly, and that its costs are borne by institutions, not by individual authors. Conversely, fields whose knowledge landscapes reward trend-following can converge on search strategies that are optimal locally and unproductive globally; a numerical model of virtual knowledge landscapes finds two diverging optimal search strategies, with trend-following maximized precisely when the popularity of new discoveries determines the number of researchers pursuing them [4]. The question this paper answers is quantitative: under what reward parameters does a rational researcher stop making falsifiable predictions, and what change in those parameters reverses the outcome?

If the incentive analysis below holds, three decisions change. Program officers can compute the confirmed-prediction reward needed to make prediction individually rational for a population of given accuracy. Editors can audit whether their scoring rules implicitly raise the narrative reward $s$. Reformers can state a falsifiable condition on their own interventions, in the spirit of explicit falsification experiments proposed in other QNFO analyses [9].

**Contributions.**
- **C1.** Formulation of a two-strategy evolutionary-game model of scientific strategy choice, with all parameters stated as explicit assumptions (Section 3).
- **C2.** Derivation of the rationality threshold $p^{*}=(s+c)/(b+c)$ and proof that the all-Post-hoc state is a strict Nash equilibrium, hence an evolutionarily stable strategy, whenever $p<p^{*}$ (Section 4).
- **C3.** Full numerical evaluation under the assumptions $b=2$, $c=1$, $s=1$, $p=0.6$: threshold $p^{*}=0.6667$, payoffs $\pi_F=0.8$ and $\pi_P=1.0$, replicator coefficient $-0.2$, time from $x=0.5$ to $x=0.1$ of $10.99$ generations, and flip point $b_{\text{flip}}=2.3333$ (Sections 4 and 5).
- **C4.** Comparative statics of the threshold and flip point with respect to $b$, $c$, and $s$, and three reform scenarios including an adverse one (Section 4).
- **C5.** Translation into policy levers for funding agencies, journal editors, and research-pipeline designers, with a corrected falsification criterion for the proposed pilot (Section 7).

## 2. Background and Related Work

The claim that institutions can make unfalsifiability stable sits at the intersection of the demarcation problem, the economics of science, and evolutionary game theory. The closest prior statement is the QNFO analysis of institutionalized predictive jeopardy, which derives the same one-line criterion — falsifiable practice is individually rational exactly when $p>p^{*}=(s+c)/(b+c)$ — and reports the identical baseline numbers $\pi_F=0.8$, $\pi_P=1.0$, $p^{*}=2/3\approx0.6667$, and $\dot{x}=-0.2\,x(1-x)$ under $b=2$, $c=1$, $s=1$, $p=0.6$ [10]. That work also derives an antifragility result, $R(k)=R(0)+k/N$ with $dR/dk=1/N>0$ when failures are registered and removed, giving $R(0)=0.60$ and $R(100)=0.70$ for $N=1000$ registered claims and $U=400$ failures, and it states explicitly that its empirical content — whether real institutions occupy the Post-hoc-dominant region — was proposed but not performed [10]. The present paper is a revision of that line of work: it removes an unsupported numerological anchoring of the parameters, corrects an inverted falsification criterion, and grounds the model in the surrounding literature.

On the side of unfalsifiable content, the computational-linguistics literature treats unfalsifiability as an operational property. Work on structure in unfalsifiable claims notes that social-media posts carrying unfalsifiable opinions are ill-suited to fact-checking pipelines and therefore require methods that cluster them into narratives, evaluated with embedding-quality metrics such as the triplet generalization ratio and nearest-neighbour generalization ratio [1]. This supports the model's premise that a narrative strategy can be produced, distributed, and rewarded without any verification step. On the side of narrative rewards outside science, the oral-history study of the Nakba archive finds that narrative cohesion is higher within same-origin and same-residence pairs and strongest when both coincide, which the authors interpret through group-memory theory as cohesion depending on the continuity of shared space [7]. The model's parameter $s$ is a formalization of exactly such cohesion payoffs inside a scientific community.

On the cost side, large-scale falsifiable science illustrates what the parameter $b$ must compete against. The Large Synoptic Survey Telescope's Dark Energy Science Collaboration plans a decade of operation to measure weak-lensing shear, a signal of $\lesssim 1\%$ that must be extracted statistically from galaxy images with root-mean-square ellipticity $\sim 0.36$, and to address a vacuum-energy discrepancy in which naive Planck-scale predictions exceed the observed density by roughly one hundred orders of magnitude [2]. The SKA Observatory, two telescopes on two continents covering $50\,\text{MHz}$ to $15\,\text{GHz}$ operated by an inter-governmental organisation of more than thirteen nations, expects its first major array assembly to double the known pulsar population in new surveys [3]. These programs show that confirmed-prediction rewards in real science are delivered through decade-scale collective instruments; the model's $b$ is the individual author's share of such rewards. Instrument-level risk is equally concrete: the XRISM mission exists to recover the science lost when Astro-H/Hitomi failed in 2016 approximately one month after launch, and its checkout, calibration, and performance-verification phases alone last approximately nine months before the general-observer phase begins [6].

The closest external theoretical result is the knowledge-landscape model of Jaffe, whose numerical experiments over virtual knowledge landscapes reveal two diverging optimal search strategies and show that trend-following is maximized when the popularity of new discoveries determines how many researchers pursue them, a regime the author associates with fields where many researchers explore few large areas of knowledge [4]. This is an independent, simulation-based statement of the same mechanism the present model captures analytically: when reward flows to popular narratives rather than to risky predictions, the population converges on narrative strategies. Complementary evidence on verification limits comes from the quantum-advantage literature: the audit of Huang, Choi, McClean and Preskill's five-keystone framework — Predictability, Typicality, Robustness, Verifiability, Usefulness — highlights their Theorem 1 showing that, assuming $\text{BPP}\neq\text{BQP}$, detecting quantum advantage for a specific circuit is in BQP but not in BPP, so some advantage claims cannot be verified classically at all [11]. Verifiability is thus a graded, resource-dependent property, which is why the model treats the verification-bearing strategy as carrying a cost $c$ rather than being free.

Finally, the engineering pathway proposed in Section 7 borrows its readiness vocabulary from mission practice: the Lynx2030 Science Analysis Group reports that the microcalorimeter distinguished in the original Lynx concept has been flight-validated (XRISM) and scaled (LEM) and is under development towards TRL 5, while the optic remains the pacing technical and programmatic risk [8]. The certainty-labeling conventions used in QNFO analyses — including labels up to and including $[\text{not yet falsifiable}]$ for claims for which no disconfirming observation can currently be stated [9] — motivate the explicit falsification criterion this paper states for its own central claim, correcting the inverted criterion of the previous version.

## 3. Methods

### 3.1 Model

We consider a large, well-mixed population of agents (researchers). Each period an agent produces one unit of research output and chooses one of two strategies:

- **Falsifiable (F):** submit a testable prediction. With probability $p$ the prediction is confirmed and the agent receives reward $b$; with probability $1-p$ it fails and the agent incurs cost $c$.
- **Post-hoc (P):** submit a flexible narrative fitted to existing evidence. The agent receives the baseline narrative reward $s$ with certainty.

Let $x$ denote the fraction of the population playing F. Expected payoffs are

$$\pi_F = p\,b - (1-p)\,c, \qquad \pi_P = s.$$

Agents adopt the higher-payoff strategy, yielding the replicator dynamics

$$\dot{x} = x\,(1-x)\,(\pi_F - \pi_P).$$

### 3.2 Parameter assumptions

All parameter values in this paper are explicit assumptions, not measurements and not values derived from any external source:

- **A1.** $b=2$ — assumed baseline reward for a confirmed prediction.
- **A2.** $c=1$ — assumed cost of a failed prediction.
- **A3.** $s=1$ — assumed baseline narrative reward.
- **A4.** $p=0.6$ — assumed average predictive accuracy of the agent population.

A previous version of this analysis described these values as "anchored" to external facts (a reward of $2$ from the SKA's two telescopes, a cost of $1$ from the $1\,\text{keV}$ energy unit in X-ray mission design, and a narrative reward of $1$ from weak-lensing shear being below $1\%$). That anchoring is retracted: the coincidence of numerals carries no information about payoff magnitudes, which are dimensionless quantities of the incentive model, and the sources in question report instrument facts (two telescopes covering $50\,\text{MHz}$ to $15\,\text{GHz}$ [3]; a soft X-ray bandpass of $\sim 0.3\text{--}12\,\text{keV}$ [6]; shear signals of $\lesssim 1\%$ [2]) that say nothing about researcher payoffs. The analysis below is valid for any positive $(b,c,s,p)$; the assumed quadruple is one illustrative point in parameter space.

### 3.3 Analytic procedure

1. Derive the individual-rationality condition $\pi_F>\pi_P$ and solve for the accuracy threshold $p^{*}$.
2. Verify that the all-P state satisfies the strict-Nash and evolutionarily stable strategy conditions by invasion analysis.
3. Compute the replicator coefficient, the time to near-extinction, the flip point $b_{\text{flip}}$, and the sensitivities of $p^{*}$ and $b_{\text{flip}}$ with respect to $b$, $c$, and $s$.
4. Evaluate three reform scenarios, including one in which the narrative reward rises.

All arithmetic steps are shown in Section 4. No step in this paper involves an experiment, simulation on hardware, survey, or measurement; every number is derived from the assumptions A1–A4.

## 4. Analysis

### 4.1 Rationality threshold

Individual rationality of F requires

$$p\,b - (1-p)\,c > s.$$

Expanding the left side and collecting the $p$ terms,

$$p\,b - c + p\,c > s \quad\Longrightarrow\quad p\,(b+c) > s+c \quad\Longrightarrow\quad p^{*} = \frac{s+c}{b+c}.$$

Substituting the assumed values $s=1$, $c=1$, $b=2$:

$$p^{*} = \frac{1+1}{2+1} = \frac{2}{3} \approx 0.6667.$$

### 4.2 Payoff comparison at $p=0.6$

$$\pi_F = 0.6 \times 2 - (1-0.6)\times 1 = 1.2 - 0.4 = 0.8, \qquad \pi_P = s = 1.0.$$

Since $\pi_F = 0.8 < 1.0 = \pi_P$, the Post-hoc strategy yields the higher payoff at the assumed accuracy.

### 4.3 Evolutionary stability of the all-P equilibrium

At the all-P state ($x=0$) a rare mutant playing F earns $\pi_F = 0.8$ against residents earning $\pi_P = 1.0$. Because $\pi_F$ and $\pi_P$ are independent of $x$ in this model, $\pi_F < \pi_P$ holds for every population composition, so the mutant's payoff against any resident mixture is strictly below the residents' payoff for every invasion fraction $\epsilon \in (0,1)$. The strict inequality on the first part of the standard evolutionarily stable strategy condition makes the second part vacuous, establishing the all-P state as a strict Nash equilibrium and therefore an evolutionarily stable strategy whenever $p < p^{*}$. By the symmetric argument, whenever $p > p^{*}$ the all-F state is a strict Nash equilibrium and the unique evolutionarily stable strategy; at $p = p^{*}$ the dynamics vanish and every mixture is neutrally stable.

### 4.4 Replicator dynamics

$$\dot{x} = x(1-x)(\pi_F - \pi_P) = x(1-x)(0.8 - 1.0) = -0.2\,x(1-x).$$

The negative coefficient drives $x$ monotonically to $0$.

**Time to near-extinction.** Separating variables,

$$\frac{dx}{x(1-x)} = -0.2\,dt \quad\Longrightarrow\quad \ln\frac{x}{1-x} = \ln\frac{x_0}{1-x_0} - 0.2\,t.$$

With $x_0 = 0.5$ and target $x = 0.1$ (the odds ratio $x/(1-x)$ falls from $1$ to $1/9$, a factor of $9$):

$$t = \frac{\ln 9}{0.2} = \frac{2.19722}{0.2} \approx 10.99 \text{ generations}.$$

### 4.5 Flip point in the prediction reward

Set $\pi_F = \pi_P$ and solve for $b$, keeping $p=0.6$, $c=1$, $s=1$:

$$0.6\,b - 0.4 = 1.0 \quad\Longrightarrow\quad b_{\text{flip}} = \frac{1.4}{0.6} = \frac{7}{3} \approx 2.3333.$$

Equivalently, inverting the threshold condition in general form,

$$b = \frac{s + (1-p)\,c}{p} = \frac{1 + 0.4}{0.6} = \frac{1.4}{0.6} \approx 2.3333,$$

which agrees with the direct solution. For any $b > b_{\text{flip}}$, the falsifiable strategy is individually optimal and, by the strict-Nash argument of Section 4.3, the all-F state becomes the evolutionarily stable strategy.

### 4.6 Sensitivity analysis

With $p^{*} = (s+c)/(b+c)$:

$$\frac{\partial p^{*}}{\partial b} = -\frac{s+c}{(b+c)^2} = -\frac{2}{9} \approx -0.2222,$$

$$\frac{\partial p^{*}}{\partial c} = \frac{(b+c) - (s+c)}{(b+c)^2} = \frac{b-s}{(b+c)^2} = \frac{2-1}{9} = \frac{1}{9} \approx 0.1111,$$

$$\frac{\partial p^{*}}{\partial s} = \frac{1}{b+c} = \frac{1}{3} \approx 0.3333.$$

A unit increase in $b$ lowers the required accuracy by approximately $0.22$; a unit increase in $c$ raises it by approximately $0.11$; a unit increase in $s$ raises it by approximately $0.33$. The narrative reward is the most destabilizing lever per unit.

For the flip point $b_{\text{flip}} = (s + (1-p)\,c)/p$:

$$\frac{\partial b_{\text{flip}}}{\partial s} = \frac{1}{p} = \frac{1}{0.6} \approx 1.6667, \qquad \frac{\partial b_{\text{flip}}}{\partial c} = \frac{1-p}{p} = \frac{0.4}{0.6} \approx 0.6667.$$

### 4.7 Reform scenarios

- **Strong reform ($b=10$).** $\pi_F = 0.6 \times 10 - 0.4 = 5.6$, $\pi_P = 1$, $p^{*} = 2/11 \approx 0.1818$. The replicator coefficient becomes $5.6 - 1.0 = +4.6$, driving the population toward the falsifiable equilibrium.
- **Weak reform ($b=5$).** $\pi_F = 0.6 \times 5 - 0.4 = 2.6$, $p^{*} = (1+1)/(5+1) = 1/3 \approx 0.3333$. The flip point is cleared with margin.
- **Adverse reform ($s'=2$).** Keeping $b=2$, $c=1$, the new threshold is $p^{*}_{\text{new}} = (2+1)/(2+1) = 1.0$, and the payoff gap becomes $0.8 - 2.0 = -1.2$, so $\dot{x} = -1.2\,x(1-x)$: extinction of the falsifiable strategy accelerates by a factor of $1.2/0.2 = 6$ relative to baseline.

The adverse scenario is the practically important one: any policy that raises the premium on compelling narratives — impact prizes, storytelling metrics, media visibility — moves the system away from falsifiability even if the prediction reward is left untouched.

## 5. Results

All quantities in this section are derived directly from the arithmetic in Section 4, from the assumptions A1–A4; none are empirical measurements.

| Quantity | Formula and inputs | Value | Interpretation |
|---|---|---|---|
| Accuracy threshold $p^{*}$ | $(s+c)/(b+c)$, $s=1$, $c=1$, $b=2$ | $0.6667$ | Predictions must succeed above $66.7\%$ to be individually rational. |
| Falsifiable payoff $\pi_F$ | $p\,b-(1-p)\,c$, $p=0.6$, $b=2$, $c=1$ | $0.8$ | Below the narrative payoff. |
| Post-hoc payoff $\pi_P$ | $s=1$ | $1.0$ | Dominates at the assumed baseline. |
| Replicator coefficient | $\pi_F-\pi_P$ | $-0.2$ | Drives $x \to 0$; $10.99$ generations from $x=0.5$ to $x=0.1$. |
| Flip reward $b_{\text{flip}}$ | $(s+(1-p)\,c)/p$ | $2.3333$ | Minimum prediction reward that reverses the equilibrium. |
| Sensitivities of $p^{*}$ | $\partial p^{*}/\partial b$, $\partial p^{*}/\partial c$, $\partial p^{*}/\partial s$ | $-0.2222$, $0.1111$, $0.3333$ | The narrative reward is the most destabilizing per unit. |
| Sensitivities of $b_{\text{flip}}$ | $\partial b_{\text{flip}}/\partial s$, $\partial b_{\text{flip}}/\partial c$ | $1.6667$, $0.6667$ | A rise in $s$ raises the required reward faster than a rise in $c$. |
| Strong reform ($b=10$) | $\pi_F$, $p^{*}$ | $5.6$, $0.1818$ | Falsifiable dominates by $4.6$. |
| Weak reform ($b=5$) | $\pi_F$, $p^{*}$ | $2.6$, $0.3333$ | Clears the flip point. |
| Adverse reform ($s'=2$) | $\pi_F-\pi_P$ | $-1.2$ | Sixfold faster extinction of F. |

The central quantitative finding is that, under the assumed parameters, unfalsifiable narrative-making is a strict evolutionarily stable strategy, and an increase of the confirmed-prediction reward above $b \approx 2.3333$ — a $16.7\%$ rise over the assumed $b=2$ — suffices to make falsifiable practice the stable outcome. The symmetric finding is that a doubling of the narrative reward $s$ from $1$ to $2$ pushes the required accuracy to $1.0$, making falsifiable practice unreachable at any accuracy below certainty.

## 6. Discussion

### 6.1 Limitations

- **L1. Payoff linearity.** Real reputational gains may be convex in track record; a single celebrated confirmation may be worth many routine ones, as the prior version of this analysis already noted [10]. Convexity shifts the threshold and weakens the clean comparative statics.
- **L2. Fixed accuracy.** Agents can invest to raise $p$; the model then becomes a two-dimensional choice, and the threshold analysis describes only the margin of investment, not its level [10].
- **L3. Assumed parameters.** The values $b=2$, $c=1$, $s=1$, $p=0.6$ are assumptions. The qualitative structure (threshold form, strict-Nash dichotomy, flip point) holds for all positive parameters, but every numerical value is specific to this quadruple.
- **L4. Binary strategies.** Hybrid approaches — partial predictions, incremental testing — are omitted. The knowledge-landscape literature shows that richer strategy spaces can support diverging optimal search strategies rather than a single dichotomy [4].
- **L5. Well-mixed population.** Network effects, citation cascades, and the spatial continuity that drives narrative cohesion in the oral-history evidence [7] are ignored; they could generate multiple equilibria.
- **L6. Origin versus persistence.** Like the prior analysis [10], the model explains the persistence of post-hoc strategies once present, not their initial emergence.
- **L7. Deterministic dynamics.** If agents randomize or sample payoffs with noise, the sharp threshold at $p^{*}$ becomes a band; the model has no stochastic choice rule.
- **L8. No empirical calibration.** No parameter has been estimated from data on real funding agencies, journals, or tenure processes. The claim that real institutions occupy the P-dominant region is a hypothesis, stated as such in [10], not a finding of this paper.

### 6.2 What would falsify the model

The model's central empirical prediction is: **raising the effective prediction reward $b$ above the flip point, while holding $s$ and $c$ approximately constant, increases the share of prospectively registered, falsifiable research.** The correct falsification criterion is therefore: a pilot that raises $b$ above $b_{\text{flip}}$ and observes no increase (or a decrease) in the fraction of registered predictions, with $s$ and $c$ audited as stable, would falsify the central claim. Conversely, an observed increase is consistent with the model but is not confirmatory on its own, because a simultaneous change in $s$ or $c$ could produce the same effect; the audit of the narrative reward is therefore part of the test, not an afterthought. A previous version of this paper stated the criterion with the polarity reversed — treating a rise in the falsifiable fraction as falsifying and stasis as supporting — and that statement is corrected here: it contradicted the model's own comparative statics in Section 4.5, under which raising $b$ above $2.3333$ moves the system into the F-dominant region.

A second, structural falsification path exists: if a well-designed audit found that real scoring rules already price prospective registration above retrospective fitting (that is, that real institutions sit in the F-dominant region), the premise that the incentive gap exists would fail, and the model would describe a regime science has already exited.

### 6.3 Open questions

- How do citation-network effects reshape the payoff structure, and can they generate multiple evolutionarily stable strategies?
- What is the effect of heterogeneous accuracies $p$ across sub-fields on the population-level threshold?
- Can the funder's own optimization be formalized as a leader setting $(b,c,s)$ against followers playing the evolutionarily stable strategy?
- How does stochastic strategy adoption smooth the threshold, and how does that affect the statistical power of the proposed pilot?
- What is the elasticity of researcher behavior with respect to $b$? The replicator dynamics assume a fixed response; no estimate exists.

## 7. Practical Implications and Engineering Pathways

### (a) Primary