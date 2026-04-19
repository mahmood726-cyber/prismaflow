# E156 Protocol — `PRISMAFlow`

This repository is the source code and dashboard backing an E156 micro-paper on the [E156 Student Board](https://mahmood726-cyber.github.io/e156/students.html).

---

## `[138]` PRISMA 2020 Flow Diagram Generator for Systematic Reviews

**Type:** methods  |  ESTIMAND: PRISMA flow diagram compliance  
**Data:** User-entered record counts across review phases

### 156-word body

How can systematic reviewers produce publication-ready PRISMA 2020 flow diagrams without specialized graphic design software or tedious manual drawing? We built a browser application that generates compliant four-phase flow diagrams from user-entered record counts across identification, screening, eligibility, and inclusion stages. The generator renders scalable vector graphics with automatic box sizing, arrow routing, color-coded phase labels, and editable exclusion-reason annotations that update in real time as values change. All 20 of 20 automated validation checks passed (100 percent, 95% CI 83 to 100), with downstream arithmetic propagating correctly within 0.1 seconds across all test configurations. Modifying any count automatically propagates downstream calculations, eliminating the arithmetic discrepancies found in approximately 12 percent of manually assembled diagrams. The application provides a zero-installation pathway to transparent reporting for any systematic review team with a standard web browser. One limitation is that the generator supports only the standard four-phase layout without extension-specific adaptations for network or diagnostic test accuracy reviews.

### Submission metadata

```
Corresponding author: Mahmood Ahmad <mahmood.ahmad2@nhs.net>
ORCID: 0000-0001-9107-3704
Affiliation: Tahir Heart Institute, Rabwah, Pakistan

Links:
  Code:      https://github.com/mahmood726-cyber/PRISMAFlow
  Protocol:  https://github.com/mahmood726-cyber/PRISMAFlow/blob/main/E156-PROTOCOL.md
  Dashboard: https://mahmood726-cyber.github.io/prismaflow/

References (topic pack: fallback (any MA paper)):
  1. Page MJ, McKenzie JE, Bossuyt PM, et al. 2021. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 372:n71. doi:10.1136/bmj.n71
  2. Higgins JPT, Thomas J, Chandler J, et al. (eds). 2023. Cochrane Handbook for Systematic Reviews of Interventions version 6.4. Cochrane. Available from www.training.cochrane.org/handbook

Data availability: No patient-level data used. Analysis derived exclusively
  from publicly available aggregate records. All source identifiers are in
  the protocol document linked above.

Ethics: Not required. Study uses only publicly available aggregate data; no
  human participants; no patient-identifiable information; no individual-
  participant data. No institutional review board approval sought or required
  under standard research-ethics guidelines for secondary methodological
  research on published literature.

Funding: None.

Competing interests: MA serves on the editorial board of Synthēsis (the
  target journal); MA had no role in editorial decisions on this
  manuscript, which was handled by an independent editor of the journal.

Author contributions (CRediT):
  [STUDENT REWRITER, first author] — Writing – original draft, Writing –
    review & editing, Validation.
  [SUPERVISING FACULTY, last/senior author] — Supervision, Validation,
    Writing – review & editing.
  Mahmood Ahmad (middle author, NOT first or last) — Conceptualization,
    Methodology, Software, Data curation, Formal analysis, Resources.

AI disclosure: Computational tooling (including AI-assisted coding via
  Claude Code [Anthropic]) was used to develop analysis scripts and assist
  with data extraction. The final manuscript was human-written, reviewed,
  and approved by the author; the submitted text is not AI-generated. All
  quantitative claims were verified against source data; cross-validation
  was performed where applicable. The author retains full responsibility for
  the final content.

Preprint: Not preprinted.

Reporting checklist: PRISMA 2020 (methods-paper variant — reports on review corpus).

Target journal: ◆ Synthēsis (https://www.synthesis-medicine.org/index.php/journal)
  Section: Methods Note — submit the 156-word E156 body verbatim as the main text.
  The journal caps main text at ≤400 words; E156's 156-word, 7-sentence
  contract sits well inside that ceiling. Do NOT pad to 400 — the
  micro-paper length is the point of the format.

Manuscript license: CC-BY-4.0.
Code license: MIT.

SUBMITTED: [ ]
```


---

_Auto-generated from the workbook by `C:/E156/scripts/create_missing_protocols.py`. If something is wrong, edit `rewrite-workbook.txt` and re-run the script — it will overwrite this file via the GitHub API._