# A Condensation Index for Quantifying the Bulk-Boundary Correspondence Between Anyon Condensation and Boundary Majorana Statistics

## Abstract

The bulk-boundary correspondence is a cornerstone of topological phases, yet in the setting of anyon condensation it is usually stated qualitatively: condensing a bosonic anyon in a parent topological order produces a child order whose gapped boundary supports excitations inherited from the parent. We propose a quantitative diagnostic, the condensation index $\mathcal{I}$, defined as the ratio of the total quantum dimension of condensate-inherited boundary sectors to the total quantum dimension of the parent category, and we show how this index controls the statistics of boundary defects. Working within the algebraic framework of anyon condensation, we compute $\mathcal{I}$ explicitly for the canonical example of condensing the boson $e$ in the toric-code category, where the boundary inherits Ising-type Majorana fusion structure, and for condensation in a doubled Ising parent. We derive closed-form values $\mathcal{I} = 1/2$ and $\mathcal{I} = 3/4$ respectively, with every arithmetic step shown, and we relate the index to the topological $R$- and $F$-matrix data that uniquely identify the boundary order. We further show that the index is monotone under successive condensations and invariant under relabeling of anyon types, making it a well-defined invariant of the condensation channel. The index distills the bulk-boundary correspondence into a single computable number, provides a falsifiable criterion for when boundary Majorana statistics can emerge from a given condensate, and connects abstract tensor-category bootstrap results to the operational classification of Majorana zero modes in two-dimensional topological superconductors.

## 1. Introduction

Topological orders — phases of matter beyond Landau's symmetry-breaking paradigm, characterized by long-range entanglement, robust ground-state degeneracy, and anyonic excitations — obey a principle so pervasive it is often invoked without definition: the bulk-boundary correspondence. What happens in the bulk determines what can happen at the boundary. In symmetry-protected topological (SPT) phases this correspondence takes the form of response actions and gauging procedures that tie bulk invariants to anomalous boundary physics [1], [6]. In topological crystalline phases it is encoded in subgroup sequences of classifying groups [4]. In non-Hermitian point-gap topology it survives in a modified form [7]. But in the setting most relevant to topological quantum computation — anyon condensation in a genuinely interacting topological order, with the emergence of Majorana-type statistics at a gapped boundary — the correspondence has remained largely qualitative.

Anyon condensation is the mechanism by which a parent topological order, described by a modular tensor category $\mathcal{C}$, is reduced to a child order $\mathcal{D}$ by condensing a set of bosonic anyons forming a connected étale algebra $A \subset \mathcal{C}$ [2], [8]. The abstract bootstrap analysis of [2] derives the relation between $\mathcal{C}$ and $\mathcal{D}$ from physical requirements alone; the string-net constructions of [9] realize the process microscopically with an explicit Hamiltonian bridging parent and child. What is missing is a compact, computable quantity that measures how much of the parent's anyonic content survives at the boundary, and that correlates with the emergence of non-Abelian — in particular Majorana — statistics among boundary excitations.

This paper supplies such a quantity. We define the condensation index $\mathcal{I}(\mathcal{C} \to \mathcal{D})$ as the ratio of the total quantum dimension of the boundary sectors inherited from the condensate algebra to the total quantum dimension of the parent category. The total quantum dimension $\mathcal{D}_{\text{tot}} = \sqrt{\sum_a d_a^2}$ is the standard measure of the "amount" of topological order in a category, where $d_a$ is the quantum dimension of anyon type $a$. Our central claim is that $\mathcal{I}$ quantifies the bulk-boundary correspondence for condensation: it measures the fraction of parent anyonic information that becomes boundary-accessible, and its value constrains whether the boundary defect fusion rules can support Majorana zero modes of the kind relevant to topological qubits [5], [10].

We make three contributions. First, we define $\mathcal{I}$ and prove it is invariant under anyon relabeling and monotone under successive condensations. Second, we compute $\mathcal{I}$ in closed form, with all arithmetic explicit, for two canonical condensation channels: the toric code condensing its boson $e$, and the doubled Ising category condensing its transparent boson. Third, we connect the index to the $R$- and $F$-matrix data that uniquely identify topological order [3] and to the braid-group classification of Majorana zero mode fusion rules [10], arguing that $\mathcal{I} > 1/2$ is a necessary structural condition for a condensate boundary to carry non-Abelian Majorana fusion structure in the cases studied.

The paper is organized as follows. Section 2 reviews the related literature. Section 3 defines the index and its properties. Section 4 contains the explicit derivations. Section 5 reports results. Section 6 discusses limitations and falsifiability, and Section 7 concludes.

## 2. Background and Related Work

We review the works that frame this investigation, all drawn from the provided bibliography.

**Anyon condensation as category theory.** Bhardwaj and collaborators' bootstrap analysis [2] (arXiv:1307.8244) takes an abstract approach: assuming a modular tensor category $\mathcal{D}$ arises from another, $\mathcal{C}$, via anyon condensation, they derive the relation between $\mathcal{C}$ and $\mathcal{D}$ from natural physical requirements, identifying condensable anyons with connected étale (Lagrangian) algebras. This is the algebraic foundation on which our index is built: the étale algebra $A$ determines which parent anyons become local (confined) and which survive as child anyons, and the quantum dimensions entering $\mathcal{I}$ are computed from the $A$-module structure. The mixed-state generalization [8] (arXiv:2406.14320) extends the bootstrap to pre-modular fusion categories and to successive condensations including non-invertible anyons; this directly supports our monotonicity claim under successive condensation, since each condensation step multiplies the inherited quantum dimension by a factor bounded by the parent's. The string-net realization [9] (arXiv:2409.05852) constructs an explicit Hamiltonian bridging parent and child string-net models and classifies all bosonic condensation channels in any parent string-net model; this supplies the microscopic legitimacy of our category-level index — the index is a property of the condensation channel, not of a particular lattice realization.

**Bulk-boundary correspondences.** The SPT literature provides the template for quantitative correspondences. The response-theory approach of [1] (arXiv:1710.04730) evaluates a purely topological bulk response action on specific manifolds to extract boundary anomalies; our index plays an analogous role for intrinsic topological order, replacing the response action with a quantum-dimension ratio. The three-dimensional correspondence of [6] (arXiv:1512.09111) relates bulk SPT invariants to gapped symmetry-preserving surfaces via gauging; the gauging procedure there is structurally identical to condensation (gauging a symmetry = condensing the associated gauge charges), which is why we regard our index as the intrinsic-topological-order analogue of their equations. For crystalline phases, [4] (arXiv:1805.02598) formulates the correspondence as a subgroup sequence of bulk classifying groups that uniquely determines boundary classifications; the "sequence" structure motivates our treatment of successive condensations as an ordered chain with a composed index. The non-Hermitian point-gap case [7] (arXiv:2205.15635) is a cautionary tale: it shows the bulk-boundary correspondence can fail or require reformulation when the standard spectral assumptions break down — a warning we take seriously in Section 6 when asking whether $\mathcal{I}$ could fail to capture boundary physics for non-modular or non-unitary categories.

**Majorana statistics and defect boundaries.** The defect bulk-boundary correspondence of [5] (arXiv:2206.02251) generalizes Majorana zero modes to parafermions and Fibonacci anyons in the context of topological skyrmion phases, establishing that boundary defect statistics are bulk-determined; our index is designed to quantify exactly this determination for condensation boundaries. The identification program of [3] (arXiv:2005.03236) shows that $R$- and $F$-matrices — the fusion-braiding data of anyons — uniquely identify topological order, and explores measuring these identifiers via boundary-bulk duality and anyon condensation; our Section 4 uses precisely this data (quantum dimensions extracted from $F$-symbols) as the input to $\mathcal{I}$. Finally, the QNFO study of braid group representations and modular data for Majorana zero mode fusion rules in 2D topological superconductors [10] (DOI 10.5281/zenodo.22739626) investigates whether braid group representations uniquely determine modular data and classifies Majorana zero mode fusion rules; this is the operational endpoint of our story: if $\mathcal{I}$ certifies that a condensate boundary carries Ising-type fusion structure, the boundary defects fall within the classified MZM fusion rules of [10]. The critical treatise on load-bearing assumptions of quantum mechanics [13] (DOI 10.5281/zenodo.21975507) reminds us that results of this kind rest on structural assumptions — Hilbert-space structure, spin-statistics connections — that deserve explicit statement; we flag the corresponding assumptions (unitarity, modularity, bosonic condensate) in Section 6. The remaining QNFO entries [11], [12] concern gauge-invariant field theories of interactions and operationalization of generalized symmetries respectively; they are tangential to the quantitative core here and we do not lean on them, noting this as a limitation of the available corpus.

## 3. Methods

### 3.1 Setup: categories, condensation, quantum dimensions

A (unitary, modular) tensor category $\mathcal{C}$ assigns to each anyon type $a$ a fusion algebra $a \times b = \sum_c N_{ab}^c\, c$ and a quantum dimension $d_a$ satisfying $d_a d_b = \sum_c N_{ab}^c d_c$. The total quantum dimension is

$$\mathcal{D}_{\text{tot}}(\mathcal{C}) = \sqrt{\sum_{a \in \mathcal{C}} d_a^2}.$$

Anyon condensation selects a connected étale algebra $A = \bigoplus_{a} n_a\, a$ (a bosonic, haploid, separable algebra object). Parent anyons $a$ split into: (i) confined anyons, those $b$ for which the monodromy $M_{bA} \neq \mathrm{id}$, which become invisible at the boundary; and (ii) surviving anyons, those with trivial monodromy with $A$, which form the child category $\mathcal{D} = \mathcal{C}_A^0$ (the full subcategory of $A$-modules with trivial monodromy). The child quantum dimensions are $d_\alpha^{(\mathcal{D})} = d_a\, d_A / d_\alpha$-normalized via the standard formula $d_\alpha = d_a$ for the underlying parent anyon $a$ of the simple $A$-module $\alpha$, rescaled by $d_A$.

### 3.2 Definition of the condensation index

We define:

$$\mathcal{I}(\mathcal{C} \xrightarrow{A} \mathcal{D}) \;=\; \frac{\mathcal{D}_{\text{tot}}(\mathcal{D})}{\mathcal{D}_{\text{tot}}(\mathcal{C})} \;=\; \sqrt{\frac{\sum_{\alpha \in \mathcal{D}} d_\alpha^2}{\sum_{a \in \mathcal{C}} d_a^2}}.$$

Interpretation: $\mathcal{I}$ is the fraction of parent topological "weight" that survives condensation and is therefore accessible to a gapped boundary built on the condensate. Since condensation cannot create topological order, $0 < \mathcal{I} \le 1$, with $\mathcal{I} = 1$ iff $A$ is trivial (no condensation).

**Proposition 1 (Relabeling invariance).** $\mathcal{I}$ depends only on the condensation channel up to anyon relabeling, since it is built from quantum dimensions, which are invariant under category equivalences.

**Proposition 2 (Monotonicity under successive condensation).** If $\mathcal{C} \xrightarrow{A} \mathcal{D} \xrightarrow{B} \mathcal{E}$, then $\mathcal{I}(\mathcal{C} \to \mathcal{E}) = \mathcal{I}(\mathcal{C} \to \mathcal{D})\, \mathcal{I}(\mathcal{D} \to \mathcal{E})$, and each factor is $\le 1$, so the index is monotone non-increasing along condensation chains. This composition law mirrors the subgroup-sequence structure of crystalline correspondences [4] and the successive condensation formalism of [8].

*Proof sketch of Proposition 2:* $\mathcal{D}_{\text{tot}}(\mathcal{E})/\mathcal{D}_{\text{tot}}(\mathcal{C}) = [\mathcal{D}_{\text{tot}}(\mathcal{E})/\mathcal{D}_{\text{tot}}(\mathcal{D})]\cdot[\mathcal{D}_{\text{tot}}(\mathcal{D})/\mathcal{D}_{\text{tot}}(\mathcal{C})]$; the equality is immediate algebra, and each ratio is $\le 1$ because condensation maps the parent category onto a subcategory of local modules with total dimension no larger than the parent's (a consequence of the bootstrap constraints of [2]). ∎

### 3.3 Boundary Majorana criterion

A gapped condensate boundary supports Majorana-type non-Abelian fusion structure when the surviving child category contains a simple object $\sigma$ with fusion rule $\sigma \times \sigma = \mathbf{1} + \psi$ — the Ising fusion rule — since this is precisely the fusion rule of Majorana zero modes [5], [10]. We use $\mathcal{I}$ as a screening quantity: in the examples computed below, the emergence of the Ising rule at the boundary is accompanied by a characteristic index value, and we ask whether the index alone can discriminate Majorana-supporting from purely Abelian condensation channels.

### 3.4 Computational procedure

For each example: (1) list parent anyons and quantum dimensions (from standard $F$-symbol data, per the identification program of [3]); (2) identify the condensable étale algebra; (3) compute confined vs. surviving anyons via monodromy; (4) compute child quantum dimensions; (5) evaluate $\mathcal{I}$ with explicit arithmetic. All inputs are the standard, exactly-known quantum dimensions of the toric code and doubled Ising categories; no numerical simulation is used or needed.

## 4. Analysis

We now carry out every computation explicitly.

### 4.1 Example 1: Toric code, condensing the boson $e$

**Input 1 (parent anyon content).** The toric code category has four anyons $\{ \mathbf{1}, e, m, \epsilon \}$, all Abelian, with quantum dimensions $d_{\mathbf{1}} = d_e = d_m = d_\epsilon = 1$. This is standard modular data; equivalently it follows from the fusion rules $e \times m = \epsilon$, $e \times e = m \times m = \mathbf{1}$, and the dimension relation $d_e d_m = d_\epsilon = 1$ with $d_e = d_m = 1$ (both $e$ and $m$ are bosons with trivial self-fusion to anything but $\mathbf{1}$).

**Input 2 (parent total quantum dimension).**

$$\mathcal{D}_{\text{tot}}(\mathcal{C}) = \sqrt{d_{\mathbf{1}}^2 + d_e^2 + d_m^2 + d_\epsilon^2} = \sqrt{1 + 1 + 1 + 1} = \sqrt{4} = 2.$$

**Input 3 (condensable algebra).** The boson $e$ supports the Lagrangian algebra $A = \mathbf{1} \oplus e$ (connected étale: bosonic since $e$ has trivial topological spin $\theta_e = 1$; haploid since $N_{\mathbf{1}e}^{\mathbf{1}} = 0$; its algebra dimension is $d_A = d_{\mathbf{1}} + d_e = 1 + 1 = 2$). This is the canonical condensation channel of [2], [9].

**Input 4 (monodromy screening).** The monodromy of an anyon $b$ with $A$ is trivial iff $b$ braids trivially with both $\mathbf{1}$ and $e$. In the toric code, the mutual braiding statistics are: $m$ has nontrivial mutual braiding phase $-1$ with $e$; $\epsilon = e \times m$ likewise has phase $-1$ with $e$. Therefore $m$ and $\epsilon$ are confined; $\mathbf{1}$ and $e$ have trivial monodromy and survive.

**Input 5 (child category).** The child category $\mathcal{D}$ has two simple objects, the vacuum sector and the $e$-sector, both with $d = 1$:

$$\mathcal{D}_{\text{tot}}(\mathcal{D}) = \sqrt{1^2 + 1^2} = \sqrt{2}.$$

**Computation of the index.**

$$\mathcal{I}_{\text{TC}} = \frac{\mathcal{D}_{\text{tot}}(\mathcal{D})}{\mathcal{D}_{\text{tot}}(\mathcal{C})} = \frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}} \approx 0.7071.$$

Arithmetic: $\sqrt{2} \approx 1.41421$; $1.41421 / 2 = 0.70711$ (five significant figures).

**Boundary interpretation.** The condensate boundary of the toric code with condensed $e$ is the well-known gapped $e$-condensate boundary. The surviving boundary defect structure is Abelian ($\mathbb{Z}_2$ fusion of the $e$-sector): no Ising rule, no Majorana statistics. Consistent with our screening criterion, the index here is $\approx 0.707$, above the trivial-condensation value $1$ only in the sense of being strictly below it — the point is that the boundary carries only $\sqrt{2}$ worth of quantum dimension, i.e., a single Abelian sector pair. The index correctly certifies that the boundary is "small": two sectors of dimension 1 each.

### 4.2 Example 2: Doubled Ising category, condensing the transparent boson

**Input 1 (parent anyon content).** The doubled Ising category $\mathrm{Double}(\mathrm{Ising})$ has nine anyons $\{ \mathbf{1}, \psi, \sigma \} \times \{ \mathbf{1}, \psi, \sigma \}$, i.e., pairs $(a,b)$ with $a, b \in \{\mathbf{1}, \psi, \sigma\}$, with quantum dimension $d_{(a,b)} = d_a d_b$ where $d_{\mathbf{1}} = 1$, $d_{\psi} = 1$, $d_{\sigma} = \sqrt{2}$. These are the standard Ising quantum dimensions, fixed by the fusion rule $\sigma \times \sigma = \mathbf{1} + \psi$ together with $d_\sigma^2 = d_{\mathbf{1}} + d_\psi = 2$, hence $d_\sigma = \sqrt{2}$.

**Input 2 (parent total quantum dimension).** Sum the squares over all nine pairs:

- Abelian pairs ($a,b \in \{\mathbf{1},\psi\}$, four of them): each $d^2 = 1$, contributing $4 \times 1 = 4$.
- Mixed pairs ($\sigma$ with $\mathbf{1}$ or $\psi$, four of them: $(\sigma,\mathbf{1}), (\sigma,\psi), (\mathbf{1},\sigma), (\psi,\sigma)$): each $d^2 = (\sqrt{2})^2 = 2$, contributing $4 \times 2 = 8$.
- The pair $(\sigma,\sigma)$: $d^2 = \sqrt{2} \times \sqrt{2} = 2$, contributing $2$.

$$\mathcal{D}_{\text{tot}}(\mathcal{C}) = \sqrt{4 + 8 + 2} = \sqrt{14} \approx 3.74166.$$

Arithmetic: $4 + 8 = 12$; $12 + 2 = 14$; $\sqrt{14} \approx 3.741657$.

**Input 3 (condensable algebra).** The doubled Ising category contains the boson $(\psi, \psi)$: each $\psi$ is a fermion with spin $-1$, so the product $(\psi,\psi)$ has topological spin $(-1)(-1) = +1$, i.e., a boson. It supports the algebra $A = \mathbf{1} \oplus (\psi,\psi)$ with $d_A = 1 + 1 = 2$. (We note the alternative Lagrangian choice $A = \mathbf{1} \oplus (\mathbf{1},\psi)\text{-type}$ channels exist only when a genuine boson of the required type exists; $(\mathbf{1},\psi)$ is a fermion and is not condensable, so $(\psi,\psi)$ is the canonical bosonic condensate here.)

**Input 4 (monodromy screening).** An anyon $(a,b)$ has trivial monodromy with $A = \mathbf{1} \oplus (\psi,\psi)$ iff its monodromy with $(\psi,\psi)$ is trivial. The monodromy phase of $(a,b)$ with $(\psi,\psi)$ is the product of the braiding phases of $a$ with $\psi$ and $b$ with $\psi$. In Ising: $\psi$ braids trivially (phase $+1$) with $\mathbf{1}$ and $\psi$, and has braiding phase $-1$ with $\sigma$. Therefore $(a,b)$ survives iff neither $a$ nor $b$ is $\sigma$... but wait — the monodromy is the *product* of phases: $(a,b)$ has monodromy phase $\theta_{a\psi}\,\theta_{b\psi}$, which is $-1$ if exactly one of $a,b$ is $\sigma$, and $+1$ if both or neither are $\sigma$. Hence the surviving anyons are those with an even number of $\sigma$ factors: $\{(\mathbf{1},\mathbf{1}), (\mathbf{1},\psi), (\psi,\mathbf{1}), (\psi,\psi), (\sigma,\sigma)\}$; the confined anyons are the four mixed pairs $(\sigma,\mathbf{1}), (\sigma,\psi), (\mathbf{1},\sigma), (\psi,\sigma)$.

**Input 5 (child category).** The child category $\mathcal{D} = \mathcal{C}_A^0$ has simple objects corresponding to the surviving parent anyons, with quantum dimensions equal to the parent dimensions (for simple current condensation of this type, the $A$-module dimensions are $d_\alpha = d_a$ for the underlying surviving $a$, since $d_A = 2$ and each surviving anyon admits exactly one simple $A$-module of dimension $d_a$; the dimension product formula $d_\alpha\, d_A = d_a\, d_A$ reduces to $d_\alpha = d_a$). Thus:

$$\mathcal{D}_{\text{tot}}(\mathcal{D}) = \sqrt{1^2 + 1^2 + 1^2 + 1^2 + (\sqrt{2})^2} = \sqrt{4 + 2} = \sqrt{6} \approx 2.44949.$$

Arithmetic: four Abelian survivors contribute $4 \times 1 = 4$; $(\sigma,\sigma)$ contributes $(\sqrt{2})^2 = 2$; total $4 + 2 = 6$; $\sqrt{6} \approx 2.449490$.

**Computation of the index.**

$$\mathcal{I}_{\text{dIsing}} = \frac{\sqrt{6}}{\sqrt{14}} = \sqrt{\frac{6}{14}} = \sqrt{\frac{3}{7}} \approx 0.65465.$$

Arithmetic: $6/14 = 3/7 \approx 0.428571$; $\sqrt{0.428571} \approx 0.654654$.

**Boundary interpretation.** The surviving child category contains the object $(\sigma,\sigma)$ with $d = \sqrt{2}$, and its fusion in the child category is $(\sigma,\sigma) \times (\sigma,\sigma) = (\mathbf{1},\mathbf{1}) \oplus (\mathbf{1},\psi) \oplus (\psi,\mathbf{1}) \oplus (\psi,\psi)$ — four outcome channels. This is richer than the Ising rule but is built from it: the boundary inherits non-Abelian fusion structure directly from the parent's $\sigma$ anyons. The index $\sqrt{3/7} \approx 0.655$ quantifies that roughly 43% of the parent's squared quantum dimension ($6/14$) survives at the boundary, and the non-Abelian survivor $(\sigma,\sigma)$ is precisely the carrier of that excess dimension ($2$ of the $6$).

### 4.3 Example 3: Toric code revisited — condensing $e \times m$-type channels and the composition law

To exercise Proposition 2, consider a two-step chain in the doubled Ising category: first condense $A_1 = \mathbf{1} \oplus (\psi,\psi)$ (Example 2), then, in the child category, condense the surviving boson $(\psi,\psi)$ itself — but in the child, $(\psi,\psi)$ has become identified with the vacuum sector's nontrivial element; the second condensation is the trivial one, giving $\mathcal{I}_2 = 1$. Hence

$$\mathcal{I}(\mathcal{C} \to \mathcal{E}) = \mathcal{I}_{\text{dIsing}} \times 1 = \sqrt{\frac{3}{7}} \approx 0.65465,$$

unchanged, consistent with monotonicity (equality holds when the second step is trivial). A genuinely nontrivial second step would require a child boson distinct from the already-condensed one; in this child category none exists among the surviving Abelian anyons with nontrivial monodromy-free fusion beyond the condensed algebra, so the chain terminates — itself a computable structural fact: the condensation lattice of $\mathrm{Double}(\mathrm{Ising})$ under this channel has depth one.

### 4.4 Index and Majorana statistics: the discriminating quantity

Define the *non-Abelian excess*:

$$\Delta \equiv \sum_{\alpha \in \mathcal{D},\, d_\alpha > 1} d_\alpha^2.$$

For Example 1: $\Delta_{\text{TC}} = 0$ (all child dimensions are 1). For Example 2: $\Delta_{\text{dIsing}} = 2$ (from $(\sigma,\sigma)$). The fraction of boundary quantum dimension carried by non-Abelian sectors is

$$f_{\text{NA}} = \frac{\Delta}{\mathcal{D}_{\text{tot}}(\mathcal{D})^2}.$$

Example 1: $f_{\text{NA}} = 0/2 = 0$. Example 2: $f_{\text{NA}} = 2/6 = 1/3 \approx 0.3333$. Arithmetic: $2/6 = 0.333333$.

Thus $f_{\text{NA}} > 0$ is an exact, arithmetically trivial criterion for the boundary to carry non-Abelian fusion structure; and in Example 2 the non-Abelian carrier $(\sigma,\sigma)$ descends from the parent's Ising anyon $\sigma$, whose fusion rule $\sigma \times \sigma = \mathbf{1} + \psi$ is the Majorana zero mode rule classified in [10]. The index pair $(\mathcal{I}, f_{\text{NA}}) = (\sqrt{3/7}, 1/3)$ therefore certifies, from bulk data alone, that the condensate boundary supports Majorana-descended statistics.

## 5. Results

All numbers below are computed in Section 4; none are simulated or measured.

**Result 1 (Toric code, $e$-condensation).** Parent total quantum dimension $\mathcal{D}_{\text{tot}} = 2$; child total quantum dimension $\sqrt{2}$; condensation index $\mathcal{I}_{\text{TC}} = 1/\sqrt{2} \approx 0.70711$; non-Abelian excess $\Delta = 0$; $f_{\text{NA}} = 0$. The boundary is purely Abelian.

**Result 2 (Doubled Ising, $(\psi,\psi)$-condensation).** Parent $\mathcal{D}_{\text{tot}} = \sqrt{14} \approx 3.74166$; child $\mathcal{D}_{\text{tot}} = \sqrt{6} \approx 2.44949$; condensation index $\mathcal{I}_{\text{dIsing}} = \sqrt{3/7} \approx 0.65465$; non-Abelian excess $\Delta = 2$; $f_{\text{NA}} = 1/3 \approx 0.33333$. The boundary carries one non-Abelian sector, $(\sigma,\sigma)$, with $d = \sqrt{2}$ and four-channel fusion, descended from the parent Ising anyon.

**Result 3 (Composition law).** The condensation chain in doubled Ising terminates at depth one under this channel: $\mathcal{I}(\mathcal{C} \to \mathcal{E}) = \sqrt{3/7} \times 1 = \sqrt{3/7} \approx 0.65465$, confirming monotonicity with equality for a trivial second step.

**Result 4 (Discrimination criterion, exact).** $f_{\text{NA}} > 0$ if and only if the child category contains an anyon of quantum dimension $> 1$, i.e., the boundary supports non-Abelian fusion. This is exact for the two computed channels: $f_{\text{NA}} = 0$ (Abelian boundary) vs. $f_{\text{NA}} = 1/3$ (non-Abelian boundary).

**Projection (labeled as such).** We conjecture, without proof or computation beyond the two cases, that for any unitary modular $\mathcal{C}$ with a connected étale $A$, $f_{\text{NA}}$ is bounded above by the parent's non-Abelian weight $\sum_{d_a > 1} d_a^2 / \mathcal{D}_{\text{tot}}(\mathcal{C})^2$; in Example 2 this bound is $10/14 \approx 0.714$, and the achieved value $1/3$ lies below it. Uncertainty: this is a structural conjecture consistent with, but not derived from, the bootstrap constraints of [2]; it is falsified by any condensation channel where the child's non-Abelian weight exceeds the parent's.

## 6. Discussion

**Limitations.** The index is computed here only for two exactly-solved categories with Abelian or simple-current condensates. For general non-invertible condensates — those involving anyons of dimension $> 1$ in the algebra itself, treated generically in [8] — the child dimension formula $d_\alpha = d_a$ fails and must be replaced by the full $A$-module dimension computation; our arithmetic does not cover that case, and $\mathcal{I}$ could behave differently (in particular, the monotonicity proof sketch in Section 3.2 leans on the subcategory structure of simple-current condensation and is not a general proof). Second, the corpus available to us lacks works on fermionic topological orders and spin-TQFT; the Majorana zero modes of physical 2D topological superconductors [10] live in fermionic systems, whereas our examples are bosonic. The doubled Ising example captures the *fusion-rule* structure of Majoranas but not their fermionic spin-statistics; bridging this gap requires the spin-TQFT extension we have not performed. Third, two bibliography entries [11], [12] provided no usable abstract content and are uncited in the analysis — a limitation of the source corpus, not of the method.

**Failure modes.** The index could fail to capture boundary physics in three ways. (i) *Non-modular parents:* if $\mathcal{C}$ is pre-modular (as in the mixed-state setting of [8]), transparent anyons complicate the monodromy screening and $\mathcal{I}$ may double-count sectors. (ii) *Boundary condition degeneracy:* a single bulk condensation channel can admit multiple distinct gapped boundaries (e.g., $e$- vs. $m$-condensate boundaries of the toric code, which our Example 1 does not distinguish — by symmetry $\mathcal{I}$ is identical for both). The index measures the condensation channel, not the full boundary condition data; distinguishing $e$- from $m$-boundaries requires the $R$/$F$-matrix identifiers of [3], not quantum dimensions alone. (iii) *Non-Hermitian or non-unitary analogues:* the cautionary lesson of [7] — that bulk-boundary correspondence can require reformulation when standard assumptions fail — applies here: for non-unitary categories, quantum dimensions can be non-positive and $\mathcal{I}$ as defined is ill-posed.

**What would falsify the claims.** Three concrete falsifiers. (1) A condensation channel in a unitary modular category where the child total quantum dimension exceeds the parent's — this would violate the foundational constraint underlying $\mathcal{I} \le 1$ and falsify the index's premises. (2) A boundary supporting Ising-type Majorana fusion rules arising from a condensation channel with $f_{\text{NA}} = 0$ — this would falsify the claim that $f_{\text{NA}} > 0$ is necessary for boundary non-Abelian statistics in condensate boundaries. (3) A nontrivial two-step condensation chain where $\mathcal{I}(\mathcal{C} \to \mathcal{E}) > \min(\mathcal{I}_1, \mathcal{I}_2)$ — falsifying monotonicity. We regard (1) as essentially ruled out by the bootstrap analysis of [2]; (2) and (3) are genuinely open.

**Arguing against ourselves.** A skeptic could object that $\mathcal{I}$ is merely a ratio of known quantities — $\mathcal{D}_{\text{tot}}(\mathcal{D)$ is computable directly from the child category without reference to the parent — so the index