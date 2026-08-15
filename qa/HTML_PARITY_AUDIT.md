# HTML PARITY AUDIT (PHASE 2.5A)

Tài liệu này đánh giá sự đồng bộ giữa bản thảo Markdown (`report/REPORT_FULL.md`) và bản trình bày HTML (`report/REPORT_FULL.html`).

## KẾT QUẢ ĐỐI CHIẾU

| Hạng mục | Trạng thái đồng bộ | Nhận xét chi tiết & Rủi ro |
| :--- | :--- | :--- |
| **Bố cục tổng thể (Cover, TOC, Chapters)** | ĐỒNG BỘ | Bố cục cơ bản được giữ nguyên. Mã HTML đã bổ sung trang bìa (cover-page) chuyên nghiệp theo đúng chuẩn học thuật đại học. |
| **Nội dung Văn bản (Text)** | ĐỒNG BỘ | Toàn bộ các đoạn văn bản (từ Chương 1 đến Chương 4 và Kết luận) đều được ánh xạ đầy đủ sang thẻ `<p>` trong HTML. |
| **Phân cấp tiêu đề (Heading H1-H4)** | ĐỒNG BỘ | Hệ thống tiêu đề đã được chuyển sang các thẻ `<h1>`, `<h2>`, `<h3>`, `<h4>` kèm CSS phân tách màu sắc. |
| **Đánh dấu in đậm, in nghiêng** | ĐỒNG BỘ | Các thẻ `**` và `*` trong Markdown đã được dịch thành `<strong>` và `<em>` trong HTML đầy đủ. |
| **Bảng biểu (Tables)** | ĐỒNG BỘ VỀ NỘI DUNG | Dữ liệu bảng (Phân công nhiệm vụ, Bảng dữ kiện, Ma trận 4 yếu tố) được giữ nguyên. HTML có thêm style border, background-color cho `<th>`. |
| **Sơ đồ / Biểu đồ (Diagrams)** | **BẤT ĐỒNG BỘ NẶNG** | Trong bản `.md`, các sơ đồ được vẽ bằng ASCII Art (text block/code block). Trong bản HTML hiện tại chưa có CSS/khung hiển thị phù hợp cho sơ đồ ASCII, hoặc thiếu block `<pre>` chuyên dụng hiển thị biểu đồ, dẫn đến nguy cơ vỡ layout hoặc mất sơ đồ. |
| **Trích dẫn / Chú thích (Citations)** | ĐỒNG BỘ | Danh mục tài liệu tham khảo nằm ở thẻ `<ol>` tương đương. |
| **Print CSS (Dành cho in ấn offline)** | TẠM ỔN | Có media query `@media print` nhưng cần rà soát lại việc vỡ trang (page-break) ở các bảng lớn. |

## ĐỀ XUẤT SỬA LỖI TRONG BẢN HTML KẾ TIẾP (P4)
1. **Sơ đồ:** Các khối ASCII Art cần được gói cẩn thận vào `<pre style="font-family: monospace; white-space: pre;">` hoặc chuyển đổi sang thẻ SVG/ảnh minh họa để đảm bảo không bị vỡ giao diện trên di động hoặc khi in ấn.
2. **Neo liên kết (Anchor Links):** Bổ sung thuộc tính `id` cho các tiêu đề con (H2, H3) trong HTML để Table of Contents có thể jump đến đúng vị trí thay vì chỉ jump đến đầu chương H1.
3. **Màu sắc học thuật:** Giảm độ tương phản của một số thẻ tiêu đề (ví dụ chữ màu xanh quá sáng) để phù hợp hơn với phong cách tiểu luận chính quy.
