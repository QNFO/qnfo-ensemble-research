{
  "verdict": "revise",
  "hard": [
    {
      "id": "C1",
      "severity": "HARD",
      "claim": "In fusion energy, the China Fusion Engineering Test Reactor (CFETR) and the Huazhong Field Reversed Configuration (HFRC) represent low‑density steady‑state and high‑density pulsed pathways whose magnetohydrodynamic stability assessments differ, so that for CFETR active control methods may be required for resistive‑wall‑mode stabilization in $80\\%$ of steady‑state‑operation scenarios [4].",
      "reason": "The excerpt for reference [4] does not contain any quantitative statement about \"80% of steady‑state‑operation scenarios\"; the claim is not supported by the supplied bibliography entry.",
      "fix": "Remove the unsupported quantitative claim or replace it with a statement that is directly supported by the excerpt for [4]."
    },
    {
      "id": "C2",
      "severity": "HARD",
      "claim": "In quantum computing, the field itself has split into two ontologies—mimetic simulation rooted in structural isomorphism and algorithmic calculation rooted in fault‑tolerant abstraction—whose hardware requirements and near‑term viability diverge [11].",
      "reason": "No excerpt is provided for reference [11]; the paper cites a claim that cannot be verified from the supplied bibliography.",
      "fix": "Delete or re‑phrase the sentence to avoid citing [11] for unsupported content."
    },
    {
      "id": "C3",
      "severity": "HARD",
      "claim": "A systematic inventory of such fractures enumerates 29 distinct unresolved bifurcations, spanning topics from the nature of the continuum to the status of the observer, and argues that they are interconnected rather than isolated puzzles [9].",
      "reason": "The bibliography entry for [9] contains only a URL and no excerpt that confirms the enumeration of 29 bifurcations or their interconnection; the claim is unsupported.",
      "fix": "Remove the citation to [9] or replace the claim with a statement that can be directly sourced from an available excerpt."
    },
    {
      "id": "C4",
      "severity": "HARD",
      "claim": "Independent scrutiny of one of those schisms—the observer inside versus outside—finds that a proposed ultrametric resolution survives only in a limited sense and is not currently empirically distinguishable from relational alternatives [12].",
      "reason": "No excerpt is provided for reference [12]; the claim cannot be verified from the supplied bibliography.",
      "fix": "Delete or re‑write the sentence without citing [12] for unsupported content."
    },
    {
      "id": "C5",
      "severity": "HARD",
      "claim": "road‑marking mediated calibration enables targetless extrinsic calibration of a stereo camera and a LiDAR whose fields of view do not overlap, reporting positional accuracy of approximately $0.02\\ \\mathrm{m}$ and angular accuracy of approximately $0.086^{\\circ}$ without manual operation; the authors explicitly flag that their assumption of locally accurate odometry can fail under repeated accelerations and decelerations, which distorts the 3D map, and recommend folding odometry uncertainty into the calibration optimization [3].",
      "reason": "The excerpt for reference [3] is not provided; the detailed quantitative accuracy figures and the comment on odometry are not supported by the supplied bibliography.",
      "fix": "Remove the unsupported quantitative details or replace them with information that is present in the excerpt for [3] (if any)."
    },
    {
      "id": "C6",
      "severity": "HARD",
      "claim": "[5] discusses calibration across multiple environments and its relevance to out‑of‑domain generalization.",
      "reason": "No excerpt is provided for reference [5]; the statement cannot be verified from the supplied bibliography.",
      "fix": "Delete the citation to [5] or replace it with a claim that is supported by an available excerpt."
    },
    {
      "id": "C7",
      "severity": "HARD",
      "claim": "The published version of the present paper [10] established the framework definitions, the counting derivations, and the closure‑error algebra that this revision carries forward; its Derivation 2 (21 pairs against 29 schisms, leaving at least 8 unassigned) and Derivation 6 (energy‑window factors 2 and 3; mean schisms per domain $29/7\\approx4.14$) are reproduced unchanged here because their arithmetic is correct.",
      "reason": "No excerpt is provided for reference [10]; the claim about its content cannot be verified from the supplied bibliography.",
      "fix": "Remove the citation to [10] or replace the sentence with a self‑contained description that does not rely on an unsupported source."
    },
    {
      "id": "C8",
      "severity": "HARD",
      "claim": "The Feynman–Shor bifurcation supplies a concrete two‑ontology schism: quantum computing has split into a mimetic‑simulation lineage, described as inherently robust to noise and viable on current hardware, and an algorithmic‑calculation lineage, described as practically intractable without fault tolerance because of the fragility of phase estimation [11].",
      "reason": "Reference [11] has no excerpt; the detailed description of the bifurcation is unsupported.",
      "fix": "Delete or re‑write the sentence to avoid citing [11] for unsupported content."
    },
    {
      "id": "C9",
      "severity": "HARD",
      "claim": "Independent scrutiny of the observer schism (S10) finds that embedding the observer as a node in an ultrametric tree relocates rather than eliminates the external vantage point, that the resolution is distinct from relational quantum mechanics and QBism, and that it is not currently empirically distinguishable from them [12]; this supports the paper's classification of the observer schism as, at present, lacking any admissible calibrated translation.",
      "reason": "Reference [12] lacks an excerpt; the claim cannot be verified.",
      "fix": "Remove the citation to [12] or replace the claim with a statement that can be sourced from an available excerpt."
    },
    {
      "id": "C10",
      "severity": "HARD",
      "claim": "Input 1 (from [9]): number of unresolved bifurcations $N_{\\mathrm{schism}}=29$.",
      "reason": "No excerpt for [9] provides this numeric value; the input is unsupported.",
      "fix": "Replace the input with a statement that does not rely on an unsupported citation, or remove the citation."
    },
    {
      "id": "C11",
      "severity": "HARD",
      "claim": "Input 3 (assumption): a two‑ontology bifurcation partitions one domain into $m=2$ frameworks; a representative example is provided in [11].",
      "reason": "The excerpt for [2] does not contain this partitioning claim, and [11] has no excerpt; the statement is unsupported.",
      "fix": "Delete the unsupported citation and re‑state the assumption without referencing [11] or [2]."
    },
    {
      "id": "C12",
      "severity": "HARD",
      "claim": "Input 7 (from [3]): mediated (road‑marking) calibration achieved positional accuracy $\\approx0.02\\ \\mathrm{m}$ and angular accuracy $\\approx0.086^{\\circ}$.",
      "reason": "No excerpt for [3] contains these quantitative results; the claim is unsupported.",
      "fix": "Remove the citation to [3] for this quantitative claim or replace it with a supported statement."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The paper provides a thorough literature review but could deepen discussion of how the combinatorial bounds compare to prior work on calibration in engineering domains.",
      "reason": "Depth of literature treatment could be improved.",
      "fix": "Add a brief comparative paragraph referencing existing engineering calibration studies."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Appendix A reports no divergent claims, but the reviewer notes that the absence of divergence may be due to insufficient reporting of draft differences.",
      "reason": "Potential omission of divergence details.",
      "fix": "Verify that all draft divergences are captured; if none exist, keep as is."
    }
  ]
}