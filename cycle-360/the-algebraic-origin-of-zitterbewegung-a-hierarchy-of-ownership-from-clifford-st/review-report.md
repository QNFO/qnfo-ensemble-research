{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Examples include band electrons in graphene [2] , cavity electrodynamics [3] , ultracold atoms …",
      "reason": "Reference [3] is cited but does not appear in the References list, violating citation integrity.",
      "fix": "Add a proper reference entry for [3] to the References section, using the exact bibliographic information from the supplied bibliography."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Examples include … ultracold atoms … [5] , … [6] , …",
      "reason": "References [5] and [6] are cited in the text but are missing from the References list, violating citation integrity.",
      "fix": "Insert correct reference entries for [5] and [6] into the References section, matching the supplied bibliography."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "arXiv:1003.3074 [4] considers mirror oscillation …",
      "reason": "Citation [4] is used without a supporting excerpt from its full text; the paper must only cite works for which specific statements are derivable from the supplied excerpts.",
      "fix": "Either provide a supporting excerpt for [4] that justifies the claim or remove/replace the statement with one supported by an available excerpt."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Examples include … cavity electrodynamics [3] …",
      "reason": "Citation [3] lacks a supporting excerpt from its full text; the paper must only cite works for which specific statements are derivable from the supplied excerpts.",
      "fix": "Either add the required excerpt for [3] or delete/modify the statement to rely only on works with available excerpts."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Examples include … ultracold atoms … [5] , … [6] …",
      "reason": "Citations [5] and [6] lack supporting excerpts; the paper must not cite works without such excerpts.",
      "fix": "Either supply appropriate excerpts for [5] and [6] or remove/replace the statements that depend on them."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "The work of arXiv:1105.2884 [1] shows that ZB can be converted to directed centre‑of‑mass motion …",
      "reason": "The excerpt for [1] confirms this claim, so this is acceptable. No hard issue.",
      "fix": ""
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "The work of arXiv:1210.5030 [2] investigates ZB … Zeeman field can suppress or enhance the ZB amplitude …",
      "reason": "The excerpt for [2] confirms these statements, so this is acceptable. No hard issue.",
      "fix": ""
    }
  ],
  "soft": []
}