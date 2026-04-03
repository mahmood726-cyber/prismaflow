# Code Review Findings: PRISMAFlow

**Reviewer**: Claude Opus 4.6 (1M context)
**Date**: 2026-04-03
**Files reviewed**: `prisma-flow.html` (1,309 lines), `index.html` (44 lines)

## P0 (Critical) -- 0 found

No critical issues.

## P1 (Important) -- 3 found

### P1-1: Missing skip-nav link (Accessibility)
- **File**: `prisma-flow.html`
- **Line**: 293 (body start)
- **Issue**: No skip navigation link for keyboard/screen-reader users. The TransportabilityCalc app has one; this should too.
- **Fix**: Add `<a href="#tab-entry" class="skip-link">Skip to main content</a>` before the header, plus CSS for `.skip-link`.

### P1-2: No CSV export = no CSV injection risk, but no export functionality
- **File**: `prisma-flow.html`
- **Issue**: App exports JSON and SVG but not CSV. Not a bug per se, but limits usability.

### P1-3: Dead code from first renderDiagram attempt (lines 758-928)
- **File**: `prisma-flow.html`, lines 758-928
- **Issue**: The first `renderDiagram` function is immediately overwritten at line 969. The first version is dead code containing a buggy SVG close attempt (line 920-924).

## P2 (Minor) -- 3 found

### P2-1: `escapeHtml` function is correct (quotes included)
- Good: The function escapes `&`, `<`, `>`, `"`, and `'`.

### P2-2: Blob URL correctly revoked in downloadBlob (line 1149)
- Good practice observed.

### P2-3: localStorage key is app-specific (`prismaflow-data`)
- Good: unique key avoids collision.

## Summary
- P0: 0 | P1: 3 | P2: 3
- Overall: Clean app with proper escaping, ARIA tabs, and validation. Main gap is skip-nav link.
