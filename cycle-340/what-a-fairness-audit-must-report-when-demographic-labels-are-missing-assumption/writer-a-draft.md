# What a Fairness Audit Must Report When Demographic Labels Are Missing: Assumption‑Free Disparity Intervals, a Determinacy Rule, and a Disclosure Checklist

## Abstract

Fairness audits of machine‑learning systems publish group‑level rates such as selection rates, but the protected labels those rates depend on are frequently missing for a substantial fraction of the audited population, and no settled rule says what the audit must disclose in that case. The gap is practical: an oversight reader who sees a rate computed only on labeled records cannot tell from the published numbers alone whether the rate would survive, shrink, or reverse if the unlabeled records were labeled. We close the gap with an assumption‑free worst‑case analysis. For any published rate we derive the exact interval $[\hat{p}(1-m),\ \hat{p}(1-m)+m]$ containing the full‑population rate under any pattern of missingness, where $\hat{p}$ is the labeled‑subset rate and $m$ the missing‑label fraction; the interval width equals $m$ exactly. For a two‑group disparity the assumption‑free interval has width $m_{1}+m_{2}$, independent of the rates: a reported gap of $0.10$ with missingness rates $0.6$ and $0.5$ is compatible with any true gap in $[-0.475,\ 0.625]$. We derive a determinacy rule—certification of a threshold $\delta_{\min}$ is impossible exactly when the shifted threshold $\delta_{\min}+p_{B}$ lies inside $[p_{\min,A},\,p_{\max,A}]$, while $m<\delta_{\min}$ guarantees that some certification is possible whatever the point estimate—and instantiate it: with $m=0.2$, an observed rate of $0.30$ against a fully labeled comparison rate of $0.35$ gives a four‑fifths ratio interval $[0.686,\ 1.257]$, so compliance cannot be certified even though the point estimate $0.857$ suggests it, and $134$ labels must be recovered to change that. The framework converts incomplete labels from an unstated caveat into a computed, reportable quantity with a concrete remediation target.

## 1. Introduction

Fairness audits are a key component of responsible machine‑learning deployment [1], and their basic currency is the group‑level rate: a selection rate, a false‑positive rate, a referral rate, computed per protected group and compared across groups. Producing those rates requires knowing, for each person in the audited population, which group they belong to. In operational data that knowledge is routinely incomplete: the data needed to compute these rates is largely unavailable in practice, which hinders the adoption of algorithmic fairness, and collecting it carries risks that the literature characterizes [2]; a substantial fraction of audited records therefore carries no usable group label. The audit then publishes a rate whose denominator is silently the labeled subset, and the reader has no way to know how much of the population the published number actually describes.

The cost of this gap is concrete. An oversight reader who sees “group A is selected at 25 %”, “group B at 15 %” cannot currently tell from the report whether that ten‑point gap would survive, shrink, or reverse if the unlabeled records were labeled. The reader therefore faces a decision—accept the audit, demand remediation, or halt deployment—with a number whose evidentiary value is unquantified. A system can pass an audit on labeled records while its behavior on unlabeled records is materially different, and no published number flags the possibility. Conversely, a model that appears unfair under the observed data may be acceptable once the missing‑label uncertainty is accounted for.

What would change if the gap were closed? The oversight reader would see, next to every published rate, an interval stating how far the true rate could deviate given the missing labels, together with a determinacy verdict: either the audit certifies that the disparity is (or is not) larger than a stated threshold of concern, or it reports that the missing labels make certification impossible and states how many labels would have to be recovered to change that. Audit teams would get a design rule—a minimum labeled fraction—before deployment rather than a discovery of indeterminacy after it.

This paper builds that disclosure rule from first principles, and its stance is deliberately conservative. We make no assumption about the mechanism that causes labels to be missing—neither missing‑at‑random nor ignorable nor adversarial—because in the audit setting the missingness may be precisely what an adversarial or negligent process produces. Instead we compute worst‑case bounds over all assignments of the unlabeled records; the bounds depend only on two numbers the audit already has, the labeled fraction and the observed rate among labeled records. The worst case is tight, so the intervals we report are the narrowest any assumption‑free method can give; any narrower interval smuggles in an assumption about missingness that the audit must then state and defend. The price of this conservatism is width, and a second contribution is to quantify that price so an audit designer can decide when assumption‑free reporting is informative and when it is not.

Our contributions are:

- An exact worst‑case interval $[\hat{r}_{g}(1-m_{g}),\ \hat{r}_{g}(1-m_{g})+m_{g}]$ containing any group’s full‑population rate given its labeled‑subset rate $\hat{r}_{g}$ and missingness rate $m_{g}$, with width exactly $m_{g}$ (Section 4.1).  
- The result that the width of the assumption‑free interval on a two‑group disparity equals $m_{1}+m_{2}$, independent of the rates (Section 4.2), with the worked example $[-0.475,\ 0.625]$ for a reported gap of $0.10$.  
- A determinacy rule—certification of a threshold $\delta_{\min}$ is impossible exactly when $\delta_{\min}+p_{B}$ lies inside $[p_{\min,A},\,p_{\max,A}]$, with $m<\delta_{\min}$ sufficient for some certification whatever the point estimate—and a reported positive gap surviving scrutiny if $\hat{g}>m_{1}+m_{2}$ (Section 4.3), together with a counter‑example showing the shortcut is not necessary (Section 4.4).  
- A worked numerical audit in the mixed‑completeness case: for $n=1000$, $k=800$, $\hat{p}_{A}=0.30$ against a fully labeled comparison rate of $0.35$, the rate interval is $[0.24,\ 0.44]$, the four‑fifths ratio interval is $[0.686,\ 1.257]$, the verdict is indeterminate, and the label‑recovery target is $134$ labels (Section 4.5).  
- A combined treatment of missingness and finite‑sample binomial error, showing that at near‑complete labeling ($m_{1}=m_{2}=0.02$, $n_{g}=980$) sampling contributes a half‑width of approximately $0.0542$ against $0.04$ of missingness width, and that at $m=0.2$ missingness contributes roughly $7$ times more uncertainty than sampling (Section 4.6).  
- A disclosure checklist specifying the minimum set of numbers an audit must publish when labels are incomplete (Section 5) and a discussion of practical implications (Section 7).

## 2. Background and Related Work

The starting point for this paper is [1], which asks what a fairness audit must disclose when the protected labels it depends on are incomplete, and focuses on the rates an audit publishes and on what an oversight reader needs beside them; its approach pairs every published rate with a matched baseline drawn from the same audit. Our work formalizes one part of that program: we take the published rate and its matched context and derive exactly what the reader can and cannot conclude from them when the labeled subset is a proper subset of the audited population. Where [1] frames the disclosure problem, this paper supplies the arithmetic that makes a specific disclosure—the missingness rate—load‑bearing.

The reason labels are incomplete is treated in [2], whose excerpt states that most algorithmic fairness techniques require access to a sensitive attribute such as race, ethnicity, gender, or sexuality, that such data is largely unavailable in practice, and that this unavailability hinders the widespread adoption of algorithmic fairness. Our analysis is complementary: rather than asking whether to collect more demographic data, we ask what an audit can honestly report given the collection level it already has.

The failure mode of auditing too few groups is documented in [6], which studies statistical fairness definitions that fix a small collection of pre‑defined groups and ask for parity of some statistic across them, and shows that such constraints are susceptible to “fairness gerrymandering,” where a classifier appears fair on each individual group but violates fairness on a larger structured set of subgroups. This matters for our setting because missingness rates are a property of groups, and if the audit’s group partition is too coarse the missingness it discloses for a coarse group can conceal heterogeneous missingness across intersections where [6] shows violations hide. Moreover, widening the group structure multiplies the number of rates, and each additional rate on a smaller subgroup has a larger effective missing‑label fraction, so our interval widths grow exactly where gerrymandering risk is highest. The disclosure rule therefore applies per group, and Section 6 discusses the compositional limitation.

A structural analogy for our worst‑case analysis comes from the Byzantine‑resilience literature. [3] studies distributed optimization with $m$ worker machines of which $t$ may be corrupt and may arbitrarily deviate from their pre‑specified programs, while [4] studies Byzantine‑resilient SGD in a master‑worker architecture with no probabilistic assumptions on data generation. Both adopt the design pattern we use: assume the worst admissible deviation—in our case an arbitrary assignment of outcomes and group memberships to unlabeled records—and derive guarantees that hold under it.

Two remote‑sensing papers mark the boundary of the related work. [7] proposes TerraGen, a unified multi‑task layout generation framework for remote‑sensing data augmentation, and [8] proposes AeroGen, a diffusion‑driven data generation method for remote‑sensing object detection. Both respond to label scarcity by synthesizing labeled data; our setting forbids that response because a synthesized protected label is precisely the unquantified inference an audit cannot silently rely on. The contrast is instructive: where the task permits generative fill‑in, scarcity is an engineering problem; where the label is protected and audited, scarcity is an epistemic limit that must be disclosed. Neither summary supports any claim about fairness auditing, so we cite [7] and [8] only for this contrast.

A distant but clarifying example of inference under data limitations outside machine learning is [5], which constrains dark‑energy cosmological model parameters using H II starburst galaxy apparent‑magnitude versus redshift data and reports constraints that are generally consistent with other datasets but not as restrictive as the tightest available. The pattern—a data‑limited analysis that is honest about being less restrictive than the best achievable—is the reporting posture we formalize: an audit under missingness should publish its bound and state plainly that it is less restrictive than a complete‑label audit would be.

Finally, three entries inform the epistemic framing. [11] describes the Universal Ignorance Audit, a fifteen‑question, five‑phase method for interrogating the structure of not‑knowing in any domain, treating ignorance as an active, structured state. [10] synthesizes three threads from one research organization’s experience with AI‑assisted research, including the development of the Universal Ignorance Audit and lessons about falsifiability‑first audit programs. [9] describes a falsifiability‑first audit program applied to a cluster of physics claims. We use these works for one methodological commitment that shapes the whole paper: a reported number should be published together with the structure of what is not known about it, and a claim should be stated so that it can fail. Our missingness interval and determinacy rule are that commitment applied to fairness‑audit statistics.

Across these works, no entry in the supplied bibliography computes a certifiability threshold for group rates under label missingness; that computation is the contribution of Sections 3 through 5.

## 3. Methods

### 3.1 Setting and notation

An audit covers a population of $n$ records partitioned into protected groups $g=1,\dots,G$; the two‑group case carries the derivations and the extension to more groups is by repetition. Each record has an outcome $Y\in\{0,1\}$ used by the audit (e.g., selected or not selected) and, in principle, a group label. For group $g$, let $N_{g}$ be the number of records truly in group $g$, $n_{g}\le N_{g}$ the number with a usable label, and $k_{g}$ the number of labeled records with outcome $1$. Define

$$
m_{g}=1-\frac{n_{g}}{N_{g}}\qquad\text{(missingness rate of group }g\text{)},
$$

$$
\hat{r}_{g}=\frac{k_{g}}{n_{g}}\qquad\text{(labeled‑subset outcome rate)}.
$$

The quantity an oversight reader cares about is the full‑population rate $r_{g}$, the rate that would be observed if every record carried its true label. Records without a label still have a true group membership and a true outcome; only the audit’s knowledge is missing. We assume only that every labeled record is genuinely in group $g$ and that $0\le\hat{r}_{g}\le1$; no assumption is made about the mechanism generating missing labels.

Two knowledge regimes are treated. In the **known‑group‑size regime** (Section 4.1), the audit knows $N_{g}$ for each group, so $m_{g}$ is computable per group. In the **pooled regime** (Section 4.5), the audit knows only the total population $n$, the total labeled count $k$, and the overall missing fraction $m=1-k/n$; the group membership of the unlabeled records is itself unknown. The pooled regime is the weaker‑knowledge case and is the one used for the four‑fifths worked example.

### 3.2 The worst‑case missingness model

We assume nothing about which records are unlabeled or why. Formally, the audit’s knowledge is a set of admissible assignments of the unlabeled records to groups and outcome configurations, and we take the worst case over all of them. This is the same posture as the Byzantine model of [3] and [4]: the untrusted component (unlabeled records; corrupt workers) is given arbitrary power, and the guarantee is whatever survives that power. The guarantee is then an interval, not a point. The worst case is tight: for any narrower interval, an admissible assignment exists that pushes the true rate outside it, so any narrower interval presupposes a missingness model that the audit must state and defend.

### 3.3 What the audit publishes

Under our framework, an audit with incomplete labels publishes, for each group rate:

1. the point estimate $\hat{r}_{g}$ on labeled records,  
2. the missing‑label fraction ($m_{g}$ in the known‑group‑size regime, $m$ in the pooled regime),  
3. the worst‑case interval $[r_{\min,g},\,r_{\max,g}]$ derived in Section 4.1,  
4. a determinacy verdict for each disparity threshold $\delta_{\min}$ of interest (Section 4.3), and  
5. the minimum number of labels to recover, $\Delta k$, that would make the verdict determinate (Section 4.5).

Items 1 and 2 are already computable from any audit’s own data, which is what makes the framework deployable without new measurement infrastructure; items 3 through 5 are closed‑form computations on the same counts and are the additions this paper derives.

### 3.4 Comparison baselines and the four‑fifths rule

We use a ratio threshold of $0.8$ (the four‑fifths threshold) as a stated example; the derivations hold for any threshold $\rho_{\min}$, and the difference‑form determinacy rule of Section 4.3 holds for any policy‑set threshold $\delta_{\min}$. We analyze the ratio of two group rates under missingness in one group and completeness in the other, because that mixed case is the common one and it exhibits the mechanism most cleanly.

### 3.5 Sampling error

The worst‑case interval covers missingness only. Labeled records are a finite sample, so $\hat{r}_{g}$ also carries binomial sampling error with standard error $\mathrm{SE}_{g}=\sqrt{\hat{r}_{g}(1-\hat{r}_{g})/n_{g}}$. We combine the two sources by adding the $95\%$ half‑width $1.96\,\mathrm{SE}_{g}$ (with $z_{0.975}=1.96$) to the missingness width, in Section 4.6. For a two‑group disparity the two groups’ sampling half‑widths are added, a conservative combination; the two uncertainties are not independent in general, and we state the combination as an approximation, not an exact convolution.

## 4. Analysis

All derivations in this section are exact arithmetic on the definitions of Section 3; no simulation and no external data are used. Every input number is stated where it is used.

### 4.1 Worst‑case interval for a single group’s rate (known group size)

Given $\hat{r}_{g}=k_{g}/n_{g}$ and known $N_{g}$, the number of outcome‑1 records among the labeled is fixed at $k_{g}$. Among the $N_{g}-n_{g}$ unlabeled records of group $g$, the count of outcome‑1 records can be anything from $0$ to $N_{g}-n_{g}$: no assumption about missingness rules any of these out. Therefore

$$
r_{g}^{\min}=\frac{k_{g}}{N_{g}}=\frac{k_{g}}{n_{g}}\cdot\frac{n_{g}}{N_{g}}=\hat{r}_{g}(1-m_{g}),
$$

$$
r_{g}^{\max}=\frac{k_{g}+(N_{g}-n_{g})}{N_{g}}=\hat{r}_{g}(1-m_{g})+m_{g}.
$$

Every value in $[r_{g}^{\min},\,r_{g}^{\max}]$ is attained by some assignment of outcomes to unlabeled records, so the interval is exact. Its width is

$$
r_{g}^{\max}-r_{g}^{\min}=m_{g}.
$$

Thus the width of what can be said about a group’s rate equals the group’s missingness rate, exactly, regardless of the rate itself.

### 4.2 Interval on a two‑group disparity

Let $\Delta=r_{1}-r_{2}$. Since $r_{1}\in[\ell_{1},u_{1}]$ and $r_{2}\in[\ell_{2},u_{2}]$ with $\ell_{i}=\hat{r}_{i}(1-m_{i})$ and $u_{i}=\ell_{i}+m_{i}$, and the two groups’ unlabeled assignments are independent (any combination is admissible),

$$
\Delta^{\min}=\ell_{1}-u_{2}=\hat{r}_{1}(1-m_{1})-\hat{r}_{2}(1-m_{2})-m_{2},
$$

$$
\Delta^{\max}=u_{1}-\ell_{2}=\hat{r}_{1}(1-m_{1})+m_{1}-\hat{r}_{2}(1-m_{2}).
$$

The width is

$$
\Delta^{\max}-\Delta^{\min}=m_{1}+m_{2}.
$$

**The width of the assumption‑free interval on a disparity is the sum of the two groups’ missingness rates, independent of the rates and of the reported gap.** This is the paper’s central result.

**Worked example.** Take a plausible audit: group A with $N_{1}=1000$, $n_{1}=400$, $k_{1}=100$; group B with $N_{2}=1000$, $n_{2}=500$, $k_{2}=75$. Then

$$
m_{1}=1-\frac{400}{1000}=0.6,\qquad m_{2}=1-\frac{500}{1000}=0.5,
$$

$$
\hat{r}_{1}=\frac{100}{400}=0.25,\qquad \hat{r}_{2}=\frac{75}{500}=0.15,\qquad \hat{g}=0.10.
$$

Bounds:

$$
\ell_{1}=0.25\times0.4=0.10,\qquad u_{1}=0.10+0.6=0.70,
$$

$$
\ell_{2}=0.15\times0.5=0.075,\qquad u_{2}=0.075+0.5=0.575,
$$

$$
\Delta^{\min}=0.10-0.575=-0.475,\qquad \Delta^{\max}=0.70-0.075=0.625.
$$

Check of the width identity:

$$
0.625-(-0.475)=1.100=m_{1}+m_{2}=0.6+0.5.
$$

The reported ten‑point gap is compatible with any true gap from a $47.5$‑point gap in B’s favor to a $62.5$‑point gap in A’s favor. Under assumption‑free scrutiny this audit’s headline disparity carries no sign information whatsoever.

### 4.3 The determinacy rule

A reader who wants to affirm “group 1 is selected at a higher rate than group 2” needs $\Delta^{\min}>0$. Since $\hat{r}_{i}\le1$ implies $\hat{r}_{i}(1-m_{i})\ge\hat{r}_{i}-m_{i}$, and $u_{2}=\hat{r}_{2}(1-m_{2})+m_{2}\le\hat{r}_{2}+m_{2}$,

$$
\Delta^{\min}\ge(\hat{r}_{1}-m_{1})-(\hat{r}_{2}+m_{2})=\hat{g}-(m_{1}+m_{2}).
$$

Hence

$$
\hat{g}>m_{1}+m_{2}\ \Rightarrow\ \Delta^{\min}>0,
$$

a sufficient condition checkable by the reader from three disclosed numbers. The exact necessary and sufficient condition is $\hat{r}_{1}(1-m_{1})>\hat{r}_{2}(1-m_{2})+m_{2}$, which the reader can also check directly; the $\hat{g}>m_{1}+m_{2}$ form is the conservative shortcut.

For a policy‑set threshold $\delta_{\min}$ (the smallest disparity that would trigger action) and a fully labeled comparison group B with known rate $p_{B}$, the disparity $D=p_{A}-p_{B}$ is bounded by $D_{\min}=p_{\min,A}-p_{B}$ and $D_{\max}=p_{\max,A}-p_{B}$. Certification of “no actionable disparity” is possible only if $D_{\max}<\delta_{\min}$, and certification of “actionable disparity present” only if $D_{\min}>\delta_{\min}$. Since $p_{\max,A}-p_{\min,A}=m$, if $m<\delta_{\min}$ then the interval width is smaller than the threshold and at least one of the two certifications is possible whatever the point estimate. This condition is sufficient, not necessary: the exact condition for at least one certification is that $\delta_{\min}+p_{B}$ lies outside $[p_{\min,A},\,p_{\max,A}]$, which can hold even when $m\ge\delta_{\min}$ (e.g., $p_{\min,A}\ge\delta_{\min}+p_{B}$ certifies compliance at any $m$).

### 4.4 The shortcut is sufficient but not necessary

The condition $\hat{g}>m_{1}+m_{2}$ is conservative: it can fail while the exact condition $\hat{r}_{1}(1-m_{1})>\hat{r}_{2}(1-m_{2})+m_{2}$ holds, because the shortcut bounds $\hat{r}_{i}(1-m_{i})$ by $\hat{r}_{i}-m_{i}$, and that bound is loose whenever $\hat{r}_{i}<1$. A counter‑example shows the gap is real. Take group 1 with $\hat{r}_{1}=0.8$, $m_{1}=0.2$, and group 2 with $\hat{r}_{2}=0.2$, $m_{2}=0.5$. Then

$$
\ell_{1}=0.8\times0.8=0.64,\qquad u_{2}=0.2\times0.5+0.5=0.6,
$$

$$
\Delta^{\min}=0.64-0.6=0.04>0.
$$

The shortcut quantity is $\hat{g}=0.6$ against $m_{1}+m_{2}=0.7$, so the shortcut fails. The exact condition $0.64>0.6$ holds. The moral is that the shortcut should be published as a fast screening test that can produce false negatives for determinacy, never as the verdict itself; the exact condition $\hat{r}_{1}(1-m_{1})>\hat{r}_{2}(1-m_{2})+m_{2}$ is equally checkable by the reader from the same disclosed numbers and should be the computed verdict.

### 4.5 Worked numerical audit in the pooled regime

The pooled regime of Section 3.1 is the weaker‑knowledge case and the one an oversight reader most often faces, because many audits disclose population and labeled counts but not per‑group population counts. The inputs, all stated here, are: total population $n=1000$; total labeled records $k=800$, so the overall missing fraction is

$$
m=1-\frac{800}{1000}=0.2.
$$

A labeled‑subset rate for group A of $\hat{p}_{A}=0.30$ (i.e., $k_{A}=240$ of the $800$ labeled records are outcome‑1 and belong to group A); and a fully labeled comparison rate for group B of $p_{B}=0.35$, known exactly because group B’s labeling is complete in this scenario.

**Rate interval.** Applying the construction of Section 4.1 with the pooled missing fraction,

$$
p_{\min,A}=\hat{p}_{A}(1-m)=0.30\times0.8=0.24,
$$

$$
p_{\max,A}=p_{\min,A}+m=0.24+0.2=0.44.
$$

The interval width is $m=0.2$, exactly as derived.

**Four‑fifths ratio interval.** The ratio $R=p_{A}/p_{B}$ is monotone in $p_{A}$ because $p_{B}>0$ is fixed, so the interval endpoints are the ratios of the rate endpoints:

$$
R_{\min}=\frac{0.24}{0.35}=0.68571\ldots\approx0.686,\qquad
R_{\max}=\frac{0.44}{0.35}=1.25714\ldots\approx1.257.
$$

The point estimate is $\hat{R}=0.30/0.35=0.85714\ldots\approx0.857$, which sits above the four‑fifths threshold $0.8$ and would suggest compliance if read alone. But $0.8\in[0.686,\ 1.257]$: the threshold lies inside the assumption‑free interval, so the audit cannot certify either compliance or adverse impact. The verdict is **indeterminate**, and the point estimate $0.857$ carries no certifiable content.

**Label‑recovery target.** How many labels must be recovered before a determinate verdict becomes possible? Two answers exist.

*Worst‑case answer: no finite number.* Under the fully adversarial model, the outcomes of unlabeled records are unknown, and recovering $\Delta k$ labels converts those particular unknowns into observations—but before recovery the audit must reason about what recovery might reveal. If the recovered labels could all be outcome 1, the worst‑case upper bound stays at $p_{\max,A}=0.44$; if they could all be outcome 0, the worst‑case lower bound stays at $p_{\min,A}=0.24$. Certifying compliance requires $p_{\min,A}\ge0.8\times0.35=0.28$, and $0.24<0.28$ regardless of $\Delta k$; certifying adverse impact requires $p_{\max,A}<0.28$, and $0.44>0.28$ regardless of $\Delta k$. Thus under the assumption‑free