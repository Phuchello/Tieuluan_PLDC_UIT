# KIỂM ĐỊNH ĐỊNH DẠNG VÀ XUẤT BẢN WORD DOCX V3 (DOCX QA V3)

**Trạng thái kiểm định:** **PASS TOÀN DIỆN (STRUCTURAL & AUTOMATION PASS)**

---

## I. THÔNG SỐ QUY CHUẨN ĐỊNH DẠNG HỌC THUẬT

1. **Khổ giấy & Căn lề:**
   - Khổ giấy: A4 chuẩn ($21.0 \times 29.7$ cm).
   - Lề trái (Left margin): **3.2 cm** (chuẩn đóng gáy tiểu luận UIT).
   - Lề phải (Right margin): **2.0 cm**.
   - Lề trên (Top margin): **2.2 cm**.
   - Lề dưới (Bottom margin): **2.2 cm**.

2. **Quy cách Font chữ & Đoạn văn:**
   - Font chữ chính: **Times New Roman** cho toàn bộ văn bản (tiêu đề, thân bài, bảng biểu).
   - Cỡ chữ thân bài: **13 pt**.
   - Giãn dòng: **1.5 line spacing**.
   - Giãn đoạn: Space after **6 pt**, space before **0 pt**.
   - Căn lề đoạn văn: **Justified (Căn đều hai bên)**.
   - Thụt đầu dòng: **First-line indent 1.25 cm**.

3. **Cấu trúc Tiêu đề (Heading Styles):**
   - **Cover Title / Tiêu đề bìa:** Căn giữa, cỡ 14–16 pt, in đậm.
   - **Heading 1 (Tên chương / Mở đầu / Kết luận):** Căn giữa, cỡ **15 pt**, in đậm, chữ hoa, ngắt trang tự động trước mỗi chương (`page_break_before = True`).
   - **Heading 2 (Tiểu mục 1.1, 2.1, 3.1...):** Căn trái, cỡ **13.5 pt**, in đậm, `keep_with_next = True`.
   - **Heading 3 (Tiểu mục 3.1.1, 3.2.1...):** Căn trái, cỡ **13 pt**, in đậm, `keep_with_next = True`.
   - **Heading 4 (Tiểu mục A, B, C...):** Căn trái, cỡ **13 pt**, in đậm nghiêng.

4. **Trang bìa & Đánh số trang:**
   - Trang bìa thiết kế riêng biệt trên trang 1, ẩn số trang (`different_first_page_header_footer = True`).
   - Đánh số trang tự động ở chân trang (Footer): `Trang [PAGE]`, căn giữa, cỡ 10 pt từ trang 2 trở đi.

5. **Mục lục tự động Word (Native Word TOC):**
   - Tiêu đề "MỤC LỤC" căn giữa, cỡ 15 pt, in đậm (không gán style Heading 1 để tránh tự lập chỉ mục).
   - Mã trường TOC: `TOC \o "1-2" \h \z \u` hiển thị phân cấp Chương và Mục cấp 2, dot leaders và số trang cập nhật tự động qua Word COM.

6. **Bảng biểu & Mã nguồn:**
   - Bảng biểu: Bảng 1 đến Bảng 7 căn giữa trang, viền đen mảnh (0.6 pt), hàng tiêu đề nền xám nhạt (#ECECEC) in đậm. Độ rộng các cột được tự động cân đối tối ưu.
   - Đoạn mã / Sơ đồ ASCII: Đặt trong khối font Courier New 8.5 pt, viền khung cách biệt.

---

## II. KẾT QUẢ KIỂM ĐỊNH TỰ ĐỘNG
- Rò rỉ cú pháp Markdown `](#`: **0 lỗi**.
- Khoảng trống số hiệu tham khảo: **0 lỗi** (Đã chuẩn hóa 1 $\rightarrow$ 6).
- Cập nhật trường Word qua COM Automation: **THÀNH CÔNG (SUCCESS)**.
