# vietnamese-it

Skill viết tiếng Việt trang trọng và dịch Anh - Việt cho văn bản công nghệ thông tin và kinh doanh số: trang nội bộ, slide, đặc tả, báo cáo, quy trình, giao diện.

Skill này chuyển các quy tắc của ASD-STE100 (tiêu chuẩn tiếng Anh kỹ thuật giản lược) sang tiếng Việt, gọi là STE-VI. Skill có thêm 5 nhóm quy tắc riêng cho tiếng Việt, gói thuật ngữ, bước rà soát bằng vietnamizer và một bộ kiểm tra tự động.

## Nội dung

| Tệp | Nội dung |
|---|---|
| [SKILL.md](SKILL.md) | Quy trình viết và dịch (tiếng Anh, cho tác tử AI đọc) |
| [ste-vi.md](ste-vi.md) | 60 quy tắc ASD-STE100 chuyển sang tiếng Việt và 5 nhóm quy tắc VI-1 đến VI-5 |
| [terms/](terms/README.md) | Gói thuật ngữ: từ công việc chung, công nghệ thông tin, ứng dụng di động và quảng cáo, mẫu cho tổ chức |
| [tools/ste_vi_check.py](tools/ste_vi_check.py) | Bộ kiểm tra: đọc tệp .md, .txt, .html; in OK hoặc FAIL |
| [examples.md](examples.md) | 22 ví dụ trước và sau khi sửa |
| [EVALUATION.md](EVALUATION.md) | Cách kiểm tra và kết quả |
| [vendor/vietnamizer/](vendor/vietnamizer/SKILL.md) | Skill biên tập tiếng Việt của fioenix (giấy phép MIT) |

## Năm nhóm quy tắc riêng cho tiếng Việt

| Nhóm | Vấn đề | Ví dụ sau khi sửa |
|---|---|---|
| VI-1 | Tiếng Anh nêu rõ phạm vi, số và sở hữu. Tiếng Việt để ngữ cảnh mang các ý này | Các nhóm sử dụng chung hệ thống. |
| VI-2 | Người đọc không hiểu câu: thiếu chủ thể, thiếu giải nghĩa | Lợi nhuận xấp xỉ bằng LTV (tổng doanh thu một người dùng mang lại) trừ CPI (chi phí cho một lượt cài). |
| VI-3 | Không có từ tương đương, câu giữ khung tiếng Anh | Số lượt tải cao nhất đạt khoảng 20 triệu trong một tháng. |
| VI-4 | Câu chỉ dẫn và câu cấm dịch theo hình thức tiếng Anh | Mỗi dự án cần có báo cáo tuần. |
| VI-5 | Ngữ pháp khác nhau: bị động, thì, phủ định, từ nối | Không tải được tệp. |

## Cài đặt

Claude Code, cho mọi dự án:

```
git clone https://github.com/lagz0ne/vietnamese-it ~/.claude/skills/vietnamese-it
```

Claude Code, cho một dự án: sao chép thư mục vào `.claude/skills/vietnamese-it` của dự án.

Tác tử AI khác: cho tác tử đọc `SKILL.md` trước khi viết tiếng Việt.

## Sử dụng

1. Yêu cầu tác tử viết hoặc dịch sang tiếng Việt. Skill tự áp dụng văn phong, thuật ngữ và các bước dịch.
2. Thêm tên riêng và thuật ngữ nội bộ: sao chép `terms/org-template.md` thành `terms/org.md`, rồi điền tên, công cụ và thuật ngữ.
3. Kiểm tra một tệp:

```
python3 -I tools/ste_vi_check.py ban-dich.md --org "Công ty ABC"
```

Với văn bản cho người đọc kỹ thuật (README, hướng dẫn cài đặt), thêm `--tech` để cho phép mã và đường dẫn trong câu.

Quy tắc Bắt buộc: 0 lỗi. Quy tắc Mặc định: ít nhất 80% số câu đạt.

## Kết quả kiểm tra

Mỗi nhóm quy tắc có một bài kiểm tra độc lập. Chi tiết trong [EVALUATION.md](EVALUATION.md).

| Bài kiểm tra | Bản cũ | Bản có quy tắc mới |
|---|---|---|
| VI-3, người chấm chọn bản tự nhiên hơn (9 đoạn) | 3 | 5 |
| VI-4, người chấm chọn bản tự nhiên hơn (22 câu) | 6 | 12 |
| VI-5, người chấm chọn bản tự nhiên hơn (22 câu) | 5 | 10 |
| Người đọc là quản lý hiểu rõ câu | 16 trên 26 | 81 trên 84 (96%) |
| Người đọc là nhân viên mới hiểu rõ câu | 14 trên 26 | 78 trên 84 (93%) |

## Nguồn

ASD-STE100 Issue 9 (2025), RFC 2119, Microsoft Vietnamese Style Guide, Mona Baker (*In Other Words*), Vinay và Darbelnet, thuyết dịch diễn ý (Seleskovitch và Lederer), Cao Xuân Hạo (*Tiếng Việt: sơ thảo ngữ pháp chức năng*). Danh sách đầy đủ trong [sources.md](sources.md). Skill chỉ diễn giải tên quy tắc của ASD-STE100, không sao chép tiêu chuẩn.

## English

A skill for formal Vietnamese writing and English to Vietnamese translation in IT and digital business. It adapts ASD-STE100 to Vietnamese (STE-VI), adds five Vietnamese rule groups found by native readers, ships term packs, a vietnamizer edit pass and a checker script. Install: clone into `~/.claude/skills/vietnamese-it`. Test method and numbers: [EVALUATION.md](EVALUATION.md).

## Giấy phép

MIT. Thư mục `vendor/vietnamizer` giữ giấy phép MIT của fioenix/vietnamizer.
