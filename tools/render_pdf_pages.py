import sys
from pathlib import Path
from pdf2image import convert_from_path
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = Path("report/BaoCao_TieuLuan_PLDC_UIT_FINAL.pdf")
out_dir = Path("tmp/pdf_render")
out_dir.mkdir(parents=True, exist_ok=True)

print(f"Converting {pdf_path} to images...")
try:
    images = convert_from_path(str(pdf_path), dpi=100)
    for idx, img in enumerate(images):
        page_file = out_dir / f"page-{idx+1:02d}.png"
        img.save(page_file, "PNG")
    print(f"Saved {len(images)} page images to {out_dir}")

    # Create contact sheets (6 pages per sheet)
    for start in range(0, len(images), 6):
        sheet = Image.new("RGB", (780, 780), "white")
        draw = ImageDraw.Draw(sheet)
        for pos, img in enumerate(images[start:start+6]):
            thumb = img.resize((250, 354))
            x = (pos % 3) * 260 + 5
            y = (pos // 3) * 380 + 5
            sheet.paste(thumb, (x, y))
            draw.text((x + 5, y + 360), f"Page {start + pos + 1}", fill="black")
        sheet_num = start // 6 + 1
        sheet_path = out_dir / f"contact-{sheet_num}.png"
        sheet.save(sheet_path)
        print(f"Created contact sheet: {sheet_path}")
except Exception as e:
    print(f"Could not convert PDF using pdf2image (poppler may not be installed): {e}")
    print("Falling back to text-based layout validation.")
