import sys
from pathlib import Path
import pdfplumber

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = Path("report/BaoCao_TieuLuan_PLDC_UIT_FINAL.pdf")

with pdfplumber.open(pdf_path) as pdf:
    print(f"=== DETAILED PDF LAYOUT & VISUAL AUDIT ({len(pdf.pages)} pages) ===")
    
    for idx, page in enumerate(pdf.pages):
        page_num = idx + 1
        width = page.width
        height = page.height
        
        # Extract text & lines
        text = page.extract_text() or ""
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        
        # Check fonts used on this page
        fonts = set()
        font_sizes = set()
        for char in page.chars:
            fonts.add(char.get('fontname', 'Unknown'))
            font_sizes.add(round(char.get('size', 0), 1))
            
        print(f"\n--- Page {page_num:2d} | Size: {width:.1f} x {height:.1f} pt | Lines: {len(lines)} | Fonts: {', '.join(sorted(fonts))} | Sizes: {sorted(font_sizes)}")
        
        # Check first line (header/title)
        first_line = lines[0] if lines else "EMPTY"
        last_line = lines[-1] if lines else "EMPTY"
        print(f"    Top line   : {first_line[:75]}")
        print(f"    Bottom line: {last_line[:75]}")
        
        # Check page number footer
        if page_num > 1:
            has_footer = any("Trang" in l for l in lines[-2:])
            if not has_footer:
                print(f"    [WARN] Page {page_num} might lack standard footer: {last_line}")
        else:
            if any("Trang" in l for l in lines[-2:]):
                print(f"    [WARN] Cover page has footer page number!")
