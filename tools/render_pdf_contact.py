from pathlib import Path
from PIL import Image, ImageDraw

folder = Path("tmp/pdf_render")
files = sorted(folder.glob("page-*.png"))
for start in range(0, len(files), 6):
    canvas = Image.new("RGB", (780, 780), "white")
    draw = ImageDraw.Draw(canvas)
    for position, file in enumerate(files[start:start + 6]):
        image = Image.open(file).convert("RGB").resize((260, 368))
        x, y = (position % 3) * 260, (position // 3) * 390
        canvas.paste(image, (x, y))
        draw.text((x + 5, y + 370), f"Page {start + position + 1}", fill="black")
    canvas.save(folder / f"contact-{start // 6 + 1}.png")
