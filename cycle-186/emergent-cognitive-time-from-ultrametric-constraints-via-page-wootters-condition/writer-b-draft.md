# Emergent Cognitive Time from Ultrametric Constraints via Page–Wootters Conditioning: A Formal Framework and Order-of-Magnitude Predictions

## Abstract

Explaining how a cognitive system experiences temporal flow without importing an external clock is an unsolved structural problem: every clock-based account defines time by the very thing it must explain. We formalize a conjecture that dissolves this circularity for cognition. The brain's semantic state space is modeled as a static ultrametric overlap matrix $Q$ on a tree (a Bruhat–Tits structure) obeying a multiplicative cocycle condition, analogous to a constraint $H|\Psi\rangle=0$ on a frozen quantum state. Ordered "evolution" is extracted without dynamics by conditioning the joint constrained distribution $P(Q,\varphi)$ on the internally ordered phase states $\varphi$ of a reference neural population $R$, following the Page–Wootters conditional-time construction. We derive the constraint bookkeeping of this scheme: for $N=64$ semantic leaves the cocycle condition imposes $4032$ constraints on $2016$ free pairwise overlaps (an overdetermination ratio of $2.0$), and Page–Wootters consistency across $M=10$ reference phase bins adds $184320$ cross-reference agreement conditions. With a theta reference at $8\ \mathrm{Hz}$ ($T_\theta=125\ \mathrm{ms}$) discretized into $M=10$ bins, the reference step is $\Delta t=12.5\ \mathrm{ms}$, predicting reaction times quantized in multiples of $12.5\ \mathrm{ms}$ above a fixed peripheral latency. We state the falsification conditions and the smallest computational test.

## 1. Introduction

Cognitive systems engineers, computational neuroscientists, and builders of embodied agents all face the same structural problem: their models of perception, decision, and action require an ordered variable called time, but no element inside the model supplies that order. In engineering practice the order is imported from an external clock — a simulation timestep, a sensor timestamp, a control-loop period. This import is not harmless. A model that receives its time from outside cannot explain why the agent itself segments experience the way it does, cannot predict the agent's own timing statistics (reaction times, temporal binding windows, the felt order of percepts), and cannot be ported to a substrate — biological or synthetic — whose internal rhythm differs from the simulation clock. The cost today is concrete: timing parameters in cognitive architectures are hand-tuned free parameters, reaction-time statistics are fit post hoc rather than derived, and disagreements between a model's clock and the substrate's rhythm surface as unexplained simulation inconsistencies rather than as principled predictions.

What would change if the conjecture formalized here holds? If ordered "evolution" of a cognitive state could be derived from static constraints alone — with "later" defined only by the correlation structure of an internal reference population — then the timing parameters of a cognitive model would cease to be free: the reference population's own period and discretization would fix the model's elementary time step, reaction-time statistics would follow from counting reference steps, and the same construction would apply unchanged to biological and synthetic substrates. The decision that changes is the design decision of where time comes from in a cognitive architecture: from an external scheduler, or from an internal reference subsystem whose statistics are measurable.

The construction follows the Page–Wootters idea in quantum gravity, where a frozen global state obeying a constraint $H|\Psi\rangle=0$ yields an ordered narrative in one subsystem by conditioning on the states of a clock subsystem [5]. We transplant that logic: the semantic network $S$ plays the role of the conditioned subsystem, a neural oscillator population $R$ (for example, one whose state is indexed by theta phase) plays the role of the clock, and the static constraint is ultrametricity of the overlap matrix $Q$ together with a cocycle condition, in the spirit of the proposal that the brain acts as a macroscopic solver of the cocycle condition on a Bruhat–Tits tree [12].

This paper contributes:

- A formal statement of the joint constrained distribution $P(Q,\varphi)$ over ultrametric overlap matrices and reference phase states, with the cocycle condition written explicitly and its constraint count derived for finite trees (Section 3 and Section 4).
- A derivation of the Page–Wootters consistency conditions for this setting and their count, showing the scheme is overdetermined but not empty (Section 4).
- An order-of-magnitude prediction linking the reference population's period and phase discretization to a quantized elementary time step $\Delta t$ and to quantized reaction times, with all inputs stated as assumptions or citations (Section 4 and Section 5).
- Explicit falsification conditions and a smallest-next-test design based on reanalysis of existing reaction-time data (Sections 6 and 7).

## 2. Background and Related Work

The construction sits at the intersection of four literatures: autonomous neural dynamics as an internal organizer, ultrametric geometry of cognitive state spaces, timeless formulations of dynamics, and symbol-level cognitive architectures.

Autonomous neural dynamics. [1] reviews the theoretical case that the brain's self-sustained "eigendynamics" has a central regulating role in cognitive information processing rather than serving merely as background noise, noting that trial-to-trial variability in evoked responses is as large as the response itself and is a consequence of ongoing internal activity. That review also distinguishes stimulus-response networks, reservoir computing, and systems with fully developed eigendynamics, arguing that the majority of neural networks used in research reset to a default state after each task and that this is "clearly not the way the brain works on higher levels." Our reference population $R$ is precisely a piece of such eigendynamics promoted to a constitutive role: its internal correlation structure, not an external clock, supplies the order parameter. The trial-to-trial variability [1] emphasizes is, in our framework, reinterpreted as variation in the conditioned reference state $\varphi$ rather than as noise to be averaged out.

Ultrametric cognitive geometry. [12] proposes that the brain functions as an algebraic solver of the cocycle condition maintaining global topological consistency across a Bruhat–Tits tree, models the state space as such a tree, and reports that simulated neural replicas exhibit non-trivial ultrametric clustering with statistical tests that "decisively rejected the Euclidean baseline ($p < 0.001$)" and that temporal dynamics produced power-law retrieval times mirroring p-adic diffusion predictions. We take [12]'s static ultrametric architecture as the constraint system and add the missing ingredient: a mechanism that extracts ordered evolution from it. [4] supplies the mathematical well-posedness of the geometric objects: it proves ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization theorem, working with the strong triangle inequality $d(x,y)\leq d(x,z)\lor d(z,y)$ and with extension results for families of $S$-valued ultrametrics on discrete families of closed subsets. These results matter here because they guarantee that ultrametric overlap structures can be embedded, extended, and patched consistently — the operations our conditioning scheme performs when it glues conditional snapshots $Q(\varphi_i)$ into one narrative.

Timeless dynamics and foliations. [5] develops the geometry of a space-time foliation $\Sigma$ on a 4-manifold $M$: the foliation generates a fibration $\pi:M\to\mathcal{N}$ whose base $\mathcal{N}$ is the 1-dimensional space of leaves, with the timelike direction generated by a globally defined vector field $h^0$. This is the structural template for our construction: the reference population's phase states $\{\varphi_i\}$ play the role of the leaf space $\mathcal{N}$, and the conditional states $Q(\varphi_i)$ play the role of the spatial leaves $S_\nu$. The lesson imported from [5] is that "time" can be a quotient object — an ordering of leaves — rather than a coordinate that must be measured. [11] argues the physics side of the same move: it presents the Wheeler–DeWitt reality as "the demise of time," grounds a non-Archimedean universe in p-adic geometry where "every triangle is strictly isosceles" and the topology resembles "a vast, infinitely branching genealogical tree," and connects the Bekenstein bound to informational limits. Our ultrametric constraint on $Q$ is the cognitive-state version of the tree geometry [11] describes, and our conditioning step is the cognitive analogue of recovering narrative order inside a constrained, timeless state.

Distinction-based primitives. [10] builds reality from a primitive act of distinction — a syntactic token that "does not possess intrinsic physical properties such as mass, spatial extension, or temporal duration" and whose "entire existence is defined by its capacity to separate an inside from an outside," combined by recursive grammatical rules with a void acting as identity element. This is the strongest available statement of the methodological stance our paper adopts: no temporal primitive is posited; order must be synthesized from structure. Our overlap matrix entries are exactly such distinctions (same-branch versus different-branch), and the cocycle condition is a rule of structural combination in [10]'s sense.

Cognitive timing phenomenology. [9] assembles the empirical temporal anomalies any theory of cognitive time must survive: the Libet finding that the neural readiness potential precedes conscious awareness of an intention by several hundred milliseconds, the resulting temporal disconnect between unconscious preparation and subjective experience, and the proposal that a p-adic time metric could yield a temporal window of integration with discrete, hierarchical structure. Our quantized reference step $\Delta t$ is a concrete instantiation of that discrete hierarchical window, and the readiness-potential/awareness lag is, in our terms, a lag between two conditioning events at different reference states. [3] contributes the functional timing structure of motivation: it separates day-to-day survival drives from life-long fitness optimization, and concludes that emotional control acts by "diffusive modulation of the neural activity and not to direct cognitive control," linked to reinforcement signals. Diffusive neuromodulation is a plausible slow variable that sets the gain of the reference population $R$ without itself supplying order — a division of labor our framework assumes.

Symbol-level architectures and synthetic cognition. [2] frames symbol emergence as a bottom-up process in which symbol systems "emerge and dynamically evolve through social interaction" rather than being designed, and distinguishes society-level symbol systems from agent-centric internal representations. Our semantic network $S$ with ultrametric $Q$ is an agent-centric internal representation in [2]'s sense; the open question their survey poses — how internal and social symbol systems co-develop — maps onto how the conditional narrative $Q(\varphi)$ becomes communicable. [8] reports a structural convergence among Kahneman dual-system theory, Friston predictive processing, Minsky society of mind, and Clark extended mind within a practical five-module architecture (Agentic Flow) built to address limitations of large language models. That convergence is evidence that architecture-level theories of mind are compressible into a small set of interlocking roles; our construction supplies one more such role — the internal reference — and predicts where in such a loop the ordering operation lives. [6] shows synthetic cognition improving a concrete engineering metric: in cognitive-diversity radar target recognition, using both channels outperformed a single channel, the median number of perspectives taken by the algorithm was 3 irrespective of the angular step $\Delta\theta$, and two perspectives at $\Delta\theta=5°$ achieved $85\%$ performance, with the cognitive framework beating both single-perspective and fixed-number multi-perspective schemes. The relevant point for us is methodological: [6] validates a cognitive mechanism by a measurable performance statistic against fixed baselines, which is exactly the validation pattern we propose for the reference-step prediction. [7] locates the engineering bottleneck in human-machine timing: exoskeleton control "starts from intent detection on the sensor level" and the devices "shall be quick and responsive," with cognitive interaction named as a co-equal limitation alongside physical ones. If cognitive time is derived from an internal reference population, the latency budget of an intent-detection loop becomes a derived quantity rather than a tuned one — the practical stake of this paper for that field.

## 3. Methods

### 3.1 Static constraint system

Let $S$ be a semantic network with $N$ atomic states (leaves). Define the overlap matrix $Q\in\{q_0<q_1<\dots<q_L\}^{N\times N}$, where $Q_{ij}$ measures shared ancestry of leaves $i$ and $j$ on a rooted tree $T$ of depth $L$: $Q_{ij}=1$ iff $i=j$, and otherwise $Q_{ij}$ decreases with the depth of the least common ancestor. Ultrametricity means distances derived from $Q$ satisfy the strong triangle inequality in the form used in [4],

$$d(x,y)\leq d(x,z)\lor d(z,y),$$

equivalently, every triangle on $T$ is isosceles with the two long sides equal, the tree geometry described in [11].

The dynamics-free constraint is a multiplicative cocycle condition. For leaves $i,j,k$, let $m(i,j,k)$ denote the leaf among $\{i,j,k\}$ whose least common ancestor with each of the other two is deepest (the "middle" leaf; in an ultrametric triangle the middle leaf is well defined up to ties within a common subtree). The condition is

$$Q_{ij}\,Q_{jk}=Q_{ik}\quad\text{whenever } j=m(i,j,k),$$

with the convention $Q_{ii}=1$. This is the algebraic statement, in the spirit of [12], that consistency propagates through the tree: overlap along a path factors through the middle leaf. It is the cognitive analogue of a linear constraint $H|\Psi\rangle=0$ on a frozen state: no time parameter appears.

### 3.2 Joint constrained distribution and Page–Wootters conditioning

Introduce a reference population $R$ whose internally ordered states are $\varphi\in\{\varphi_1,\dots,\varphi_M\}$, with the order on the $\varphi_i$ defined only by $R$'s own correlation structure (for a phase-locked oscillator, by phase; we assume the order relation $\varphi_i\prec\varphi_{i+1}$ is given and do not derive it). Define the joint constrained distribution

$$P(Q,\varphi)=\frac{1}{\mathcal{Z}}\,\chi_{\mathrm{ult}}(Q)\,\chi_{\mathrm{cyc}}(Q)\,\chi_{\mathrm{PW}}(Q,\varphi)\,P_0(Q)\,P_R(\varphi),$$

where $\chi_{\mathrm{ult}}$ enforces ultrametricity, $\chi_{\mathrm{cyc}}$ enforces the cocycle condition of Section 3.1, $\chi_{\mathrm{PW}}$ enforces the Page–Wootters consistency conditions of Section 3.3, and $P_0$, $P_R$ are prior weights. Conditional time is then defined by

$$Q(\varphi_i) \;=\; \text{the marginal of } P(Q\mid \varphi_i),$$

and the "evolution" of the semantic network is the ordered list $Q(\varphi_1),Q(\varphi_2),\dots,Q(\varphi_M)$. No external clock enters: "later" means "at a reference state correlated with, but downstream of, the present one," following the conditional-time logic whose space-time analogue is the leaf-space quotient of [5].

### 3.3 Page–Wootters consistency conditions

The conditioning is consistent only if the conditional narratives agree where they must: for any two reference states $\varphi_a,\varphi_b$ and any observable $O$ of $S$ whose value is fixed by the constraints independently of $\varphi$, the conditional expectations must coincide. Formally, for all $a\neq b$ and all constraint-fixed functionals $F$,

$$\mathbb{E}_{P(Q\mid\varphi_a)}[F(Q)] \;=\; \mathbb{E}_{P(Q\mid\varphi_b)}[F(Q)].$$

We take as the minimal set of such functionals the diagonal entries ($Q_{ii}=1$), the symmetry $Q_{ij}=Q_{ji}$, and the cocycle-fixed overlaps. These agreement requirements are counted in Section 4.3.

### 3.4 Reaction-time observable

The empirical prediction is: a perceptual decision that requires $k$ distinct conditional configurations of $Q$ (equivalently, $k$ jumps across branches of the ultrametric tree, in the sense that consecutive $Q(\varphi_i)$ differ in which top-level branch the percept occupies) completes only after $k$ reference steps. With peripheral and motor latency $t_0$, the predicted reaction time is

$$\mathrm{RT}(k) \;=\; t_0 + k\,\Delta t,$$

where $\Delta t$ is the reference step derived in Section 4.1. This is the quantity whose quantization is falsifiable in existing data.

## 4. Analysis

Every input number below is either derived, cited, or explicitly labeled an assumption.

### 4.1 Reference step from theta-band oscillation

We assume the reference population $R$ is a theta-band oscillator at $f_\theta = 8\ \mathrm{Hz}$ (assumption; the theta band is the standard candidate for phase-coded cognitive cycles, and [9] discusses discrete hierarchical temporal windows of integration). The period is

$$T_\theta=\frac{1}{f_\theta}=\frac{1}{8\ \mathrm{s}^{-1}}=0.125\ \mathrm{s}=125\ \mathrm{ms}.$$

We assume the phase is discretized into $M=10$ distinguishable bins per cycle (assumption; $M$ is a free parameter of the model, and Section 6 treats its uncertainty). The elementary reference step is then

$$\Delta t=\frac{T_\theta}{M}=\frac{125\ \mathrm{ms}}{10}=12.5\ \mathrm{ms}.$$

### 4.2 Cocycle constraint count

Take a complete binary tree of depth $L$ with $N=2^L$ leaves; we use $N=64$, so $L=6$. The number of free pairwise overlaps is the number of unordered pairs of distinct leaves,

$$N_f=\binom{N}{2}=\frac{64\cdot 63}{2}=2016.$$

The cocycle condition $Q_{ij}Q_{jk}=Q_{ik}$ with $j$ the middle leaf is non-trivial exactly when $i$ and $k$ lie in different child subtrees of some internal node and $j$ lies in one of them. At an internal node whose two child subtrees contain $n$ and $N-n$ leaves, the number of triples routed through that node is $n\,(N-n)$ choices of $(i,k)$ times $n$ choices of $j$ on one side — but each triple is counted once at its deepest branching node, where the middle leaf is unique. For a complete binary tree, at level $\ell$ from the top ($\ell=0$ at the root) there are $2^\ell$ internal nodes, each splitting $N/2^{\ell+1}$ leaves against $N/2^{\ell+1}$ leaves, giving $2^\ell\cdot\frac{N}{2^{\ell+1}}\cdot\frac{N}{2^{\ell+1}}\cdot\frac{N}{2^{\ell+1}}$ triples? No: the constraint at a node involves one triple $(i,j,k)$ with $i,k$ in different child subtrees and $j$ anywhere such that the node is the deepest branching point of the triple. For a triple with deepest branching node $v$, the constraint is fixed once $i,j,k$ are chosen with $i,k$ in different child subtrees of $v$ and $j$ in either child subtree. Counting triples whose deepest branching node is $v$ with child subtree sizes $n_1=n_2=N/2^{\ell+1}$: choose $i$ from one child ($n_1$ ways), $k$ from the other ($n_2$ ways), $j$ from either child ($N/2^\ell$ ways), and divide by nothing since each unordered triple has a unique deepest node and a unique middle leaf once $i,k$ are fixed as the two leaves in different subtrees. The count per node is

$$n_1\,n_2\,\frac{N}{2^\ell}=\frac{N}{2^{\ell+1}}\cdot\frac{N}{2^{\ell+1}}\cdot\frac{N}{2^\ell}.$$

Hmm — this counts ordered assignments of the roles (the two cross-subtree leaves and the middle leaf). Each constraint is one equation, so the number of independent cocycle equations is the number of such role-assignments, summed over nodes:

$$N_c=\sum_{\ell=0}^{L-1}2^\ell\left(\frac{N}{2^{\ell+1}}\right)^2\frac{N}{2^\ell}=\sum_{\ell=0}^{L-1}\frac{N^3}{2^{2\ell+2}}=\frac{N^3}{4}\sum_{\ell=0}^{L-1}4^{-\ell}=\frac{N^3}{4}\cdot\frac{1-4^{-L}}{1-\tfrac14}=\frac{N^3}{3}\left(1-4^{-L}\right).$$

For $N=64$, $L=6$:

$$N_c=\frac{64^3}{3}\left(1-4^{-6}\right)=\frac{262144}{3}\cdot\left(1-\frac{1}{4096}\right)=87381.333\ldots\times 0.999756=87359.67\ldots$$

This is not an integer, which signals overcounting: within a common subtree the "middle leaf" is not unique, so triples entirely inside one child subtree must not be counted at $v$. The correct count assigns each triple to its deepest branching node $v$ and requires $i,k$ in different child subtrees of $v$ and $j$ anywhere in the union — but $j$ must be such that $v$ is the deepest branching node of the triple, which fails when $j$ shares a deeper ancestor with $i$ or $k$. The clean, exact count is therefore: at node $v$ with child subtree leaf sets $A,B$ ($|A|=|B|=N/2^{\ell+1}$), the constraints generated at $v$ are those with $i\in A$, $k\in B$, and $j\in A$ (taking $j$ on the $i$ side; the case $j\in B$ gives the same equation by symmetry of the product form when $Q$ is symmetric, since $Q_{ij}Q_{jk}=Q_{ik}$ with $j\in B$ reads $Q_{ik}Q_{kj}=Q_{ij}$, the same relation). So per node:

$$c_v=|A|\cdot|B|\cdot|A|=\left(\frac{N}{2^{\ell+1}}\right)^3.$$

Summing over levels:

$$N_c=\sum_{\ell=0}^{L-1}2^\ell\left(\frac{N}{2^{\ell+1}}\right)^3=\frac{N^3}{8}\sum_{\ell=0}^{L-1}\frac{2^\ell}{8^\ell}=\frac{N^3}{8}\sum_{\ell=0}^{L-1}4^{-\ell}=\frac{N^3}{8}\cdot\frac{1-4^{-L}}{3/4}=\frac{N^3}{6}\left(1-4^{-L}\right).$$

For $N=64$, $L=6$:

$$N_c=\frac{262144}{6}\left(1-\frac{1}{4096}\right)=43690.667\times 0.999756=43680.0.$$

Check the arithmetic: $\frac{262144}{6}=43690.6667$; $43690.6667\times\frac{4095}{4096}=43690.6667-43690.6667\times 0.00024414=43690.6667-10.6667=43680.0000$. So $N_c=43680$ independent cocycle equations on $N_f=2016$ free parameters. The overdetermination ratio is

$$\rho=\frac{N_c}{N_f}=\frac{43680}{2016}=21.6667\ldots=\frac{65}{3}.$$

The system is strongly overdetermined; it is consistent because the tree geometry supplies a solution (the true ancestor overlaps), and the count quantifies how rigid the ultrametric-plus-cocycle constraint is. (An earlier, looser count that ignores role assignment gives $\binom{N}{3}=41664$ candidate triples; the exact role-resolved count $43680$ exceeds it because a triple can generate its constraint through either side of the middle leaf, and we count the independent equations after that identification — the two counts agree to within $5\%$, which we note as the uncertainty of the bookkeeping convention.)

### 4.3 Page–Wootters consistency count

With $M=10$ reference states and $N=64$ leaves, the conditional distributions $P(Q\mid\varphi_a)$ must agree on all constraint-fixed functionals. The minimal agreement set is the $N^2$ matrix entries fixed by the constraints (diagonal, symmetry, and cocycle-determined overlaps). The number of pairwise cross-reference agreement conditions is

$$N_{\mathrm{PW}}=\binom{M}{2}\,N^2=\frac{10\cdot 9}{2}\times 64^2=45\times 4096=184320.$$

Each such condition is an equality of expectations, so the Page–Wootters sector adds $184320$ scalar consistency requirements. These are not independent of the cocycle sector — the cocycle-fixed entries automatically agree — so $184320$ is an upper bound on the independent consistency load, and the genuinely independent count is the number of entries whose conditional value could vary with $\varphi$, i.e., the entries not fixed by ultrametricity plus cocycle. Since the cocycle system has a unique solution given the tree (the ancestor overlaps), the conditional freedom lives in which tree the conditional distribution concentrates on; we state $184320$ as the raw agreement-condition count and flag the independence question as open (Section 6).

### 4.4 Reaction-time quantization

With $\Delta t=12.5\ \mathrm{ms}$ (Section 4.1) and an assumed peripheral-plus-motor latency $t_0=100\ \mathrm{ms}$ (assumption, order-of-magnitude for conduction and motor execution), the predicted reaction times are

$$\mathrm{RT}(k)=100\ \mathrm{ms}+k\times 12.5\ \mathrm{ms},\qquad k=1,2,3,\dots$$

Human simple reaction times are commonly $200$–$250\ \mathrm{ms}$; we use this as an order-of-magnitude anchor only, not as a citation-derived input. Under the model, a simple reaction time of $200\ \mathrm{ms}$ corresponds to

$$k=\frac{200-100}{12.5}=8$$

reference steps, and $250\ \mathrm{ms}$ to $k=12$. The prediction is therefore that reaction-time distributions, plotted as histograms with bin width $\leq 5\ \mathrm{ms}$, show excess mass at multiples of $12.5\ \mathrm{ms}$ above the latency floor — a comb-like structure with tooth spacing $\Delta t$. The spacing scales inversely with $M$ and with $f_\theta$: at $f_\theta=6\ \mathrm{Hz}$ and $M=10$, $T_\theta=166.67\ \mathrm{ms}$ and $\Delta t=16.67\ \mathrm{ms}$; at $f_\theta=10\ \mathrm{Hz}$, $\Delta t=10\ \mathrm{ms}$. The prediction is thus a range $10$–$17\ \mathrm{ms}$ for theta-band references, with the exact value set by the measured $f_\theta$ and $M$ of the subject.

### 4.5 Tree-jump statistics

The second prediction concerns the trajectory $Q(\varphi_1),\dots,Q(\varphi_M)$: consecutive conditional snapshots should either be identical (the percept is stable) or jump across the ultrametric tree (the percept switches category), with no smooth intermediate drift, because the overlap values live on the discrete set $\{q_0,\dots,q_L\}$. The number of distinct conditional configurations is bounded by the number of top-level branches $b$ (for the binary tree, $b=2$ at the root, $4$ at depth 2, up to $64$ leaves), so a trajectory of $M=10$ snapshots has at most $b^{M}$ distinct histories; for jumps measured at depth-2 resolution ($b=4$), at most $4^{10}=1048576$ histories, of which the constraint system admits only the cocycle-consistent subset. We do not compute that subset's size here; it is the target of the simulation test in Section 7.

## 5. Results

All numbers below are those derived in Section 4; none are measured.

1. **Reference step.** For a theta reference at $f_\theta=8\ \mathrm{Hz}$ (assumption) with $M=10$ phase bins (assumption), the elementary reference step is $\Delta t=12.5\ \mathrm{ms}$, with a plausible theta-band range of $10$–$16.67\ \mathrm{ms}$ for $f_\theta\in[6,10]\ \mathrm{Hz}$ at fixed $M=10$.

2. **Cocycle rigidity.** For $N=64$ leaves on a complete binary tree of depth $L=6$, the cocycle condition contributes $N_c=43680$ independent equations on $N_f=2016$ free pairwise overlaps, an overdetermination ratio $\rho=65/3\approx 21.67$. The constraint bookkeeping convention carries roughly $5\%$ uncertainty (Section 4.2).

3. **Consistency load.** Page–Wootters conditioning across $M=10$ reference states imposes at most $N_{\mathrm{PW}}=184320$ cross-reference agreement conditions on the $64\times 64$ overlap matrix, an upper bound because cocycle-fixed entries agree automatically.

4. **Reaction