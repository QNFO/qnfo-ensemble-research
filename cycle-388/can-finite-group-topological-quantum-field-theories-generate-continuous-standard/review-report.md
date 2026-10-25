{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Finite 2‑group gauge theories – A (weak) 2‑group \\(\\mathbb{G}=(G,H,t,\\alpha)\\) is defined by a pair of groups together with a homomorphism \\(t:H\\to G\\) and an action \\(\\alpha:G\\to\\mathrm{Aut}(H)\\) satisfying \\(t(\\alpha(g)(h))=gt(h)g^{-1}\\) and \\(\\alpha(t(h))(h')=hh'h^{-1}\\) [2, §2.1].  The associated TQFT generalises Dijkgraaf–Witten theory and admits both 1‑form and 2‑form gauge fields.  Crucially, the classification of such theories relies on the finite group \\(G\\) and its cohomology, reinforcing the finiteness of the charge spectrum.",
      "reason": "The cited source [2] excerpt only defines 2‑groups and does not contain any statement about the classification of such TQFTs relying on the finite group \\(G\\) and its cohomology. The claim is therefore unsupported by the provided bibliography entry.",
      "fix": "Remove the unsupported sentence about classification relying on \\(G\\) and its cohomology, or replace it with a statement directly supported by the excerpt, e.g., \"A (weak) 2‑group \\(\\mathbb{G}=(G,H,t,\\alpha)\\) is defined ...\"."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Density of states for finite‑group symmetry – Using Euclidean gravity, a universal formula for the density of black‑hole microstates transforming in each irreducible representation \\(\\alpha\\) of a finite gauge group \\(G\\) is derived [3, §2].  The formula shows that each representation appears with a non‑zero density, but the number of representations is finite, namely the number of irreducible representations of \\(G\\).",
      "reason": "No excerpt from source [3] is provided; therefore the claim cannot be verified against the bibliography and is unsupported.",
      "fix": "Delete the entire sentence or replace it with a claim that can be directly supported by an available source."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Gauge symmetry factorisation on intervals – Imposing Dirichlet–Neumann boundary conditions on a fifth‑dimensional interval factorises an arbitrary gauge group into mutually orthogonal one‑ or two‑dimensional subspaces, each giving an independent Kaluza–Klein tower [4, §V].  The mass spectrum of each tower is controlled by a twist angle \\(\\phi\\), but the number of independent subspaces is bounded by the rank of the original gauge algebra.",
      "reason": "The bibliography entry for [4] does not include any excerpt; the claim is not supported by the supplied text.",
      "fix": "Remove the unsupported description or rewrite it to reflect only what is given in the excerpt (if any)."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Mirror symmetry and Lorentz representations – Irreducible representations of the full Lorentz group $O(1,3)$ decompose into $(m,m)$ or $(m,n)\\oplus(n,m)$ types [5, §II].  While this enriches the classification of particle states, it does not increase the number of independent gauge charges beyond those supplied by the underlying gauge group.",
      "reason": "No excerpt from source [5] is provided; the statement cannot be verified and is therefore unsupported.",
      "fix": "Delete or replace the sentence with a claim that can be substantiated by an available source."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Structure of the Standard Model – The SM Lagrangian contains non‑abelian gauge fields $G_\\mu^i$ with field strength $F_{\\mu\\nu}^i$ and a Higgs sector that spontaneously breaks $SU(2)_L\\times U(1)_Y$ [8, §1].  The continuous gauge groups entail infinitely many charge sectors, a fact that any candidate emergent model must reproduce.",
      "reason": "The bibliography entry for [8] provides no excerpt; the claim about infinite charge sectors is not supported by the supplied text.",
      "fix": "Remove the unsupported claim or qualify it as an assumption without citation."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Standard representation theory (see e.g. [2]) tells us that the simple objects of $Z(\\mathrm{Rep}(G))$ are in bijection with pairs $(C,\\rho)$ where $C$ is a conjugacy class of $G$ and $\\rho$ is an irrep of the centraliser $Z_G(g)$ for any $g\\in C$.  The total number of such pairs equals $|G|$ because each group element belongs to exactly one conjugacy class and each centraliser contributes exactly one irrep per element of the class.",
      "reason": "The excerpt from [2] does not contain any discussion of Drinfeld centres, conjugacy classes, or the counting of simple objects. The claim is unsupported by the cited source.",
      "fix": "Replace the citation with a source that actually contains this representation‑theoretic result, or remove the unsupported statement."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "It is observed that the prime $p=2$ encodes spin and $p=3$ encodes colour charge via $p$‑adic completions of $\\mathbb{Q}$.  In that framework a quantum number $q$ is associated with a $p$‑adic valuation $v_{p}(q)$.  For a particle carrying spin $s\\in\\{0,\\tfrac12,1,\\dots\\}$ the $2$‑adic valuation satisfies $v_{2}(s)=0$ (since spin is a half‑integer, not divisible by $2$), whereas colour representations of $SU(3)$ correspond to $3$‑adic valuations $v_{3}(c)\\in\\{0,1\\}$ distinguishing the fundamental and anti‑fundamental triplets.",
      "reason": "The claim relies on source [9], but no excerpt from [9] is provided; thus the statement cannot be verified against the bibliography.",
      "fix": "Delete the paragraph or rephrase it as an assumption without citation."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "The analysis in [6] derives a gauge field by locally gauging the translational group of a crystal lattice.  The key step is to promote the global translation $x\\to x+a$ to a local transformation $x\\to x+\\epsilon(x)$, introducing a connection $R_{\\mu}(x)$ that transforms as $R_{\\mu}(x)\\;\\longrightarrow\\;R_{\\mu}(x)-\\partial_{\\mu}\\epsilon(x)$.  The covariant derivative acting on an electron field $\\psi(x)$ becomes $D_{\\mu}\\psi = (\\partial_{\\mu}+g\\,R_{\\mu}(x))\\psi$, with $g$ a coupling constant.  The field strength follows from the commutator $[F_{\\mu\\nu}] = [D_{\\mu},D_{\\nu}] = g(\\partial_{\\mu}R_{\\nu}-\\partial_{\\nu}R_{\\mu}+g\\,[R_{\\mu},R_{\\nu}])$.",
      "reason": "While the excerpt from [6] does discuss gauging translations, the specific formulae for the covariant derivative and field strength are not present in the provided excerpt, making the detailed claim unsupported.",
      "fix": "Simplify the description to match the excerpt, e.g., mention only that gauging translations introduces a connection, without specifying the exact formulas."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "The adelic product formula of [12], $\\prod_{v}|q|_{v}=1\\qquad\\forall\\,q\\in\\mathbb{Q}^{\\times}$, relates the Archimedean absolute value $|\\cdot|_{\\infty}$ to all $p$‑adic absolute values $|\\cdot|_{p}$.  If a physical theory were to be built solely on a finite‑group symmetry (hence only on a discrete set of $p$‑adic places), the product over the omitted Archimedean factor would not equal unity, violating the global consistency condition.",
      "reason": "No excerpt from source [12] is provided; the statement about the product formula and its physical implication is unsupported.",
      "fix": "Remove the claim or rephrase it as an unreferenced speculation without citation."
    }
  ],
  "soft": []
}