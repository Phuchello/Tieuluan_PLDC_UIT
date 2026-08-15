# KẾ HOẠCH CHỈNH SỬA BÁO CÁO (PHASE 2.5A PATCH PLAN)

Tài liệu này hướng dẫn trực tiếp cho LLM (Gemini 3.7) ở Phase tiếp theo thực hiện chỉnh sửa chuyên sâu (surgical hardening) đối với bản thảo `REPORT_WORKING.md` dựa trên kết quả kiểm định khắt khe.

---

## P0 — MUST FIX BEFORE CODEX (Sửa lỗi Pháp lý & Dữ kiện nghiêm trọng)
**1. Cập nhật phiên bản Luật Quảng cáo (Issue A)**
- *Vị trí:* Xuyên suốt báo cáo và phần Tài liệu tham khảo.
- *Hành động:* Sửa "Luật Quảng cáo 2012 (sửa đổi 2018)" thành **"Luật Quảng cáo năm 2012 (được sửa đổi, bổ sung năm 2018 và năm 2025)"** vì luật mới có hiệu lực từ 01/01/2026.

**2. Đính chính ngưỡng 50 triệu đồng của Điều 198 (Issue B)**
- *Vị trí:* Phần nhận xét về doanh thu 2,67 tỷ đồng.
- *Hành động:* Sửa nhận định "50 triệu là ngưỡng khởi điểm định lượng trách nhiệm hình sự" thành "vượt xa ngưỡng quy định tại khoản 2 Điều 198 BLHS (thu lợi bất chính từ 50.000.000 đồng)". Phải nêu rõ 5 triệu mới là ngưỡng khởi điểm của khoản 1.

**3. Thay thế thuật ngữ "chiếm đoạt tài sản" (Issue I)**
- *Vị trí:* Rải rác ở Mặt chủ quan (Chương 3).
- *Hành động:* Xóa bỏ các từ "chiếm đoạt tài sản", "lừa đảo". Thay bằng thuật ngữ chính xác của Điều 198 là **"thu lợi bất chính"** thông qua hành vi lừa dối.

---

## P1 — MUST HARDEN (Kiểm soát Overclaim, Nguyên tắc vô tội, Cấu thành)
**1. Xóa bỏ các chi tiết vận hành không có thật (Issue E)**
- *Vị trí:* Chương 2 (Thủ đoạn hoạt động) và phân tích Mặt khách quan.
- *Hành động:* Xóa sạch các đoạn mô tả "telesale tự xưng bác sĩ đầu ngành", "bắt mạch từ xa", "hù dọa bệnh nhân", "kho vận COD khép kín". Đây là các chi tiết tự bịa ra (hallucination) dựa trên mô típ chung, không có trong báo cáo Công an về vụ này. Chỉ giữ lại "hành vi cắt ghép video nghệ sĩ/chuyên gia để quảng cáo sai sự thật".

**2. Đính chính Đơn hàng $\neq$ Khách hàng (Issue C)**
- *Vị trí:* Các đoạn ghi "5.429 khách hàng" hoặc "hơn 5.429 người tiêu dùng".
- *Hành động:* Sửa toàn bộ thành **"5.429 đơn hàng"**. Không tự động quy đổi 1 đơn hàng = 1 con người.

**3. Làm mềm khẳng định về Mối quan hệ nhân quả (Issue F)**
- *Vị trí:* Phân tích Mặt khách quan.
- *Hành động:* Thay cụm "nhân quả trực tiếp và tất yếu", "chính hành vi này khiến toàn bộ khách hàng..." bằng các cụm từ an toàn học thuật hơn: "có mối liên hệ nhân quả trực tiếp", "là yếu tố dẫn dắt hàng ngàn đơn hàng được chốt".

**4. Phân hóa trạng thái tâm lý Lỗi / Động cơ (Issue G)**
- *Vị trí:* Phân tích Chủ thể và Mặt chủ quan.
- *Hành động:* Không gộp chung 21 người. Xác định rõ: Nguyễn Tiến Đạt và nhóm marketing có lỗi cố ý trực tiếp. Nhóm đóng gói, vận đơn cần được cơ quan chức năng làm rõ thêm về mức độ nhận thức (có thể là giúp sức). 

**5. Đảm bảo nguyên tắc Suy đoán vô tội**
- *Vị trí:* Xuyên suốt báo cáo.
- *Hành động:* Đảm bảo chỉ dùng từ "bị can", "hành vi bị cáo buộc", "dưới góc độ lý thuyết", không dùng các từ như "hành vi tội phạm của chúng", "những kẻ lừa đảo".

---

## P2 — SOURCE IMPROVEMENT (Làm rõ tính suy luận vs Dữ kiện thực tế)
**1. Khẳng định về Năng lực trách nhiệm pháp lý (Issue H)**
- *Vị trí:* Phân tích Chủ thể (Năng lực nhận thức).
- *Hành động:* Thay vì khẳng định 100% "không ai bị tâm thần", hãy dùng lối hành văn diễn dịch: "Theo dữ kiện công bố, Đạt sinh năm 1997, đủ tuổi thành niên. Đối với các bị can khác, quá trình làm việc, thiết lập hệ thống quảng cáo cho thấy họ có năng lực nhận thức và điều khiển hành vi bình thường. Trừ phi có kết luận giám định pháp y tâm thần, về mặt nguyên tắc, các chủ thể này đáp ứng điều kiện về năng lực trách nhiệm pháp lý."

**2. Rút gọn Luật Dược**
- *Vị trí:* Chương 3, phần Khách thể.
- *Hành động:* Lược bớt hoặc bỏ hẳn trích dẫn Điều 7 Luật Dược, vì "Xương khớp bà Sáu" chưa được công bố là thuốc chữa bệnh. Chỉ tập trung vào Luật Quảng cáo và Luật Bảo vệ quyền lợi NTD.

---

## P3 — STYLE (Văn phong Học thuật con người)
- Lược bỏ hoặc viết lại các cụm từ sáo rỗng, mang hơi hướng AI (filler words): 
  - "bộ máy doanh nghiệp ngầm" $\rightarrow$ "tổ chức phân công công việc chặt chẽ"
  - "rung lên hồi chuông cảnh tỉnh sâu sắc" $\rightarrow$ "đặt ra vấn đề cấp thiết về quản lý"
  - "tội phạm công nghệ cao" $\rightarrow$ không dùng vì tội lừa dối khách hàng không thuộc nhóm tội phạm công nghệ cao theo BLHS, chỉ là tội phạm sử dụng mạng xã hội làm công cụ.

---

## P4 — HTML (Đồng bộ và In ấn)
- Trong lần xuất HTML tiếp theo, cần gói các sơ đồ ASCII vào thẻ `<pre>` với font monospace.
- Điều chỉnh ID anchor tag để mục lục hoạt động chính xác cho cả thẻ H2, H3.
