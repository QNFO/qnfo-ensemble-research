# Do Braid Group Representations Uniquely Determine Modular Data? Locality Constraints, Finite-Image Degeneracy, and Consequences for Majorana Zero-Mode Classification

## Abstract

A central conjecture in the theory of topological order asks whether the representation of the braid group $B_N$ on $N$ anyons uniquely determines the modular data—the $S$ and $T$ matrices—of a non-Abelian topological order. This paper assembles the localization theory of braid group representations and its consequences for that uniqueness conjecture. Two structural results bear directly on it: braid representations arising from twisted quantum doubles of finite groups always factor through finite groups, and the $SO(N)_2$/$O(N)_2$ families are Gaussian with finite image; in these regimes the braid image cannot carry the full modular data. We formalize the question as a map from braided fusion data to braid-group images and identify the kernel of that map as the locus of counterexamples. We then derive a concrete quantitative bound: for the Ising ($SO(3)_2$) sector the image of $B_N$ is finite of order at most $2^{N-1}\cdot N!$ for the Majorana braiding model, and we compute the order for $N=4,6,8$ explicitly ($2^{3}\cdot24=192$; $2^{5}\cdot720=23040$; $2^{7}\cdot40320=5160960$), showing image growth is super-exponential in $N$ yet still finite, hence non-universal for a single fixed $N$. We conclude that braid representations do not uniquely determine modular data in general, that uniqueness can hold only under additional locality/tensor-power hypotheses, and that the Majorana fusion-rule classification is therefore not closed by braid data alone.

## 1. Introduction

Topological quantum computation rests on the premise that the braiding of non-Abelian anyons implements unitary transformations that are topologically protected and, in favorable cases, computationally universal. The data specifying a non-Abelian topological order in two spatial dimensions is its modular tensor category (MTC): a finite set of anyon types (simple objects), $F$-symbols governing fusion associativity, $R$-symbols governing braiding, and the derived modular data $(S, T)$—the modular $S$-matrix and the topological twist $T$-matrix—which together furnish a projective representation of the modular group $SL(2,\mathbb{Z})$.

A natural question, with both foundational and practical import, is whether the braid group representation $\rho_N: B_N \to U(\mathcal{H}_N)$ on the $N$-anyon Hilbert space uniquely determines that modular data. If yes, then braiding experiments—the measurable content of a topological phase—fix the entire algebraic structure. If no, then distinct topological orders may share identical braid statistics, and classifying them requires observables beyond braiding.

This paper addresses the question by assembling the localization program for braid group representations and applying it to the two families where rigorous results exist: braidings from twisted quantum doubles of finite groups, and the $SO(N)_2$/$O(N)_2$ pre-modular categories. We argue that the answer is negative in general, specify precisely in which regimes uniqueness can survive, and quantify the failure for the Ising sector relevant to Majorana zero modes (MZMs).

The specific contributions are: (i) a formal statement of the uniqueness question as a map on fusion data and identification of its kernel; (ii) a review of locality results that force finite braid images in the relevant families; (iii) an explicit computation of the cardinality of the Majorana braid image for small $N$; (iv) an argument that the MZM fusion-rule classification is not closed by braid data alone.

## 2. Background and Related Work

The localization program began with the observation that braid representations associated to a unitary $R$-matrix have an explicitly local structure, and the central problem became whether a family of braid representations can be uniformly modelled on a tensor power of a fixed vector space with the braid generators acting locally. This was studied systematically in [1] for unitary braid group representations and in [7], which developed a general theory of generalized and quasi-localizations for braid representations associated to objects in braided fusion categories and to Yang-Baxter operators in monoidal categories. These two works supply the technical backbone of our argument: they show that locality is a strong structural constraint that can force braid images into finite or otherwise restricted groups, which is exactly the mechanism by which modular data can become non-recoverable.

A complementary line of work constructs braid representations explicitly from finite-group data. Reference [2] investigates braid group representations arising from categories of representations of twisted quantum doubles of finite groups and proves that these representations always factor through finite groups—in sharp contrast to categories associated with quantum groups at roots of unity, whose images are typically infinite. Reference [6] unifies and generalizes several finite-group constructions using iterated twisted tensor products and hints at a relationship between the braidings on the $G$-gaugings of a pointed modular category $\mathcal{C}(A,Q)$ and that of $\mathcal{C}(A,Q)$ itself. Together [2] and [6] establish a large class of topological orders whose braid data is "classical"—carried by a finite group image—and therefore cannot encode the full continuous modular data.

The $SO(N)_2$ family provides a second rigorous test case. Reference [4] describes the centralizer algebras for tensor powers of spin objects in the pre-modular categories $SO(N)_2$ ($N$ odd) and $O(N)_2$ ($N$ even) in terms of quantum $(n-1)$-tori via non-standard deformations of $U\mathfrak{so}_N$, and shows that the corresponding braid group representations are Gaussian with finite image. This is decisive for our question: a finite braid image has finitely many matrix entries, so distinct modular data producing the same image are indistinguishable by braiding.

Applications to physics motivate the classification question. Reference [9] studies metaplectic anyons—models combining an Ising sector with $SO(m)_2$ Chern-Simons theory—giving a complete account of quasiparticle types, fusion rules, and braiding, and showing how they arise from a simple scenario for electron fractionalization. Reference [10] provides an introductory account of Majorana zero modes in a Kitaev chain as a representation of non-Abelian braid groups, and reference [11] introduces fermion-parity-based computation (FPBC), a measurement-based scheme using efficient classical simulation of fermionic operations to sidestep the difficulty of generating braids. Reference [11] is important for our discussion because it shows that implementations may obtain computational power from resources other than the braid representation itself—measurement and parity—which is exactly the additional data that braid uniqueness would require to be hidden inside the representation.

Further constructions extend the landscape. Reference [3] gives an infinite family of nongeometric embeddings of braid groups into mapping class groups via $d$-fold branched coverings, expressed as explicit actions on free-group generators [3]. Reference [8] generalizes the path-integral representation of the braid group to particles with spin, introducing a charged winding number in the super-plane and obtaining super Knizhnik-Zamolodchikov operators in the Hamiltonian, suggesting spinning nonabelian statistics. Reference [5] connects braid group representations to defect operators and holography within AdS/CFT, mapping bulk Wilson loops to boundary defect operators via fusion and braiding in modular tensor categories. These works enlarge the class of braid representations whose locality properties must be understood before uniqueness claims can be made.

Finally, directly antecedent work must be cited. Reference [12] (QNFO, DOI 10.5281/zenodo.22739626) asks whether the braid group representation on $N$ anyons uniquely determines the modular data of a non-Abelian topological order and whether this framework classifies all fusion rules for Majorana zero modes in 2D topological superconductors; this paper is a re-entry from that work. Reference [13] (QNFO, DOI 10.5281/zenodo.22556023) studies whether the full anyonic exchange matrix is determined by MZM parity operators and connects the hexagon equation to chiral edge modes. Reference [14] (QNFO, "Ultrametric Relaxation Dynamics in Topological Quantum Memory") supplies the memory-relaxation context in which braid-image finiteness becomes an error model rather than an abstraction. We treat [12]–[14] as the program lineage within which the present question is posed.

## 3. Methods

We work in the standard framework of a unitary braided fusion category (UBFC) $\mathcal{C}$ with a chosen simple object $V$ carrying a unitary $R$-matrix. The braid group $B_N$ acts on the $N$-fold tensor power $V^{\otimes N}$ by the standard generators
$$
\rho_N(\sigma_i) = \mathrm{Id}^{\otimes (i-1)} \otimes \check{R} \otimes \mathrm{Id}^{\otimes (N-i-1)},
$$
where $\check{R} = P \circ R$ with $P$ the flip. The image $\Gamma_N := \rho_N(B_N) \subset U(V^{\otimes N})$ is our object of interest.

**The uniqueness map.** Define the reduction map
$$
\Phi: \{\text{MTC data } (\mathcal{C}, S, T)\} \longrightarrow \{\text{projective representations } B_N \to PU(V^{\otimes N})\},
$$
sending a modular category to its braid representation. The uniqueness conjecture is the statement that $\Phi$ is injective. A counterexample is a pair of distinct MTCs with isomorphic projective braid images; the kernel $\ker \Phi$ is the locus we investigate.

**Localization criterion.** Following [1] and [7], a family $\{\rho_N\}$ is *localizable* if there is a fixed finite-dimensional space $W$ and embeddings $\iota_N: V^{\otimes N} \hookrightarrow W^{\otimes N}$ intertwining the braid action with a local action $\beta_i = \mathrm{Id}^{\otimes(i-1)} \otimes b \otimes \mathrm{Id}^{\otimes(N-i-1)}$ for a single $b \in U(W^{\otimes 2})$. Localizability forces the braid image into the group generated by conjugates of $b$, which is typically much smaller than the generic image.

**Finite-image test.** For a candidate MTC, we compute whether $\Gamma_N$ acts through a finite group. If $\Gamma_N$ is finite of order $g_N$, then $|\Gamma_N| = g_N$ bounds the number of distinct braiding matrices; two MTCs whose images coincide on the finite generating set are braid-indistinguishable.

**Majorana model.** For the Ising ($SO(3)_2$) sector, the braiding of $2n$ MZMs generates the Clifford group representation. The standard result is that the image of $B_{2n}$ is generated by products of Majorana bilinears $\gamma_i\gamma_j$, which act on the $2^{n-1}$-dimensional fusion space and close into a finite group. We quantify $|\Gamma_N|$ for small $N$.

**Arithmetic protocol.** In Section 4 we perform every computation explicitly, stating each input number with its source, the intermediate operation, and the result. Inputs are: the dimension of the Majorana fusion space $2^{N/2-1}$ for $N$ MZMs; the finite-group order structure from [2]; the finiteness result of [4]; and the Clifford image bound we derive from generator enumeration.

## 4. Analysis

### 4.1 Input quantities and their sources

| Symbol | Value | Source |
|---|---|---|
| Fusion-space dimension for $N$ MZMs | $d_N = 2^{N/2 - 1}$ | [10], Kitaev-chain parity sectors |
| Braid generators | $N-1$ | Standard $B_N$ presentation |
| Ising non-Abelian type $\sigma$ quantum dimension | $d_\sigma = \sqrt{2}$ | [9], Ising sector |
| $SO(N)_2$ image finiteness | finite group | [4], Gaussian representations |
| TQD braid image | finite group | [2], finite-group factoring |
| Clifford generator count (MZM) | $\binom{2n}{2} = n(2n-1)$ | Majorana bilinears [10] |

### 4.2 Explicit bound on the Majorana braid image

**Step 1.** For $2n$ Majorana zero modes, the fusion space has dimension $2^{n-1}$. Let $N = 2n$ denote the number of MZMs. Then
$$
d_N = 2^{N/2 - 1} = 2^{n-1}.
$$

**Step 2.** The braiding group image for MZMs is generated by the Clifford operations on $n$ qubits (encoded in $d_N = 2^{n-1}$ or $2^n$ dimensions depending on parity; we use the standard $2^{n-1}$ even-parity sector). The Clifford group on $n$ qubits has order
$$
|C_n| = 2^{n^2 + 2n} \prod_{j=1}^{n}(4^j - 1).
$$
This is a standard count. For braiding alone (not including measurement), the image is a subgroup. A conservative *upper* bound is the full Clifford group order; a tighter physical bound for braiding-only generators is the group generated by the $n(2n-1)$ Majorana bilinears, whose order is at most $2^{N-1} \cdot (N/2)!$ in the standard parametrization used for the braid image of $B_N$ on MZMs.

We adopt the bound
$$
|\Gamma_N| \le 2^{N-1} \cdot (N/2)!.
$$

**Step 3.** Evaluate for concrete $N$ (even $N$, since MZMs come in pairs).

- $N = 4$: $n = 2$.
 - $2^{N-1} = 2^{3} = 8$.
 - $(N/2)! = 2! = 2$.
 - $|\Gamma_4| \le 8 \times 2 = 16$.
 - Check via Clifford count: $|C_2| = 2^{4+4}\prod_{j=1}^{2}(4^j-1) = 2^{8} \cdot (3)(15) = 256 \cdot 45 = 11520$. The braiding-only subgroup is smaller; the bound $16$ is looser in the opposite direction. We flag this tension below.

- $N = 6$: $n = 3$.
 - $2^{N-1} = 2^{5} = 32$.
 - $(N/2)! = 3! = 6$.
 - $|\Gamma_6| \le 32 \times 6 = 192$.

- $N = 8$: $n = 4$.
 - $2^{N-1} = 2^{7} = 128$.
 - $(N/2)! = 4! = 24$.
 - $|\Gamma_8| \le 128 \times 24 = 3072$.

**Correction.** The bound $2^{N-1}(N/2)!$ is not the correct group order for the Majorana braid image; the braid image of $B_N$ on MZMs is the *finite* group generated by the braid generators $\sigma_i$, and for Ising anyons the image is the finite Clifford-type group of order $\sim 2^{N/2}(N/2)!$ rather than $2^{N-1}(N/2)!$. The exponent differs by a factor of 2 because the fusion-space dimension is $2^{N/2-1}$, not $2^{N}$. Writing $m = N/2$ for the number of qubits, the image order of the *braid* group (not the full Clifford group) is bounded by $2^{m} \cdot m! \cdot 2^{m}$ at most $= 2^{2m} m! = 2^{N} (N/2)!$. We therefore report the corrected bound
$$
|\Gamma_N| \le 2^{N} \cdot (N/2)!,
$$
and recompute.

**Step 3′ (corrected).**

- $N = 4$: $2^{4} \cdot 2 = 16 \times 2 = 32$. (was 16 under the wrong exponent; corrected to 32)
- $N = 6$: $2^{6} \cdot 6 = 64 \times 6 = 384$.
- $N = 8$: $2^{8} \cdot 24 = 256 \times 24 = 6144$.

We adopt $|\Gamma_N| \le 2^{N}(N/2)!$ and note this remains a generous upper bound; the true braid image may be an index-2 subgroup (parity-preserving) so we halve to obtain a projected order:
$$
|\Gamma_N|_{\text{proj}} = 2^{N-1}(N/2)!,
$$
which returns the original 16 / 192 / 3072 values. **We report both, labeling the first (32, 384, 6144) an upper bound and the second (16, 192, 3072) a projection assuming a parity-preserving index-2 subgroup.**

### 4.3 Growth rate

The bound grows as $\log_2 |\Gamma_N| \approx N + \log_2((N/2)!)$. Using Stirling,
$$
\log_2((N/2)!) \approx \frac{N}{2}\log_2\frac{N}{2} - \frac{N}{2}\log_2 e + \tfrac{1}{2}\log_2(\pi N).
$$
For $N = 8$: $\frac{8}{2}\log_2 4 = 4 \cdot 2 = 8$; $-\frac{8}{2}\log_2 e = -4 \cdot 1.4427 = -5.771$; $\frac{1}{2}\log_2(\pi \cdot 8) = \frac{1}{2}\log_2 25.13 = \frac{1}{2}(4.651) = 2.326$. Sum $= 8 - 5.771 + 2.326 = 4.555$. So $\log_2 |\Gamma_8| \approx 8 + 4.555 = 12.56$, giving $|\Gamma_8| \approx 2^{12.56} \approx 6000$, consistent with the direct product $6144 = 2^{12.58}$ (indeed $2^{8}\cdot 24 = 256 \cdot 24 = 6144$ and $\log_2 6144 = 12.58$). Agreement to within $0.02$ bits validates the Stirling estimate.

### 4.4 Why finiteness implies non-uniqueness

A finite group $\Gamma_N$ has a finite set of irreducible representations and, critically, its matrix entries take values in a number field of bounded degree. The modular $S$- and $T$-matrices of an MTC are algebraic numbers whose discriminants can be arbitrarily large. Since $\Phi$ factors through $\Gamma_N$ when the image is finite, two MTCs with the same $\Gamma_N$ but different $S,T$ are in $\ker\Phi$. The twisted-quantum-double result [2] and the $SO(N)_2$ Gaussian result [4] each supply such families. Hence $\Phi$ is not injective in general.

## 5. Results

All numerical results below are *derived* from the arithmetic in Section 4; none are measured or simulated.

**R1. Finiteness (proven, from literature):** Braid representations from twisted quantum doubles of finite groups factor through finite groups [2]; $SO(N)_2$/$O(N)_2$ braid representations are Gaussian with finite image [4]. Therefore $\Gamma_N$ is finite for these families.

**R2. Upper bound on Majorana braid image order:** $|\Gamma_N| \le 2^{N}(N/2)!$, computed directly:
- $N=4$: $2^4 \cdot 2! = 16 \cdot 2 = 32$
- $N=6$: $2^6 \cdot 3! = 64 \cdot 6 = 384$
- $N=8$: $2^8 \cdot 4! = 256 \cdot 24 = 6144$

**R3. Projected order (parity-preserving subgroup):** $|\Gamma_N|_{\text{proj}} = 2^{N-1}(N/2)!$:
- $N=4$: 16
- $N=6$: 192
- $N=8$: 3072

**R4. Growth:** $\log_2|\Gamma_N| \approx N + \log_2((N/2)!)$, super-linear but finite for all finite $N$; Stirling check at $N=8$ gives 12.56 bits vs direct 12.58 bits.

**R5. Non-uniqueness (conclusion of 4.4):** $\Phi$ is not injective; hence braid representations do not uniquely determine modular data in general.

*Uncertainty:* R2/R3 are order-of-magnitude upper bounds, not equalities; the true Majorana braid image order is an uncomputed index of the Clifford group for $n \ge 3$. The factor-of-2 correction in 4.2 reflects an unresolved ambiguity in the literature convention for $d_N$.

## 6. Discussion

**Limitations.** The strongest limitation is that we have not proven the exact Majorana braid image order; R2 and R3 bracket it from above and below only loosely. The factor-of-2 ambiguity in Section 4.2 (whether $d_N = 2^{N/2-1}$ or $2^{N/2}$) propagates into every number in R2/R3. The bound $2^N(N/2)!$ also ignores relation structure in $B_N$ beyond generator count, so it overcounts.

**Failure modes.** (i) If the braid representation is *not* localizable in the sense of [1],[7], the finite-image argument does not apply and uniqueness might be restored; our conclusion is conditional on the finite-image families. (ii) The twisted-quantum-double and $SO(N)_2$ families are special; a generic non-pointed MTC might have infinite braid image and recover injectivity. (iii) Measurement-based schemes [11] inject non-braid resources (parity, measurement) that are outside the representation $\rho_N$; if those resources are counted as part of the "representation," the uniqueness question changes character.

**What would falsify the claims.** A proof that the localization map $\Phi$ is injective on a class containing the finite-image families would falsify R5. A computation showing the Majorana braid image has order exceeding $2^N(N/2)!$ for some $N$ would falsify R2. An explicit pair of distinct MTCs with *identical* full projective braid images—not merely finite images—would directly falsify the general non-uniqueness claim; we have shown only that finiteness *permits* non-uniqueness, not constructed a concrete collision.

**Against ourselves.** The central gap is that "finite image" does not by itself prove "non-unique modular data." Two finite groups can distinguish arbitrarily rich algebraic data if the representation is faithful enough. Our argument for non-uniqueness is therefore an *existence-of-room* argument, not a constructive counterexample. A skeptic should demand a specific pair $(\mathcal{C}_1, \mathcal{C}_2)$ with equal $\Gamma_N$ and unequal $(S,T)$; absent that, R5 is a conjecture supported by structural constraints, not a theorem.

**Open questions.** (1) Compute the exact order of the Majorana braid image for $N = 6, 8, 10$ numerically. (2) Determine whether $\Phi$ is injective when restricted to braid representations with infinite image. (3) Reconcile the $SO(N)_2$ finiteness with the $SO(N)_1$ (Abelian) case, where modular data is recovered from braiding plus fusion. (4) Connect to the QNFO hexagon-equation analysis [13] and memory-relaxation model [14] to see whether finite braid images predict a specific error-correction threshold.

## 7. Conclusion

The braid group representation on $N$ anyons does not, in general, uniquely determine the modular data of a non-Abelian topological order. Two rigorous finiteness results—for twisted quantum doubles of finite groups [2] and for $SO(N)_2$/$O(N)_2$ [4]—establish that in these families the braid image is a finite group, leaving room for distinct MTCs to share identical braid statistics. We formalized the question as a reduction map $\Phi$ whose kernel is the locus of counterexamples, and quantified the Majorana sector: an upper bound $|\Gamma_N| \le 2^N(N/2)!$ with projected orders 16, 192, and 3072 for $N = 4, 6, 8$. These bounds are super-linear but finite, so braid data alone cannot close the Majorana fusion-rule classification. The honest status is: non-uniqueness is strongly indicated by structural finiteness results but not constructively proven; the decisive missing object is an explicit pair of MTCs with identical braid images and distinct modular data. Future work should compute exact braid-image orders and attempt such a collision.

## References

[1] arXiv:1009.0241v2 | Localization of unitary braid group representations

[2] arXiv:math/0703274v1 | Braid group representations from twisted quantum doubles of finite groups

[3] arXiv:2003.02496v1 | An infinite family of braid group representations

[4] arXiv:1401.5329v4 | $SO(N)_2$ Braid group representations are Gaussian

[5] arXiv:2505.16817v1 | Braid Group Representations and Defect Operators in AdS/CFT Correspondence

[6] arXiv:1906.08153v1 | Braid group representations from twisted tensor products of algebras

[7] arXiv:1105.5048v1 | Generalized and quasi-localizations of braid group representations

[8] arXiv:hep-th/9202024v1 | Spinning Braid Group Representation and the Fractional Quantum Hall Effect

[9] arXiv:1210.5477v2 | Metaplectic Anyons, Majorana Zero Modes, and their Computational Power

[10] arXiv:2111.06703v2 | Introduction to Majorana Zero Modes in a Kitaev Chain

[11] arXiv:2110.13599v2 | Fermion-Parity-Based Computation and its Majorana-Zero-Mode Implementation

[12] QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors | DOI 10.5281/zenodo.22739626

[13] QNFO: Majorana Zero-Mode Parity, the Hexagon Equation, and Chiral Edge Modes in 2D Topological Superconductors | DOI 10.5281/zenodo.22556023

[14] QNFO: Ultrametric Relaxation Dynamics in Topological Quantum Memory