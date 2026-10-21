# The Silent Radix Is Not a Key: A Security Analysis of Unknown‑Radix Encoding as a Cryptographic Primitive

## Abstract

Positional numerals do not internally specify their own base, and a recent informal proposal—Silent Radix Encryption (SRE)—conjectures that this “silent radix” can serve as a cryptographic secret. No formal security analysis of this construction exists. We formalize the encoding core, define its key space over admissible radices $B\in[2,2^{16}]$ and digit maps on a 26‑symbol alphabet, and compute its entropy as $104.38$ bits. We then show that the construction reduces to a monoalphabetic substitution cipher with base‑dependent segmentation, and we derive a two‑stage ciphertext‑only attack: a histogram test recovers $B$ at a cost of at most $6.5535\times10^{7}$ digit operations for a 1000‑symbol ciphertext, after which standard frequency analysis applies within a unicity distance of $149.1$ symbols, computed from the key entropy and an assumed language redundancy of $0.70$ bits/symbol. Brute‑force over the full key space at $10^{9}$ keys/s would take $8.36\times10^{14}$ years, yet the structural attack succeeds on a single short message, making key‑space size irrelevant. We conclude that radix obscurity offers no security advantage over classical substitution ciphers and therefore no quantum‑relevant advantage, and we state the conditions under which this negative result would be falsified.

## 1. Introduction

A recurring failure mode in cryptographic engineering is the deployment of primitives whose security rests on the secrecy of a design parameter rather than on the secrecy of a key under a public, well‑scrutinized algorithm. Security architects performing cryptographic migration and inventory work face this problem concretely: the Cryptographic Bill of Materials (CBOM) methodology exists precisely because organizations must decide which deployed mechanisms to trust and which to retire as algorithms are deprecated and post‑quantum readiness is planned [5]. If a mechanism such as unknown‑radix encoding were believed to be a viable lightweight cipher or key‑encapsulation trapdoor, it could enter that inventory as a candidate; if it is in fact breakable by classical statistical attacks on a single ciphertext, it must be excluded before it is ever deployed. Today no formal analysis exists that lets an architect, a standards body, or a protocol designer make that decision with confidence: the proposal circulates as an informal conjecture that a secret base $B$—the observation that a positional numeral cannot specify its own base—could act as a cryptographic trapdoor [10].

The stakes are concrete. An organization that adopted such a scheme for key encapsulation would believe its encapsulated keys were protected by a large key space—over $2^{100}$ combinations of radix and digit map in the parameterization analyzed here—and might further believe that a scheme built from integer arithmetic rather than from structured lattices or block ciphers resists quantum attack by being “unusual.” This paper shows that both beliefs are wrong: the entire key space collapses under a statistical test that costs less than $10^{8}$ elementary operations, and the residual problem is a monoalphabetic substitution cipher, a primitive broken by classical statistical means long before the era of digital computers. The decision that changes if this result holds is simple: unknown‑radix encoding is classified as obfuscation, not encryption, and is excluded from cryptographic inventories and migration plans at the same tier as encoding tricks, with no post‑quantum consideration owed to it.

We analyze the scheme named Silent Radix Encryption in the source literature [10], which states that SRE uses a secret base $b$ as a trapdoor for key encapsulation and that its security reduces to an unknown‑weight integer knapsack problem. We analyze the core encoding primitive directly and show that the knapsack reduction, even if correct, does not confer security, because the encoding admits a direct statistical attack that bypasses the knapsack structure entirely.

**Contributions.**
- A formal definition of the unknown‑radix encoding scheme, its key space (admissible radices $B\in[2,B_{\max}]$ and digit maps over an $m$‑symbol alphabet), and the computation of its entropy: $104.38$ bits for $m=26$, $B_{\max}=2^{16}$ (Sections 3 and 4.1).
- A reduction showing that decryption under a known radix is exactly a monoalphabetic substitution with base‑dependent segmentation, and a derivation of the unicity distance $n_{0}=149.1$ symbols for the full key space (Sections 4.2 and 4.3).
- An explicit two‑stage ciphertext‑only attack with full arithmetic: radix recovery by histogram discrimination at a cost of at most $6.5535\times10^{7}$ digit operations for $n=1000$, followed by frequency analysis of the residual substitution (Section 4.4).
- A comparison against brute‑force benchmarks showing that the key‑space entropy of $104.38$ bits is structurally irrelevant: the binding constraint is the unicity distance, not the key count (Sections 4.5 and 5).
- A statement of the negative result for quantum relevance—a scheme broken classically on a single ciphertext cannot offer a quantum‑relevant advantage—together with falsification conditions and the limits of the analysis (Section 6).

## 2. Background and Related Work

The immediate ancestor of this work is the silent‑radix proposal itself. The QNFO note on Silent‑Radix Cryptography states the core observation—that a positional numeral cannot internally specify its own base, so the base is “silent”—and proposes Silent Radix Encryption (SRE), which uses a secret base $b$ as a trapdoor for key encapsulation and claims that security reduces to an unknown‑weight integer knapsack problem [10]. A companion QNFO note connects the silent‑radix principle to factoring and adelic complexity [9]; the summary supplied for that entry is empty, so we do not rely on it. A third QNFO note, HM‑LWE v3.0, proposes hidden‑modulus LWE as a novel hardness assumption [11]; the supplied summary states only that title‑level claim, so we cite it solely as evidence that novel hardness assumptions of this family are being proposed and require exactly the kind of adversarial analysis this paper performs for the radix case.

The broader literature supplies the evaluation standards against which any new primitive must be judged. Kerckhoffs’s principle— the system must remain secure even if everything about it except the key is public— is operationalized in modern formal methods: the first formal model of Bitcoin’s Payment Protocol (BIP70) formalised the previously shown refund‑attack vulnerability arising from lack of authentication of refund addresses [4]. That work is the template we follow: an informal belief about a protocol’s security is converted into a formal model, and the model is then attacked. Our Section 3 formalization and Section 4 attack play the same role for unknown‑radix encoding that the formal model and refund‑attack analysis played for BIP70.

On the constructive side, the literature shows what real key‑establishment machinery looks like, and thereby sharpens the comparison in Section 4.5. The Multi‑Factor Key Derivation Function (MFKDF) construction extends password‑based key derivation with additional authentication factors such as TOTP, HOTP, and hardware tokens, and reports an exponential security improvement over PBKDFs at less than 12 ms of added latency [7]. The relevant lesson is that practical key management derives security from multiple independent secret inputs under public algorithms—the exact opposite of deriving it from a single obscure encoding parameter. Biometric key‑generation work makes the same point from another direction: two closely related papers on generating cryptographic keys from multimodal biometric feature‑level fusion of fingerprint and iris address the problem that users cannot remember long keys, by deriving repeatable keys from user biometrics while incorporating the volatility of those features [2], [3]. Both accept that the key must be a high‑entropy secret consumed by a standard primitive; neither proposes that the encoding of data could itself carry the secrecy. Our result explains why: encoding secrecy is structurally weak.

The threat model and deployment context are framed by work on how security mechanisms actually fail in the field. An analysis of Extended Reality (XR) devices presents a device‑centric survey of security and privacy attacks and defenses and argues for robust, privacy‑aware mechanisms and design considerations [8]; a study of non‑expert users’ perspectives on cyber security and privacy, based on online discussions on Twitter, analyzes those perspectives for traditional and smart‑home and IoT devices [6]; the entry’s summary states no further findings, and the inference that non‑expert deployers cannot evaluate mechanisms whose security depends on subtlety is this paper’s own, not a finding of [6]. Both support the practical stakes in Section 7: mechanisms whose security depends on subtlety (such as a silent radix) are precisely the mechanisms non‑expert deployers cannot evaluate, so a provable negative result is the only protection that scales. Finally, work on cryptographically verifiable authorization for autonomous AI agents proposes a falsifiable hypothesis and proof of concept for giving agents’ requests cryptographic evidence of policy compliance in context [1]. That work illustrates the standard a new primitive must meet—a falsifiable, verifiable security claim with a proof of concept—and Section 6 states the falsification conditions for our own claim in the same spirit.

Two methodological gaps emerge from this survey. First, no cited work analyzes base‑ambiguity or radix‑obscurity constructions; the silent‑radix proposal [10] asserts a reduction to knapsack but supplies no key‑space entropy, no unicity distance, and no attack cost. Second, the cited formal‑analysis work [4] shows the value of converting informal proposals into models, but has not been applied to encoding‑based primitives. This paper fills both gaps for the unknown‑radix case.

## 3. Methods

### 3.1 The scheme

Let $\Sigma$ be a plaintext alphabet of $m$ symbols (for concreteness, English letters, $m=26$). The secret key is a pair $K=(B,\pi)$ where:

- $B\in[2,B_{\max}]$ is the radix, an integer, with $B_{\max}$ a public parameter of the scheme;
- $\pi:\Sigma\to\{0,1,\dots,m-1\}$ is a secret bijection assigning each plaintext symbol a digit value.

Encryption of a plaintext $P=s_{1}s_{2}\dots s_{n}$ of $n$ symbols proceeds in two steps:

1. Map each symbol to its digit: $d_{i}=\pi(s_{i})$ for $i=1,\dots,n$.
2. Interpret the digit string $d_{1}d_{2}\dots d_{n}$ as a positional numeral in base $B$, i.e., compute the integer  

$$C=\sum_{i=1}^{n}d_{i}\,B^{\,n-i}.$$

The ciphertext is the integer $C$, transmitted without base information. Decryption by the holder of $K$ writes $C$ in base $B$, recovers the digit string $d_{1}\dots d_{n}$, and applies $\pi^{-1}$.

This is the encoding core of the scheme described as Silent Radix Encryption in [10], restricted to the pure encoding primitive; we do not model any additional encapsulation layers, and our conclusions apply to the core.

### 3.2 Key space and adversary model

The key space is  

$$\mathcal{K}=\{(B,\pi):B\in\{2,\dots,B_{\max}\},\ \pi\in\mathrm{Sym}(m)\},$$  

where $\mathrm{Sym}(m)$ is the set of bijections from $\Sigma$ to $\{0,\dots,m-1\}$. Its size is  

$$|\mathcal{K}|=(B_{\max}-1)\cdot m!.$$

The adversary model is ciphertext‑only: the attacker sees the integer $C$ (and possibly several such integers under the same key), knows the scheme, the alphabet size $m$, and $B_{\max}$, but not $B$ or $\pi$. This is the Kerckhoffs‑consistent model: everything about the design except $K$ is public. We verify the model’s assumptions against the scheme’s own description: the base is “silent”—carried by neither the ciphertext nor any public parameter—so its secrecy is the entire claim of the primitive [10].

### 3.3 Language model

Frequency analysis requires a source model. We adopt the following explicitly assumed parameters for English text over $m=26$ symbols, used consistently throughout and labeled as assumptions wherever they enter a computation:

- $A_{1}$: per‑symbol source entropy $H_{1}=4.0$ bits (against a maximum of $\log_{2}26\approx4.70$ bits for a uniform source), giving redundancy per symbol $D=\log_{2}26-H_{1}=0.70$ bits.
- $A_{2}$: the most frequent symbol occurs with probability $p_{\max}=0.12$.
- $A_{3}$: the least frequent symbol occurring in ordinary text has probability $p_{\min}=0.005$.

These are modeling assumptions about the plaintext source, not measurements; Section 6 states how the results shift if they are varied.

### 3.4 Analysis methods

We use four analytic instruments, all standard and all applied with explicit arithmetic in Section 4: (i) key‑space entropy $H(K)=\log_{2}|\mathcal{K}|$; (ii) the unicity distance $n_{0}=H(K)/D$, the number of ciphertext symbols beyond which only one key yields a plausible plaintext; (iii) a histogram discrimination test for the radix, comparing the digit‑frequency skew of the true base against the near‑uniform digit frequencies of a wrong base; and (iv) brute‑force cost arithmetic for benchmarking. No simulations were run and no empirical attack data were collected; every number in Section 5 is either derived in Section 4 or labeled a projection with stated assumptions.

## 4. Analysis

### 4.1 Key‑space entropy

With $m=26$ and $B_{\max}=2^{16}=65536$:

- Number of admissible radices: $B_{\max}-1=65535$.
- Number of digit maps: $26!$.

Compute $\log_{2}(26!)$. We have $26!=403291461126605635584000000\approx4.0329\times10^{26}$. Then  

$$\log_{2}(26!)=\log_{10}(4.0329\times10^{26})\times\log_{2}10=26.6055\times3.32193=88.38\text{ bits}.$$

Step by step: $\log_{10}(4.0329)=0.6055$, so $\log_{10}(26!)=26.6055$; multiplying by $\log_{2}10=3.32193$ gives $88.38$.

The radix contributes $\log_{2}65535$ bits. Since $65535=2^{16}-1=2^{16}(1-2^{-16})$,  

$$\log_{2}65535=16+\log_{2}(1-2^{-16})\approx16-2^{-16}\cdot\log_{2}e\approx16-0.000022=15.99998,$$

which we carry as $16.00$ bits rounded to two decimals.

Total key entropy:  

$$H(K)=\log_{2}\big[(B_{\max}-1)\cdot26!\big]=16.00+88.38=104.38\text{ bits}.$$

This is the number a naive analysis would stop at: the key space holds $2^{104.38}\approx2.64\times10^{31}$ keys, comparable to a substantial symmetric key length. Section 4.5 shows this number is irrelevant to security.

### 4.2 Reduction to monoalphabetic substitution

Fix the correct radix $B$. Decryption is: write $C$ in base $B$ to obtain the digit string $d_{1}\dots d_{n}$, then apply $\pi^{-1}$. Because each plaintext symbol $s_{i}$ maps to exactly one digit $d_{i}=\pi(s_{i})$ independent of position, the map from plaintext symbols to ciphertext digits is position‑independent: the scheme with known $B$ is exactly a monoalphabetic substitution cipher over the digit alphabet $\{0,\dots,m-1\}$, with the substitution table being $\pi$.

The only structural difference from a textbook substitution cipher is segmentation: the attacker does not know where the digit boundaries fall, because that depends on $B$. Once $B$ is known, segmentation is determined. Therefore the total security of the scheme is at most the security of a monoalphabetic substitution cipher, plus whatever protection the unknown segmentation adds. The following two subsections bound both terms.

### 4.3 Unicity distance

The unicity distance for a cipher with key entropy $H(K)$ over a redundant source with redundancy $D$ bits per symbol is  

$$n_{0}=\frac{H(K)}{D}.$$

With $H(K)=104.38$ bits (Section 4.1) and the assumed redundancy $D=0.70$ bits/symbol (assumption $A_{1}$):  

$$n_{0}=\frac{104.38}{0.70}=149.1\text{ symbols}.$$

Arithmetic: $104.38/0.70=149.114\ldots$, rounded to $149.1$.

For the radix alone (if $\pi$ were public and only $B$ secret):  

$$n_{0}^{(\text{radix})}=\frac{16.00}{0.70}=22.9\text{ symbols}.$$

Arithmetic: $16.00/0.70=22.857\ldots$, rounded to $22.9$.

Interpretation: a single ciphertext of $150$ or more symbols is, in principle, sufficient to determine the key uniquely by statistical evidence alone. The unicity distance does not give an algorithm, but it bounds from below the message length at which any ciphertext‑only attack must succeed, and it shows that no parameter choice in $B$ or $\pi$ raises this bound except by increasing $H(K)$—which, as the next subsection shows, does not help because $B$ is recoverable directly.

### 4.4 The two‑stage attack

**Stage 1: radix recovery by histogram discrimination.** The attacker guesses a candidate radix $B'$ and computes the base‑$B'$ digit string of $C$, then examines the digit histogram. Two facts drive the test.

(a) Under the correct $B'=B$, the digit string is $\pi(s_{1})\dots\pi(s_{n})$, so digit frequencies equal plaintext letter frequencies permuted by $\pi$. In particular, the most frequent digit occurs with relative frequency $p_{\max}=0.12$ (assumption $A_{2}$).

(b) Under a wrong $B'\neq B$, the integer $C$ behaves as an arbitrary integer in base $B'$, and its digits are spread over $B'$ values. As an explicitly labeled projection, we assume a uniformity heuristic: under a wrong $B'\neq B$ the integer $C$ behaves as an arbitrary integer in base $B'$, so its $n$ digits are approximately uniformly distributed over $B'$ values, giving an expected most‑common‑digit frequency of approximately $1/B'+O(1/n)$; for $B'\ge2^{16}$ and $n=1000$ this is at most about $1.53\times10^{-5}+O(10^{-3})$, i.e., on the order of $10^{-3}$ at worst from discretization, versus $0.12$ for the correct base. This heuristic is an assumption, not a derivation; Section 6 lists it among the limitations.

The test statistic is the maximum digit frequency $\hat{f}_{\max}$. The gap between the two hypotheses is a factor of at least  

$$\frac{0.12}{10^{-3}}=120$$  

for $n=1000$ and $B'\ge2^{16}$, and grows linearly in $n$. For smaller candidate bases $B'\le m$, the digit alphabet is compressed but the correct base still yields the permuted letter‑frequency profile, which is highly non‑uniform, while a wrong small base distributes the integer’s value over few digits in a pattern that does not match a permutation of the letter‑frequency profile; the same skew test applies.

Cost of Stage 1: for each candidate $B'\in\{2,\dots,B_{\max}\}$, extracting the $n$ base‑$B'$ digits of $C$ costs $O(n)$ division steps. Total  

$$W_{1}\le(B_{\max}-1)\cdot c\cdot n$$  

elementary operations, with $c$ a small constant (we take $c=1$ digit‑extraction step per digit as the counting convention). For $B_{\max}=2^{16}$ and $n=1000$:  

$$W_{1}\le65535\times1000=65\,535\,000=6.5535\times10^{7}\text{ digit operations}.$$

Arithmetic: $65535\times1000=65\,535\,000$.

At a conservative $10^{8}$ elementary operations per second on a single core, this is  

$$\frac{6.5535\times10^{7}}{10^{8}}=0.66\text{ s};$$  

at $10^{9}$/s, $0.066$ s. Even granting a factor‑of‑100 overhead for histogram bookkeeping, Stage 1 completes in about a minute on one core: $0.66\text{ s}\times100=66\text{ s}$ at $10^{8}$ ops/s, and $6.6\text{ s}$ at $10^{9}$ ops/s.

**Stage 1b: consistency check on the digit map’s range.** Independently, the observed maximum digit value $d_{\max}$ in the correct segmentation satisfies $B\ge d_{\max}+1$, and the number of distinct digits observed bounds $m$ from below. The probability that a digit whose plaintext symbol has probability $p\ge p_{\min}=0.005$ (assumption $A_{3}$) fails to appear in $n$ symbols is at most  

$$(1-p_{\min})^{n}=0.995^{1000}=e^{1000\ln0.995}=e^{-5.01254}=0.006654.$$

Arithmetic: $\ln0.995=-0.00501254$; multiplied by $1000$ gives $-5.01254$; $e^{-5.01254}=0.006654$.

So with $n=1000$ symbols, a symbol with frequency $p_{\min}=0.005$ appears with probability $1-0.006654=0.993346$; the correct segmentation exhibits essentially the full letter‑frequency profile, and any candidate base whose digit histogram lacks the expected skew is eliminated. The check costs $O(n)$ per surviving candidate and does not change the Stage 1 cost bound.

**Stage 2: frequency analysis of the residual substitution.** With $B$ recovered, the attacker holds the digit string $d_{1}\dots d_{n}$, which is the plaintext under a monoalphabetic substitution $\pi$. Standard frequency analysis against English letter statistics recovers $\pi$; the unicity distance computed in Section 4.3 shows that $n\ge149.1$ symbols suffice in principle for unique determination, and $n=1000$ exceeds this by a factor of $6.7$ ($1000/149.1=6.71$). No new machinery is needed: the attack is the classical one, and its cost is dominated by Stage 1 in our parameterization.

### 4.5 Brute‑force benchmark and the irrelevance of key‑space size

For contrast, consider exhaustive search over $\mathcal{K}$. With $|\mathcal{K}|=2^{104.38}\approx2.64\times10^{31}$ keys (Section 4.1) and a hypothetical $10^{9}$ keys/s:  

$$T_{\text{bf}}=\frac{2.64\times10^{31}}{10^{9}}\text{ s}=2.64\times10^{22}\text{ s}.$$

Converting to years at $3.156\times10^{7}$ s/year:  

$$T_{\text{bf}}=\frac{2.64\times10^{22}}{3.156\times10^{7}}=8.36\times10^{14}\text{ years}.$$

Arithmetic: $2.64/3.156=0.8364$, and $10^{22}/10^{7}=10^{15}$, giving $0.8364\times10^{15}=8.36\times10^{14}$ years.

The comparison is the paper’s central quantitative point: exhaustive search needs $8.36\times10^{14}$ years, while the structural attack of Section 4.4 needs $0.66$ s of single‑core work at the conservative rate of $10^{8}$ operations/s. The ratio is  

$$\frac{8.36\times10^{14}\text{ years}}{0.66\text{ s}\times(1\text{ year}/3.156\times10^{7}\text{ s})}= \frac{8.36\times10^{14}}{2.09\times10^{-8}}\approx4.0\times10^{22}.$$

Arithmetic: $0.66/3.156\times10^{7}=2.09\times10^{-8}$ years; $8.36\times10^{14}/2.09\times10^{-8}=4.0\times10^{22}$. A key‑space‑size argument therefore overestimates the attack cost by roughly $10^{22}$; the binding constraint is the unicity distance and the statistical structure of the plaintext, not the key count.

## 5. Results

All numbers below are derived in Section 4 under the stated assumptions $A_{1}$–$A_{3}$; none is a simulation or measurement.

- **R1 (key‑space entropy).** For $m=26$, $B_{\max}=2^{16}$: $H(K)=104.38$ bits, $|\mathcal{K}|\approx2.64\times10^{31}$ (Section 4.1).
- **R2 (unicity distance).** $n_{0}=149.1$ symbols for the full key; $n_{0}^{(\text{radix})}=22.9$ symbols if $\pi$ is public (Section 4.3).
- **R3 (radix‑recovery cost).** Stage 1 costs at most $6.5535\times10^{7}$ digit operations for $n=1000$, i.e., $0.66$ s at $10^{8}$ ops/s on one core, or $0.066$ s at $10^{9}$ ops/s (Section 4.4).
- **R4 (discrimination gap, projection).** Under the uniformity heuristic stated in Section 4.4, the maximum‑digit‑frequency gap between correct and wrong base is a factor of at least $120$ for $n=1000$ and $B'\ge2^{16}$ (Section 4.4); this is a projection conditional on that heuristic, not a derived bound.
- **R5 (appearance probability).** A symbol of frequency $p_{\min}=0.005$ fails to appear in $n=1000$ symbols with probability $0.006654$ (Section 4.4, Stage 1b).
- **R6 (brute‑force benchmark).** Exhaustive search at $10^{9}$ keys/s takes $8.36\times10^{14}$ years; the structural attack is faster by a factor of about $4.0\times10^{22}$ (Section 4.5).
- **R7 (negative result).** With $B$ recoverable at cost R3 and the residual cipher a monoalphabetic substitution breakable within R2 symbols, the scheme’s ciphertext‑only security on a single message is bounded by the cost of classical frequency analysis; radix obscurity contributes no security beyond obfuscation, and hence no quantum‑relevant advantage (Sections 4.2–4.5).

## 6. Discussion

The result is a negative one, and its strength depends entirely on the assumptions behind the arithmetic. We state the limitations, the failure modes, and the falsification conditions explicitly.

**Limitations.** The result rests on the following assumptions, with the sensitivity of the headline numbers to each:

- *Language model ($A_{1}$–$A_{3}$).* The redundancy $D=0.70$ bits/symbol sets the unicity distance $n_{0}=H(K)/D$; if the true redundancy were $D=0.5$, then $n_{0}=208.8$ symbols, and if $D=1.0$ (near‑uniform source), $n_{0}=104.4$ symbols. The qualitative conclusion—a single message of a few hundred symbols suffices in principle—is stable across this range, but the exact threshold scales as $1/D$.
- *Frequency skew ($A_{2}$).* The Stage 1 gap factor of $120$ scales linearly with $p_{\max}$; a flatter source with $p_{\max}=0.05$ would reduce the gap to $50$, still decisive for $n=1000$.
- *Cost convention.* The Stage 1 cost takes $c=1$ operation per digit extraction; real implementations pay a larger constant, which is why we granted a factor‑of‑100 overhead and still obtained sub‑minute runtimes. The bound is on digit operations, not wall‑clock time on any specific machine.
- *Scope of the model.* We analyze the pure encoding core of the scheme described in [10]. If the full SRE construction adds layers that randomize digit frequencies or re‑encrypt per message, the Stage 1 histogram test may fail; the source proposal’s supplied description states only the trapdoor claim and the knapsack reduction, and gives no such layer, so we cannot assess one.
- *Ciphertext‑only model.* The attack assumes the attacker sees only $C$. A known‑plaintext adversary recovers $\pi$ directly from a single aligned pair and $B$ from the digit range, making the scheme trivially broken; our model is the weaker and therefore stronger setting.

**Failure modes of the analysis.** The reduction in Section 4.2 assumes the digit map is position‑independent, which follows from the encoding definition; if a variant made $\pi$ position‑dependent (a polyalphabetic generalization), the residual cipher after Stage 1 would be a polyalphabetic substitution, and the unicity distance would change because the effective key entropy per message would grow. Our result does not cover such variants.

**Falsification.** The main result—that radix obscurity adds no security beyond obfuscation—would be falsified by a concrete demonstration of either of the following: (i) a parameterization of the scheme in which the digit histogram under the correct base is statistically indistinguishable from that under all wrong bases for message lengths at which the scheme is claimed to be usable, i.e., a failure of the Stage 1 discrimination gap of Section 4.4; or (ii) a variant construction whose security proof does not pass through the encoding core analyzed here, for example one where the transmitted object is not the integer $C$ but a transformed value that destroys the base‑$B$ digit structure. Absent either, the negative result stands: any scheme whose ciphertext is the bare positional integer in a secret base falls to the two‑stage attack.

**Open questions.** Whether the knapsack reduction claimed in [10] is correct is not settled here, and it does not need to be: even a correct reduction to an NP‑hard problem would not help, because the direct attack bypasses the knapsack structure entirely. Whether some non‑encoding layer built on top of the core could be secure is a separate design question, not a rescue of the radix‑as‑trapdoor idea.

## 7. Practical Implications and Engineering Pathways

**(a) Who uses the result and what changes.** The direct users are security architects performing cryptographic inventory and migration work under the CBOM methodology [5],