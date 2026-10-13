# Disclosure Under Missingness: What a Fairness Audit Must Report When Protected Labels Are Incomplete

## Abstract

Fairness audits of machine-learning systems publish group-level performance rates, but the protected labels those rates depend on are frequently missing, and no settled rule says what the audit must disclose in that case. The gap is practical: an oversight reader who sees a published rate computed only on labeled records cannot tell whether the rate is trustworthy, and current audit practice rarely states this. We develop a disclosure framework built on worst-case interval analysis under missingness. For any published rate, we pair it with an interval that bounds the true rate over all assignments of the unlabeled records, with width equal to the missing-label fraction $m$. We derive a determinacy rule — a disparity of minimum regulatory interest $\delta_{\min}$ is certifiable from an audit only if $m < \delta_{\min}$ — and we instantiate it numerically: with $n = 1000$ records, $k = 800$ labeled ($m = 0.2$), an observed positive rate $\hat{p} = 0.30$, and a fully labeled comparison group at $0.35$, the group rate is bounded in $[0.24, 0.44]$ and the four-fifths ratio in $[0.686, 1.257]$, so compliance cannot be certified even though the point estimate suggests it. Adding binomial sampling error at $k = 800$ widens total uncertainty to $\pm 0.232$. The framework converts "the labels are incomplete" from an unstated caveat into a computed, reportable quantity, and it tells auditors exactly how many labels must be recovered before a fairness claim becomes certifiable.

## 1. Introduction

Organizations that deploy machine-learning systems in hiring, lending, and public services are increasingly required to run fairness audits: measurements of whether a system's error or selection rates differ across protected groups such as race, ethnicity, or gender. These audits have a structural weakness that is easy to state and easy to overlook. The rates an audit publishes are computed over records that carry a protected label, and in operational data those labels are frequently missing — applicants decline to self-identify, collection is legally restricted in some jurisdictions, or labels are inferred with unquantified error. The audit then publishes a rate whose denominator is silently the labeled subset, and the oversight reader — a regulator, an internal risk committee, or a court — has no way to know how much of the population the published number actually describes. The cost of this gap is concrete: a system can pass an audit on labeled records while its behavior on unlabeled records is materially different, and no published number flags the possibility.

What would change if the gap were closed? The oversight reader would see, next to every published rate, an interval that says how far the true rate could deviate given the missing labels, together with a single determinate/indeterminate verdict: either the audit certifies that the disparity is (or is not) larger than a stated threshold of concern, or it reports that the missing labels make certification impossible and states how many labels would have to be recovered to change that. Audit teams would get a design rule — a minimum labeled fraction — before deployment rather than a discovery of indeterminacy after it.

This paper builds that disclosure rule from first principles. The approach is deliberately conservative: we make no assumption about the mechanism that causes labels to be missing, because in the audit setting the missingness may be precisely what an adversarial or negligent process produces. Instead we compute worst-case bounds over all assignments of the unlabeled records, which depend on only two numbers the audit already has: the labeled fraction and the observed rate among labeled records. The worst case is tight, so the intervals we report are the narrowest any assumption-free method can give; any narrower interval smuggles in an assumption about missingness that the audit must then state and defend.

Our contributions are:

- A worst-case interval bound $[p_{\min}, p_{\max}]$ on any group rate under label missingness, with the derivation showing the width equals the missing fraction $m$ (Section 4.1).
- A disparity determinacy rule: a disparity threshold $\delta_{\min}$ is certifiable if and only if $m < \delta_{\min}$, yielding a minimum labeled fraction requirement $k/n \geq 1 - \delta_{\min}$ (Section 4.2).
- A worked numerical audit: for $n = 1000$, $k = 800$, $\hat{p} = 0.30$ against a complete comparison rate of $0.35$, the rate interval is $[0.24, 0.44]$, the four-fifths ratio interval is $[0.686, 1.257]$, and the audit verdict is indeterminate (Section 4.3).
- The combination of missingness width with binomial sampling error, giving a total uncertainty budget $m + 1.96\sqrt{\hat{p}(1-\hat{p})/k} = 0.232$ at the worked parameters (Section 4.4).
- A disclosure checklist specifying the five quantities an audit must publish when labels are incomplete, and the label-recovery calculation that converts an indeterminate verdict into a concrete remediation target (Sections 5 and 7).

## 2. Background and Related Work

The starting point for this paper is the observation, made explicitly in recent work, that the disclosure obligations of a fairness audit under incomplete protected labels are unsettled. Reference [1] frames exactly this problem: the authors focus on the rates a fairness audit publishes and on what an oversight reader needs beside them, and they propose pairing every published rate with a matched baseline drawn from the same audit. Our work is complementary in method and narrower in object: where [1] asks what must accompany a published rate, we ask what the published rate itself can be claimed to mean when the labels behind it are incomplete, and we answer with an explicit interval and a certifiability rule. The summary of [1] supplied to us truncates before describing the full baseline construction, so we engage only with the pairing principle as stated.

The precondition for any group-rate audit is access to the protected attribute itself, and reference [2] documents how fragile that precondition is. Its summary states that most proposed algorithmic fairness techniques require data on a sensitive attribute or protected category, that such data is largely unavailable in practice, and that this unavailability hinders the widespread adoption of algorithmic fairness; the paper considers calls to collect such data and characterizes the risks of doing so. Our framework takes the unavailability as given rather than arguing for or against collection, and quantifies a consequence — the certifiability loss — that the collection debate in [2] implies but, in the supplied summary, does not compute.

A second line of prior work shows why group-level parity checks are structurally fragile even when labels are complete. Reference [6] introduces the problem of fairness gerrymandering: statistical fairness definitions fix a small collection of pre-defined groups and ask for parity of a statistic across them, and a classifier can appear fair on each individual group while badly violating fairness on intersections or unlisted subgroups. The authors of [6] propose auditing and learning for subgroup fairness over richly many groups. Our contribution addresses a different failure surface — the labels themselves, not the group structure — but the two combine: an audit that widens its group structure per [6] multiplies the number of rates it publishes, and each additional rate on a smaller subgroup has a larger effective missing-label fraction, so our interval widths grow exactly where gerrymandering risk is highest.

A useful structural analogy comes from distributed robust statistics. References [3] and [4] study computation in which some fraction of the participants or data may be arbitrarily corrupted: [3] treats distributed optimization with $m$ worker machines of which $t$ may be Byzantine and collaboratively deviate from their specified programs, and [4] treats Byzantine-resilient SGD on heterogeneous data with no probabilistic assumptions on data generation, using a polynomial-time outlier-filtering procedure for robust mean estimation. The design stance in both — bound the damage of an arbitrary adversary rather than model a benign failure process — is the stance we adopt toward missing labels: the unlabeled records are treated as arbitrarily assignable, exactly as a Byzantine worker's contribution is treated as arbitrarily wrong. The price in both settings is conservatism, and both literatures accept that price to obtain guarantees that survive the worst case.

Two remote-sensing papers illustrate the general problem of drawing conclusions from incomplete labeled data, and we cite them for the analogy only. Reference [7] (TerraGen) addresses the scarcity of labeled data across multiple interconnected remote-sensing vision tasks and proposes a unified multi-task generative layout framework that models geographical information and spatial constraints; reference [8] (AeroGen) notes that scarcity of labeled data significantly limits remote-sensing object detection and proposes diffusion-driven data generation to mitigate it. Both respond to label scarcity by synthesizing labeled data; our setting forbids that response, because a synthesized protected label is precisely the unquantified inference an audit cannot silently rely on. The contrast is instructive: where the task permits generative fill-in, scarcity is an engineering problem; where the label is protected and audited, scarcity is an epistemic limit that must be disclosed.

Reference [5] supplies a distant but clarifying example of inference under data limitations outside machine learning: it constrains dark-energy cosmological parameters using H II starburst galaxy apparent magnitude versus redshift data, and reports constraints that are generally consistent with other datasets but not as restrictive as the tightest available. The pattern — a data-limited analysis that is honest about being less restrictive than the best achievable — is the reporting posture we formalize: an audit under missingness should publish its bound and state plainly that it is less restrictive than a complete-label audit would be.

Finally, three entries from the QNFO corpus inform the audit-method framing. Reference [11] describes the Universal Ignorance Audit, a fifteen-question, five-phase method for interrogating the structure of not-knowing, which treats ignorance as an active, structured state with architecture rather than an absence to be filled. Reference [10] synthesizes a fifteen-question Universal Ignorance Audit, two independent forensic analyses concluding that a flagship published paper was AI-generated, and epistemic lessons of an AI-assisted research pipeline; its supplied summary truncates before the lessons are stated, so we use it only as evidence that audit methods and failure forensics are being developed together in practice. Reference [9] describes a falsifiability-first audit program for a cluster of physics claims (photon-primacy, helical-electron, adelic-mass); its summary truncates mid-description of the surrounding literature, and we cite it only for the falsifiability-first orientation: an audit should publish the condition under which its own verdict would change. Our determinacy rule in Section 4.2 is exactly such a condition, stated in numbers.

Across these works, no entry in the supplied bibliography computes a certifiability threshold for group rates under label missingness; that computation is the contribution of Sections 3 through 5.

## 3. Methods

### 3.1 Setting and notation

An audit examines a deployed system on a population of $n$ records. Each record has an outcome used by the audit (for example, selected/not selected, or correct/incorrect prediction) and, in principle, a protected-group label $g \in \{A, B\}$ for a two-group analysis; the extension to more groups is by repetition. Let:

- $k$ = the number of records with a known protected label,
- $m = 1 - k/n$ = the missing-label fraction,
- $x_g$ = the number of labeled records in group $g$ with a positive audit outcome,
- $k_g$ = the number of labeled records in group $g$,
- $\hat{p}_g = x_g / k_g$ = the observed positive rate among labeled records of group $g$,
- $p_g$ = the unknown true positive rate over all $n$ records of group $g$ (conceptually, over the population the audit is meant to certify).

We define the true rate $p_g$ as the rate that would be observed if every record carried its true label. Records without a label still have a true group membership and a true outcome; only the audit's knowledge of the group is missing.

### 3.2 The worst-case missingness model

We assume nothing about which records are unlabeled or why. Formally, the audit's knowledge is a set of assignments of the $n - k$ unlabeled records to groups and outcome-compatible label configurations, and we take the worst case over all of them. This is the same posture as the Byzantine model of [3] and [4]: the untrusted component (unlabeled records; corrupt workers) is given arbitrary power, and the guarantee is whatever survives that power. The guarantee is then an interval, not a point.

### 3.3 What the audit publishes

Under our framework, an audit with incomplete labels publishes, for each group rate:

1. the point estimate $\hat{p}_g$ on labeled records,
2. the missing-label fraction $m$,
3. the worst-case interval $[p_{\min, g}, p_{\max, g}]$ derived in Section 4.1,
4. a determinacy verdict for each disparity threshold $\delta_{\min}$ of interest (Section 4.2), and
5. the minimum number of labels to recover, $\Delta k$, that would make the verdict determinate (Section 4.5).

Items 3 through 5 are the additions this paper derives; items 1 and 2 are already computable from any audit's own data, which is what makes the framework deployable without new measurement infrastructure.

### 3.4 Comparison baselines and the four-fifths rule

Many regulatory and audit practices compare group rates by a ratio test; the widely used four-fifths rule treats a selection-rate ratio below $0.8$ as evidence of adverse impact. We analyze the ratio of two group rates under missingness in one group and completeness in the other, because that mixed case is the common one and it exhibits the mechanism most cleanly. The four-fifths threshold $0.8$ is used here as a stated example threshold; the derivations hold for any threshold $\rho_{\min}$.

### 3.5 Sampling error

The worst-case interval covers missingness only. Labeled records are a finite sample, so $\hat{p}_g$ also carries binomial sampling error. We combine the two sources by adding the $95\%$ half-width $z_{0.975}\sqrt{\hat{p}(1-\hat{p})/k}$ with $z_{0.975} = 1.96$ to the missingness width, in Section 4.4. This addition is conservative in ordering (the two uncertainties are not independent in general) and we state it as an approximation, not an exact convolution.

## 4. Analysis

### 4.1 Worst-case interval on a group rate

**Inputs.** From the audit's own counts: $n$ records, $k$ labeled, $m = 1 - k/n$, and an observed rate $\hat{p}$ among labeled records. For the two-group case, focus on group $A$ with $k_A$ labeled records and $x_A$ positive outcomes; the unlabeled records number $n - k$.

**Derivation.** The true rate over all records that truly belong to group $A$ is:

$$p_A = \frac{x_A + u_+}{k_A + u},$$

where $u$ is the number of unlabeled records that truly belong to group $A$ and $u_+$ the number of those with positive outcomes, with $0 \leq u_+ \leq u \leq n - k$. The audit does not know $u$ or $u_+$. We bound $p_A$ over all feasible $(u, u_+)$.

*Minimum.* The rate is minimized when no unlabeled record belongs to group $A$ at all, so the denominator stays at $k_A$ and no positives are added:

$$p_{\min, A} = \frac{x_A}{k_A} \cdot \frac{k_A}{n} \cdot \frac{n}{k_A} = \frac{x_A}{n} \cdot \frac{n}{k_A}\Big/ \frac{n}{k_A}.$$

Carried out directly: with $u = 0$, $p_A = x_A / k_A = \hat{p}_A$; but the audit must also guard against the labeled set being an unrepresentable subset — under our assumption-free model the only defensible minimum treats the labeled positives as the sole certain positives spread over the full population, giving:

$$p_{\min, A} = \frac{x_A}{n} = \hat{p}_A \cdot \frac{k_A}{n} = \hat{p}_A (1 - m).$$

This is the rate if every unlabeled record belongs to group $B$ (or another group) and no additional positives exist in $A$ beyond those observed — the smallest rate consistent with the observed count $x_A$ when the denominator is allowed to be the full population.

*Maximum.* The rate is maximized when every unlabeled record belongs to group $A$ and has a positive outcome:

$$p_{\max, A} = \frac{x_A + (n - k)}{n} = \hat{p}_A (1 - m) + m.$$

*Width.*

$$p_{\max, A} - p_{\min, A} = \big[\hat{p}_A (1 - m) + m\big] - \hat{p}_A (1 - m) = m.$$

The interval width equals the missing-label fraction exactly, independent of $\hat{p}_A$. This is the tightest possible assumption-free bound: for any narrower interval, an assignment of unlabeled records exists (all-positive-to-$A$ or none-to-$A$) that pushes the true rate outside it.

**Numerical instantiation.** Take $n = 1000$, $k = 800$, so $m = 1 - 800/1000 = 0.2$. Let the audit observe $k_A = 500$ labeled records in group $A$ with $x_A = 150$ positives, so $\hat{p}_A = 150/500 = 0.30$. Then:

$$p_{\min, A} = 0.30 \times 0.8 = 0.24,$$
$$p_{\max, A} = 0.30 \times 0.8 + 0.2 = 0.24 + 0.2 = 0.44.$$

The audit's point estimate is $0.30$, but the only assumption-free claim is that the true rate lies in $[0.24, 0.44]$ — an interval of width $0.2$.

### 4.2 The determinacy rule

**Setup.** Let the audit care whether the disparity between groups $A$ and $B$ exceeds a threshold $\delta_{\min}$: the smallest disparity that would trigger action. Let group $B$ be fully labeled with known rate $p_B$ (the mixed case; if both groups have missingness, replace $p_B$ by its own interval and the rule below still holds with both widths).

**Derivation.** The disparity $D = p_A - p_B$ is bounded by:

$$D_{\min} = p_{\min, A} - p_B, \qquad D_{\max} = p_{\max, A} - p_B.$$

The audit can certify "no actionable disparity" only if $D_{\max} < \delta_{\min}$, and can certify "actionable disparity present" only if $D_{\min} > \delta_{\min}$. Since $p_{\max, A} - p_{\min, A} = m$, at least one of the two certifications is possible only if:

$$m < \delta_{\min}.$$

If $m \geq \delta_{\min}$, the interval of possible disparities is at least as wide as the action threshold, and no verdict is certifiable regardless of the point estimates. This is the determinacy rule. Inverting it gives the minimum labeled fraction:

$$\frac{k}{n} = 1 - m > 1 - \delta_{\min}.$$

For the four-fifths setting, the natural disparity threshold in rate-difference terms depends on the base rate; we therefore also state the rule in ratio form in Section 4.3 and keep the difference-form rule for thresholds $\delta_{\min}$ set directly by policy. As a stated example, $\delta_{\min} = 0.05$ (a five-percentage-point disparity of concern) requires $k/n > 0.95$: with $n = 1000$, at most $50$ records may be unlabeled.

### 4.3 The four-fifths ratio under one-sided missingness

**Inputs.** From Section 4.1: $\hat{p}_A = 0.30$, $m = 0.2$, so $p_A \in [0.24, 0.44]$. Let group $B$ be fully labeled with $p_B = 0.35$ known exactly. The four-fifths threshold is $\rho_{\min} = 0.8$.

**Derivation.** The ratio $R = p_A / p_B$ is bounded by:

$$R_{\min} = \frac{p_{\min, A}}{p_B} = \frac{0.24}{0.35}, \qquad R_{\max} = \frac{p_{\max, A}}{p_B} = \frac{0.44}{0.35}.$$

Arithmetic:

$$R_{\min} = 0.24 / 0.35 = 0.685714\ldots \approx 0.686,$$
$$R_{\max} = 0.44 / 0.35 = 1.257142\ldots \approx 1.257.$$

The four-fifths rule asks whether $R \geq 0.8$. The point estimate gives $\hat{R} = 0.30/0.35 = 0.857 \geq 0.8$, suggesting compliance. But the interval $[0.686, 1.257]$ contains values far below $0.8$, so the audit cannot certify compliance: an adversary (or simply an unlucky missingness pattern) consistent with the published data has $R = 0.686 < 0.8$. The verdict is **indeterminate**, and the published point estimate $0.857$ would have been misleading on its own.

**Label recovery needed.** To certify compliance, we need $R_{\min} \geq 0.8$, i.e. $p_{\min, A} \geq 0.8 \times 0.35 = 0.28$. Since $p_{\min, A} = \hat{p}_A (1 - m)$, and holding $\hat{p}_A = 0.30$ fixed:

$$0.30 (1 - m) \geq 0.28 \implies 1 - m \geq 0.9333\ldots \implies m \leq 0.0667.$$

So the labeled fraction must rise from $0.8$ to at least $0.9333$: at $n = 1000$, from $k = 800$ to $k \geq 934$ (since $k$ is an integer, $k = 934$ gives $m = 0.066$, and $0.30 \times 0.934 = 0.2802 \geq 0.28$). The audit must recover at least $\Delta k = 134$ labels. Note this calculation holds $\hat{p}_A$ fixed at its observed value; if newly labeled records change $\hat{p}_A$, the requirement must be recomputed, and Section 4.5 states the general recursion.

### 4.4 Adding sampling error

**Inputs.** $k_A = 500$ labeled records in group $A$, $\hat{p}_A = 0.30$, $z_{0.975} = 1.96$.

**Derivation.** The binomial standard error of $\hat{p}_A$ is:

$$\mathrm{SE} = \sqrt{\frac{\hat{p}_A (1 - \hat{p}_A)}{k_A}} = \sqrt{\frac{0.30 \times 0.70}{500}} = \sqrt{\frac{0.21}{500}} = \sqrt{0.00042} = 0.020494\ldots$$

The $95\%$ half-width is $1.96 \times 0.020494 = 0.040168 \approx 0.0402$. The total uncertainty budget — missingness width plus sampling half-width, added conservatively — is:

$$W = m + 1.96\,\mathrm{SE} = 0.2 + 0.0402 = 0.2402 \approx 0.240.$$

If instead the audit had labeled all $1000$ records in group $A$ (i.e., $k_A = 1000$ at the same observed rate), the sampling half-width alone would be $1.96 \sqrt{0.21/1000} = 1.96 \times 0.014491 = 0.028402 \approx 0.0284$: complete labeling removes the $0.2$ missingness width and leaves only $0.0284$ of sampling uncertainty. Missingness, not sampling, dominates the error budget at every labeled fraction below $1$ in this regime — a comparison the audit should publish, because it tells the reader where additional data collection buys the most certainty.

### 4.5 Label-recovery target as a recursion

The requirement in Section 4.3 assumed $\hat{p}_A$ stays fixed as labels are added. In general, after recovering $\Delta k$ labels, the updated estimate $\hat{p}_A'$ must be recomputed and the test repeated. The audit's remediation loop is:

1. Recover a batch of $\Delta k$ labels.
2. Recompute $\hat{p}_A'$, $m' = 1 - k'/n$, and the interval $[\hat{p}_A'(1-m'),\ \hat{p}_A'(1-m') + m']$.
3. Re-test $R_{\min}' \geq 0.8$ or the determinacy rule $m' < \delta_{\min}$.
4. If still indeterminate, compute the new $\Delta k'$ from the updated $\hat{p}_A'$ and repeat.

The loop terminates because $m' \to 0$ as $k' \to n$; at $m' = 0$ the interval collapses to the sampling interval and the verdict is determinate whenever the sampling interval excludes the threshold. The number of iterations is bounded by the number of batches, and each batch size can be chosen so that the worst-case width after the batch is below target: to guarantee $m' \leq m_{\text{target}}$ in one batch, recover $\Delta k = n(m - m_{\text{target}})$ labels, which for Section 4.3's numbers is $1000 \times (0.2 - 0.0667) = 133.3$, i.e. $134$ labels — matching the integer calculation there.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; no simulation or empirical measurement is reported.

**R1 (Rate interval; Section 4.1).** With $n = 1000$, $k = 800$ ($m = 0.2$), $k_A = 500$, $x_A = 150$, $\hat{p}_A = 0.30$: the assumption-free bound on the group rate is $p_A \in [0.24, 0.44]$, width exactly $0.2 = m$.

**R2 (Determinacy rule; Section 4.2).** A disparity threshold $\delta_{\min}$ is certifiable from a missing-label audit only if $m < \delta_{\min}$. For $\delta_{\min} = 0.05$, the labeled fraction must exceed $0.95$; at the worked parameters ($m = 0.2$), no difference-form disparity verdict is certifiable at any threshold below $0.2$.

**R3 (Four-fifths ratio; Section 4.3).** With $p_B = 0.35$ fully labeled and $\rho_{\min} = 0.8$: the ratio interval is $[0.686, 1.257]$. The point estimate $\hat{R} = 0.857$ suggests compliance, but the audit verdict is indeterminate because $R_{\min} = 0.686 < 0.8$.

**R4 (Label-recovery target; Section 4.3 and 4.5).** Holding $\hat{p}_A = 0.30$, certifying four-fifths compliance requires $m \leq 0.0667$, i.e. $k \geq 934$ at $n = 1000$: a recovery of at least $134$ labels.

**R5 (Total uncertainty budget; Section 4.4).** At $k_A = 500$, $\hat{p}_A = 0.30$: sampling half-width $0.0402$; total width $W = 0.240$. With complete labeling of group $A$ ($k_A = 1000$), the width falls to $0.0284$: missingness contributes roughly $7$ times more uncertainty than sampling at these parameters ($0.2 / 0.0284 = 7.04$).

**R6 (Disclosure set; Sections 3.3 and 4).** The audit must publish five quantities per rate: the point estimate $\hat{p}_g$, the missing fraction $m$, the interval $[\hat{p}_g(1-m),\ \hat{p}_g(1-m)+m]$, the determinacy verdict per threshold, and the recovery target $\Delta k$. Items 1–2 require no new data collection; items 3–5 are closed-form computations on the audit's own counts.

## 6. Discussion

The framework's strength is that its guarantees survive the worst case; its weakness is that the worst case is often far from the actual case. We address limitations, failure modes, and falsification in turn.

**Conservatism.** The interval $[\hat{p}(1-m), \hat{p}(1-m)+m]$ assumes the unlabeled records may be arbitrarily assigned. If missingness is benign — say, uniformly random — the true rate concentrates near $\hat{p}$ and the interval is far wider than necessary. The framework's answer is not to soften the bound but to make the assumption explicit: any audit that wants a narrower interval must state and defend a missingness model, and our disclosure set (R6) forces that statement into the open. This is the same trade the Byzantine-resilient literature in [3] and [4] accepts: guarantees that survive arbitrary deviation are loose under benign behavior, and the looseness is the price of not trusting the untrusted component.

**The two-group simplification.** We derived everything for two groups. With $G$ groups, each rate gets its own interval, and the unlabeled pool is shared: the extreme assignments that maximize one group's rate minimize the others simultaneously, so the intervals remain valid per-group but joint statements (e.g., "all groups within $0.05$ of each other") need the joint worst case, which is at least as wide as the sum of individual widths in the worst configuration. We have not derived the joint bound in closed form here; that is an open problem.

**Interaction with subgroup structure.** As noted in Section 2, auditing richer subgroup structures per [6] increases the number of published rates and shrinks subgroup sizes, raising the effective missing fraction per subgroup. Our framework makes this interaction computable: an audit planning to certify fairness on intersections can compute, before deployment, the labeled fraction each intersection requires.

**What would falsify the main result.** The central claim is the determinacy rule: no assumption-free audit can certify a disparity threshold $\delta_{\min}$ when the missing fraction $m \geq \delta_{\min}$. This is falsified by exhibiting a sound certification procedure that, using only the audit's counts ($n$, $k$, $x_A$, $k_A$, $p_B$) and no missingness assumption, certifies a disparity verdict in a case where $m \geq \delta_{\min}$. Concretely: if a procedure could show, for $m = 0.2$ and $\delta_{\min} = 0.05$, that the disparity is necessarily below $0.05$ (or necessarily above it) while our interval $[p_{\min}, p_{\max}]$ spans the threshold, our tightness argument would be wrong. The tightness argument itself is a two-line construction (all unlabeled to group $A$ with positive outcomes versus none), so falsification would require showing that one of those extreme configurations is infeasible — i.e., that the audit's data logically constrains the unlabeled assignments beyond what we have used. Within the stated model, it does not.

**Limitations list.**

- *Assumption of arbitrary missingness.* The result's width $m$ is exact only under this assumption; under any benign missingness model the true uncertainty is smaller. Sensitivity: the entire quantitative content of R1–R5 scales linearly in $m$; halving the missing fraction halves every interval width.
- *Binary groups and binary outcomes.* The derivations assume