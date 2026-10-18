{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "References list includes entries [4], [5], [6], [8], [10] that are not present in the provided bibliography.",
      "reason": "Citation integrity requires every reference to correspond to a bibliography entry; missing entries violate this rule.",
      "fix": "Remove all reference entries that are not in the bibliography or add the missing bibliography entries if they are part of the supplied list."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Section 2 cites works [5], [4], [6], [3], [8], and [7] which are absent from the provided bibliography.",
      "reason": "Citations must refer to bibliography entries; citing non‑existent works breaches citation integrity.",
      "fix": "Delete or replace each citation with a citation to a work that exists in the bibliography, ensuring each cited statement is supported by the cited work’s excerpt."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Section 2 does not acknowledge that the bibliography contains fewer than eight works, violating the requirement to state this limitation in the Discussion.",
      "reason": "The paper must note the limitation when fewer than eight bibliography entries are available; omission is a structural violation.",
      "fix": "Add a sentence in the Discussion (Section 6) stating that the bibliography contains fewer than eight works, limiting the breadth of related‑work coverage."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Reference entry [10] appears in the References list but there is no corresponding bibliography entry, and the paper does not cite it in the main text.",
      "reason": "Including a reference without a bibliography entry breaches citation integrity and adds an unsupported source.",
      "fix": "Remove reference [10] from the References list."
    }
  ],
  "soft": []
}