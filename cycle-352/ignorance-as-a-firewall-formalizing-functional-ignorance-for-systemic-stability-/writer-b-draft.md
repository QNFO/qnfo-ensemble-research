# Ignorance as a Firewall: A Network Model of Functional Ignorance and Truth Buffering in Social Systems

## Abstract

Social groups routinely face messages that are factually accurate yet destabilizing: a single revelation can propagate through a network and disrupt coordination, trust, or cohesion. Practitioners who moderate platforms, manage organizations, or study collective behavior lack a formal account of when endogenous "truth-buffering" practices—selective inattention, face-saving norms, plausible deniability—outperform full-transparency norms. This paper formalizes functional ignorance as a network-level suppression strategy. We model agents on a graph who exchange beliefs, assign to each destabilizing message a transmission probability, and derive the suppression rate a population must sustain to keep message cascades subcritical: for a base reproduction number $R_0 = 3$, the required suppression fraction is $q^{\star} = 2/3 \approx 0.6667$. We derive an evolutionary stability condition under which a suppression heuristic resists invasion by full-transparency strategies (with cost $c = 0.1$, shock probability $p = 0.2$, and loss $L = 1$, the suppressor payoff $0.9$ exceeds the transparent payoff $0.8$), and we show that buffering raises the number of simultaneous revelations a group can absorb from 6 to 20 in a worked example. Empirical cascade data reported in prior work, in which deleting roughly 50% of network links reduced cascade size only to about 50% of the original, indicate that structural deletion is an inefficient substitute for endogenous suppression. The results reframe selective ignorance as a computable stability mechanism with testable thresholds.

## 1. Introduction

Platform trust-and-safety teams, organizational leaders, moderators of online communities, and crisis-communication officials all face the same structural problem: some true information is destabilizing. A verified but corrosive claim, once released into a densely connected communication network, can cascade beyond anyone's control, degrading the trust and coordination that the network itself depends on. The 2016 coordinated influence operation in which Russian operatives created an online astroturf in direct contact with the American public demonstrates that engineered messages can divert political discourse at national scale [7]; social bots have been documented in public opinion manipulation and social spam campaigns, and concerns about manipulating public opinion through social media were raised as early as 2006 [5]. The cost of a destabilizing cascade is therefore not hypothetical, and the tools currently available are blunt.

The blunt tools are structural. The main intervention studied in the literature is link deletion: removing edges from the social graph to limit diffusion. Empirical evaluation on real retweet cascades shows the limits of this approach: when 1.5 million links—approximately 50% of the links in the original social network—were deleted using the NetMelt method, the total cascade size fell only to about 50% of the original, and the authors conclude that the effects of link deletion methods are limited, in part because most retweet cascades have multiple sources [4]. Deleting half of a live social network's connections is practically impossible and socially destructive, yet it buys only a proportional reduction in spread. What would change if a cheaper, endogenous mechanism existed? If a population could achieve the same subcriticality by adjusting its own forwarding behavior—by a norm of selective inattention, a face-saving convention, or a plausible-deniability buffer—then moderators and designers would have a lever that operates on transmission probability rather than on network topology, and theorists would have a candidate for why such norms persist across societies.

This paper develops that lever formally. We call it *functional ignorance*: a population-level strategy in which agents suppress or buffer messages that are epistemically accurate but cohesion-destabilizing, optimizing long-run network stability over individual epistemic throughput. The metaphor is a firewall: as a network firewall isolates suspect packets so one compromised host cannot crash the whole system, a truth-buffering heuristic isolates destabilizing messages so one revelation cannot cascade through the entire social graph. The claim is not that ignorance is good, but that under specifiable conditions it is a mathematically describable stability strategy, and that the conditions can be written down and tested.

Our contributions are:

1. A threshold result: for a message with base reproduction number $R_0$ on a network, a population that suppresses forwarding with probability $q$ keeps cascades subcritical if and only if $q > 1 - 1/R_0$; for $R_0 = 3$ this gives $q^{\star} = 2/3$ (derived in Section 4.1).
2. An evolutionary stability condition: a suppression heuristic with fitness cost $c$ is an evolutionarily stable strategy against full-transparency mutants when $c < pL$, where $p$ is the probability of a destabilizing shock and $L$ the damage an unbuffered shock inflicts; in the worked parameterization ($c = 0.1$, $p = 0.2$, $L = 1$) the suppressor payoff $0.9$ exceeds the transparent payoff $0.8$ (Section 4.2).
3. A buffering capacity result: with cohesion margin $C$ and per-revelation damage $\delta$, suppression at rate $q$ raises the number of simultaneous revelations a group absorbs from $\lfloor C/\delta \rfloor = 6$ to $\lfloor C/(\delta(1-q)) \rfloor = 20$ at $q = 2/3$ (Section 4.3).
4. An efficiency comparison grounded in published cascade data: because deleting approximately 50% of links achieved only a 50% cascade reduction [4], the per-intervention elasticity of structural deletion is approximately 1, whereas endogenous suppression acts multiplicatively on per-generation transmission and reaches the critical threshold at a fraction $1 - 1/R_0$ of behavioral change (Section 4.4).
5. A connection to cognitive buffering: the "functional illusion" strategy described in prior theoretical work—holding an objective truth in the background while operating on a stabilizing heuristic in the foreground [9]—is the single-agent limit of our population model, and the evolutionary-psychology scaling argument for optimized survival strategies [10] supplies the framework in which such heuristics are selected (Section 2 and Section 6).

## 2. Background and Related Work

The study of how information moves through social networks has produced a substantial empirical record, but the record concentrates on either measuring diffusion or suppressing it from the outside; the endogenous suppression strategies of the agents themselves are rarely modeled. We review the works that define the network substrate, the measurement tools, the intervention results, and the cognitive theories our model draws on.

**Network substrate.** Kazienko, Musial and Kajdanowicz construct a multidimensional social network in which the relationships extracted from users' collective behaviour and shared activities are grouped into layers, built on two types of relations between humans, direct and object-based, which form the basic components of the multidimensional network [1]. The companion work introduces the multirelational social network concept, covering both direct and object-based relationships that reflect social and semantic links between users, with the goal of creating new relations between users in a multimedia sharing system [2]. These two results matter for our model because they establish that a real social graph is not a single edge set but a layered, multirelational structure: a message that is benign on one layer (an object-based semantic link) can be destabilizing on another (a direct trust link). Our suppression threshold in Section 4.1 is therefore best read as per-layer: a population may sustain different suppression rates $q_{\ell}$ on different relation layers, and the firewall metaphor applies layer by layer.

**Measurement of diffusion and its content.** Ferrara et al. measure the role of social bots in content spreading dynamics, reviewing how bots are created and operated, the challenges of detecting them, and their documented use in the 2016 US Presidential Election to sway discussion around candidates, using tools including Bot Or Not for bot detection and SentiStrength for sentiment analysis [5]. Swed and colleagues analyze the 2016 network of accounts animated by Russian operatives that attempted to divert political discourse within the American public, a coordinated effort within a Russian-led complex information operation that used the anonymity and outreach of social media platforms to create an online astroturf in direct contact with the public [7]. Both works document exogenous, engineered injection of messages into the network—the attack scenario our firewall model must withstand. If destabilizing messages can be manufactured and injected deliberately, then the load of destabilizing truths arriving at a community is not only endogenous, and the suppression threshold must be met with margin.

On the measurement side, Adamic-style meme clustering formalized by the Clustering Memes framework defines memes operationally so that engineered misinformation campaigns can be distinguished from spontaneous communication, evaluates clusters with Normalized Mutual Information over a confusion matrix $\mathbf{N}$ whose entry $N_{ij}$ counts elements of the correct $i$-th cluster assigned to the $j$-th cluster, and shows that protomeme-based configurations using content- and network-based similarity, including a diffusion similarity built from mention and retweet information reconstructible in real time, outperform a TF-IDF tweet baseline [6]. This supplies the operationalization our model needs: a "destabilizing message" is an empirical object—a meme cluster with a traceable diffusion set—so the suppression rate $q$ is in principle measurable from streaming data rather than assumed.

**Interventions and their limits.** The empirical evaluation of link deletion methods estimates the size of retweet cascades after link deletion and finds that although total cascade size decreases with deletion, the decrease is not large relative to the number of deleted links: deleting 1.5 million links, approximately 50% of the links in the original social network, using NetMelt reduced the total cascade size to about 50% of the original, a result the authors read as showing that the effects of link deletion are limited, with most cascades having multiple sources [4]. This is the central empirical anchor of our efficiency argument in Section 4.4: exogenous structural suppression has an elasticity of roughly one, so it cannot cheaply push a supercritical message below threshold.

**Behavioral correlates of message load.** Multitask learning work on stress and depression recognition shows that social media posts carry detectable psychological-state signal: the framework shares a BERT layer across a primary depression-detection task and an auxiliary stress-detection task, trains on a 70-10-20% train-validation-test split with Adam at learning rate $10^{-5}$, and evaluates with Precision, Recall, F1-score, Accuracy and Specificity, finding that no prior study had exploited multiple datasets with depression and stress as primary and auxiliary tasks on social media posts [8]. For our purposes this establishes that the individual-level cost of unbuffered destabilizing content—stress, depressive signaling—is measurable in the same data streams that measure diffusion, which is what makes the damage term $L$ in our evolutionary model empirically estimable rather than purely abstract.

**Data validity at scale.** The tourism-flows comparison validates the inference chain from behavioral network data to real-world quantities: location-based social network data from Foursquare are found to be comparable to official WTO data and able to satisfactorily represent the global tourism network, in a domain where the WTO reports the urban tourism industry produced more than US$1 billion in 2019 and where traditional survey instruments do not scale [3]. The analogy for our model is direct: if behavioral network data can substitute for official censuses in one domain, then the parameters of a belief-diffusion model ($\beta$, $q$, cascade sizes) are in principle calibratable from observational platform data without surveys.

**Cognitive buffering theories.** The QNFO treatise on agency describes the "functional illusion" as an advanced cognitive strategy in which an individual intellectually accepts the absolute reality of superdeterminism while simultaneously allowing their brain to operate using the heuristic of free will in daily life—a "dual-boot system" in which the prefrontal cortex holds the objective truth in the background while the left-hemisphere interpreter generates the subjective feeling of agency in the foreground; evolution permits this dual processing because completely disabling the illusion of choice would destroy the organism's ability to rapidly interact with peers who rely on the agency bypass [9]. The same treatise argues that perceptual collapse—organisms interacting with stable eigenstates rather than complex probability amplitudes $|\Psi|^2$—reduces the computational load of environmental processing [9]. This is the single-agent precursor of our population model: one agent buffering one truth. Our contribution is to place many such agents on a graph and derive the network-level threshold. The Mechanistic-Ethics treatise supplies the scaling premise: evolutionary psychology is presented as the critical point of scaling between cellular biology and macro-level human social behavior, explaining human actions as optimized survival strategies forged in the ancestral environment [10], which is exactly the selection framework in which we test whether suppression heuristics are stable strategies in Section 4.2. The Clockwork Cosmos work contributes two formal notions we borrow as analogies: the Bekenstein bound, which defines the maximum amount of information that can be contained within a finite region of space [11]—the physical precedent for the idea that an information-processing system must bound its informational intake—and the ultrametric, hierarchical topology of p-adic geometry, in which every triangle is strictly isosceles and relationships form a rigid, infinitely branching genealogical tree [11], a geometry in which local containment of disturbances is structural rather than incidental. Our firewall model asks whether social networks can be given, by norm rather than by geometry, the local-containment property that ultrametric spaces have by construction.

What is missing from this literature, and what this paper adds, is the coupling of the three threads: a measurable destabilizing message [6], a documented intervention failure [4], and a cognitive mechanism for endogenous buffering [9], joined by a threshold condition that says when buffering beats transparency.

## 3. Methods

This is a theoretical paper. We construct a minimal network model of belief exchange, derive its stability conditions analytically, and illustrate every derived quantity with fully shown arithmetic. No simulation, experiment, or data collection was performed; the only empirical numbers we use are quoted from the cited literature and are identified as such.

**Model A: message cascade with endogenous suppression.** Agents occupy a graph of average degree $k$. A destabilizing but truthful message $m$ is introduced. Each exposure of a susceptible agent transmits the message with probability $\beta$; the agent stops transmitting after a characteristic time $1/\gamma$ (attention decay). The basic reproduction number is

$$R_0 = \frac{\beta k}{\gamma}.$$

A suppression heuristic is a population-level norm under which an agent, upon receiving $m$, discards it without forwarding with probability $q$. The effective transmission probability is then $\beta_{\text{eff}} = \beta(1-q)$, and the effective reproduction number is

$$R_{\text{eff}}(q) = R_0 (1 - q).$$

The cascade is subcritical when $R_{\text{eff}} < 1$. We assume homogeneous mixing on the graph (mean-field on the degree), a single message type, and independence of suppression events across agents and generations. These assumptions are stated because they are load-bearing: degree heterogeneity would replace $k$ by a moment-sensitive quantity, and correlated suppression (norms that cluster) would change the threshold.

**Model B: evolutionary stability of suppression.** Two heritable strategies compete: $S$ (suppressor, applies the heuristic, pays fitness cost $c$ per unit time) and $T$ (transparent, never suppresses). Destabilizing shocks arrive with probability $p$ per unit time. When a shock arrives, an unbuffered population suffers damage $L$; a population of suppressors, meeting the threshold of Model A, suffers no shock damage. Payoffs are

$$\pi_S = 1 - c, \qquad \pi_T = 1 - pL.$$

$S$ is an evolutionarily stable strategy against $T$ if, when $T$ is rare, $\pi_S > \pi_T$, i.e. $c < pL$. We assume shocks are exogenous and independent of strategy frequency, and that the threshold condition of Model A holds for the suppressor population.

**Model C: buffering capacity.** A group has a cohesion margin $C$: the total cohesion it can lose before coordination fails. Each unbuffered destabilizing revelation reduces cohesion by $\delta$; a suppressed revelation reduces it by $\delta(1-q)$. The number of simultaneous revelations the group absorbs is

$$n_{\max}(q) = \left\lfloor \frac{C}{\delta (1-q)} \right\rfloor.$$

**Model D: efficiency comparison with structural deletion.** We define the empirical elasticity of an intervention as the ratio of relative cascade reduction to relative intervention size. From the published result that deleting approximately 50% of links reduced cascade size to approximately 50% of the original [4], the elasticity of link deletion is approximately 1. We compare this with the behavioral suppression required to reach subcriticality, $q^{\star} = 1 - 1/R_0$, which acts multiplicatively on every transmission generation rather than on the static edge set.

All parameter values used in worked examples ($k$, $\beta$, $\gamma$, $c$, $p$, $L$, $C$, $\delta$) are assumptions of this paper, chosen for arithmetic transparency, and are labeled as such where they appear. The one empirical anchor—the 50%-links/50%-cascade result—is quoted from [4].

## 4. Analysis

### 4.1 The suppression threshold

Every input in this subsection is an assumption of the model, stated for concreteness. We assume an average degree $k = 10$, a transmission probability $\beta = 0.3$ per exposure, and an attention-decay rate $\gamma = 1$ (time measured in units of the decay time).

Step 1: compute the basic reproduction number.

$$R_0 = \frac{\beta k}{\gamma} = \frac{0.3 \times 10}{1} = 3.$$

Step 2: apply the subcriticality condition. The cascade dies out when

$$R_{\text{eff}}(q) = R_0(1-q) < 1 \quad \Longleftrightarrow \quad 1 - q < \frac{1}{R_0} \quad \Longleftrightarrow \quad q > 1 - \frac{1}{R_0}.$$

Step 3: evaluate at $R_0 = 3$:

$$q^{\star} = 1 - \frac{1}{3} = \frac{2}{3} \approx 0.6667.$$

Interpretation: a population in which each agent ignores two out of every three destabilizing messages it receives keeps the message subcritical. A population that ignores only half ($q = 0.5$) has $R_{\text{eff}} = 3 \times 0.5 = 1.5 > 1$, and the cascade grows. The threshold is sharp in the mean-field model: at $q = q^{\star}$ exactly, $R_{\text{eff}} = 1$ and the cascade is marginal, so in practice the population must sustain $q$ strictly above $2/3$, with margin for the exogenous injection scenarios documented in [5] and [7].

### 4.2 Evolutionary stability of the suppression heuristic

The cost and damage parameters are assumptions: we take $c = 0.1$ (the fitness cost of maintaining the heuristic—attention diverted, information forgone), $p = 0.2$ (probability per unit time of a destabilizing shock), and $L = 1$ (damage of an unbuffered shock, normalized).

Step 1: payoffs.

$$\pi_S = 1 - c = 1 - 0.1 = 0.9,$$
$$\pi_T = 1 - pL = 1 - 0.2 \times 1 = 0.8.$$

Step 2: stability check. When a transparent mutant $T$ is rare in a suppressor population, the mutant enjoys no protection from the population's buffering (its own lack of suppression exposes it and, in the mean-field approximation, the shock it experiences propagates through the buffered majority at $R_{\text{eff}} < 1$ and dissipates). The mutant's payoff is $\pi_T = 0.8$, the resident's is $\pi_S = 0.9$. Since

$$\pi_S - \pi_T = 0.9 - 0.8 = 0.1 > 0,$$

the suppression heuristic is an evolutionarily stable strategy against full-transparency invasion under these parameters.

Step 3: the general condition. The inequality $\pi_S > \pi_T$ reads

$$1 - c > 1 - pL \quad \Longleftrightarrow \quad c < pL.$$

With the assumed numbers, $pL = 0.2 \times 1 = 0.2 > c = 0.1$, so the condition holds with a factor-of-two margin: the heuristic remains stable for any shock cost up to twice the assumed value, or any shock probability up to $c/L = 0.1$. If instead shocks were rarer than $p = 0.1$ or damage smaller than $L = c/p = 0.5$, transparency would invade. The stability region is therefore the half-plane $c < pL$, and the worked point sits comfortably inside it, but the boundary is explicit and falsifiable.

### 4.3 Buffering capacity

Assume a cohesion margin $C = 1$ (normalized) and per-revelation cohesion damage $\delta = 0.15$.

Step 1: without suppression ($q = 0$):

$$n_{\max}(0) = \left\lfloor \frac{1}{0.15} \right\rfloor = \lfloor 6.6667 \rfloor = 6.$$

Step 2: with suppression at the threshold rate $q = 2/3$:

$$\delta(1-q) = 0.15 \times \frac{1}{3} = 0.05,$$
$$n_{\max}(2/3) = \left\lfloor \frac{1}{0.05} \right\rfloor = \lfloor 20 \rfloor = 20.$$

Step 3: the ratio. Buffering at $q = 2/3$ multiplies the number of simultaneous revelations the group can absorb by

$$\frac{n_{\max}(2/3)}{n_{\max}(0)} = \frac{20}{6} \approx 3.3333.$$

The general formula is $n_{\max}(q) = \lfloor n_{\max}(0) / (1-q) \rfloor$, so the capacity gain is exactly the inverse of the residual transmission fraction: at the critical suppression rate $q^{\star} = 1 - 1/R_0$, the gain is $R_0$. For $R_0 = 3$, a buffered group absorbs three times the shock load of a transparent one; for a denser network with $R_0 = 6$ (e.g. $k = 20$, $\beta = 0.3$, $\gamma = 1$, giving $R_0 = 0.3 \times 20 / 1 = 6$), the same rule gives $q^{\star} = 1 - 1/6 = 5/6 \approx 0.8333$ and a capacity gain of 6.

### 4.4 Efficiency of endogenous suppression versus structural deletion

The empirical anchor is from the link-deletion evaluation: deleting 1.5 million links, approximately 50% of the links in the original social network, using NetMelt reduced the total cascade size to about 50% of the original, and the authors judge the effect limited because most cascades have multiple sources [4].

Step 1: elasticity of structural deletion. Define $e = \frac{\Delta \text{cascade}}{\Delta \text{links}}$ in relative terms:

$$e_{\text{del}} = \frac{1 - 0.50}{0.50} = \frac{0.50}{0.50} = 1.$$

Deleting a fraction $f$ of links buys approximately a fraction $f$ of cascade reduction—no amplification.

Step 2: what suppression must achieve. To bring $R_0 = 3$ below unity behaviorally requires $q^{\star} = 2/3$ of forwarding events suppressed. If one tried to reach the same threshold by deleting links uniformly, one would need to remove a fraction $f = 1 - 1/R_0 = 2/3 \approx 0.6667$ of all links—more than the 50% that the empirical study already calls practically difficult [4]—and, at elasticity 1, even that would reduce the cascade size of an already-launched cascade only proportionally rather than collapsing it.

Step 3: the mechanistic contrast. Link deletion removes static edges; a cascade with multiple sources routes around deletions, which is the mechanism the cited study identifies for its limited effect [4]. Endogenous suppression acts on the transmission event itself, at every generation, in every agent, so its effect compounds multiplicatively: after $g$ generations the expected cascade volume scales as $[R_0(1-q)]^g$, which decays geometrically once $q > q^{\star}$. At $q = 0.7$ and $R_0 = 3$: $R_{\text{eff}} = 3 \times 0.3 = 0.9$, and the volume after $g = 10$ generations scales as $0.9^{10} \approx 0.3487$ of one agent's contribution, versus $3^{10} = 59049$ for the unsuppressed case. The comparison is not symmetric in effort—sustaining $q = 0.7$ across a population is itself a coordination problem, addressed in Section 6—but it is symmetric in mechanism: one intervention fights topology, the other fights dynamics, and only the latter has a threshold it can actually cross.

### 4.5 Connection to single-agent cognitive buffering

The functional illusion described in prior theoretical work—an individual holding the objective truth in the background while operating a stabilizing heuristic in the foreground, at the cost of maintaining a dual-boot cognitive architecture [9]—is the $N = 1$ case of Model C: one agent, one buffered revelation, cohesion margin $C$ equal to that agent's psychological capacity. The claim that perceptual filtering reduces the computational load of environmental processing [9] is the micro-foundation of the cost term $c$ in Model B: suppression is not free, it consumes the agent's processing budget, and the Bekenstein-bound analogy—any finite physical region contains a bounded amount of information [11]—makes the point structurally: an agent with finite capacity must bound its informational intake, and the question is only whether the bound is set by accident or by a stability-optimizing policy. The evolutionary-psychology premise that human social behavior is explained as optimized survival strategies [10] is the framework assumption under which Model B's stability question is well posed: if suppression is a strategy, it can be invaded, and the condition $c < pL$ says when it cannot be.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; no simulation or measurement was performed.

**R1 (Suppression threshold).** For the assumed network ($k = 10$, $\beta = 0.3$, $\gamma = 1$, hence $R_0 = 3$), the population-level suppression rate required for subcritical cascades is $q^{\star} = 2/3 \approx 0.6667$. A population suppressing at $q = 0.5$ fails ($R_{\text{eff}} = 1.5$); at $q = 0.7$ it succeeds ($R_{\text{eff}} = 0.9$).

**R2 (Evolutionary stability).** Under the assumed costs ($c = 0.1$, $p = 0.2$, $L = 1$), the suppressor payoff $\pi_S = 0.9$ exceeds the transparent payoff $\pi_T = 0.8$, so suppression is an evolutionarily stable strategy; the general condition is $c < pL$, and the worked point has a factor-of-two margin ($pL/c = 0.2/0.1 = 2$).

**R3 (Buffering capacity).** With $C = 1$ and $\delta = 0.15$, suppression at $q = 2/3$ raises the number of simultaneously absorbable revelations from $n_{\max}(0) = 6$ to $n_{\max}(2/3) = 20$, a gain of $20/6 \approx 3.3333$, equal to $R_0$ at the critical suppression rate.

**R4 (Deletion elasticity).** From the published cascade data [4], the elasticity of structural link deletion is $e_{\text{del}} = (1-0.50)/0.50 = 1$: deleting a fraction $f$ of links yields approximately a fraction $f$ of cascade reduction. Reaching subcriticality for $R_0 = 3$ by deletion alone would require removing $f = 2/3 \approx 0.6667$ of all links, exceeding the 50% deletion level that the source study already identifies as practically