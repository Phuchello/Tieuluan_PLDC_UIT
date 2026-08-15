# KIỂM ĐỊNH TRỰC QUAN VÀ BỐ CỤC PDF V3 (PDF VISUAL QA V3)

**Trạng thái kiểm định:** **PASS TOÀN DIỆN TRÊN 26 TRANG (100% VISUAL & LAYOUT PASS)**

---

## I. TỔNG QUAN TẬP TIN XUẤT BẢN
- **Đường dẫn tập tin:** `report/BaoCao_TieuLuan_PLDC_UIT_FINAL.pdf`
- **Phương thức khởi tạo:** Xuất trực tiếp từ `report/BaoCao_TieuLuan_PLDC_UIT_FINAL.docx` thông qua Microsoft Word COM Automation (`ExportAsFixedFormat`).
- **Tổng số trang:** **26 trang A4**.
- **Kích thước trang:** $595.3 \times 841.9$ pt ($21.0 \times 29.7$ cm).

---

## II. KẾT QUẢ KIỂM ĐỊNH TỪNG TRANG (PAGE-BY-PAGE AUDIT)

| Trang | Nội dung chính | Đánh giá bố cục & Trực quan |
| :---: | :--- | :--- |
| **1** | **Trang bìa chính thức** | Căn giữa trang trọng; tên ĐHQG-HCM, UIT, Bộ môn Lý luận Chính trị; tên đề tài nổi bật; khung thông tin học phần; không có số trang ở chân trang. |
| **2** | **Bảng phân công nhiệm vụ** | Tiêu đề căn giữa; Bảng danh sách 5 thành viên cân đối; không có tỷ lệ 100% ảo; ngắt trang sạch sẽ trước Mục lục. |
| **3–4** | **Mục lục tự động (TOC)** | Tiêu đề "MỤC LỤC" căn giữa; các mục phân cấp rõ ràng kèm dot leaders và số trang tương ứng; không có anchor ID hay cú pháp markdown. |
| **5–7** | **MỞ ĐẦU** | Bắt đầu đầu trang 5; gồm 6 tiểu mục (Lý do chọn đề tài, Mục tiêu, Đối tượng, Phạm vi, Giới hạn dữ liệu, Phương pháp); căn đều hai bên; thụt lề 1.25cm. |
| **8–12** | **CHƯƠNG 1: Cơ sở lý luận** | Bắt đầu đầu trang 8; trình bày 7 mục lý luận nền tảng; Bảng 1 hiển thị đẹp mắt ở trang 9; mục 1.5 làm rõ bản chất mặt khách quan; kết thúc gọn gàng ở trang 12. |
| **13–15** | **CHƯƠNG 2: Khái quát vụ việc** | Bắt đầu đầu trang 13; Bảng 2 (chuỗi hoạt động) ở trang 14; Bảng 3 (tổng hợp dữ kiện) và Bảng 4 (mốc thời gian) ở trang 15; không bị tràn lề. |
| **16–22** | **CHƯƠNG 3: Phân tích 4 yếu tố cấu thành** | Trọng tâm học thuật (7 trang); Bảng 5 (phân biệt khách thể) ở trang 17; Bảng 6 (mặt chủ quan) ở trang 21; Bảng 7 (tổng hợp 4 yếu tố) ở trang 22; lập luận logic chặt chẽ. |
| **23–24** | **CHƯƠNG 4: Nhận xét và bài học** | Bắt đầu đầu trang 23; gồm 3 mục thực tiễn (ý nghĩa phòng ngừa, bài học kinh doanh/NTD, bài học đạo đức số cho sinh viên UIT); độ dài ~1.5 trang chuẩn mực. |
| **25** | **KẾT LUẬN** | Bắt đầu đầu trang 25; tổng kết súc tích 4 yếu tố và lưu ý tố tụng; dung lượng 1 trang hoàn chỉnh. |
| **26** | **TÀI LIỆU THAM KHẢO** | Bắt đầu đầu trang 26; danh mục 6 tài liệu đánh số chuẩn xác từ [1] đến [6]; phân nhóm Luật, Giáo trình và Nguồn báo chí chính thống; định dạng ngắt dòng URL hoàn hảo. |

---

## III. DANH MỤC CÁC LỖI TỪ CHỐI (REJECTION DEFECTS SCAN)
- Cú pháp Markdown rò rỉ (`](#`, `](http`, `#33-`): **0 lỗi (PASS)**.
- Tiêu đề mồ côi (Orphan headings): **0 lỗi (PASS)**.
- Trang trắng vô nghĩa (Blank pages): **0 lỗi (PASS)**.
- Bảng tràn lề / vỡ khung (Table overflow): **0 lỗi (PASS)**.
- Sai lệch số trang mục lục (Mismatched TOC page numbers): **0 lỗi (PASS)**.
- Lỗi font / vỡ ký tự tiếng Việt (Broken Vietnamese unicode): **0 lỗi (PASS)**.
