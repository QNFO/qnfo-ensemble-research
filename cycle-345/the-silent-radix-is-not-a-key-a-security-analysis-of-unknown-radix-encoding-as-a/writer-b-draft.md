# The Silent Radix Is Not a Key: A Security Analysis of Unknown-Radix Encoding as a Cryptographic Primitive

## Abstract

Positional numerals do not internally specify their own base, and a recent informal proposal — Silent Radix Encryption (SRE) — conjectures that this "silent radix" can serve as a cryptographic secret: plaintext symbols are mapped to digits by a secret map and read as an integer in a secret radix $B$, with $B$ acting as a trapdoor for key encapsulation. No formal security analysis of this construction existed when the proposal was made. We formalize the encoding core, define its key space over admissible radices $B \in [2, 2^{16}]$ and digit maps on a 26-symbol alphabet, and compute its entropy: $104.38$ bits. We then show the construction reduces to a monoalphabetic substitution cipher with base-dependent segmentation, and we derive a two-stage ciphertext-only attack: a histogram test recovers $B$ at a cost of at most $6.5535 \times 10^{7}$ digit operations for a 1000-symbol ciphertext, after which standard frequency analysis applies within a unicity distance of $149.1$ symbols, computed from the key entropy and an assumed language redundancy of $0.70$ bits/symbol. Brute force over the full key space at $10^{9}$ keys/s would take $8.36 \times 10^{14}$ years, yet the structural attack succeeds on a single short message: key-space size is irrelevant. We conclude that radix obscurity offers no security advantage over classical substitution ciphers and therefore no quantum-relevant one, and we state the conditions under which this negative result would be falsified.

## 1. Introduction

A recurring failure mode in cryptographic engineering is the deployment of primitives whose security rests on the secrecy of a design parameter rather than on the secrecy of a key under a public, well-scrutinized algorithm. The practitioners who face this problem concretely are security architects performing cryptographic migration and inventory work: the Cryptographic Bill of Materials (CBOM) methodology exists precisely because organizations must decide which deployed mechanisms to trust and which to retire as algorithms are deprecated and post-quantum readiness is planned [5]. If a mechanism such as unknown-radix encoding were believed to be a viable lightweight cipher or key-encapsulation trapdoor, it could enter that inventory as a candidate; if it is in fact breakable by classical statistical attacks on a single ciphertext, it must be excluded before it is ever deployed. Today no formal analysis exists that lets an architect, a standards body, or a protocol designer make that decision with confidence: the proposal circulates as an informal conjecture that a secret base $B$ — the observation that a positional numeral cannot specify its own base — could act as a cryptographic trapdoor [9].

The stakes are concrete. An organization that adopted such a scheme for key encapsulation would believe its encapsulated keys were protected by a large key space — over $2^{100}$ combinations of radix and digit map in the parameterization analyzed here — and might further believe that a scheme built from integer arithmetic rather than from structured lattices or block ciphers resists quantum attack by being "unusual." This paper shows that both beliefs are wrong: the entire key space collapses under a statistical test that costs less than $10^{8}$ elementary operations, and the residual problem is a monoalphabetic substitution cipher, a primitive broken by classical statistical means long before the era of digital computers. The decision that changes if this result holds is simple: unknown-radix encoding is classified as obfuscation, not encryption, and is excluded from cryptographic inventories and migration plans at the same tier as encoding tricks, with no post-quantum consideration owed to it.

This paper treats the scheme named Silent Radix Encryption in the source literature [9], which specifies SRE as a non-interactive key encapsulation mechanism in which two parties pre-share a secret base $b$, the sender generates $k$ random decimal digits, computes the shared secret as the base-$b$ interpretation of those digits, derives a symmetric key from it, and transmits the decimal interpretation of the digit string as a public envelope. The source claims that security reduces to an unknown-weight integer knapsack problem [9]. We analyze the core encoding primitive directly and show that the knapsack reduction, even if correct, does not confer security, because the encoding admits a direct statistical attack that bypasses the knapsack structure entirely. A companion paper in the same series already reports that the naive, noise-free version of the cipher is categorically insecure — a single known-plaintext pair recovers the secret base by an elementary greatest-common-divisor computation regardless of radix size [11] — but that result covers the known-plaintext setting only; the ciphertext-only question, which is the stronger and more realistic demand on a KEM, has not been answered. This paper answers it.

**Contributions.**

- A formal definition of the unknown-radix encoding scheme, its key space (admissible radices $B \in [2, B_{\max}]$ and digit maps over an $m$-symbol alphabet), and the computation of its entropy: $104.38$ bits for $m = 26$, $B_{\max} = 2^{16}$ (Sections 3 and 4.1).
- A reduction showing that decryption under a known radix is exactly a monoalphabetic substitution with base-dependent segmentation, and a derivation of the unicity distance $n_0 = 149.1$ symbols for the full key space (Sections 4.2 and 4.3).
- An explicit two-stage ciphertext-only attack with full arithmetic: radix recovery by histogram discrimination at a cost of at most $6.5535 \times 10^{7}$ digit operations for $n = 1000$, followed by frequency analysis of the residual substitution (Section 4.4).
- A comparison against brute-force benchmarks showing that the key-space entropy of $104.38$ bits is structurally irrelevant: the binding constraint is the unicity distance, not the key count (Sections 4.5 and 5).
- A statement of the negative result for quantum relevance — a scheme broken classically on a single ciphertext cannot offer a quantum-relevant advantage — together with falsification conditions and the limits of the analysis (Section 6).

## 2. Background and Related Work

The immediate ancestor of this work is the silent-radix proposal itself. The Silent-Radix Cryptography paper states the core observation — that in any integer base $b \geq 2$ the digit string "10" denotes the number $b$, so every base named in its own numeral system calls itself "base-10," and the radix is therefore a silent parameter supplied only by an external meta-language — and proposes Silent Radix Encryption (SRE) as a non-interactive key encapsulation mechanism built on this ambiguity [9]. Its construction is explicit: the sender generates $k$ random decimal digits, computes the shared secret $K = \sum_{i=0}^{k-1} d_i \cdot b^{i}$ under the secret base $b$, derives a symmetric key via SHA-256, encrypts by counter-mode XOR, and transmits the decimal interpretation $N = \sum_{i=0}^{k-1} d_i \cdot 10^{i}$ as the public envelope; the receiver extracts the decimal digits of $N$ and recomputes $K$ in base $b$ [9]. The same paper frames the digit string as a path through a rooted tree under the $b$-adic ultrametric $d(x,y) = b^{-v_b(x-y)}$ and claims that security reduces to an unknown-weight integer knapsack problem [9]. What the proposal does not contain is any key-space entropy computation, any unicity distance, or any ciphertext-only attack cost; those are exactly the quantities this paper supplies for the encoding core.

A companion paper in the same series, on factoring and adelic complexity, reports two results that bound what the proposal can achieve. First, it states that the naive symmetric base-change cipher is categorically insecure: a single known-plaintext pair suffices to recover the secret base via elementary greatest-common-divisor computation, regardless of radix size, because security cannot be obtained from key entropy alone when the cipher is linear and deterministic [11]. Second, it describes SRE as a key encapsulation mechanism with a $2^{128}$-class key space and reports that the scheme closes the known-plaintext attack vector via digit randomization [11]. Our analysis is complementary and more demanding: we show that even against a ciphertext-only adversary who sees no known-plaintext pair, the encoding core falls to a statistical attack on a single message, so digit randomization against known-plaintext does not rescue the construction.

A third paper in the program, HM-LWE v3.0, proposes hidden-modulus Learning With Errors as a novel hardness assumption: standard lattice-based cryptography operates over a publicly known modulus, and the paper asks what happens when the modulus itself is secret, forcing the adversary into a joint search over modulus and key [10]. Its own account of prior work records that the initial hidden-radix observation was followed by a comparative analysis establishing that noise-free hidden-radix ciphers fail catastrophically under known-plaintext attack, and that noise-augmented constructions were then introduced in response [10]. Its experimental section reports a GCD-based modulus-recovery rate of $1.00$ at noise level $t=0$, $0.07$ at $t=1$, and $0.00$ at $t \geq 2$, and characterizes the resulting scheme as approximately four orders of magnitude slower than Kyber-1024 with $16\times$ larger ciphertexts [10]. This sequence matters for our argument: the hidden-modulus program itself concedes that the noise-free encoding layer is broken and turns to injected noise for security. Our result formalizes the ciphertext-only half of that concession for the pure radix case; the noise-augmented variants change the attack surface and are outside our scope, and nothing in this paper evaluates them.

The broader literature supplies the evaluation standards against which any new primitive must be judged. Kerckhoffs's principle — the system must remain secure even if everything about it except the key is public — is operationalized in modern formal methods: the first formal model of Bitcoin's Payment Protocol (BIP70) formalised the previously shown refund-attack vulnerability arising from lack of authentication of refund addresses, using the symbolic model-checker OFMC and the AnB formal language in which communication channels are modeled as abstractions conveying security goals such as authenticity and secrecy [4]. That work is the template we follow: an informal belief about a protocol's security is converted into a formal model, and the model is then attacked. Our Section 3 formalization and Section 4 attack play the same role for unknown-radix encoding that the formal model and refund-attack analysis played for BIP70.

On the constructive side, the literature shows what real key-establishment machinery looks like, and thereby sharpens the comparison in Section 4.5. The Multi-Factor Key Derivation Function (MFKDF) construction extends password-based key derivation with additional authentication factors such as TOTP, HOTP, and hardware tokens, and reports an exponential security improvement over PBKDFs at less than 12 ms of added latency, with benchmarks of a JavaScript implementation reported on single-thread performance [6]. The relevant lesson is that practical key management derives security from multiple independent secret inputs consumed by public algorithms — the exact opposite of deriving it from a single obscure encoding parameter. Biometric key-generation work makes the same point from another direction: two closely related papers on generating cryptographic keys from multimodal biometric feature-level fusion of fingerprint and iris address the problem that human users have a tough time remembering long cryptographic keys, by deriving repeatable keys from user biometrics while incorporating the volatility of those features into the generated key [2], [3]. Both accept that the key must be a high-entropy secret consumed by a standard primitive; neither proposes that the encoding of data could itself carry the secrecy. Our result explains why: encoding secrecy is structurally weak.

The deployment context is framed by work on how security mechanisms actually fail in the field. A device-centric analysis of Extended Reality (XR) devices surveys security and privacy attacks and defenses — selecting 41 papers from an initial pool of 319 and identifying 30 XR devices — and argues for robust, privacy-aware mechanisms and design considerations [7]. The lesson we draw is about evaluation culture: mechanisms deployed on consumer hardware are examined adversarially after deployment, so a mechanism whose security depends on a subtle parameter is a liability regardless of platform. The same conclusion motivates classifying unknown-radix encoding before deployment rather than after.

Finally, work on cryptographically verifiable authorization for autonomous AI agents proposes a falsifiable hypothesis and proof of concept for giving agents' requests cryptographic evidence of policy compliance in context, and explicitly separates binding layers — identity binding, authorization-request binding, and runtime execution binding — as structurally distinct security properties requiring separate mechanisms [1]. That work illustrates the standard a new primitive must meet — a falsifiable, verifiable security claim — and Section 6 states the falsification conditions for our own claim in the same spirit. The prior version of the analysis presented here established the key-space entropy, the substitution reduction, and the two-stage attack in their initial form [8]; the present paper is the remediated revision of that analysis, with the related-work grounding and the attack arithmetic completed.

Two methodological gaps emerge from this survey. First, no cited work analyzes base-ambiguity or radix-obscurity constructions against a ciphertext-only adversary; the silent-radix proposal [9] asserts a reduction to knapsack but supplies no key-space entropy, no unicity distance, and no attack cost, and the known-plaintext result of [11] leaves the ciphertext-only question open. Second, the cited formal-analysis work [4] shows the value of converting informal proposals into models, but has not been applied to encoding-based primitives. This paper fills both gaps for the unknown-radix case.

## 3. Methods

### 3.1 The scheme

Let $\Sigma$ be a plaintext alphabet of $m$ symbols (for concreteness, English letters, $m = 26$). The secret key is a pair $K = (B, \pi)$ where:

- $B \in [2, B_{\max}]$ is the radix, an integer, with $B_{\max}$ a public parameter of the scheme;
- $\pi: \Sigma \to \{0, 1, \ldots, m-1\}$ is a secret bijection assigning each plaintext symbol a digit value.

Encryption of a plaintext $P = s_1 s_2 \ldots s_n$ of $n$ symbols proceeds in two steps:

1. Map each symbol to its digit: $d_i = \pi(s_i)$ for $i = 1, \ldots, n$.
2. Interpret the digit string $d_1 d_2 \ldots d_n$ as a positional numeral in base $B$, i.e., compute the integer

$$C = \sum_{i=1}^{n} d_i \, B^{\,n-i}.$$

The ciphertext is the integer $C$, transmitted without base information. Decryption by the holder of $K$ writes $C$ in base $B$, recovers the digit string $d_1 \ldots d_n$, and applies $\pi^{-1}$.

This is the encoding core of the scheme described as Silent Radix Encryption in [9], generalized from the source's fixed decimal digit alphabet to an arbitrary $m$-symbol plaintext alphabet with a secret digit map; we do not model any additional encapsulation layers, and our conclusions apply to the core. We note that the source proposal claims a reduction of SRE security to an unknown-weight integer knapsack problem [9]; Section 4.4 shows that the core encoding is attacked without touching any knapsack structure.

### 3.2 Key space and adversary model

The key space is

$$\mathcal{K} = \{(B, \pi) : B \in \{2, \ldots, B_{\max}\},\ \pi \in \mathrm{Sym}(m)\},$$

where $\mathrm{Sym}(m)$ is the set of bijections from $\Sigma$ to $\{0, \ldots, m-1\}$. Its size is

$$|\mathcal{K}| = (B_{\max} - 1) \cdot m!.$$

The adversary model is ciphertext-only: the attacker sees the integer $C$ (and possibly several such integers under the same key), knows the scheme, the alphabet size $m$, and $B_{\max}$, but not $B$ or $\pi$. This is the Kerckhoffs-consistent model: everything about the design except $K$ is public. The model's assumptions match the scheme's own description: the base is silent — carried by neither the ciphertext nor any public parameter — so its secrecy is the entire claim of the primitive [9].

### 3.3 Language model

Frequency analysis requires a source model. We adopt the following explicitly assumed parameters for English text over $m = 26$ symbols, used consistently throughout and labeled as assumptions wherever they enter a computation:

- $A_1$: per-symbol source entropy $H_1 = 4.0$ bits (against a maximum of $\log_2 26 \approx 4.70$ bits for a uniform source), giving redundancy per symbol $D = \log_2 26 - H_1 = 0.70$ bits.
- $A_2$: the most frequent symbol occurs with probability $p_{\max} = 0.12$.
- $A_3$: the least frequent symbol occurring in ordinary text has probability $p_{\min} = 0.005$.

These are modeling assumptions about the plaintext source, not measurements; Section 6 states how the results shift if they are varied.

### 3.4 Analysis methods

We use four analytic instruments, all standard and all applied with explicit arithmetic in Section 4: (i) key-space entropy $H(K) = \log_2 |\mathcal{K}|$; (ii) the unicity distance $n_0 = H(K)/D$, the number of ciphertext symbols beyond which only one key yields a plausible plaintext; (iii) a histogram discrimination test for the radix, comparing the digit-frequency skew of the true base against the near-uniform digit frequencies of a wrong base; and (iv) brute-force cost arithmetic for benchmarking. No simulations were run and no empirical attack data were collected; every number in Section 5 is either derived in Section 4 or labeled a projection with stated assumptions.

## 4. Analysis

### 4.1 Key-space entropy

With $m = 26$ and $B_{\max} = 2^{16} = 65536$:

- Number of admissible radices: $B_{\max} - 1 = 65535$.
- Number of digit maps: $26!$.

Compute $\log_2(26!)$. We have $26! = 403291461126605635584000000 \approx 4.0329 \times 10^{26}$. Then

$$\log_2(26!) = \log_{10}(4.0329 \times 10^{26}) \times \log_2 10 = 26.6055 \times 3.32193 = 88.38 \text{ bits}.$$

Step by step: $\log_{10}(4.0329) = 0.6055$, so $\log_{10}(26!) = 26.6055$; multiplying by $\log_2 10 = 3.32193$ gives $26.6055 \times 3.32193 = 88.38$.

The radix contributes $\log_2 65535$ bits. Since $65535 = 2^{16} - 1 = 2^{16}(1 - 2^{-16})$,

$$\log_2 65535 = 16 + \log_2(1 - 2^{-16}) \approx 16 - 2^{-16} \cdot \log_2 e \approx 16 - 0.000022 = 15.99998,$$

which we carry as $16.00$ bits rounded to two decimals.

Total key entropy:

$$H(K) = \log_2\big[(B_{\max}-1) \cdot 26!\big] = 16.00 + 88.38 = 104.38 \text{ bits}.$$

This is the number a naive analysis would stop at: the key space holds $2^{104.38}$ keys. Converting: $104.38 \times \log_{10} 2 = 104.38 \times 0.30103 = 31.42$, so $|\mathcal{K}| \approx 10^{31.42} = 2.64 \times 10^{31}$ keys, comparable to a substantial symmetric key length. Section 4.5 shows this number is irrelevant to security.

### 4.2 Reduction to monoalphabetic substitution

Fix the correct radix $B$. Decryption is: write $C$ in base $B$ to obtain the digit string $d_1 \ldots d_n$, then apply $\pi^{-1}$. Because each plaintext symbol $s_i$ maps to exactly one digit $d_i = \pi(s_i)$ independent of position, the map from plaintext symbols to ciphertext digits is position-independent: the scheme with known $B$ is exactly a monoalphabetic substitution cipher over the digit alphabet $\{0, \ldots, m-1\}$, with the substitution table being $\pi$.

The only structural difference from a textbook substitution cipher is segmentation: the attacker does not know where the digit boundaries fall, because that depends on $B$. Once $B$ is known, segmentation is determined. Therefore the total security of the scheme is at most the security of a monoalphabetic substitution cipher, plus whatever protection the unknown segmentation adds. The following two subsections bound both terms.

### 4.3 Unicity distance

The unicity distance for a cipher with key entropy $H(K)$ over a redundant source with redundancy $D$ bits per symbol is

$$n_0 = \frac{H(K)}{D}.$$

With $H(K) = 104.38$ bits (Section 4.1) and the assumed redundancy $D = 0.70$ bits/symbol (assumption $A_1$):

$$n_0 = \frac{104.38}{0.70} = 149.1 \text{ symbols}.$$

Arithmetic: $104.38 / 0.70 = 149.114\ldots$, rounded to $149.1$.

For the radix alone (if $\pi$ were public and only $B$ secret):

$$n_0^{(\text{radix})} = \frac{16.00}{0.70} = 22.9 \text{ symbols}.$$

Arithmetic: $16.00 / 0.70 = 22.857\ldots$, rounded to $22.9$.

Interpretation: a single ciphertext of $150$ or more symbols is, in principle, sufficient to determine the key uniquely by statistical evidence alone. The unicity distance does not give an algorithm, but it bounds from below the message length at which any ciphertext-only attack must succeed, and it shows that no parameter choice in $B$ or $\pi$ raises this bound except by increasing $H(K)$ — which, as the next subsection shows, does not help because $B$ is recoverable directly.

### 4.4 The two-stage attack

**Stage 1: radix recovery by histogram discrimination.** The attacker guesses a candidate radix $B'$ and computes the base-$B'$ digit string of $C$, then examines the digit histogram. Two facts drive the test.

(a) Under the correct $B' = B$, the digit string is $\pi(s_1) \ldots \pi(s_n)$, so digit frequencies equal plaintext letter frequencies permuted by $\pi$. In particular, the most frequent digit occurs with relative frequency $p_{\max} = 0.12$ (assumption $A_2$).

(b) Under a wrong $B' \neq B$, the integer $C$ behaves as an arbitrary integer in base $B'$, and its digits are spread over $B'$ values. As an explicitly labeled projection, we assume a uniformity heuristic: under a wrong $B' \neq B$ the integer $C$ behaves as an arbitrary integer in base $B'$, so its $n$ digits are approximately uniformly distributed over $B'$ values, giving an expected most-common-digit frequency of approximately $1/B' + O(1/n)$; for $B' \geq 2^{16}$ and $n = 1000$ this is at most about $1.53 \times 10^{-5} + O(10^{-3})$, i.e., on the order of $10^{-3}$ at worst from discretization, versus $0.12$ for the correct base. This heuristic is an assumption, not a derivation; Section 6 lists it among the limitations.

The test statistic is the maximum digit frequency $\hat{f}_{\max}$. The gap between the two hypotheses is a factor of at least

$$\frac{0.12}{10^{-3}} = 120$$

for $n = 1000$ and $B' \geq 2^{16}$, and grows linearly in $n$. For smaller candidate bases $B' \leq m$, the digit alphabet is compressed but the correct base still yields the permuted letter-frequency profile, which is highly non-uniform, while a wrong small base distributes the integer's value over few digits in a pattern that does not match a permutation of the letter-frequency profile; the same skew test applies.

Cost of Stage 1: for each candidate $B' \in \{2, \ldots, B_{\max}\}$, extracting the $n$ base-$B'$ digits of $C$ costs $O(n)$ division steps. Total:

$$W_1 \leq (B_{\max} - 1) \cdot c \cdot n$$

elementary operations, with $c$ a small constant (we take $c = 1$ digit-extraction step per digit as the counting convention). For $B_{\max} = 2^{16}$ and $n = 1000$:

$$W_1 \leq 65535 \times 1000 = 65{,}535{,}000 = 6.5535 \times 10^{7} \text{ digit operations}.$$

Arithmetic: $65535 \times 1000 = 65{,}535{,}000$.

At a conservative $10^{8}$ elementary operations per second on a single core, this is

$$\frac{6.5535 \times 10^{7}}{10^{8}} = 0.66 \text{ s};$$

at $10^{9}$/s, $0.066$ s. Even granting a factor-of-100 overhead for histogram bookkeeping, Stage 1 completes in about a minute on one core: $0.66 \text{ s} \times 100 = 66$ s at $10^{8}$ operations/s, and $6.6$ s at $10^{9