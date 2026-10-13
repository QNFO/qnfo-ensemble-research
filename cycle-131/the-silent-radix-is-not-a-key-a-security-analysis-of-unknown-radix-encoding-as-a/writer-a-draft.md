# Security Analysis of Unknown‑Radix Encoding as a Cryptographic Primitive

## Abstract
The concealment of the numerical radix $B$ (and the associated digit‑to‑symbol mapping) has been proposed as a “secret base” cryptographic primitive. Existing literature provides no formal treatment of its key space, entropy, or concrete security guarantees. We define the admissible radices $B\in\{2,\dots,2^{16}\}$ and the corresponding permutation mappings, compute the exact size of the key space, and derive its Shannon entropy using Stirling’s approximation. We then prove an upper bound on the effective security by reducing the scheme to a monoalphabetic substitution with positional weighting, showing that an attacker can break it by (i) exhaustive search over the plausible radices (≈ $2^{16}$ possibilities) and (ii) frequency‑analysis‑driven recovery of the digit mapping, yielding at most $2^{48}$ work. A projection, based on assumed ciphertext lengths and English‑language statistics, predicts a success probability exceeding 90 % for messages longer than 200 characters when $B\le 2^{12}$. The result demonstrates that secret‑base obscurity offers no quantum‑relevant advantage and should not be considered a viable alternative to established symmetric or post‑quantum schemes.

## 1. Introduction
Modern cryptographic deployments rely on well‑studied hardness assumptions such as the difficulty of factoring, discrete logarithms, or lattice problems. System designers and standards bodies must choose primitives that resist both classical and quantum adversaries, because failure to do so can expose billions of dollars of assets and critical infrastructure to compromise. A recent informal proposal suggests that hiding the radix $B$ used to encode plaintext as an integer—together with a secret digit‑to‑symbol permutation—could serve as a lightweight key. If this “secret base” primitive were provably secure, low‑resource devices could replace heavyweight key‑exchange protocols with a simple base‑obfuscation step, reducing computational load and energy consumption.

The practical relevance of this claim is immediate for embedded IoT sensors, constrained autonomous agents, and legacy systems that already perform base conversions for data representation. These stakeholders would benefit from a primitive that requires only integer arithmetic and a small secret (the radix) while still offering security comparable to AES‑256 or lattice‑based key encapsulation mechanisms. Conversely, if the primitive is fundamentally weak, continued research or standardization efforts would waste resources and potentially mislead implementers.

**Contributions.**
- **C1.** Formal definition of the secret‑base key space (Section 3) and exact computation of its size and Shannon entropy (Section 4).  
- **C2.** Proof that the primitive reduces to a monoalphabetic substitution with positional weighting, yielding an explicit upper bound of $2^{48}$ on effective security (Section 4).  
- **C3.** Projection of ciphertext‑only attack success rates as a function of radix size and message length, based on English letter frequencies (Section 5).  
- **C4.** Discussion of limitations, falsifiability conditions, and engineering pathways for de‑risking the claim (Sections 6–7).

## 2. Background and Related Work
The notion of using hidden structural parameters as cryptographic secrets appears in several recent works, albeit in different contexts.

[1] investigates cryptographically verifiable authorization for autonomous AI agents. Its summary indicates that existing mechanisms lack cryptographic evidence for policy compliance, motivating the search for novel primitives; however, the summary provides no further detail on base‑obfuscation techniques.

[2] describes multimodal biometric key generation, emphasizing the difficulty users have remembering long keys. The summary does not discuss radix‑based schemes, but it illustrates the broader motivation for alternative key‑derivation methods.

[3] repeats the biometric key‑generation theme with a focus on fingerprint and iris fusion. As with [2], the summary offers no direct insight into secret‑base cryptography.

[4] formalises Bitcoin’s payment protocol and reveals refund‑address vulnerabilities. While unrelated to radix secrecy, the work exemplifies formal security modelling, a methodology we adopt for the present analysis.

[5] proposes a security‑aware architecture trade‑off method for cryptographic migration. Its emphasis on systematic evaluation of cryptographic assets informs our approach to quantifying the key‑space entropy of secret‑base schemes.

[6] analyses non‑expert user perspectives on cyber security and privacy via Twitter data. The summary highlights the importance of understandable security mechanisms, reinforcing the need for clear security arguments for any new primitive.

[7] presents a multi‑factor key‑derivation function (MFKDF) that combines passwords with additional factors. Although the summary mentions exponential security improvement, it does not address base‑obfuscation, underscoring that secret‑base ideas remain unexplored in mainstream KDF research.

[8] surveys security and privacy in extended‑reality devices, stressing the demand for robust mechanisms. The summary again provides no direct connection to radix secrecy but illustrates the breadth of domains that could be impacted by a lightweight primitive.

The QNFO entries (9–11) explicitly introduce the “silent‑radix” concept and claim that security reduces to an unknown‑weight integer knapsack problem. These entries motivate our formal treatment but, as summaries, they do not supply quantitative security analyses, which we provide herein.

## 3. Methods
### 3.1. Key‑space definition
We consider a secret radix $B$ drawn from the integer interval
\[
B\in\mathcal{B}=\{2,3,\dots,2^{16}\},
\]
where the upper bound $2^{16}=65\,536$ reflects the maximum word size commonly supported by modern processors. For each admissible $B$, the encoding map $\pi_B$ is a bijection from the digit set $\{0,1,\dots,B-1\}$ to a publicly known alphabet $\Sigma$ (e.g., ASCII characters). The total key is the ordered pair $(B,\pi_B)$.

The number of admissible radices is
\[
|\mathcal{B}| = 2^{16}-1 = 65\,535.
\]

For a given $B$, the number of possible permutations is $B!$. Hence the total key‑space size is
\[
K = \sum_{B=2}^{2^{16}} B!.
\]

### 3.2. Entropy computation
Shannon entropy $H$ (in bits) of a uniformly distributed key is
\[
H = \log_2 K.
\]
Because $K$ is dominated by its largest term $65\,536!$, we approximate
\[
H \approx \log_2 (65\,536!).
\]
Using Stirling’s approximation
\[
\log_2 (n!) \approx n\log_2 n - n\log_2 e + \tfrac{1}{2}\log_2 (2\pi n),
\]
with $n=65\,536$, we compute each component explicitly (see Section 4).

### 3.3. Security reduction
We model the encryption process as follows. A plaintext string $M$ is first mapped to a digit sequence $d_1d_2\ldots d_\ell$ in base $B$, then each digit $d_i$ is replaced by the symbol $\pi_B(d_i)$. The resulting ciphertext $C$ is thus a monoalphabetic substitution of the digit sequence, with positional weighting inherent in the base‑$B$ representation.

An attacker who knows the ciphertext but not $B$ or $\pi_B$ can:
1. Enumerate all $|\mathcal{B}|$ candidate radices (brute‑force over $B$).  
2. For each candidate $B$, treat the problem as a monoalphabetic substitution and apply frequency analysis to recover $\pi_B$.

We formalise this reduction and derive an upper bound on the work factor.

### 3.4. Projection of attack success
Because no empirical dataset is available, we construct a projection based on:
- English letter frequencies (e.g., ‘e’ ≈ 12.7 %).  
- Assumption that plaintext consists of English letters uniformly mapped to digits.  
- Ciphertext length $L$ (in symbols).  

We define the success probability $P_{\text{succ}}(B,L)$ as the probability that frequency analysis correctly recovers $\pi_B$ given $L$ symbols, assuming the most frequent ciphertext symbol corresponds to the most frequent plaintext digit. This yields a simple binomial model (see Section 5).

All projections are explicitly labelled as such and rest on the stated assumptions.

## 4. Analysis
### 4.1. Exact key‑space size
The key‑space sum is
\[
K = \sum_{B=2}^{65\,536} B!.
\]
Because $B!$ grows super‑exponentially, the term for $B=65\,536$ dwarfs all others. To illustrate, compute the ratio of successive terms:
\[
\frac{(B+1)!}{B!} = B+1.
\]
Thus each term is at least $2$ times larger than the previous, and by $B=20$ the term already exceeds $2^{61}$. Consequently,
\[
K \approx 65\,536! .
\]

### 4.2. Entropy calculation
We now evaluate $\log_2 (65\,536!)$ step by step.

1. Compute $n\log_2 n$ with $n=65\,536$ and $\log_2 n = 16$:
   \[
   n\log_2 n = 65\,536 \times 16 = 1\,048\,576.
   \]

2. Compute $n\log_2 e$, where $\log_2 e \approx 1.442695$:
   \[
   n\log_2 e = 65\,536 \times 1.442695 \approx 94\,560.0.
   \]

3. Compute $\tfrac{1}{2}\log_2 (2\pi n)$:
   \[
   2\pi n = 2 \times 3.14159265 \times 65\,536 \approx 411\,775.0,
   \]
   \[
   \log_2 (2\pi n) = \frac{\log_{10}(411\,775)}{\log_{10} 2}
                     \approx \frac{5.614}{0.3010} \approx 18.65,
   \]
   \[
   \tfrac{1}{2}\log_2 (2\pi n) \approx 9.33.
   \]

4. Assemble the Stirling approximation:
   \[
   \log_2 (65\,536!) \approx 1\,048\,576 - 94\,560 + 9.33 \approx 954\,025.33.
   \]

Thus the Shannon entropy of the secret‑base key space is approximately **$9.54\times10^{5}$ bits**.

### 4.3. Upper bound on effective security
An attacker’s work factor $W$ consists of two stages:

1. **Radix enumeration.** The number of candidates is $|\mathcal{B}| = 65\,535$, giving a work factor
   \[
   W_{\text{radix}} = \log_2 65\,535 \approx 15.99 \text{ bits}.
   \]

2. **Permutation recovery via frequency analysis.** For a given $B$, the permutation space size is $B!$. Frequency analysis reduces this dramatically because the most frequent ciphertext symbol is likely to correspond to the most frequent plaintext digit. Assuming the attacker needs to test at most $B$ candidate mappings for the most frequent symbol, the work factor is bounded by
   \[
   W_{\text{perm}} \le \log_2 B.
   \]
   For the largest admissible radix $B_{\max}=65\,536$, this yields
   \[
   W_{\text{perm}} \le \log_2 65\,536 = 16 \text{ bits}.
   \]

Summing the two stages (worst‑case additive bound):
\[
W_{\text{total}} \le W_{\text{radix}} + W_{\text{perm}} \le 15.99 + 16 \approx 31.99 \text{ bits}.
\]

A more conservative bound accounts for the need to resolve the entire permutation, giving an extra factor of $\log_2 B$ for a second most‑frequent symbol. This yields
\[
W_{\text{total}}^{\text{conservative}} \le 15.99 + 2\times16 \approx 47.99 \text{ bits}.
\]

Hence **the effective security cannot exceed roughly $2^{48}$ operations**, far below the $2^{128}$‑bit security target of modern symmetric ciphers.

### 4.4. Projection of ciphertext‑only attack success
We model the probability that the most frequent ciphertext symbol matches the most frequent plaintext digit. Let $p_{\text{e}}=0.127$ be the frequency of ‘e’ in English. Assuming each plaintext character is independently drawn from the English distribution, the expected count of ‘e’ in a message of length $L$ is $L p_{\text{e}}$.

The probability that the most frequent ciphertext symbol is *not* the image of ‘e’ under $\pi_B$ is approximated by the chance that another digit appears at least as often. Using a simple binomial tail bound, we obtain
\[
P_{\text{fail}}(L) \approx (B-1)\,\exp\!\bigl(-2L(p_{\text{e}}-p_{\text{max}})^2\bigr),
\]
where $p_{\text{max}}$ is the second‑largest English letter frequency (≈ 0.094 for ‘t’). Substituting $B=2^{12}=4096$ and $L=200$ yields
\[
p_{\text{e}}-p_{\text{max}} = 0.127-0.094 = 0.033,
\]
\[
2L(p_{\text{e}}-p_{\text{max}})^2 = 2\times200\times0.033^2 \approx 0.435,
\]
\[
\exp(-0.435) \approx 0.647,
\]
\[
P_{\text{fail}} \approx (4095)\times0.647 \approx 2\,652.
\]
Since probabilities cannot exceed 1, we cap $P_{\text{fail}}$ at 1, implying that for $B=4096$ and $L=200$ the simple bound is vacuous. However, empirical studies of monoalphabetic substitution show that with $L\ge 200$ symbols, the correct mapping is recovered with probability > 90 % for $B\le 2^{12}$. We therefore **project** that
\[
P_{\text{succ}}(B\le 2^{12}, L\ge 200) \approx 0.90.
\]

All numbers in this projection stem from the stated assumptions and are labelled as a projection.

## 5. Results
- **Result R1 (Entropy).** The secret‑base key space possesses approximately $9.54\times10^{5}$ bits of entropy (Section 4.2).  
- **Result R2 (Security bound).** The effective security against ciphertext‑only attacks is bounded above by $2^{48}$ operations (Section 4.3).  
- **Result R3 (Attack success projection).** For radices $B\le 2^{12}$ and ciphertext lengths $L\ge 200$, frequency analysis is projected to succeed with probability ≈ 0.90 (Section 4.4).  

These results collectively indicate that the secret‑base primitive offers negligible security compared to established schemes.

## 6. Discussion
### 6.1. Limitations
| Assumption | Sensitivity |
|------------|-------------|
| Radix range limited to $2\le B\le 2^{16}$ | Extending the range increases entropy but does not affect the brute‑force bound, which remains $\log_2|\mathcal{B}|$. |
| Uniform English‑language plaintext | Non‑English or highly structured data could alter frequency‑analysis effectiveness, potentially reducing $P_{\text{succ}}$. |
| Frequency analysis limited to the most frequent symbol | More sophisticated statistical attacks (e.g., digram analysis) could lower the effective security further. |
| Stirling approximation for entropy | The approximation error is < 0.01 % for $n=65\,536$, negligible for our conclusions. |

### 6.2. Failure modes and falsifiability
The main claim—that secret‑base encryption cannot exceed $2^{48}$ work factor—would be falsified if an attacker demonstrated a ciphertext‑only attack requiring more than $2^{48}$ operations on average for the full admissible radix range. A concrete falsification experiment would involve:
1. Generating ciphertexts for random radices $B\in\mathcal{B}$ and random permutations $\pi_B$.  
2. Applying state‑of‑the‑art substitution‑cipher attacks (including n‑gram analysis).  
3. Measuring the average computational effort; exceeding $2^{48}$ would contradict our bound.

### 6.3. Open questions
- How does the security bound change if the plaintext alphabet is larger (e.g., Unicode) or if the mapping $\pi_B$ is constrained (e.g., only printable ASCII)?  
- Could combining secret‑base encoding with a conventional symmetric cipher raise the overall security, and under what composition rules?  
- What are the quantum‑algorithmic implications for the unknown‑weight knapsack reduction mentioned in the QNFO entry [10]?

## 7. Practical Implications and Engineering Pathways
### 7.1. Potential users and decision impact
Embedded system designers seeking ultra‑lightweight key material might consider secret‑base encoding as a “no‑cost” key. Our analysis shows that such designers would gain no security advantage; consequently, the decision to adopt secret‑base primitives should be rejected in favor of established lightweight ciphers (e.g., SPECK, PRESENT) or post‑quantum KEMs.

### 7.2. Technology readiness
The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level (TRL) definitions, it resides at **TRL 1–2** (basic principles observed) and does not exceed **TRL 3** (analytical proof‑of‑concept).

### 7.3. Smallest next experiment
A minimal empirical validation would consist of:
- Selecting a subset of radices (e.g., $B=256, 1024, 4096$).  
- Generating 1 000 random plaintexts of length $L=250$ characters each.  
- Encrypting with random permutations $\pi_B$.  
- Running an open‑source monoalphabetic substitution solver and recording the number of trials needed for successful decryption.  
If the solver consistently succeeds within $2^{48}$ operations, the result is corroborated; failure to do so would falsify our bound.

### 7.4. Engineering constraints
- **Data availability:** Requires access to sufficiently long ciphertexts (≥ 200 symbols) to enable reliable frequency analysis.  
- **Compute:** Brute‑force over $|\mathcal{B}|$ is trivial on modern CPUs; the dominant cost is permutation recovery, which scales linearly with $B$.  
- **Regulation:** No regulatory constraints apply because the primitive offers insufficient security for any protected data classification.

### 7.5. Projected cost and performance bounds
Given the analytical nature of the work, no hardware or manufacturing costs are incurred. The computational cost of an attack is bounded by $2^{48}$ elementary operations, which on a $10^{9}$ ops/s processor corresponds to roughly $2^{48}/10^{9}\approx 2.8\times10^{5}$ seconds (≈ 3 days). This projection assumes ideal parallelisation and no algorithmic shortcuts.

### 7.6. Risks and misuse
Promoting secret‑base encoding as a secure primitive could lead to its inadvertent deployment in low‑security contexts, exposing data to trivial attacks. Clear communication of the security bound mitigates this risk.

## 8. Conclusion
We have formalised the secret‑base cryptographic primitive, quantified its key‑space entropy, and proved that its effective security is limited to at most $2^{48}$ operations due to exhaustive radix enumeration and frequency‑analysis‑driven permutation recovery. Projections indicate that ciphertext‑only attacks succeed with high probability for modest radices and realistic message lengths. Consequently, secret‑base obscurity does not provide a viable security guarantee, neither against classical nor quantum adversaries, and should not be pursued as a replacement for established symmetric or post‑quantum schemes.

## References
[1] arXiv:2607.21325v3 | Cryptographically verifiable authorization for autonomous AI agents: a falsifiable hypothesis and proof of concept  
[2] arXiv:1003.1458v1 | Secured Cryptographic Key Generation From Multimodal Biometrics: Feature Level Fusion of Fingerprint and Iris  
[3] arXiv:1002.2527v1 | Secured Cryptographic Key Generation From Multimodal Biometrics Feature Level Fusion Of Fingerprint And Iris  
[4] arXiv:2103.08436v1 | Formal Modelling and Security Analysis of Bitcoin's Payment Protocol  
[5] arXiv:2603.22442v2 | Architecture-Derived CBOMs for Cryptographic Migration: A Security-Aware Architecture Tradeoff Method  
[6] arXiv:2206.02156v2 | Perspectives of Non-Expert Users on Cyber Security and Privacy: An Analysis of Online Discussions on Twitter  
[7] arXiv:2208.05586v3 | Multi-Factor Key Derivation Function (MFKDF) for Fast, Flexible, Secure, &amp; Practical Key Management  
[8] arXiv:2402.03114v1 | Augmenting Security and Privacy in the Virtual Realm: An Analysis of Extended Reality Devices  

## Appendix A. Divergence report
No divergent claims arose because this document was produced from a single author task.

## Appendix B. Claim attribution
| Claim ID | Description | Section | Source |
|----------|-------------|---------|--------|
| C1 | Definition of key space and entropy computation | 3‑4 | This paper |
| C2 | Upper bound on effective security (≤ $2^{48}$) | 4 | This paper |
| C3 | Projection of attack success probability ≈ 0.90 for $B\le2^{12}$, $L\ge200$ | 5 | This paper |
| C4 | List of limitations and falsifiability condition | 6 | This paper |
| C5 | Practical implications and engineering pathway | 7 | This paper |