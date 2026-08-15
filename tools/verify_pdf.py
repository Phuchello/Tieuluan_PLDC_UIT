import sys
import re
from pathlib import Path
import pdfplumber

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = Path('report/BaoCao_TieuLuan_PLDC_UIT_FINAL.pdf')
with pdfplumber.open(pdf_path) as pdf:
    total_pages = len(pdf.pages)
    print(f"Total PDF Pages: {total_pages}")
    
    all_text = ""
    for idx, page in enumerate(pdf.pages):
        text = page.extract_text() or ""
        all_text += f"\n=== PAGE {idx + 1} ===\n" + text

    print("\n--- PATTERN AUDIT IN PDF ---")
    patterns = [
        r"\]\(#",
        r"\]\(http",
        r"#33-",
        r"#34-",
        r"#35-",
        r"\[7\]",
        r"\[8\]",
        r"5\.429 khách",
        r"2,67 tỷ thiệt",
        r"2,67 tỷ thu lợi",
        r"anchor",
        r"PLACEHOLDER"
    ]
    for pat in patterns:
        matches = re.findall(pat, all_text)
        print(f"Pattern '{pat}': {len(matches)} matches")

    print("\n--- TOC PAGE INSPECTION (PAGE 3) ---")
    if total_pages >= 3:
        print(pdf.pages[2].extract_text())
        
    print("\n--- FIRST 200 CHARS OF EACH PAGE ---")
    for idx, page in enumerate(pdf.pages):
        t = (page.extract_text() or "").strip()
        preview = t.replace("\n", " ")[:80]
        print(f"Page {idx+1:2d}: {preview}")
