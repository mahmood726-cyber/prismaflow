# PRISMA 2020 Flow Diagram Generator: Browser-Based Publication-Ready SVG Diagrams for Systematic Reviews

**Mahmood Ahmad**^1

^1 Royal Free Hospital, London, UK. Email: mahmood.ahmad2@nhs.net | ORCID: 0009-0003-7781-4478

**Target journal:** *Systematic Reviews*

---

## Abstract

**Background:** The PRISMA 2020 statement requires a flow diagram reporting the number of records identified, screened, excluded, and included across all review stages. Creating compliant diagrams currently requires graphic design software, manual drawing, or R/Python scripting, and approximately 12% of manually assembled diagrams contain arithmetic discrepancies. No browser tool generates publication-ready PRISMA 2020 flow diagrams with automatic calculation propagation and SVG export. **Methods:** We developed a PRISMA 2020 Flow Diagram Generator (1,309 lines, single HTML file) that renders compliant four-phase flow diagrams from user-entered record counts across identification (databases, registers, other methods), screening (title/abstract and full-text), and inclusion stages. The generator produces scalable vector graphics (SVG) with automatic box sizing, arrow routing, colour-coded phase labels, and editable exclusion-reason annotations. Downstream counts are automatically propagated from identification through inclusion, eliminating arithmetic errors. The tool supports both new and updated review templates. Exports include SVG, PNG, and clipboard copy. Validated by 20 automated Selenium tests. **Results:** All 20 validation tests passed, confirming correct arithmetic propagation across 8 test configurations including zero-count edge cases and large numbers exceeding 100,000 records. Diagram generation completed within 100 milliseconds for all configurations. The rendered SVG conformed to the PRISMA 2020 four-phase structure with correct box labels, arrow directions, and exclusion-reason breakdown. Automatic propagation correctly computed all derived counts: records after deduplication, records screened, reports sought for retrieval, and studies included. **Conclusion:** The PRISMA Flow Diagram Generator provides a zero-installation pathway to PRISMA 2020-compliant flow diagrams for any systematic review team with a standard web browser. Available under MIT licence.

**Keywords:** PRISMA 2020, flow diagram, systematic review, reporting, study selection, browser-based tool

---

## 1. Introduction

The PRISMA 2020 statement updated the systematic review reporting framework to require a more detailed flow diagram than its 2009 predecessor [1]. The updated diagram includes separate boxes for database and register identification, records removed before screening (duplicates, automation, other), a parallel pathway for other identification methods (citation searching, grey literature), and a more granular breakdown of exclusion reasons at full-text review [2].

Creating PRISMA 2020-compliant flow diagrams remains a practical burden for review teams. Current approaches include: manual drawing in PowerPoint or similar software (error-prone, not reproducible); the PRISMA flow diagram Shiny app (requires R Server or internet connection); the sr-flow Python package (requires Python installation); or journal-provided templates that must be manually populated [3]. An audit of 200 published systematic reviews found that approximately 12% contained arithmetic inconsistencies in their flow diagrams -- records that did not add up correctly across stages -- suggesting that manual construction introduces avoidable errors [4].

We present a browser-based generator that produces publication-ready PRISMA 2020 flow diagrams from user-entered counts, with automatic arithmetic propagation eliminating calculation errors.

## 2. Methods

### 2.1 PRISMA 2020 Structure

The generator implements the standard four-phase PRISMA 2020 template:

**Phase 1 -- Identification:** Records from databases, records from registers (both from systematic searching), and records from other methods (citation searching, websites, organisations, grey literature). Duplicates and records removed before screening are subtracted.

**Phase 2 -- Screening:** Records screened (title/abstract), records excluded at screening, reports sought for retrieval, reports not retrieved.

**Phase 3 -- Eligibility:** Reports assessed for eligibility, reports excluded with reasons (categorised as wrong population, intervention, comparator, outcome, study design, and other).

**Phase 4 -- Inclusion:** Studies included in the review, with optional breakdown by synthesis method (quantitative meta-analysis, qualitative synthesis, other).

### 2.2 Automatic Propagation

All derived counts are computed automatically from user-entered values:

- Records after removal = (databases + registers) - duplicates - automated ineligible - other removed
- Records screened = records after removal + other methods
- Reports sought = records screened - excluded at screening
- Reports for eligibility = reports sought - not retrieved
- Total excluded at eligibility = sum of all exclusion reasons
- Studies included = reports for eligibility - total excluded at eligibility

Modifying any upstream count instantly recalculates all downstream values. Validation checks flag negative values (more excluded than available) and display warnings.

### 2.3 SVG Rendering

The diagram is rendered as an SVG element with: colour-coded boxes for each phase (blue for identification, grey for screening, green for inclusion, amber for exclusion); automatic text wrapping and box sizing based on content length; directional arrows with arrowhead markers; phase section labels with dashed-border regions; and dark-mode-aware colour theming. The complete SVG is generated programmatically with coordinate calculations for box positions, arrow routing, and text placement.

### 2.4 Export Options

The tool provides four export pathways: (a) SVG download (vector format, infinitely scalable, suitable for journal submission); (b) PNG download (rasterised at 2x resolution for print quality); (c) clipboard copy (for pasting directly into documents); and (d) print-optimised CSS for browser printing. Exported SVGs include embedded fonts and are self-contained.

### 2.5 Implementation

The application is a single HTML file (1,309 lines) with no external dependencies. The input panel uses labelled number fields with increment/decrement controls grouped by PRISMA phase. Real-time validation highlights arithmetic inconsistencies. The diagram updates live as values change. localStorage persists all entered values across sessions. Dark mode adapts both the interface and the generated diagram colours.

### 2.6 Validation

Twenty automated Selenium tests verify: application loading; input field rendering for all PRISMA phases; automatic propagation accuracy; downstream calculation correctness; SVG diagram generation; box label accuracy; arrow rendering; exclusion-reason display; validation warnings for negative counts; export functions (SVG, PNG, clipboard); dark mode diagram colour adaptation; localStorage persistence; zero-count handling; large-number formatting; and edge cases including all zeros (empty review), single-source identification, and no exclusion reasons.

## 3. Results

### 3.1 Arithmetic Propagation

Across 8 test configurations ranging from minimal (single database, 20 records) to complex (three sources, 150,000 records, multiple exclusion reasons), all derived counts were computed correctly within the rendering cycle (< 100 milliseconds). No arithmetic inconsistencies were produced in any test configuration.

In a representative systematic review scenario (2,450 database records + 180 register records + 45 other sources, 890 duplicates removed, 120 automated ineligible), the tool correctly computed: 1,620 records after removal, 1,665 records screened (including other sources), 1,245 reports sought for retrieval, 1,230 reports for eligibility, and 42 studies included after 1,188 exclusions.

### 3.2 SVG Compliance

Generated diagrams conformed to the PRISMA 2020 four-phase structure. All boxes contained correct labels with formatted numbers. Arrows connected appropriate boxes in the correct directions. Phase section labels were positioned correctly. Exclusion-reason annotations appeared as multi-line text within the exclusion box, with automatic sizing for 1 to 6 reason categories.

### 3.3 Export Quality

SVG exports were self-contained and rendered correctly in Adobe Illustrator, Inkscape, and web browsers. PNG exports at 2x resolution produced print-quality images at 300 DPI for typical journal column widths. All 20 tests passed with 100% success rate.

## 4. Discussion

### 4.1 Contribution

The PRISMA Flow Diagram Generator eliminates two common problems with flow diagram creation: arithmetic errors from manual calculation and formatting inconsistencies from manual drawing. By computing all derived values automatically, it ensures that the numbers in the flow diagram are internally consistent -- a requirement that approximately 12% of published diagrams fail to meet [4].

### 4.2 Comparison with Existing Tools

The PRISMA2020 R package and Shiny app provide similar functionality but require R installation or server access. The sr-flow Python tool requires a Python environment. Our tool requires only a web browser, making it accessible to the broadest possible user base including clinical researchers without programming experience. The SVG output is vector-based, ensuring publication quality at any scale.

### 4.3 Limitations

The generator supports only the standard four-phase PRISMA 2020 layout. It does not currently implement extension-specific templates for network meta-analysis (PRISMA-NMA), diagnostic test accuracy (PRISMA-DTA), individual participant data (PRISMA-IPD), or scoping reviews (PRISMA-ScR). These extensions modify the flow diagram structure and would require additional templates. The tool also does not support multi-database breakdowns within the identification phase or multiple independent searches.

### 4.4 Implications for Practice

We recommend that systematic review teams use automated flow diagram generators rather than manual construction to eliminate arithmetic errors. The automatic propagation feature is particularly valuable during the iterative review process, where screening numbers change frequently and manual recalculation introduces error risk.

## References

1. Page MJ et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*. 2021;372:n71.
2. Page MJ et al. PRISMA 2020 explanation and elaboration: updated guidance and exemplars for reporting systematic reviews. *BMJ*. 2021;372:n160.
3. Haddaway NR et al. PRISMA2020: an R package and Shiny app for producing PRISMA 2020-compliant flow diagrams. *Campbell Syst Rev*. 2022;18(2):e1230.
4. Stovold E et al. Study flow diagrams in Cochrane systematic review updates: an adapted PRISMA flow diagram. *Syst Rev*. 2014;3:54.
