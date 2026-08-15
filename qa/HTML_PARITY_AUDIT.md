# HTML PARITY AUDIT (PHASE 2.5B)

Tài liệu này đánh giá sự đồng bộ 100% giữa bản thảo Markdown (`report/REPORT_FULL.md` / `report/REPORT_HARDENED.md`) và bản trình bày in ấn HTML (`report/REPORT_FULL.html`).

---

## I. KẾT QUẢ ĐỐI CHIẾU CHI TIẾT THEO CẤU TRÚC

| Hạng mục nội dung | Trạng thái Markdown (`.md`) | Trạng thái HTML (`.html`) | Đánh giá đồng bộ |
| :--- | :--- | :--- | :---: |
| **Trang bìa & Thông tin chung** | Đầy đủ thông tin UIT, môn học, năm học 2026 | Bìa đôi viền đen chuẩn quy cách in A4 | **PASS** |
| **Bảng phân công nhiệm vụ nhóm** | Đầy đủ 5 thành viên, tỷ lệ 100% | Bảng Table có border rõ ràng | **PASS** |
| **Mục lục báo cáo** | Đầy đủ từ Mở đầu đến Tài liệu tham khảo | Neo liên kết (Anchor IDs) chính xác 100% | **PASS** |
| **Phần Mở đầu (Mục 1 – 5)** | 5 tiểu mục đầy đủ | 5 tiểu mục đầy đủ | **PASS** |
| **Chương 1: Cơ sở lý luận (1.1 – 1.7)** | Đầy đủ khái niệm, dấu hiệu, 4 yếu tố | Đầy đủ 7 tiểu mục và sơ đồ ASCII cấu thành | **PASS** |
| **Chương 2: Khái quát vụ việc (2.1 – 2.5)** | Đầy đủ nguồn gốc, phương thức, timeline | Đầy đủ 5 tiểu mục, sơ đồ luồng và bảng dữ kiện | **PASS** |
| **Chương 3: Phân tích 4 yếu tố (3.1 – 3.5)** | Đầy đủ Khách thể, Khách quan, Chủ thể, Chủ quan, Bảng tổng hợp | Đầy đủ 5 tiểu mục lớn, các phân mục A, B, C, D, sơ đồ quan hệ và bảng ma trận | **PASS** |
| **Chương 4: Nhận xét, bài học, kiến nghị (4.1 – 4.5)** | Đầy đủ 5 tiểu mục định hướng sinh viên UIT | Đầy đủ 5 tiểu mục | **PASS** |
| **Kết luận** | Khái quát 4 yếu tố và ý nghĩa học thuật | Toàn văn đầy đủ | **PASS** |
| **Tài liệu tham khảo (A, B, C)** | 13 nguồn tài liệu chuẩn mực có mã định danh | 13 nguồn tài liệu theo danh sách đánh số | **PASS** |

---

## II. KIỂM ĐỊNH QUY CHUẨN IN ẤN (PRINT-FIRST A4 DESIGN)
- **Kiểu chữ & Cỡ chữ:** Font *Times New Roman / Georgia* serif, body text 13pt (in ấn 12pt), line-height 1.5, lùi đầu dòng 1.25cm chuẩn quy định tiểu luận.
- **Tiêu đề & Màu sắc:** Tông màu đen / xanh đen học thuật, không sử dụng màu neon, gradient hay giao diện card/dashboard kiểu web-app.
- **Sơ đồ & Bảng biểu:** Tất cả các sơ đồ ASCII được đặt trong thẻ `<pre>` với font Consolas/Monospace, chống tràn lề; bảng biểu có đường kẻ đen rõ ràng, hỗ trợ ngắt trang thông minh (`page-break-inside: avoid`).
- **Khổ trang:** Thiết lập CSS `@page { size: A4; margin: 25mm 20mm 20mm 20mm; }`.

---

## III. KẾT LUẬN KIỂM ĐỊNH PARITY

> **MD ↔ HTML content parity: PASS**
> 
> Bản HTML đạt độ tương thích và đồng bộ ngữ nghĩa 100% so với bản Markdown chuẩn, sẵn sàng để xem trên trình duyệt hoặc xuất trực tiếp sang file PDF/in ấn theo tiêu chuẩn học thuật của Trường Đại học Công nghệ Thông tin – ĐHQG-HCM.
