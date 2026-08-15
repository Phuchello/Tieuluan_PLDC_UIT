# Codex Final Independent Audit

**Audit basis:** remote canonical state `760f92063dda743d33ee2c658b866bcafeb61cf4`.  
**Scope:** report content, citations, facts, and final publishing artifacts. No style findings are treated as repair grounds.

## Findings

### P0

None.

### P1

1. **File / section:** `report/REPORT_FINAL.md`, 3.1.1(1), 3.2.1, 3.5, Chapter 4 and Conclusion.  
   **Issue:** Several clauses use an unqualified formulation such as “vi phạm”, “quảng cáo sai sự thật” or “lợi dụng” for the case-specific conduct. The primary article reports early allegations and charging, not a final adjudication.  
   **Evidence:** `research/PRIMARY_SOURCE_RECORD.md` identifies the source as an account of initial allegations/procedural actions, not a judgment.  
   **Impact:** Can be read as treating charge-stage facts as a guilt determination.  
   **Minimal repair:** Qualify only these case-specific clauses as conduct “bị nêu/bị xem xét” or a matter to be assessed if established in proceedings; retain the general legal propositions and analysis.

2. **File / section:** `report/REPORT_FINAL.md`, 3.4.1, “Về lý trí”.  
   **Issue:** The bullet says Đạt “nhận thức rõ” and “thấy trước” specified consequences as if they were established facts.  
   **Evidence:** The primary source reports that Đạt directed edited/cut materials and inflated/misleading content to build trust and encourage purchases; it does not directly report his internal state.  
   **Impact:** Exceeds the public evidence and weakens the report’s own evidentiary boundary.  
   **Minimal repair:** Express the two statements as academic inferences based on the reported conduct, not factual findings.

### P2

1. **File / section:** `research/LEGAL_BASIS_MATRIX.md`.  
   **Issue:** The archived support matrix still labels the advertising law as “sửa đổi 2018”, whereas the active report correctly cites VBHN 88/VBHN-VPQH (2025).  
   **Impact:** None to the canonical report; research-support consistency only.  
   **Minimal repair:** Optional; no manuscript or release repair needed.

### P3

None recorded. Style preferences were intentionally excluded under the human-writing lock.

## Audit Checks

- **Facts:** Dates, counts, terminology “sản phẩm Đông y”, “tổng giá trị tiền hàng”, and “tạm giữ” align with the primary source record.
- **Four elements:** The report maintains the UIT PLĐC framework and does not turn into an offence-threshold paper.
- **Citations:** Active reference set is sequential `[1]` through `[6]`; no `[7]`, `[8]`, or orphan citation found.
- **Publishing:** The remote final package provides DOCX/PDF/HTML. Page-level verification is recorded in the existing V3 QA; independent visual verification is repeated for the final PDF before release where technically possible.

## Repair Gate Outcome

The two P1 items were repaired only at the quoted passages. `REPORT_FINAL.html`, the DOCX master, and the Word-exported PDF were regenerated. Re-audit of the affected sections, citation set and prohibited-phrase scan found no remaining P0 or P1. The sole `5.429 người` search hit explicitly says that 5.429 successful orders do **not** equal 5.429 distinct buyers; it is a protective clarification, not a regression.

## Final Re-audit Result

- **P0 remaining:** 0
- **P1 remaining:** 0
- **P2 remaining:** 1 (non-canonical legacy `research/LEGAL_BASIS_MATRIX.md` has an abbreviated advertising-law history; it does not control the report or citations)
- **P3 remaining:** 0
- **PDF/DOCX check:** PASS. The rebuilt Word-derived PDF has 19 A4 pages; cover, member table, two-page TOC, all chapter starts, tables, conclusion and references were visually inspected. No blank pages, table clipping, broken Vietnamese glyphs or visible Markdown syntax found.

## Lecturer-Facing Report Score

**45/50.** Deductions: 1 point for reliance on a single public case account while the matter remains under investigation; 2 points because public evidence does not permit fully individualized capacity/mental-state analysis for every charged person; 1 point for identity/team fields that remain for human completion; 1 point for a concise Chapter 4 that is useful but not central to the assignment’s analytical core.
