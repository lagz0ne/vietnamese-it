# vietnamese-it

Skill viết tiếng Việt và dịch Anh - Việt cho văn bản công nghệ: tài liệu kỹ thuật, tài liệu hệ thống và nội dung sản phẩm (chuỗi giao diện, thông báo lỗi, trang giới thiệu tính năng).

Tài liệu theo STE-VI: các quy tắc của ASD-STE100 (tiêu chuẩn tiếng Anh kỹ thuật giản lược) chuyển sang tiếng Việt. Nội dung giao diện theo giọng văn tiếng Việt của Microsoft: rõ, thân thiện, ngắn. Skill có sẵn bộ thuật ngữ công nghệ lấy từ Microsoft Terminology Collection, có bước xây dựng bảng thuật ngữ cho từng lĩnh vực, bước rà soát bằng vietnamizer và một bộ kiểm tra tự động.

## Loại văn bản

| Loại | Ví dụ | Quy tắc | Bộ kiểm tra |
|---|---|---|---|
| Tài liệu kỹ thuật | hướng dẫn, README, ghi chú phát hành | STE-VI, VI-1 đến VI-5 | `--tech` |
| Tài liệu hệ thống | đặc tả, kiến trúc, runbook (hướng dẫn xử lý sự cố) | STE-VI, VI-1 đến VI-5 | `--tech` |
| Văn bản cho quản lý | trang, slide, báo cáo | STE-VI, giải nghĩa mọi chữ viết tắt | mặc định |
| Nội dung sản phẩm | nút, thông báo lỗi, màn hình hướng dẫn, trang tính năng | VI-6 | `--copy` |

## Nội dung

| Tệp | Nội dung |
|---|---|
| [SKILL.md](SKILL.md) | Quy trình viết và dịch (tiếng Anh, cho tác tử AI đọc) |
| [ste-vi.md](ste-vi.md) | 60 quy tắc ASD-STE100 chuyển sang tiếng Việt và 6 nhóm quy tắc VI-1 đến VI-6 |
| [terms/](terms/README.md) | Gói thuật ngữ: từ công việc chung, công nghệ, hệ thống; gói quảng cáo ứng dụng (tùy chọn); mẫu cho tổ chức |
| [tools/](tools/) | Bộ kiểm tra; công cụ tìm thuật ngữ trong văn bản nguồn; công cụ tra tệp TBX |
| [examples.md](examples.md) | 29 ví dụ trước và sau khi sửa |
| [EVALUATION.md](EVALUATION.md) | Cách kiểm tra và kết quả |
| [vendor/vietnamizer/](vendor/vietnamizer/SKILL.md) | Skill biên tập tiếng Việt của fioenix (giấy phép MIT) |

## Sáu nhóm quy tắc riêng cho tiếng Việt

| Nhóm | Vấn đề | Ví dụ sau khi sửa |
|---|---|---|
| VI-1 | Tiếng Anh nêu rõ phạm vi, số và sở hữu. Tiếng Việt để ngữ cảnh mang các ý này | Các nhóm sử dụng chung hệ thống. |
| VI-2 | Người đọc không hiểu câu: thiếu chủ thể, thiếu giải nghĩa | Bật đăng nhập một lần (SSO) cho mọi không gian làm việc. |
| VI-3 | Không có từ tương đương, câu giữ khung tiếng Anh | Số lượt tải cao nhất đạt khoảng 20 triệu trong một tháng. |
| VI-4 | Câu chỉ dẫn và câu cấm dịch theo hình thức tiếng Anh | Mỗi dự án cần có báo cáo tuần. |
| VI-5 | Ngữ pháp khác nhau: bị động, thì, phủ định, từ nối | Phiên bản v6 đã gỡ bỏ tính năng thống kê sử dụng có sẵn. |
| VI-6 | Nội dung giao diện: đại từ thừa, thông báo lỗi, lời đề nghị | Không lưu được hình ảnh. |

## Cài đặt

Claude Code, cho mọi dự án:

```
git clone https://github.com/lagz0ne/vietnamese-it ~/.claude/skills/vietnamese-it
```

Claude Code, cho một dự án: sao chép thư mục vào `.claude/skills/vietnamese-it` của dự án.

Tác tử AI khác: cho tác tử đọc `SKILL.md` trước khi viết tiếng Việt.

## Sử dụng

1. Yêu cầu tác tử viết hoặc dịch sang tiếng Việt. Skill tự chọn loại văn bản, văn phong, thuật ngữ và các bước dịch.
2. Với lĩnh vực mới (thanh toán, y tế, game), xây dựng bảng thuật ngữ trước theo SKILL.md mục 2b. Công cụ `tools/term_candidates.py` liệt kê thuật ngữ chưa có trong gói. Công cụ `tools/tbx_lookup.py` tra tệp VIETNAMESE.tbx của Microsoft Terminology Collection (tải từ Microsoft).
3. Thêm tên riêng và thuật ngữ nội bộ: sao chép `terms/org-template.md` thành `terms/org.md`, rồi điền tên, công cụ và thuật ngữ.
4. Kiểm tra một tệp:

```
python3 -I tools/ste_vi_check.py ban-dich.md --tech
python3 -I tools/ste_vi_check.py chuoi-giao-dien.md --copy
```

Quy tắc Bắt buộc: 0 lỗi. Quy tắc Mặc định: ít nhất 80% số câu đạt. Thêm `--org "Công ty ABC"` để kiểm tra cách nêu tên tổ chức.

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

ASD-STE100 Issue 9 (2025), RFC 2119, Microsoft Vietnamese Style Guide, Microsoft Terminology Collection, Mona Baker (*In Other Words*), Vinay và Darbelnet, thuyết dịch diễn ý (Seleskovitch và Lederer), Cao Xuân Hạo (*Tiếng Việt: sơ thảo ngữ pháp chức năng*). Danh sách đầy đủ trong [sources.md](sources.md). Skill chỉ diễn giải tên quy tắc của ASD-STE100, không sao chép tiêu chuẩn.

## English

A skill for Vietnamese tech writing and English to Vietnamese translation: tech docs, system docs and product copy (UI strings, error messages, feature pages). Documents follow STE-VI (ASD-STE100 adapted to Vietnamese); copy follows the Microsoft vi-VN voice. It adds six Vietnamese rule groups found by native readers, ships a default tech term pack from the Microsoft Terminology Collection, a glossary-building step with two tools, a vietnamizer edit pass and a checker script. Install: clone into `~/.claude/skills/vietnamese-it`. Test method and numbers: [EVALUATION.md](EVALUATION.md).

## Giấy phép

MIT. Thư mục `vendor/vietnamizer` giữ giấy phép MIT của fioenix/vietnamizer.
