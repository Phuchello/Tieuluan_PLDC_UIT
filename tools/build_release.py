"""Build the release HTML and DOCX directly from the canonical Markdown report."""
from __future__ import annotations

import html
import re
import argparse
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "report" / "REPORT_FINAL.md"
HTML = ROOT / "report" / "REPORT_FINAL.html"
DOCX = ROOT / "report" / "BaoCao_TieuLuan_PLDC_UIT_FINAL.docx"
PDF = ROOT / "report" / "BaoCao_TieuLuan_PLDC_UIT_FINAL.pdf"


def inline(value: str) -> str:
    value = html.escape(value, quote=False)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", value)
    value = re.sub(r"\[([^]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', value)
    return value


def markdown_html(text: str) -> str:
    lines, out, in_pre, in_table, list_kind = text.splitlines(), [], False, False, None
    def close_list():
        nonlocal list_kind
        if list_kind:
            out.append(f"</{list_kind}>")
            list_kind = None
    def close_table():
        nonlocal in_table
        if in_table:
            out.append("</tbody></table>")
            in_table = False
    for i, line in enumerate(lines):
        if line.startswith("```"):
            close_list(); close_table()
            out.append("</pre>" if in_pre else "<pre>"); in_pre = not in_pre; continue
        if in_pre:
            out.append(html.escape(line)); continue
        if re.match(r"^\|.*\|\s*$", line):
            close_list()
            parts = [x.strip() for x in line.strip()[1:-1].split("|")]
            if i + 1 < len(lines) and re.match(r"^\|\s*:?-+", lines[i + 1]):
                out.append("<table><thead><tr>" + "".join(f"<th>{inline(x)}</th>" for x in parts) + "</tr></thead><tbody>")
                in_table = True
            elif not re.match(r"^\|\s*:?-+", line):
                out.append("<tr>" + "".join(f"<td>{inline(x)}</td>" for x in parts) + "</tr>")
            continue
        close_table()
        if not line.strip(): close_list(); continue
        if line.strip() == "---": close_list(); out.append("<hr>"); continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            close_list(); n = len(m.group(1)); out.append(f"<h{n}>{inline(m.group(2))}</h{n}>"); continue
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            if list_kind != "ul": close_list(); out.append("<ul>"); list_kind = "ul"
            out.append(f"<li>{inline(m.group(1))}</li>"); continue
        m = re.match(r"^\s*\d+[.)]\s+(.*)$", line)
        if m:
            if list_kind != "ol": close_list(); out.append("<ol>"); list_kind = "ol"
            out.append(f"<li>{inline(m.group(1))}</li>"); continue
        close_list(); out.append(f"<p>{inline(line)}</p>")
    close_list(); close_table()
    return "\n".join(out)


CSS = """
@page { size: A4; margin: 2.2cm 2cm 2.2cm 3.2cm; }
body { font-family: 'Times New Roman', serif; font-size: 13pt; line-height: 1.5; color:#111; }
h1 { text-align:center; font-size:16pt; margin:18pt 0 12pt; page-break-before:always; page-break-after:avoid; }
h2,h3 { text-align:left; line-height:1.3; page-break-after:avoid; }
h2 { font-size:14pt; margin:16pt 0 8pt; } h3 { font-size:13pt; margin:12pt 0 6pt; } p { text-align:justify; text-indent:1.25cm; margin:0 0 8pt; }
li { text-align:justify; margin-bottom:4pt; } table { width:100%; border-collapse:collapse; font-size:10pt; margin:10pt 0; }
th,td { border:0.6pt solid #333; padding:4pt; vertical-align:top; } th { background:#ececec; text-align:center; }
pre { white-space:pre-wrap; font-family:'Courier New',monospace; font-size:9pt; line-height:1.25; padding:8pt; border:0.5pt solid #aaa; }
hr { border:0; border-top:0.7pt solid #555; margin:16pt 0; } a { color:#111; text-decoration:none; }
"""


def set_font(run, size=13, bold=None, italic=None):
    run.font.name = "Times New Roman"; run._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    run.font.size = Pt(size)
    if bold is not None: run.bold = bold
    if italic is not None: run.italic = italic


def add_runs(paragraph, value, size=13):
    pattern = re.compile(r"(\*\*.*?\*\*|\*.*?\*|`.*?`)")
    for piece in pattern.split(value):
        if not piece: continue
        bold = piece.startswith("**") and piece.endswith("**")
        italic = piece.startswith("*") and piece.endswith("*") and not bold
        code = piece.startswith("`") and piece.endswith("`")
        content = piece[2:-2] if bold else piece[1:-1] if italic or code else piece
        run = paragraph.add_run(content); set_font(run, size, bold, italic)
        if code: run.font.name = "Courier New"


def set_cell(cell, value, bold=False, size=9):
    cell.text = ""
    p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(0); p.alignment = WD_ALIGN_PARAGRAPH.CENTER if bold else WD_ALIGN_PARAGRAPH.LEFT
    add_runs(p, value, size); 
    for run in p.runs: run.bold = bold if bold else run.bold
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


def add_toc_field(paragraph):
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), 'TOC \\o "1-3" \\h \\z \\u')
    paragraph._p.append(field)


def build_docx(text: str):
    d = Document(); section = d.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.left_margin, section.right_margin = Cm(3.2), Cm(2)
    section.top_margin, section.bottom_margin = Cm(2.2), Cm(2.2)
    normal = d.styles["Normal"]; normal.font.name = "Times New Roman"; normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman"); normal.font.size = Pt(13)
    normal.paragraph_format.line_spacing = 1.5; normal.paragraph_format.space_after = Pt(6); normal.paragraph_format.first_line_indent = Cm(1.25)
    section.different_first_page_header_footer = True
    for level, size in ((1,16),(2,14),(3,13),(4,13)):
        style = d.styles[f"Heading {level}"]; style.font.name = "Times New Roman"; style._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman"); style.font.size = Pt(size); style.font.bold = True
        style.paragraph_format.space_before = Pt(14); style.paragraph_format.space_after = Pt(8); style.paragraph_format.keep_with_next = True
        style.paragraph_format.first_line_indent = Cm(0)
        style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER if level == 1 else WD_ALIGN_PARAGRAPH.LEFT
    footer = section.footer.paragraphs[0]; footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = footer.add_run("Trang "); set_font(run, 10)
    fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), "PAGE"); footer._p.append(fld)
    lines = text.splitlines(); i = 0; table_rows = []; skip_toc = False
    cover = True
    while i < len(lines):
        line = lines[i]
        if line.startswith("## MỤC LỤC"):
            p = d.add_paragraph("MỤC LỤC", style="Heading 1"); p.paragraph_format.page_break_before = True
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_toc_field(d.add_paragraph())
            d.add_page_break(); skip_toc = True; i += 1; continue
        if skip_toc:
            if line.strip() == "---": skip_toc = False
            i += 1; continue
        if line.startswith("## DANH SÁCH") and cover:
            d.add_page_break(); cover = False
        if line.startswith("|"):
            table_rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|\s*:?-+", lines[i]): table_rows.append([x.strip() for x in lines[i].strip()[1:-1].split("|")])
                i += 1
            if table_rows:
                table = d.add_table(rows=len(table_rows), cols=len(table_rows[0])); table.style = "Table Grid"; table.alignment = WD_TABLE_ALIGNMENT.CENTER
                for r, row in enumerate(table_rows):
                    for c, cell_value in enumerate(row): set_cell(table.cell(r,c), cell_value, r == 0)
            continue
        if not line.strip() or line.strip() == "---": i += 1; continue
        if line.startswith("```"):
            i += 1; block=[]
            while i < len(lines) and not lines[i].startswith("```"): block.append(lines[i]); i += 1
            p=d.add_paragraph(); p.paragraph_format.left_indent=Cm(.5); p.paragraph_format.first_line_indent=Cm(0); p.paragraph_format.line_spacing=1.0
            add_runs(p, "\n".join(block), 9); i += 1; continue
        m=re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            title = m.group(2); markdown_level = len(m.group(1))
            if cover:
                p=d.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.first_line_indent=Cm(0); add_runs(p, title, 16 if markdown_level == 1 else 14); i += 1; continue
            lvl = 1 if markdown_level == 1 else 2 if markdown_level == 2 else 3
            p=d.add_paragraph(style=f"Heading {lvl}"); p.alignment=WD_ALIGN_PARAGRAPH.CENTER if lvl == 1 else WD_ALIGN_PARAGRAPH.LEFT; p.paragraph_format.first_line_indent=Cm(0)
            if lvl == 1: p.paragraph_format.page_break_before = True
            add_runs(p,title, [16,14,13][lvl-1]); i += 1; continue
        m=re.match(r"^\s*[-*]\s+(.*)$",line)
        if m:
            p=d.add_paragraph(style="List Bullet"); p.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY; p.paragraph_format.first_line_indent=Cm(0); add_runs(p,m.group(1)); i += 1; continue
        m=re.match(r"^\s*\d+[.)]\s+(.*)$",line)
        if m:
            p=d.add_paragraph(style="List Number"); p.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY; p.paragraph_format.first_line_indent=Cm(0); add_runs(p,m.group(1)); i += 1; continue
        p=d.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER if cover else WD_ALIGN_PARAGRAPH.JUSTIFY; p.paragraph_format.first_line_indent=Cm(0) if cover else Cm(1.25); add_runs(p,line); i += 1
    d.save(DOCX)


def pdf_markup(value: str) -> str:
    value = html.escape(value, quote=False)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", value)
    value = re.sub(r"`([^`]+)`", r"<font name='CourierNew'>\1</font>", value)
    return value


def build_pdf(text: str):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
    from reportlab.lib.fonts import addMapping
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import cm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Preformatted
    font_dir = Path("C:/Windows/Fonts")
    for name, filename in [("TimesNewRoman", "times.ttf"), ("TimesNewRoman-Bold", "timesbd.ttf"), ("TimesNewRoman-Italic", "timesi.ttf"), ("CourierNew", "cour.ttf")]:
        pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
    addMapping("TimesNewRoman", 0, 0, "TimesNewRoman"); addMapping("TimesNewRoman", 1, 0, "TimesNewRoman-Bold"); addMapping("TimesNewRoman", 0, 1, "TimesNewRoman-Italic")
    doc = SimpleDocTemplate(str(PDF), pagesize=A4, leftMargin=3.2*cm, rightMargin=2*cm, topMargin=2.2*cm, bottomMargin=2.2*cm)
    styles = getSampleStyleSheet()
    body = ParagraphStyle("VNBody", parent=styles["Normal"], fontName="TimesNewRoman", fontSize=13, leading=19.5, alignment=TA_JUSTIFY, firstLineIndent=1.25*cm, spaceAfter=7)
    cover_body = ParagraphStyle("VNCover", parent=body, alignment=TA_CENTER, firstLineIndent=0, spaceAfter=9)
    heading = {n: ParagraphStyle(f"H{n}", parent=body, fontName="TimesNewRoman-Bold", fontSize=max(13,17-n), leading=max(17,21-n), alignment=TA_CENTER if n <= 2 else TA_LEFT, firstLineIndent=0, spaceBefore=13, spaceAfter=8, keepWithNext=True) for n in range(1,5)}
    bullet = ParagraphStyle("Bullet", parent=body, firstLineIndent=0, leftIndent=.6*cm, bulletIndent=.2*cm)
    story=[]; lines=text.splitlines(); i=0; cover=True
    while i < len(lines):
        line=lines[i]
        if line.startswith("## DANH SÁCH") and cover: story.append(PageBreak()); cover=False
        if line.startswith("|"):
            rows=[]
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|\s*:?-+", lines[i]): rows.append([x.strip() for x in lines[i].strip()[1:-1].split("|")])
                i+=1
            if rows:
                data=[[Paragraph(pdf_markup(x), ParagraphStyle("T", parent=body, fontSize=8.2, leading=10, firstLineIndent=0, alignment=TA_CENTER if r==0 else TA_LEFT)) for x in row] for r,row in enumerate(rows)]
                widths=[(A4[0]-5.2*cm)/len(rows[0])]*len(rows[0]); table=Table(data, colWidths=widths, repeatRows=1)
                table.setStyle(TableStyle([("GRID",(0,0),(-1,-1),.4,colors.black),("BACKGROUND",(0,0),(-1,0),colors.HexColor("#E8E8E8")),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),3),("RIGHTPADDING",(0,0),(-1,-1),3),("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3)])); story.extend([table,Spacer(1,8)])
            continue
        if not line.strip() or line.strip()=="---": i+=1; continue
        if line.startswith("```"):
            i+=1; block=[]
            while i<len(lines) and not lines[i].startswith("```"): block.append(lines[i]); i+=1
            story.extend([Preformatted("\n".join(block), ParagraphStyle("Code",fontName="CourierNew",fontSize=8,leading=9.5,leftIndent=.2*cm)),Spacer(1,6)]); i+=1; continue
        m=re.match(r"^(#{1,6})\s+(.*)$",line)
        if m: story.append(Paragraph(pdf_markup(m.group(2)),heading[min(len(m.group(1)),4)])); i+=1; continue
        m=re.match(r"^\s*[-*]\s+(.*)$",line)
        if m: story.append(Paragraph(pdf_markup(m.group(1)), bullet, bulletText="•")); i+=1; continue
        m=re.match(r"^\s*\d+[.)]\s+(.*)$",line)
        if m: story.append(Paragraph(pdf_markup(m.group(1)), bullet, bulletText="-")); i+=1; continue
        story.append(Paragraph(pdf_markup(line), cover_body if cover else body)); i+=1
    def footer(canvas, _doc):
        canvas.setFont("TimesNewRoman",10); canvas.drawCentredString(A4[0]/2,1.2*cm,f"Trang {canvas.getPageNumber()}")
    doc.build(story,onFirstPage=footer,onLaterPages=footer)


def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--pdf-only",action="store_true"); args=parser.parse_args()
    text = SOURCE.read_text(encoding="utf-8")
    if args.pdf_only:
        build_pdf(text); return
    body = markdown_html(text)
    HTML.write_text(f"<!doctype html><html lang=\"vi\"><head><meta charset=\"utf-8\"><title>Báo cáo tiểu luận PLĐC</title><style>{CSS}</style></head><body>{body}</body></html>", encoding="utf-8")
    build_docx(text)

if __name__ == "__main__": main()
