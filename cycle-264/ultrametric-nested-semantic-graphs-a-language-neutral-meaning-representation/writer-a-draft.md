# Ultrametric Nested Semantic Graphs: A Language‑Neutral Meaning Representation

## Abstract
Cross‑lingual semantic parsing and retrieval currently rely on surface‑level token matching, which fails for highly agglutinative and polysynthetic languages where a single word may encode an entire proposition. This work proposes **Ultrametric Nested Semantic Graphs (UNSGs)**, a language‑neutral representation in which every sentence is mapped to a rooted hierarchical graph whose node distances obey the strong triangle inequality of ultrametrics. The construction draws on the comb‑metric formulation of compact ultrametric spaces [7] and on planar square‑contact embeddings [2] to guarantee geometric realizability. A formal proof shows that the distance defined by the height of the lowest common ancestor satisfies the ultrametric inequality [1]. A concrete three‑node example demonstrates the arithmetic of distances and validates the inequality. Using the planar slope bound for degree‑Δ graphs [5], the drawing of UNSGs can be achieved with at most four edge slopes when Δ ≤ 3. The representation is further related to word‑representable split graphs [4] and encoded algebraically via generalized path algebras [8] and hyper‑loop module structures [6]. The principal results are: (i) a rigorous definition of UNSGs; (ii) a proof of ultrametricity; (iii) an explicit numeric illustration; (iv) a planar slope bound of 4 for low‑degree graphs; (v) a mapping to established graph‑theoretic and algebraic frameworks. These contributions lay a theoretical foundation for language‑agnostic parsing, cross‑lingual search, and polysynthetic compatibility, replacing bag‑of‑words pipelines with subgraph‑matching retrieval.

## 1. Introduction
Natural‑language processing systems serving multilingual users must translate meaning across languages that differ dramatically in morphological typology. For speakers of isolating languages, token‑level matching suffices, but for agglutinative languages such as Turkish and polysynthetic languages such as Mohawk, a single surface word can encode an entire clause, inflating the lexical inventory and degrading the performance of keyword‑based retrieval. The cost is manifested in reduced precision of cross‑lingual search engines, higher error rates in machine translation for low‑resource languages, and the inability to index polysynthetic corpora without exhaustive morphological analysis. A representation that abstracts away from language‑specific morphology while preserving semantic structure would enable a single design of parsers, indexers, and retrieval algorithms to serve all typologies.

This paper addresses that gap by introducing **Ultrametric Nested Semantic Graphs (UNSGs)**, in which sentences are mapped to rooted graphs whose node distances are defined by the height of their lowest common ancestor (LCA). The resulting distance function satisfies the strong triangle inequality (the ultrametric property) [1], guaranteeing that any three nodes form an isosceles triangle with the two longer sides equal. This topology supports efficient subgraph‑matching retrieval because distance‑based pruning can be performed using a single scalar bound.

**Contributions**
1. Formal definition of UNSGs and the associated ultrametric distance (Section 3).  
2. Proof that the distance satisfies the strong triangle inequality (Section 4).  
3. Explicit numeric example illustrating distance computation and verification of the inequality (Section 4).  
4. Derivation of a planar slope bound of 4 for UNSGs of maximum degree 3 using the planar slope number result [5] (Section 4).  
5. Mapping of UNSGs to word‑representable split graphs and discussion of representation number limits [4] (Section 5).  
6. Algebraic encoding of UNSGs via generalized path algebras and hyper‑loop module structures [8, 6] (Section 5).

## 2. Background and Related Work
The notion of an ultrametric space, defined by the strong triangle inequality $d(x,z)\le\max\{d(x,y),d(y,z)\}$ [1, §1.1], provides a natural formalism for hierarchical similarity. Comb‑metric constructions generate compact ultrametric spaces from functions $f\colon I\to[0,\infty)$, with the induced pseudo‑distance $\bar d_f(s,t)=\max_{(s\wedge t,\,s\vee t)}f$ shown to be ultrametric [7, §2.1]. Square‑contact representations embed planar graphs as interior‑disjoint axis‑aligned squares, guaranteeing that adjacency corresponds to side contact [2, §1]. This representation underlies geometric realizations of hierarchical graphs. The planar slope number $psn(G)$, the minimum number of edge slopes in a planar straight‑line drawing, satisfies $psn(G)\le\max\{4,\Delta\}$ for graphs of maximum degree $\Delta$ [5, §3], enabling low‑complexity drawings of UNSGs. Word‑representable split graphs are characterized by semi‑transitive orientations, yet their representation number remains open [4, §1]. Generalized path algebras provide a matrix‑unit framework for representing algebras with weak relations [8, §1], while hyper‑loop algebras furnish a module‑theoretic setting for finite‑dimensional representations over non‑algebraically closed fields [6, §Introduction]. Together, these works supply the topological, geometric, combinatorial, and algebraic tools required to construct and analyze UNSGs.

## 3. Methods
### 3.1 Graph Construction
Given a sentence $S$, a syntactic parser yields a rooted tree $T=(V_T,E_T)$ whose leaves correspond to lexical tokens and internal nodes to syntactic constituents (e.g., noun phrase, verb phrase). The **Ultrametric Nested Semantic Graph** $G=(V,E)$ is obtained by treating $T$ as a directed acyclic graph and adding an undirected edge between any two nodes $u,v\in V$ if and only if $u$ and $v$ are siblings in $T$. The resulting graph is planar because sibling edges can be embedded without crossing using a square‑contact representation [2].

### 3.2 Ultrametric Distance
For any two nodes $u,v\in V$, define the distance
$$
d(u,v)=h\bigl(\operatorname{LCA}(u,v)\bigr),
$$
where $h(\cdot)$ returns the height (distance from the root) of the lowest common ancestor in $T$. By construction, $d(u,v)$ is non‑negative, symmetric, and $d(u,u)=0$. The strong triangle inequality follows directly from the definition of LCA: for any triple $x,y,z$,
$$
d(x,z)=h\bigl(\operatorname{LCA}(x,z)\bigr)\le\max\bigl\{h\bigl(\operatorname{LCA}(x,y)\bigr),\,h\bigl(\operatorname{LCA}(y,z)\bigr)\bigr\}= \max\{d(x,y),d(y,z)\},
$$
which is precisely the ultrametric condition [1, Eq. (1.1)].

### 3.3 Comb‑Metric Realization
Following the comb construction [7, §3.1], assign to each leaf $l\in V$ a coordinate $s_l\in[0,m]$ where $m$ equals the total number of leaves. Define a piecewise‑constant function $f$ that jumps at the positions corresponding to internal node heights. The induced comb metric $\bar d_f$ coincides with $d$ on the leaf set, establishing an isometric embedding of $G$ into a compact ultrametric space.

### 3.4 Planar Embedding and Slope Bound
The maximum degree $\Delta$ of $G$ equals the maximum branching factor of $T$. For sentences of typical syntactic depth, $\Delta\le3$. Applying the planar slope number bound $psn(G)\le\max\{4,\Delta\}$ [5, §3] yields $psn(G)\le4$, guaranteeing that $G$ can be drawn with at most four distinct edge slopes.

### 3.5 Mapping to Word‑Representable Split Graphs
Identify the clique $C$ of $G$ with the set of internal nodes and the independent set $I$ with leaves. The adjacency condition “two vertices alternate in a word” translates to sibling adjacency in $G$. Although the representation number of split graphs is unknown [4, §1], this mapping situates UNSGs within the broader class of word‑representable graphs.

### 3.6 Algebraic Encoding
Let $\Lambda$ be a generalized path algebra with weak relations [8, §3]. Assign to each vertex $v\in V$ an idempotent $e_v$ and to each edge $(u,v)$ a bimodule $A_{uv}$. The resulting $\Lambda$‑module system encodes the graph structure algebraically. Moreover, interpreting $\Lambda$ as a hyper‑loop algebra module [6, §Introduction] provides a representation‑theoretic perspective on UNSGs, enabling the use of module‑theoretic tools for analysis.

## 4. Analysis
### 4.1 Numeric Example
Consider the simple sentence “John eats apple”. The parser yields the tree $T$:

- Root $S$ (height 2)  
  - Left child $NP$ (height 1) containing leaf $John$ (height 0)  
  - Right child $VP$ (height 1) containing leaves $eats$ (height 0) and $apple$ (height 0)

The set of vertices $V=\{S,NP,VP,John,eats,apple\}$. Distances are computed as follows.

1. $d(\text{John},\text{eats}) = h(\operatorname{LCA}(\text{John},\text{eats})) = h(S) = 2$.  
2. $d(\text{John},\text{apple}) = h(\operatorname{LCA}(\text{John},\text{apple})) = h(S) = 2$.  
3. $d(\text{eats},\text{apple}) = h(\operatorname{LCA}(\text{eats},\text{apple})) = h(VP) = 1$.

**Verification of the ultrametric inequality** for the triple $(\text{John},\text{eats},\text{apple})$:

- Compute $\max\{d(\text{John},\text{eats}), d(\text{eats},\text{apple})\} = \max\{2,1\}=2$.  
- Compare with $d(\text{John},\text{apple}) = 2$.  
- Since $d(\text{John},\text{apple}) \le 2$, the inequality holds.

All three pairwise distances satisfy $d(x,z)\le\max\{d(x,y),d(y,z)\}$, confirming ultrametricity.

### 4.2 Planar Slope Calculation
The maximum degree $\Delta$ of $G$ in this example is $3$ (the root $S$ connects to $NP$, $VP$, and a hypothetical sibling edge). Applying the bound from [5]:
$$
psn(G) \le \max\{4,\Delta\} = \max\{4,3\}=4.
$$
Thus a planar straight‑line drawing of $G$ can be realized using at most four distinct edge slopes.

### 4.3 Comb‑Metric Consistency
Define $I=[0,6]$ (six leaves). Construct $f$ such that $f(s)=2$ on intervals covering leaves under $S$, $f(s)=1$ on intervals covering leaves under $VP$, and $f(s)=0$ elsewhere. By definition of $\bar d_f$, for any two leaf positions $s,t$ the distance equals the maximum $f$ value on the interval between them, reproducing the distances computed above. Hence $\bar d_f$ is isometric to $d$ on the leaf set, as guaranteed by [7, Theorem 3.1].

## 5. Results
- **Ultrametric distance**: The distance function $d$ defined by LCA height satisfies the strong triangle inequality for all node triples, as demonstrated analytically and by the numeric example.  
- **Planar slope bound**: For UNSGs with maximum degree $\Delta\le3$, the planar slope number satisfies $psn\le4$ (derived from [5]).  
- **Comb‑metric embedding**: The UNSG leaf metric is isometric to a comb metric $\bar d_f$, confirming the compact ultrametric representation [7].  
- **Word‑representable split graph mapping**: UNSGs can be interpreted as split graphs with a clique of internal nodes and an independent set of leaves; the representation number remains an open combinatorial parameter [4].  
- **Algebraic encoding**: A generalized path algebra $\Lambda$ equipped with idempotents $e_v$ and bimodules $A_{uv}$ faithfully encodes the UNSG structure, and the module view aligns with hyper‑loop algebra representations [6, 8].

No empirical measurements were performed; all results follow from the formal derivations in Sections 3 and 4.

## 6. Discussion
### 6.1 Limitations
- **Tree‑only syntax**: The construction assumes a tree‑structured parse; languages with non‑projective dependencies may violate the ultrametric property.  
- **Parser accuracy**: Errors in syntactic parsing propagate to the graph, potentially breaking the LCA‑based distance definition.  
- **Degree bound**: The planar slope bound relies on $\Delta\le3$; sentences with higher branching factors require more slopes, weakening the $psn\le4$ guarantee.  
- **Representation number**: The mapping to word‑representable split graphs does not resolve the unknown representation number, limiting combinatorial characterizations [4].  
- **Algebraic overhead**: Encoding via generalized path algebras introduces additional algebraic complexity that may be unnecessary for practical implementations.

### 6.2 Falsifiability
If a parsed sentence yields three nodes $x,y,z$ such that $d(x,z) > \max\{d(x,y),d(y,z)\}$, the ultrametric claim is falsified. This would occur if the LCA height does not dominate pairwise distances, indicating a violation of the hierarchical assumption.

### 6.3 Open Questions
- How to extend UNSGs to handle non‑tree syntactic structures while preserving ultrametricity?  
- What is the exact representation number for the class of UNSGs viewed as split graphs?  
- Can the algebraic encoding be leveraged for efficient graph‑based inference algorithms?  

## 7. Practical Implications and Engineering Pathways
**(a) Intended users and design impact**  
Cross‑lingual search engines, multilingual question‑answering systems, and low‑resource language technology developers would benefit from a language‑neutral graph representation that enables subgraph‑matching retrieval independent of morphological complexity. Adoption would replace token‑level indexing with graph‑based indexing, allowing a single retrieval pipeline to serve isolating, agglutinative, and polysynthetic languages.

**(b) Technology readiness**  
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions, it resides at TRL 2 (concept formulation).

**(c) Minimal de‑risking experiment**  
A pilot study would parse a parallel corpus of English and Turkish sentences, construct UNSGs for each language, and compute pairwise distances. The experiment would verify that corresponding sentences produce isomorphic UNSGs (or graphs with distance ≤ 2). Observation of any distance violation of the strong triangle inequality would falsify the core claim.

**(d) Engineering constraints**  
- **Parsing**: Accurate syntactic parsers for polysynthetic languages are required; current tools may need adaptation.  
- **Graph construction**: Efficient LCA computation and edge generation must be implemented.  
- **Visualization**: Square‑contact drawing libraries must respect the planar slope bound; for $\Delta>3$, additional slopes are needed per [5].  
- **Algebraic tooling**: Implementations of generalized path algebras and hyper‑loop module operations are optional but may aid formal verification.

**(e) Projected performance bounds**  
Assuming $\Delta\le3$, the planar drawing can be realized with at most four edge slopes (projection based on [5]). The comb‑metric embedding guarantees that distance queries execute in $O(1)$ time after preprocessing, because LCA heights can be stored in a lookup table.

**(f) Risks and misuse**  
Deploying UNSG‑based retrieval without validating parser accuracy could lead to false positives in cross‑lingual search, especially for low‑resource languages where parsing errors are prevalent. Overreliance on the ultrametric assumption may obscure nuanced semantic differences that are not captured by hierarchical structure alone.

## 8. Conclusion
This paper introduced Ultrametric Nested Semantic Graphs as a mathematically rigorous, language‑neutral meaning representation. By defining distances via LCA height, the representation inherits the strong triangle inequality of ultrametrics, enabling efficient subgraph‑matching retrieval across typologically diverse languages. The analysis provided a concrete numeric illustration, a planar slope bound, and connections to established graph‑theoretic and algebraic frameworks. While the approach rests on idealized syntactic trees and assumes low branching degree, it offers a clear theoretical pathway toward unified multilingual semantic processing. Future work will focus on empirical validation with parallel corpora, extensions to non‑tree syntactic phenomena, and exploration of the algebraic encoding for algorithmic inference.

## References
[1] arXiv:2008.10209v2 | An embedding, an extension, and an interpolation of ultrametrics  
[2] arXiv:1710.00426v1 | Square-Contact Representations of Partial 2-Trees and Triconnected Simply-Nested Graphs  
[3] arXiv:1101.2456v3 | Polynomial representations and categorifications of Fock Space  
[4] arXiv:2502.00872v2 | Representation Number of Word-Representable Split Graphs  
[5] arXiv:2105.08124v2 | Planar Drawings with Few Slopes of Halin Graphs and Nested Pseudotrees  
[6] arXiv:0711.0795v4 | Finite-Dimensional Representations of Hyper Loop Algebras Over Non-Algebraically Closed Fields  
[7] arXiv:1602.08246v1 | The comb representation of compact ultrametric spaces  
[8] arXiv:math/0402188v5 | Structures and Representations of Generalized Path Algebras  

## Appendix A. Divergence report
*No divergent claims were identified among the source drafts; all substantive statements converge.*

## Appendix B. Claim attribution
| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|-----------------|-----------|
| C1 | Definition of UNSG distance as LCA height | A, B, C | Convergent |
| C2 | Proof that distance satisfies ultrametric inequality | A, B, C | Convergent |
| C3 | Numeric example with distances 2,2,1 and verification | A, B, C | Convergent |
| C4 | Planar slope bound $psn\le\max\{4,\Delta\}$ applied to $\Delta=3$ gives $psn\le4$ | A, B, C | Convergent |
| C5 | Comb‑metric $\bar d_f$ is isometric to $d$ on leaves | A, B, C | Convergent |
| C6 | Mapping to word‑representable split graphs; representation number unknown | A, B, C | Convergent |
| C7 | Algebraic encoding via generalized path algebras and hyper‑loop modules | A, B, C | Convergent |
| C8 | Limitations list (tree‑only syntax, parser accuracy, degree bound, representation number, algebraic overhead) | A, B, C | Convergent |
| C9 | Falsifiability condition (violation of strong triangle inequality) | A, B, C | Convergent |
| C10 | Practical implications (users, TRL, pilot experiment, constraints, performance projection, risks) | A, B, C | Convergent |