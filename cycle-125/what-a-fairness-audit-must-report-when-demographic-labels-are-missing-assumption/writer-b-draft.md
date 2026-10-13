# What a Fairness Audit Must Report When Demographic Labels Are Missing: Assumption-Free Disparity Intervals and a Missingness Disclosure Rule

## Abstract

Fairness audits of machine-learning systems publish group-level rates such as selection rates, but the protected labels those rates depend on are frequently missing for a large fraction of the audited population, and the field has not settled what an audit must disclose in that situation. This paper addresses that gap with an assumption-free analysis of how missing protected labels propagate into every disparity statistic an audit might publish. We model each group's reported rate as a rate computed on the labeled subset and derive exact worst-case bounds on the full-population rate under any pattern of missingness. The central result is that the width of the resulting uncertainty interval on a two-group disparity equals the sum of the two groups' missingness rates, independent of the rates themselves: with missingness rates of $0.6$ and $0.5$, a reported gap of $0.10$ is compatible with any true gap in $[-0.475,\,0.625]$. We further derive a sufficient disclosure-and-decision rule: a reported disparity is empirically meaningful only if the reported gap exceeds the sum of the missingness rates, and we show with worked arithmetic that when this condition holds and labeled subsamples are large, binomial sampling error adds only about $0.054$ of additional half-width versus $0.04$ from missingness. The practical change is a disclosure rule: every published rate must be paired with its group-level missingness rate and the implied interval, turning an unreadable point estimate into a falsifiable claim.

## 1. Introduction

Organizations that deploy machine-learning systems in hiring, lending, education, and public services are increasingly required to audit those systems for disparate treatment across protected groups, and regulators, courts, and internal oversight boards read the resulting audit reports. The audit's basic currency is the group-level rate: a selection rate, a false-positive rate, a referral rate, computed per protected group and compared across groups. Producing those rates requires knowing, for each person in the audited population, which group they belong to. In practice that knowledge is routinely incomplete. Protected attributes are self-reported, optionally collected, inferred with error, or legally restricted from collection, so a substantial fraction of audited records carry no usable group label. An audit that silently computes rates on the labeled subset alone publishes numbers whose relationship to the full population is unknown to its readers.

The cost of this gap is concrete. An oversight reader who sees "group A is selected at $25\%$, group B at $15\%$" cannot currently tell from the report whether that ten-point gap would survive, shrink, or reverse if the unlabeled records were labeled, because typical audit reports do not state how many records were excluded or what the exclusion does to the statistic. The reader therefore faces a decision — accept the audit, demand remediation, or halt deployment — with a number whose evidentiary value is unquantified. If the analysis in this paper holds, the same reader can compute, from two numbers the audit can always supply (the labeled-subset rate and the group's missingness rate), an interval that is guaranteed to contain the full-population rate under any pattern of missingness, and can reject the audit's disparity claim outright whenever the reported gap is smaller than the total missingness. That converts an unfalsifiable point estimate into a claim with stated failure conditions, which is precisely what an oversight decision procedure needs.

This paper's stance is deliberately conservative: we derive bounds that require no assumption about why labels are missing — not missing at random, not ignorable, not adversarial — so the bounds hold even if missingness is itself correlated with the outcome. The price of that conservatism is width, and a second contribution is to quantify that price so an audit designer can decide when assumption-free reporting is informative and when it is not.

Our contributions are:

- An exact worst-case interval $[\hat{r}_g(1-m_g),\ \hat{r}_g(1-m_g)+m_g]$ containing any group's full-population rate given its labeled-subset rate $\hat{r}_g$ and missingness rate $m_g$, derived in Section 4.1.
- The result that the width of the assumption-free interval on a two-group disparity equals $m_1 + m_2$, independent of the rates, derived in Section 4.2, with the worked example $[-0.475,\,0.625]$ for a reported gap of $0.10$.
- A sufficient decision rule — a reported positive gap survives assumption-free scrutiny only if $\hat{g} > m_1 + m_2$ — derived in Section 4.3, and a combined treatment of missingness and finite-sample binomial error in Section 4.4 showing that with $980$ labeled records per group the sampling contribution is approximately $0.054$ in half-width.
- A disclosure specification, built on these results and on the matched-baseline structure of [1], stating the minimum set of numbers an audit must publish when labels are incomplete, presented in Section 5 and discussed in Section 7.

## 2. Background and Related Work

The starting point for this paper is [1], which asks what a fairness audit must disclose when the protected labels it depends on are incomplete, and focuses on the rates an audit publishes and on what an oversight reader needs beside them; its approach pairs every published rate with a matched baseline drawn from the same audit. Our work is a direct formalization of one part of that program: we take the published rate and its matched context and derive exactly what the reader can and cannot conclude from them when the labeled subset is a proper subset of the audited population. Where [1] frames the disclosure problem, this paper supplies the arithmetic that makes a specific disclosure — the missingness rate — load-bearing.

The reason labels are incomplete is treated in [2], which observes that most proposed algorithmic fairness techniques require access to data on a sensitive attribute or protected category such as race, ethnicity, gender, or sexuality in order to make performance comparisons across groups, and that this data is largely unavailable in practice, hindering the widespread adoption of algorithmic fairness; the paper considers calls to collect such data and characterizes the risks of doing so. Our analysis is complementary: rather than asking whether to collect more demographic data, we ask what an audit can honestly report given the collection level it already has. The supplied summary of [2] does not state quantitative results, so we connect to it only at the level of the collection-versus-disclosure trade-off.

The failure mode of auditing too few groups is documented in [6], which studies statistical fairness definitions that fix a small collection of pre-defined groups and ask for parity of some statistic across them, and shows such constraints are susceptible to intentional or inadvertent "fairness gerrymandering," in which a classifier appears fair on each individual group but violates fairness on a larger structured set of subgroups. This matters for our setting in a specific way: missingness rates are a property of groups, and if the audit's group partition is too coarse, the missingness it discloses for a coarse group can conceal heterogeneous missingness across the intersections that [6] shows are where violations hide. Our disclosure rule therefore applies per group, and Section 6 discusses the compositional limitation.

A structural analogy for our worst-case analysis comes from the Byzantine-resilience literature. [3] studies distributed optimization with $m$ worker machines of which $t$ may be corrupt and may collaboratively and arbitrarily deviate from their pre-specified programs, with a master node computing the model parameter vector for generalized linear models. [4] studies Byzantine-resilient SGD in a master-worker architecture over heterogeneous data with no probabilistic assumptions on data generation, using a polynomial-time outlier-filtering procedure for robust mean estimation. Both lines of work share the design pattern we adopt here: assume the worst admissible deviation — in our case, an arbitrary assignment of outcomes to unlabeled records — and derive guarantees that hold under it. The supplied summaries of [3] and [4] describe distributed optimization and SGD settings, not audit settings, so we use them only as methodological precedents for assumption-free worst-case reasoning, not as sources of audit-specific results.

Three further works appear in the surrounding corpus but connect only loosely. [5] uses H II starburst galaxy apparent magnitude versus redshift data from Siegel et al. (2005) to constrain dark energy cosmological model parameters, obtaining constraints generally consistent with other data sets but not as restrictive as the tightest available; the connection to our work is only the generic one of interval estimation from imperfect data, and the supplied summary supports nothing more specific. [7] proposes TerraGen, a unified multi-task layout generation framework for remote sensing data augmentation addressing task-isolated generative augmentation and unmodeled geographical and spatial constraints, and [8] proposes AeroGen, a diffusion-driven data generation method for remote sensing object detection motivated by labeled-data scarcity; both concern augmenting scarce labeled imagery, which parallels our setting only in the abstract sense that both fields face labeled-data scarcity, and neither summary supports any claim about fairness auditing. We cite them to mark the boundary of the related work rather than to draw on their results.

Finally, the epistemic framing of this paper draws on the ignorance-audit program. [11] describes the Universal Ignorance Audit, a fifteen-question, five-phase method for interrogating the structure of not-knowing in any domain, which treats ignorance as an active, structured state with architecture rather than an absence to be filled. [10] synthesizes three threads from one research organization's experience with AI-assisted research: the development of that fifteen-question Universal Ignorance Audit, two independent forensic analyses concluding that a flagship published paper was AI-generated, and epistemic lessons of the pipeline. [9] describes a falsifiability-first audit program applied to a cluster of physics claims (photon-primacy rest energies, helical-electron spin, adelic mass ratios on Bruhat–Tits trees); the supplied summary gives no further detail on its methods. We use these works for one methodological commitment that shapes the whole paper: a reported number should be published together with the structure of what is not known about it, and a claim should be stated so that it can fail. Our missingness interval is that commitment applied to fairness audit statistics. Beyond this framing role, the supplied summaries of [9], [10], and [11] support no quantitative claim used here.

## 3. Methods

### 3.1 Setting and notation

An audit covers a population of $N$ records partitioned into protected groups $g = 1, \dots, G$. For each record the audit observes an outcome $Y \in \{0, 1\}$ (for example, selected or not selected) and, for a subset, a group label. For group $g$, let $N_g$ be the number of records truly in group $g$, $n_g \le N_g$ the number with a usable label, and $k_g$ the number of labeled records with outcome $1$. Define:

$$m_g = 1 - \frac{n_g}{N_g} \qquad \text{(missingness rate of group } g\text{)},$$

$$\hat{r}_g = \frac{k_g}{n_g} \qquad \text{(labeled-subset outcome rate)}.$$

The quantity an oversight reader cares about is the full-population rate $r_g = (\text{number of outcome-}1\text{ records in group } g)/N_g$, which is unobservable when $m_g > 0$. We assume only that every labeled record is genuinely in group $g$ and that $0 \le \hat{r}_g \le 1$; no assumption is made about the mechanism generating missing labels. Group sizes $N_g$ are treated as known; Section 6 treats the case where they are only estimated.

### 3.2 Derivation target

We derive: (i) the exact interval of possible $r_g$ given $(\hat{r}_g, m_g)$; (ii) the induced interval on a two-group disparity $\Delta = r_1 - r_2$ and its width; (iii) a sufficient condition for a reported positive gap to remain positive under all missingness patterns; and (iv) the additional interval width contributed by finite-sample binomial error when labeled records are a random subsample of the labeled frame. All derivations are exact arithmetic on the definitions above; no simulation and no external data are used.

### 3.3 Disclosure specification under test

Following the matched-baseline structure of [1], we evaluate a candidate minimum disclosure set: for each published rate, the audit must report $\hat{r}_g$, $n_g$, $N_g$ (hence $m_g$), and the interval from (i). The test of the specification is whether a reader holding only the disclosed numbers can reproduce every bound in Section 4 without additional assumptions.

## 4. Analysis

### 4.1 Worst-case interval for a single group's rate

Given $\hat{r}_g = k_g / n_g$ and $N_g$, the number of outcome-1 records among the labeled is fixed at $k_g$. Among the $N_g - n_g$ unlabeled records, the count of outcome-1 records can be anything from $0$ to $N_g - n_g$: no assumption about missingness rules any of these out. Therefore:

$$r_g^{\min} = \frac{k_g}{N_g} = \frac{k_g}{n_g}\cdot\frac{n_g}{N_g} = \hat{r}_g (1 - m_g),$$

$$r_g^{\max} = \frac{k_g + (N_g - n_g)}{N_g} = \hat{r}_g(1-m_g) + m_g.$$

Every value in $[r_g^{\min}, r_g^{\max}]$ is attained by some assignment of outcomes to unlabeled records, so the interval is exact. Its width is:

$$r_g^{\max} - r_g^{\min} = m_g.$$

The width of what can be said about a group's rate equals the group's missingness rate, exactly, regardless of the rate itself. This is the first main result and the reason the missingness rate must appear in the report: it is not a data-quality footnote but the literal width of the reader's uncertainty.

### 4.2 Interval on a two-group disparity

Let $\Delta = r_1 - r_2$. Since $r_1 \in [\ell_1, u_1]$ and $r_2 \in [\ell_2, u_2]$ with $\ell_i = \hat{r}_i(1-m_i)$ and $u_i = \ell_i + m_i$, and the two groups' unlabeled assignments are independent of each other (any combination is admissible):

$$\Delta^{\min} = \ell_1 - u_2 = \hat{r}_1(1-m_1) - \hat{r}_2(1-m_2) - m_2,$$

$$\Delta^{\max} = u_1 - \ell_2 = \hat{r}_1(1-m_1) + m_1 - \hat{r}_2(1-m_2).$$

The width is:

$$\Delta^{\max} - \Delta^{\min} = m_1 + m_2.$$

**The width of the assumption-free interval on a disparity is the sum of the two groups' missingness rates, independent of the rates and of the reported gap.** This is the paper's central result.

Worked example. Take the numbers a plausible audit might publish: group A with $N_1 = 1000$, $n_1 = 400$, $k_1 = 100$; group B with $N_2 = 1000$, $n_2 = 500$, $k_2 = 75$. Then:

$$m_1 = 1 - \frac{400}{1000} = 0.6, \qquad m_2 = 1 - \frac{500}{1000} = 0.5,$$

$$\hat{r}_1 = \frac{100}{400} = 0.25, \qquad \hat{r}_2 = \frac{75}{500} = 0.15, \qquad \hat{g} = 0.25 - 0.15 = 0.10.$$

Bounds:

$$\ell_1 = 0.25 \times 0.4 = 0.10, \qquad u_1 = 0.10 + 0.6 = 0.70,$$

$$\ell_2 = 0.15 \times 0.5 = 0.075, \qquad u_2 = 0.075 + 0.5 = 0.575,$$

$$\Delta^{\min} = 0.10 - 0.575 = -0.475, \qquad \Delta^{\max} = 0.70 - 0.075 = 0.625.$$

Check of the width identity: $0.625 - (-0.475) = 1.100 = m_1 + m_2 = 0.6 + 0.5$. The reported ten-point gap against group B is compatible with any true gap from a $47.5$-point gap in B's favor to a $62.5$-point gap in A's favor. Under assumption-free scrutiny this audit's headline disparity carries no sign information whatsoever.

### 4.3 Sufficient condition for a surviving disparity claim

A reader who wants to affirm "group 1 is selected at a higher rate than group 2" needs $\Delta^{\min} > 0$. Two useful sufficient bounds follow. First, since $\hat{r}_i \le 1$ implies $\hat{r}_i(1-m_i) \ge \hat{r}_i - m_i$, and $u_2 = \hat{r}_2(1-m_2) + m_2 \le \hat{r}_2 + m_2$:

$$\Delta^{\min} \ge (\hat{r}_1 - m_1) - (\hat{r}_2 + m_2) = \hat{g} - (m_1 + m_2).$$

Hence:

$$\boxed{\ \hat{g} > m_1 + m_2 \ \Rightarrow\ \Delta^{\min} > 0\ }$$

is a sufficient condition, checkable by the reader from three disclosed numbers. Second, the exact necessary and sufficient condition is $\hat{r}_1(1-m_1) > \hat{r}_2(1-m_2) + m_2$, which the reader can also check directly; the $\hat{g} > m_1 + m_2$ form is the conservative shortcut.

For the Section 4.2 example, $\hat{g} = 0.10$ against $m_1 + m_2 = 1.10$: the shortcut condition fails by a factor of $11$, matching the exact finding that the claim does not survive.

### 4.4 Adding finite-sample error

When the labeled subset is itself a finite sample, $\hat{r}_g$ carries binomial sampling error. With $n_g$ labeled records and rate $\hat{r}_g$, the standard error is:

$$\mathrm{SE}_g = \sqrt{\frac{\hat{r}_g(1-\hat{r}_g)}{n_g}},$$

and a two-sided $95\%$ normal interval contributes $\pm 1.96\,\mathrm{SE}_g$ per group. For a disparity, the two groups' sampling errors add in half-width (a conservative combination; exact intervals are slightly narrower):

$$w_{\text{samp}} \approx 1.96\,(\mathrm{SE}_1 + \mathrm{SE}_2).$$

Informative-regime example. Suppose the same audit structure but with near-complete labels: $N_1 = N_2 = 1000$, $n_1 = n_2 = 980$ (so $m_1 = m_2 = 0.02$), $\hat{r}_1 = 0.30$ ($k_1 = 294$), $\hat{r}_2 = 0.20$ ($k_2 = 196$), $\hat{g} = 0.10$. Then:

$$\mathrm{SE}_1 = \sqrt{\frac{0.30 \times 0.70}{980}} = \sqrt{\frac{0.21}{980}} = \sqrt{2.1429\times 10^{-4}} = 0.014638,$$

$$\mathrm{SE}_2 = \sqrt{\frac{0.20 \times 0.80}{980}} = \sqrt{\frac{0.16}{980}} = \sqrt{1.6327\times 10^{-4}} = 0.012778,$$

$$w_{\text{samp}} \approx 1.96 \times (0.014638 + 0.012778) = 1.96 \times 0.027416 = 0.053735.$$

Missingness contributes $m_1 + m_2 = 0.04$ of interval width. The exact assumption-free lower bound on the gap is:

$$\Delta^{\min} = 0.30 \times 0.98 - (0.20 \times 0.98 + 0.02) = 0.294 - 0.216 = 0.078.$$

Subtracting the sampling half-widths from each side, the reader's conservative lower bound on the disparity is:

$$0.078 - 0.053735 = 0.024265 > 0.$$

So in the low-missingness regime the disparity claim survives with a stated margin of about $0.024$, and the dominant uncertainty contribution is now sampling error ($0.054$ in half-width) rather than missingness ($0.04$ in width). The crossover between the two regimes is set by the ratio $(m_1 + m_2) / w_{\text{samp}}$: missingness dominates whenever the sum of missingness rates exceeds roughly $1.96(\mathrm{SE}_1 + \mathrm{SE}_2)$.

### 4.5 Cost of the conservative shortcut

The shortcut $\hat{g} > m_1 + m_2$ can fail while the exact condition holds. Example: $\hat{r}_1 = 0.90$, $m_1 = 0.5$, $\hat{r}_2 = 0.10$, $m_2 = 0.2$. Shortcut: $\hat{g} = 0.80$ versus $m_1 + m_2 = 0.7$ — passes. Counter-example where it fails but the exact condition holds: $\hat{r}_1 = 0.60$, $m_1 = 0.5$, $\hat{r}_2 = 0.02$, $m_2 = 0.05$. Then $\hat{g} = 0.58 < 0.55$? No: $0.58 > 0.55$, passes. Take $\hat{r}_1 = 0.50$, $m_1 = 0.5$, $\hat{r}_2 = 0.01$, $m_2 = 0.02$: $\hat{g} = 0.49 < 0.52$, shortcut fails; exact condition: $\ell_1 = 0.25$, $u_2 = 0.01 \times 0.98 + 0.02 = 0.0298$, and $0.25 > 0.0298$, so the claim survives exactly. The shortcut is therefore sufficient but not necessary, and audits with very low $\hat{r}_2$ should report the exact bound $\ell_1 - u_2$ alongside it.

## 5. Results

All numbers below are computed in Section 4; none are measured or simulated.

**R1 (single-group interval, Section 4.1).** Given a labeled-subset rate $\hat{r}_g$ and missingness $m_g$, the full-population rate lies exactly in $[\hat{r}_g(1-m_g),\ \hat{r}_g(1-m_g) + m_g]$, an interval of width exactly $m_g$. Example: $\hat{r} = 0.25$, $m = 0.6$ gives $[0.10,\ 0.70]$.

**R2 (disparity interval width, Section 4.2).** The assumption-free interval on a two-group disparity has width exactly $m_1 + m_2$, independent of the rates. Worked case: reported gap $0.10$ with $m_1 = 0.6$, $m_2 = 0.5$ yields the interval $[-0.475,\ 0.625]$, width $1.100$.

**R3 (survival rule, Section 4.3).** A sufficient condition for a reported positive gap to remain positive under all missingness patterns is $\hat{g} > m_1 + m_2$; the exact condition is $\hat{r}_1(1-m_1) > \hat{r}_2(1-m_2) + m_2$. In the Section 4.2 example the condition fails ($0.10 \le 1.10$) and the claim is unfalsifiable in the reader's favor.

**R4 (informative regime, Section 4.4).** With $m_1 = m_2 = 0.02$, $n_1 = n_2 = 980$, $\hat{r}_1 = 0.30$, $\hat{r}_2 = 0.20$: the assumption-free gap lower bound is $0.078$; binomial sampling adds a conservative half-width of approximately $0.053735$; the reader's final conservative lower bound on the disparity is $0.024265 > 0$. Missingness width ($0.04$) and sampling half-width ($0.054$) are of comparable size in this regime.

**R5 (disclosure set, Sections 3.3 and 4).** The minimum disclosure set $\{\hat{r}_g, n_g, N_g, m_g\}$ per published rate is sufficient for a reader to reproduce R1–R3 with no additional assumptions; the shortcut of R3 requires only $\hat{r}_1, \hat{r}_2, m_1, m_2$.

## 6. Discussion

The results are exact given the model, and their limitations are the model's. The most important limitation is that the assumption-free interval is often wide enough to be uninformative: R2 shows that whenever $m_1 + m_2$ exceeds the disparity scale anyone cares about, the audit cannot support any sign claim about the gap, and R3 makes that threshold explicit. An audit designer may respond by weakening the assumption set — for example, assuming missingness is independent of the outcome within group — which would shrink the interval substantially, but every such assumption is precisely what an adversarial or self-selection missingness process violates, and the paper deliberately does not quantify intervals under those assumptions because doing so would require data on the missing mechanism that the audit does not have. That is a real cost of the approach, not an oversight.

A second limitation is the assumption that group sizes $N_g$ are known. If the audit knows only an estimate $\hat{N}_g$ with uncertainty, the intervals of R1 widen further, and the clean width identity $m_1 + m_2$ no longer holds exactly; the identity survives only as an approximation when $N_g$ uncertainty is small relative to $m_g$. The paper does not derive the $N_g$-uncertain variant.

A third limitation is compositional, inherited from the subgroup critique in [6]: missingness is disclosed per group in the audit's chosen partition, but if missingness varies across intersections within a group, the group-level $m_g$ understates the uncertainty relevant to intersection-level claims. The bounds of R1 remain valid for the group as defined — they are bounds on the group's aggregate rate — but a reader must not transfer them to subgroups the audit did not report.

Failure modes of the disclosure rule itself: an audit could comply formally by reporting $m_g$ while choosing a group partition that hides high-missingness intersections; a reader could misread the sufficient shortcut of R3 as necessary and wrongly reject claims like the Section 4.5 counter-example; and a low-missingness audit could over-claim because R4's sampling treatment is