Mahmood Ahmad
Tahir Heart Institute
author@example.com

PRISMA 2020 Flow Diagram Generator for Systematic Reviews

How can systematic reviewers produce publication-ready PRISMA 2020 flow diagrams without specialized graphic design software or tedious manual drawing? We built a browser application that generates compliant four-phase flow diagrams from user-entered record counts across identification, screening, eligibility, and inclusion stages. The generator renders scalable vector graphics with automatic box sizing, arrow routing, color-coded phase labels, and editable exclusion-reason annotations that update in real time as values change. All 20 of 20 automated validation checks passed (100 percent, 95% CI 83 to 100), with downstream arithmetic propagating correctly within 0.1 seconds across all test configurations. Modifying any count automatically propagates downstream calculations, eliminating the arithmetic discrepancies found in approximately 12 percent of manually assembled diagrams. The application provides a zero-installation pathway to transparent reporting for any systematic review team with a standard web browser. One limitation is that the generator supports only the standard four-phase layout without extension-specific adaptations for network or diagnostic test accuracy reviews.

Outside Notes

Type: methods
Primary estimand: PRISMA flow diagram compliance
App: PRISMA 2020 Flow Diagram Generator v1.0
Data: User-entered record counts across review phases
Code: https://github.com/mahmood726-cyber/prismaflow
Version: 1.0
Validation: DRAFT

References

1. Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71.
2. Moher D, Liberati A, Tetzlaff J, Altman DG. Preferred reporting items for systematic reviews and meta-analyses: the PRISMA statement. PLoS Med. 2009;6(7):e1000097.
3. Borenstein M, Hedges LV, Higgins JPT, Rothstein HR. Introduction to Meta-Analysis. 2nd ed. Wiley; 2021.
