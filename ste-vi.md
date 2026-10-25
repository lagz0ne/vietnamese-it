---
title: Tiếng Việt kỹ thuật giản lược (STE-VI)
license: MIT
nguồn: ASD-STE100 Issue 9 (01/2025, 53 quy tắc, 9 phần); vietnamizer 0.10.6; phong cách ngôn ngữ hành chính - công vụ; Microsoft vi-VN style guide
---

# Tiếng Việt kỹ thuật giản lược (STE-VI)

## Tóm tắt

- STE-VI chuyển các quy tắc viết của ASD-STE100 sang tiếng Việt: 60 dòng, giữ 35, chuyển 21, bỏ 4 (bảng ở mục 2). 26 quy tắc Bắt buộc, 30 quy tắc Mặc định, cộng 5 quy tắc riêng cho tiếng Việt (VI-1, mục 2b) 6 quy tắc rõ nghĩa (VI-2, mục 2c), kiểm bằng bài đọc độc lập, 8 quy tắc dựng lại câu khi không có từ tương đương (VI-3, mục 2d), 10 quy tắc cho câu chỉ dẫn và câu mệnh lệnh (VI-4, mục 2e), và 11 quy tắc ngữ pháp khác giữa hai ngôn ngữ (VI-5, mục 2f).
- Văn phong: văn viết trang trọng, khách quan, chính xác. Không sử dụng khẩu ngữ, không sử dụng hình ảnh ẩn dụ, không bộc lộ cảm xúc.
- Hai mức áp dụng. **Bắt buộc**: áp dụng cho mọi câu. **Mặc định**: áp dụng cho ít nhất 80% số câu; chỉ bỏ qua khi bước rà soát vietnamizer cho thấy câu sẽ sai nghĩa hoặc thiếu tự nhiên.
- Kiểm tra bằng `tools/ste_vi_check.py`. Giới hạn độ dài (mục 5) là giá trị khởi đầu, sẽ hiệu chỉnh theo kết quả kiểm tra.

## 1. Phạm vi

Áp dụng cho trang, slide, ghi chú, báo cáo, quy trình nội bộ và tài liệu gửi khách hàng (ghi chú phát hành, hướng dẫn). Chuỗi giao diện cho người dùng cuối theo giọng văn sẵn có của sản phẩm. Không áp dụng cho mã nguồn, tên riêng, trích dẫn nguyên văn và số liệu.

Hai loại văn bản, như ASD-STE100:
- **Quy trình**: yêu cầu người đọc làm một việc (các bước, hướng dẫn).
- **Mô tả**: giải thích hệ thống, nguyên nhân, kết quả, kế hoạch. Trang và slide chiến lược là văn bản mô tả.

Không trộn hai loại trong cùng một đoạn.

## 2. Bảng ánh xạ ASD-STE100 sang STE-VI

Quyết định: **Giữ** = áp dụng như bản gốc. **Chuyển** = đổi cho phù hợp ngữ pháp tiếng Việt. **Bỏ** = không áp dụng được cho tiếng Việt.

| STE | Nội dung gốc | Quyết định | Quy tắc STE-VI | Mức | vietnamizer |
|---|---|---|---|---|---|
| 1.1 | Chỉ sử dụng từ được duyệt | Chuyển | Chỉ sử dụng từ phổ thông của văn viết và thuật ngữ trong gói thuật ngữ (mục 3) | Bắt buộc | V19 |
| 1.2 | Sử dụng từ đúng từ loại | Chuyển | Thuật ngữ tiếng Anh chỉ sử dụng làm danh từ | Bắt buộc | V19 |
| 1.3 | Mỗi từ một nghĩa | Giữ | Mỗi từ, mỗi thuật ngữ chỉ một nghĩa trong văn bản | Bắt buộc | |
| 1.4 | Dạng động từ, tính từ được duyệt | Bỏ | Tiếng Việt không biến hình | | |
| 1.5 | Danh từ kỹ thuật theo nhóm | Giữ | Thuật ngữ theo nhóm trong gói thuật ngữ | Bắt buộc | |
| 1.6 | Từ ngoài danh mục chỉ sử dụng làm danh từ kỹ thuật | Giữ | Từ tiếng Anh ngoài gói thuật ngữ chỉ được sử dụng khi là tên riêng hoặc danh từ kỹ thuật, và phải báo lại để thêm vào gói thuật ngữ | Bắt buộc | |
| 1.7 | Không sử dụng danh từ kỹ thuật làm động từ | Giữ | Không viết "scale app", "clone game", "test creative", "deploy" | Bắt buộc | V19 |
| 1.8 | Sử dụng thuật ngữ được công ty duyệt | Giữ | Gói thuật ngữ (thư mục terms/) là danh mục chính. Thuật ngữ ngoài gói: theo SKILL.md mục 2, rồi ghi vào báo cáo để bổ sung vào gói | Bắt buộc | |
| 1.9 | Thuật ngữ ngắn, dễ hiểu | Giữ | Chọn tên ngắn nhất mà người đọc hiểu đúng | Mặc định | |
| 1.10 | Không sử dụng tiếng lóng, từ địa phương | Giữ | Không sử dụng khẩu ngữ, từ địa phương, tiếng lóng nghề (danh sách ở mục 4) | Bắt buộc | |
| 1.11 | Một sự vật, một tên | Giữ | Không đổi tên gọi để tránh lặp | Bắt buộc | K rule 3 |
| 1.12 | Động từ kỹ thuật theo nhóm | Chuyển | Sử dụng động từ chính xác thay cho động từ chung "làm", "xử lý", "chạy" khi có từ cụ thể hơn | Mặc định | V15 |
| 1.13 | Không sử dụng động từ kỹ thuật làm danh từ | Chuyển | Không danh hóa: tránh "việc", "sự" + động từ đi với "thực hiện", "tiến hành" | Mặc định | V15 |
| 1.14 | Chính tả Anh - Mỹ | Chuyển | Một kiểu đặt dấu thanh trong một văn bản, mặc định kiểu mới (hóa, tùy, thủy) | Bắt buộc | |
| 2.1 | Cụm danh từ tối đa 3 danh từ | Chuyển | Cụm danh từ tối đa 3 thành tố danh từ; không nối chuỗi "của ... của" | Mặc định | V7 |
| 2.2 | Thuật ngữ dài: viết đủ rồi đặt tên ngắn | Giữ | Viết đầy đủ ở lần đầu, sau đó sử dụng tên ngắn | Mặc định | |
| 3.1 | Dạng động từ theo từ điển | Bỏ | Tiếng Việt không chia động từ | | |
| 3.2 | Chỉ sử dụng thì đơn | Chuyển | Chỉ sử dụng "đã", "đang", "sẽ" khi thời gian quan trọng; không chồng "đã đang", "sẽ được" | Mặc định | V4 |
| 3.3 | Quá khứ phân từ làm tính từ | Bỏ | Không có dạng tương ứng | | |
| 3.4 | Không chồng trợ động từ | Chuyển | Không chồng từ tình thái: "có thể sẽ cần phải" | Bắt buộc | V24 |
| 3.5 | Dạng -ing | Bỏ | Không có dạng tương ứng | | |
| 3.6 | Sử dụng thể chủ động | Giữ | Chủ động; bị động chỉ khi không biết tác nhân; không sử dụng "được/bị ... bởi" | Mặc định | V16 |
| 3.7 | Hành động sử dụng động từ | Giữ | Hành động viết bằng động từ, không bằng danh từ | Mặc định | V15 |
| 4.1 | Câu ngắn, rõ | Giữ | Câu ngắn, một ý chính (giới hạn ở mục 5) | Mặc định | |
| 4.2 | Không lược từ | Chuyển | Không lược chủ ngữ khi chủ thể chưa rõ; không viết tắt kiểu "ko", "đc", "vs"; giữ bổ ngữ kết quả | Bắt buộc | V1, V18, V20 |
| 4.3 | Sử dụng danh sách dọc | Giữ | Thông tin phức tạp viết thành danh sách dọc | Mặc định | |
| 4.4 | Sử dụng từ nối | Giữ | Nối câu cùng chủ đề bằng từ nối; sử dụng đủ cặp liên từ | Mặc định | V2, V12 |
| 4.5 | Mạo từ, từ chỉ định | Chuyển | Sử dụng "này", "đó" với danh từ để quy chiếu rõ; không sử dụng "nó", "điều này" khi có thể gọi tên | Mặc định | V18 |
| 5.1 | Câu quy trình ngắn | Chuyển | Câu quy trình tối đa 30 âm tiết | Mặc định | |
| 5.2 | Một chỉ dẫn một câu | Giữ | Mỗi câu một chỉ dẫn, trừ hai việc làm cùng lúc | Bắt buộc | |
| 5.3 | Câu mệnh lệnh | Chuyển | Câu quy trình mở đầu bằng động từ: "Mở...", "Chọn..."; không mở đầu bằng "Vui lòng", "Bạn hãy" | Bắt buộc | |
| 5.4 | Điều kiện trước, dấu phẩy | Giữ | "Nếu/Khi ..., [động từ] ..." | Mặc định | |
| 5.5 | Ghi chú chỉ để thông tin | Giữ | "Lưu ý:" chỉ đưa thông tin, không đưa chỉ dẫn | Bắt buộc | |
| 6.1 | Câu mô tả ngắn | Chuyển | Câu mô tả tối đa 38 âm tiết | Mặc định | |
| 6.2 | Câu chủ đề ở đầu đoạn | Giữ | Câu đầu đoạn nêu ý chính của đoạn | Mặc định | |
| 6.3 | Một đoạn một chủ đề | Giữ | Một đoạn chỉ một chủ đề | Bắt buộc | |
| 6.4 | Tối đa 6 câu một đoạn | Giữ | Tối đa 6 câu một đoạn | Mặc định | |
| 6.5 | Thay đổi độ dài, cấu trúc câu | Giữ | Không lặp một kiểu mở câu cho ba câu liền nhau | Mặc định | V13 |
| 7.1 | Từ chỉ mức rủi ro | Chuyển | "Cảnh báo:", "Thận trọng:", "Lưu ý:" (không viết hoa toàn bộ) | Bắt buộc | |
| 7.2 | Mở đầu bằng mệnh lệnh hoặc điều kiện | Giữ | Câu cảnh báo mở đầu bằng điều cần làm hoặc điều kiện | Bắt buộc | |
| 7.3 | Giải thích rủi ro | Giữ | Nêu rủi ro hoặc hậu quả | Bắt buộc | |
| 8.1 | Dấu câu chuẩn, không dấu chấm phẩy | Giữ | Không sử dụng dấu chấm phẩy, gạch ngang dài; không đặt dấu phẩy trước "và", "hoặc" | Mặc định | T2, T4 |
| 8.2 | Gạch nối cho từ liên quan | Chuyển | Gạch nối chỉ sử dụng cho khoảng (2025 - 2026) và tên ghép; không nối từ ghép tiếng Việt | Mặc định | |
| 8.3 | Được sử dụng ngoặc đơn | Giữ | Ngoặc đơn sử dụng cho giải nghĩa thuật ngữ | Mặc định | |
| 8.4 | Dấu hai chấm trong danh sách như dấu chấm | Giữ | Khi đếm độ dài, dấu hai chấm kết thúc câu, kể cả khi chữ sau dấu hai chấm viết thường; nhãn slide "Nhãn: nội dung" đếm riêng | Mặc định | |
| 8.5 | Ngoặc đơn tính là 1 từ | Giữ | Phần trong ngoặc tính là 1 âm tiết | Mặc định | |
| 8.6 | Một số thành phần tính là 1 từ | Giữ | Số, mã, tên riêng, thuật ngữ tiếng Anh tính là 1 âm tiết | Mặc định | |
| 8.7 | Từ có gạch nối tính là 1 từ | Chuyển | Thuật ngữ tiếng Anh nhiều từ tính là 1 âm tiết | Mặc định | |
| 9.1 | Đổi cấu trúc khi thay từ không đủ | Giữ | Viết lại từ nghĩa, không dịch từng từ | Bắt buộc | V7 đến V18 |
| 9.2 | Sử dụng đúng từ | Giữ | Sử dụng từ đúng nghĩa và đúng kết hợp | Bắt buộc | V1, V5 |
| 9.3 | Không sử dụng cụm động từ | Chuyển | Không sao chép cụm động từ và hình ảnh tiếng Anh: "cắm vào" (plug in), "xây trên" (build on), "đi qua mọi" (go through), "con đường" (path), "lát mỏng" (thin slice). Bộ kiểm tra có danh sách này | Bắt buộc | V19 |
| 9.4 | Văn phong nhất quán | Giữ | Một cách xưng hô, một kiểu dấu thanh, một tên cho mỗi thuật ngữ | Bắt buộc | |
| GR-1 | Liên từ "that" | Chuyển | Sử dụng "rằng", "là" khi ranh giới mệnh đề chưa rõ | Mặc định | V3 |
| GR-2 | Giới từ "with" | Chuyển | Không dịch máy móc "with" thành "với": "vòng lặp với các cổng" thành "vòng lặp có các điểm quyết định" | Mặc định | V9 |
| GR-3 | Cách sử dụng đại từ | Giữ | Chỉ sử dụng đại từ khi người đọc biết ngay nó thay cho danh từ nào | Bắt buộc | V18 |
| GR-4 | Đại từ "this" | Giữ | "Điều này", "việc này" chỉ sử dụng khi quy chiếu rõ; nên gọi tên sự vật | Mặc định | V18 |
| GR-5 | Từ dễ nhầm nghĩa | Giữ | Tránh từ dễ hiểu sai nghĩa. Không thay thuật ngữ Hán Việt đã có định nghĩa bằng từ đời thường | Mặc định | K rule 4 |
| GR-6 | Viết tắt tiếng Latin | Chuyển | Không sử dụng "e.g.", "i.e.", "vs"; viết "ví dụ", "tức là", "so với" | Bắt buộc | |
| GR-7 | Ngôn ngữ không phân biệt đối xử | Giữ | Gọi theo vai trò ("người phụ trách"), không giả định giới tính | Bắt buộc | |
| GR-8 | Sở hữu cách | Chuyển | Bỏ "của" khi quan hệ chỉ là thuộc tính; giữ khi chỉ chủ thể sở hữu | Mặc định | V7 |

Tổng: 60 dòng, gồm 52 quy tắc chính và 8 quy tắc chung (GR). Bản chính thức có 53 quy tắc; nguồn tóm tắt chỉ nêu đủ nội dung của 52 quy tắc. Số thứ tự phần 6 lấy theo nguồn tóm tắt, cần đối chiếu bản chính thức. Giữ 35, Chuyển 21, Bỏ 4.

## 2b. Quy tắc riêng cho tiếng Việt

Tiếng Anh nêu rõ phạm vi, số và sở hữu trong mỗi câu. Tiếng Việt để ngữ cảnh mang các thông tin này. Khi dịch sát, phần ngầm định trở thành dư thừa. Quy tắc này không trái với STE 4.2: STE 4.2 cấm bỏ thành phần ngữ pháp; VI-1 bỏ phần nghĩa bị lặp.

| Mã | Quy tắc | Sai | Đúng | Mức | vietnamizer |
|---|---|---|---|---|---|
| VI-1a | Không nêu lại phạm vi mà ngữ cảnh đã có. Văn bản nội bộ đã ngầm hiểu phạm vi là tổ chức viết văn bản | "các hệ thống sử dụng chung cho mọi nhóm tại công ty" | "hệ thống sử dụng chung" | Mặc định | V25 |
| VI-1b | Chỉ nêu tên tổ chức ở tiêu đề, trang bìa, câu mở đầu định nghĩa tổ chức, hoặc khi cần phân biệt với bên ngoài ("dự án của công ty" và "dự án trong hệ thống quản lý tài khoản") | "Tại Công ty ABC, nhóm sản phẩm quyết định..." (trong tài liệu nội bộ của Công ty ABC) | "Nhóm sản phẩm quyết định..." | Mặc định | |
| VI-1c | Không dịch mạo từ "a/an" thành "một" khi không cần nghĩa số lượng. Giữ "một" khi đối lập với "nhiều" hoặc "mọi", khi là đơn vị tính ("cho một người dùng"), khi nêu quan hệ một - một, hoặc khi ngữ pháp cần ("về một người") | "là một công việc thực tế" | "là công việc thực tế" | Mặc định | V8 |
| VI-1d | Không dịch sở hữu "its/their/our" khi chủ thể đã rõ: bỏ "của nó", "của họ", "của mình", "của công ty" | "trong các ứng dụng của công ty" | "trong ứng dụng" | Mặc định | V7 |
| VI-1e | Không nhắc lại "mọi", "mỗi", "tất cả" khi danh từ hoặc động từ đã mang nghĩa đó ("sử dụng chung", "toàn công ty"). Không chồng nghĩa "chỉ một": "chỉ ... một ... duy nhất", "một ... chung". Trên slide, sau nhãn "Nhãn:", không nhắc lại chủ ngữ mà nhãn đã nêu. Giữ "mọi" khi đó là ý chính và không từ nào khác mang nghĩa này | "mọi nhóm sử dụng chung" | "các nhóm sử dụng chung" hoặc "sử dụng chung" | Mặc định | V8 |

Phép thử: bỏ từ đó rồi đọc lại. Bỏ từ đó khi đủ ba điều kiện: nghĩa không đổi; người đọc vẫn biết phạm vi; mức độ khẳng định không đổi. Kiểm tra thêm: cụm còn lại không trở thành thành ngữ khác nghĩa ("theo nhu cầu riêng" khác "theo nhu cầu").

## 2c. Quy tắc rõ nghĩa cho người đọc (VI-2)

Nguồn: kiểm tra đọc độc lập ngày 25/10/2026. Hai người đọc chỉ có bản tiếng Việt, không có bản tiếng Anh. 11 trên 26 câu chỉ hiểu được một phần, 1 câu không hiểu được. VI-1 bỏ phần lặp; VI-2 giữ hoặc thêm phần người đọc cần. Khi hai quy tắc mâu thuẫn, VI-2 được ưu tiên.

| Mã | Quy tắc | Sai | Đúng | Mức |
|---|---|---|---|---|
| VI-2a | Ở lần sử dụng đầu, mỗi chữ viết tắt và tên công cụ có một cụm giải thích vai trò. Sử dụng cột giải nghĩa trong gói thuật ngữ. "CPI" luôn cần giải thích vì người đọc dễ hiểu là "chỉ số giá tiêu dùng". Khi khái niệm có tên tiếng Việt thông dụng, viết tiếng Việt trước, tiếng Anh trong ngoặc: "sở hữu trí tuệ (IP)", không viết "IP (sở hữu trí tuệ)" | "liên kết qua MMP" | "liên kết qua MMP (công cụ đo lường nguồn của lượt cài)" | Bắt buộc |
| VI-2b | Mỗi câu nêu rõ ai làm việc gì. Không bỏ chủ thể khi câu trước chưa nêu. Không đảo vai: người nhận quyền vào tài nguyên, không phải tài nguyên nhận quyền. Khi bản gốc không nêu chủ thể, không tự thêm chủ thể; sử dụng chủ thể là thao tác hoặc hệ thống ("một thao tác tại hệ thống quản lý tài khoản thu hồi quyền") | "Creative quyết định lựa chọn ứng dụng"; "Tài nguyên nhận quyền truy cập" | "Công ty chọn ứng dụng để phát hành dựa trên creative"; "Người dùng nhận quyền vào tài nguyên" | Bắt buộc |
| VI-2c | Không đưa mã, cấu hình hoặc chi tiết kỹ thuật vào văn bản mô tả cho người đọc không chuyên. Viết tác dụng của nó | "Ứng dụng chỉ ghi \"parent = project\"" | "Ứng dụng chỉ khai báo tài nguyên thuộc dự án nào; phần phân quyền còn lại do hệ thống xử lý" | Bắt buộc |
| VI-2d | Nêu mối nối giữa hai ý: vì sao, bằng cách nào, dẫn đến đâu. Khi đổi chủ đề, có một câu dẫn | "là vòng lặp" (không nói lặp gì); "liên kết qua MMP" (không nói nối gì) | "Sau mỗi điểm quyết định, ứng dụng quay lại bước thử nghiệm với mức chi mới" | Mặc định |
| VI-2f | Từ so sánh nhất ("cao nhất", "lớn nhất") phải nêu rõ đại lượng được so sánh. Đã nêu đại lượng ở đầu câu thì không nhắc lại ở cuối câu (ví dụ VD16) | "Vào tháng cao nhất, các ứng dụng này đạt khoảng 20 triệu lượt tải." | "Số lượt tải cao nhất đạt khoảng 20 triệu trong một tháng." | Bắt buộc |
| VI-2e | Nếu một nhóm hoặc vai trò xuất hiện hai lần trong một câu dưới hai tên, viết rõ là cùng một nhóm | "Bắt đầu từ nhóm phát triển: nhóm xây dựng cách làm chuẩn..." | "Nhóm phát triển đi trước: nhóm này xây dựng cách làm chuẩn và sử dụng trước" | Bắt buộc |

Kiểm tra đọc độc lập (bắt buộc cho văn bản gửi lãnh đạo): một tác tử độc lập, chỉ có bản tiếng Việt, đọc từng câu theo vai người quản lý không chuyên kỹ thuật và ghi "Có / Một phần / Không" cùng lời diễn giải. Mục tiêu: không câu nào "Không"; ít nhất 90% câu "Có"; mọi lời diễn giải khớp nghĩa bản gốc.

## 2d. Dựng lại câu khi không có từ tương đương (VI-3)

Nguồn: nhận xét của người đọc bản ngữ: khi một từ tiếng Anh không có từ tương đương trong tiếng Việt, cần dựng lại câu để ý trôi chảy, không giữ cấu trúc câu gốc. Các quy tắc dưới đây lấy từ phương pháp đã có, không tự đặt ra:

- Mona Baker, *In Other Words* (1992, tái bản 2018), chương 2: 8 cách xử lý khi không có từ tương đương ở cấp độ từ.
- Vinay và Darbelnet (1958): các thủ pháp dịch gián tiếp: chuyển loại từ (transposition), chuyển góc nhìn (modulation), tương đương (equivalence), thích ứng (adaptation).
- Thuyết dịch diễn ý (Seleskovitch và Lederer, ESIT Paris): hiểu, tách nghĩa khỏi vỏ từ (deverbalization), rồi diễn đạt lại bằng ngôn ngữ đích.
- Tiếng Việt ưu tiên cấu trúc đề - thuyết: nêu chủ đề trước, nói về chủ đề sau; điều kiện, thời gian, nguyên nhân đứng trước kết quả.

| Mã | Quy tắc | Sai | Đúng | Mức |
|---|---|---|---|---|
| VI-3a | Khi không có từ tương đương, chọn theo thứ tự: (1) dạng trong gói thuật ngữ; (2) từ khái quát hơn; (3) diễn giải bằng cụm từ hoặc bằng cả câu; (4) giữ từ gốc kèm giải thích; (5) bỏ, khi ngữ cảnh đã đủ nghĩa. Không tạo từ mới | "vòng dòng tiền" (money loop) | "Chi phí quảng cáo và doanh thu quảng cáo phụ thuộc vào nhau" | Bắt buộc |
| VI-3b | Khi cách (3) làm câu dài hoặc gượng, dựng lại cả câu: đổi danh từ thành động từ, đổi chủ ngữ, tách câu hoặc đổi thứ tự ý. Không giữ khung câu tiếng Anh | "Vòng đời ứng dụng là vòng lặp" (the app lifecycle is a loop) | "Mỗi ứng dụng lần lượt qua nhiều điểm quyết định. Tại mỗi điểm, công ty dừng ứng dụng hoặc tăng chi quảng cáo cho ứng dụng" | Bắt buộc |
| VI-3c | Khi vật trừu tượng làm chủ ngữ của động từ hành động (X drives, sets, decides Y), viết lại theo quan hệ giữa hai vế hoặc theo người làm | "Doanh thu quảng cáo trên mỗi người dùng quyết định mức chi tối đa của nhóm UA" | "Mỗi người dùng mang về bao nhiêu doanh thu quảng cáo thì nhóm UA được chi tối đa bấy nhiêu để có một người dùng" | Mặc định |
| VI-3d | Điều kiện, thời gian, nguyên nhân đứng trước; kết quả đứng sau. Chủ đề của câu đứng đầu câu | "Một thao tác thu hồi quyền của người nghỉ việc trên mọi hệ thống" | "Khi một người nghỉ việc, chỉ cần một thao tác để thu hồi quyền của người đó trên mọi hệ thống" | Mặc định |
| VI-3e | Viết từ nghĩa, không sửa từ câu dịch cũ. Bước 1: ghi ý thành các đơn vị nghĩa (ai, làm gì, với cái gì, vì sao). Bước 2: viết câu tiếng Việt từ các đơn vị nghĩa, không nhìn câu tiếng Anh | Sửa từng chữ trên bản dịch cũ | Viết lại từ danh sách đơn vị nghĩa | Bắt buộc cho văn bản gửi lãnh đạo |
| VI-3f | Sau khi viết từ đơn vị nghĩa, đọc cả đoạn và ghép các đơn vị cùng chủ đề vào một câu. Không biến phần giải nghĩa thành một câu định nghĩa riêng giữa đoạn; giữ phần giải nghĩa trong ngoặc. Không viết chuỗi câu ngắn cùng khung "X là Y" | "Vai trò là tập hợp quyền giao cho một người. Mỗi dự án có bộ vai trò riêng." | "Mỗi dự án tự đặt vai trò (tập hợp quyền giao cho một người) theo nhu cầu của dự án" | Mặc định |
| VI-3g | Trạng ngữ chỉ nơi chốn hoặc phạm vi (ở đâu, trong văn bản nào) đặt sau nòng cốt câu khi trạng ngữ đó không phải chủ đề của câu. Điều kiện và thời gian vẫn đứng trước (VI-3d) (ví dụ VD02) | "Trên trang nội bộ, các nhóm sử dụng chung hệ thống." | "Các nhóm sử dụng chung hệ thống trên trang nội bộ." | Mặc định |
| VI-3h | Một câu chỉ có một hành động chính. Khi hai hành động có vai trò khác nhau (ai xây dựng, ai sử dụng trước), tách thành hai câu hoặc sắp xếp lại để hành động chính đứng trước (ví dụ VD14) | "Nhóm phát triển phần mềm xây dựng cách làm chuẩn (golden path) và dùng cách làm này trước." | "Nhóm phát triển phần mềm xây dựng cách làm chuẩn (golden path). Nhóm này cũng là nhóm đầu tiên sử dụng cách làm chuẩn." | Mặc định |

Kết quả thử ngày 25/10/2026: viết từ đơn vị nghĩa giảm đoạn "nghe như dịch" ở phần mô tả kinh doanh từ 12 xuống 4, nhưng tăng ở danh sách kỹ thuật từ 2 lên 8 (câu bị tách vụn). Vì vậy luôn rà soát theo VI-3f sau VI-3e.

Kiểm tra: nghĩa, phạm vi và mức khẳng định giữ nguyên (như VI-1); một người đọc bản ngữ không đánh dấu đoạn nào là "nghe như dịch". Lời diễn giải của người đọc độc lập thường là câu tiếng Việt tự nhiên hơn; sử dụng lời diễn giải đó làm phương án sửa khi nó giữ đủ nghĩa.

## 2e. Câu chỉ dẫn và câu mệnh lệnh (VI-4)

Nguồn: nhận xét của người đọc bản ngữ: câu mệnh lệnh trong tiếng Việt thường đặt động từ lên trước; tiếng Anh có nhiều cách thể hiện hơn, nên dịch theo hình thức tiếng Anh làm câu kém phù hợp. Quy tắc dựa trên:

- Trần Thị Thảo (2023), so sánh câu cầu khiến Anh - Việt (Tạp chí KH&CN Đại học Thái Nguyên, tập 228, số 04): tiếng Anh sử dụng DO, LET, DON'T, động từ tình thái, câu hỏi đuôi, SHALL/WILL/MAY NOT trong quy định; tiếng Việt sử dụng động từ đứng đầu, "hãy", "đừng", "không được", "phải", "cần", "nên" và động từ ngữ vi ("đề nghị", "yêu cầu", "cấm"). Tiếng Việt không sử dụng "sẽ" cho quy định; sử dụng "phải".
- Vũ Thị Sao Chi và Phạm Thị Ninh (2012), câu trong văn bản hành chính (Tạp chí Ngôn ngữ, số 10): câu ngắn, chặt chẽ; không đảo thành phần; hạn chế câu phủ định khi diễn đạt quy phạm; sử dụng mẫu diễn đạt chuẩn.
- Vũ Ngọc Hoa (2010), dẫn theo Nguyễn Thị Hài (2014): động từ ngữ vi trong văn bản hành chính: đề nghị, kiến nghị, yêu cầu, cho phép, cấm, nghiêm cấm.
- Thang mức bắt buộc theo RFC 2119 (MUST, SHOULD, MAY) và ASD-STE100 mục 5.

Nguyên tắc: dịch theo chức năng và mức bắt buộc, không theo hình thức câu tiếng Anh. Mỗi mức sử dụng một từ trong cả văn bản.

| Mức (RFC 2119) | Tiếng Việt | Không sử dụng |
|---|---|---|
| MUST, SHALL (làm một việc) | phải | sẽ phải, được yêu cầu, là bắt buộc phải |
| REQUIRED (có một thứ) | cần có ("cần có" thường gặp hơn "phải có") | được yêu cầu |
| MUST NOT, MAY NOT, not allowed | không được | là không được phép, không bao giờ được |
| SHOULD, RECOMMENDED | nên; hoặc "được khuyến khích" khi văn phong trang trọng hơn và động từ phía sau phù hợp | được khuyến nghị là |
| SHOULD NOT, avoid | theo mức độ: "không khuyến khích" (nhẹ), "không nên", "tránh"; "Avoid X" thành "Tránh X" | "Không dùng X" (mạnh hơn bản gốc) |
| MAY, CAN (cho phép) | có thể | bạn có thể, được phép là |
| need to (điều kiện cần) | cần | |

| Mã | Hình thức tiếng Anh | Cách viết tiếng Việt | Sai | Đúng | Mức |
|---|---|---|---|---|---|
| VI-4a | Mệnh lệnh cho người đọc: "Do X", "Run X", "Please do X" | Động từ đứng đầu câu. Bỏ "please". Không sử dụng "Hãy", "Bạn hãy", "Vui lòng" trong văn bản viết | "Vui lòng gửi báo cáo trước thứ Sáu." | "Gửi báo cáo trước thứ Sáu." | Bắt buộc |
| VI-4b | Cấm cho người đọc: "Do not X", "Never X", "Avoid X" | "Không" + động từ, đứng đầu câu. "Never" không thành "Không bao giờ". "Avoid" thành "Tránh" (mức SHOULD NOT), không thành "Không dùng" (mức MUST NOT). Khi có cách nói khẳng định không thêm dữ kiện, ưu tiên câu khẳng định; khi không có, giữ "Không" | "Không bao giờ chia sẻ mật khẩu." | "Không chia sẻ mật khẩu." | Bắt buộc |
| VI-4c | Quy định cho một vai trò hoặc vật: "X must Y", "X should Y", "X is required", "X is not allowed" | Vai trò hoặc vật làm chủ ngữ + "phải / nên / không được" + động từ. Chuyển bị động thành chủ động; khi bản gốc không nêu ai, mở câu bằng "Không được" hoặc "Phải" + động từ + đối tượng ("Không được sử dụng chung gói đăng ký"); không đưa đối tượng lên đầu câu theo khung bị động tiếng Anh. Một câu chỉ mang một mức bắt buộc; hai mức thì tách hai câu. Giữ đúng mức của bản gốc kể cả khi có số ("nên có tối đa 2"). Một bước bắt buộc ("This step is required"): "Phải thực hiện bước này" | "Báo cáo tuần được yêu cầu cho mỗi dự án." | "Mỗi dự án cần có báo cáo tuần." | Bắt buộc |
| VI-4d | Cho phép: "You can X", "You may X", "Feel free to X" | "Có thể" + động từ, không có "bạn". Khi cần nêu ai, nêu vai trò | "Bạn có thể đổi tên tệp." | "Có thể đổi tên tệp." | Bắt buộc |
| VI-4e | "Make sure X", "Be sure to X", "Ensure X" | "Bảo đảm" + nội dung, hoặc viết thẳng điều phải đạt bằng "phải". Không sử dụng "Hãy chắc chắn rằng", "Đảm bảo rằng" | "Hãy chắc chắn rằng tệp đã được lưu." | "Bảo đảm tệp đã lưu trước khi đóng." | Bắt buộc |
| VI-4f | Mệnh lệnh có điều kiện: "If X, do Y" | Điều kiện trước, động từ sau: "Nếu X, [động từ] Y" hoặc "Khi X, [động từ] Y" | "Gửi lại yêu cầu nếu hệ thống báo lỗi." | "Nếu hệ thống báo lỗi, gửi lại yêu cầu." | Mặc định |
| VI-4g | Quy định viết ở thì hiện tại: "Threads add X first" | Giữ câu trần thuật, chủ ngữ là vai trò; thêm "phải" khi quy định là bắt buộc. Không dịch thành "sẽ" | "Các nhóm sẽ cập nhật bảng mỗi thứ Hai." | "Các nhóm cập nhật bảng mỗi thứ Hai." | Mặc định |
| VI-4h | Quy định dẫn từ nguồn ngoài: "The spec says X must Y" | Nêu nguồn trước: "Theo [nguồn], X phải / không được Y" | "Hợp đồng nói rằng nhà cung cấp không được chia sẻ dữ liệu." | "Theo hợp đồng, nhà cung cấp không được chia sẻ dữ liệu." | Mặc định |
| VI-4i | Câu nhấn mạnh hoặc tu từ: "What you must not do is X", "should be rare" | Viết thành quy định thẳng; "should be rare" thành giới hạn cụ thể nếu bản gốc có số; nếu không có số, viết "ít khi" + động từ | "Điều bạn không được làm là sửa số liệu gốc." | "Không sửa số liệu gốc." | Mặc định |
| VI-4j | Câu cấm có nêu cách làm: viết rõ việc bị cấm và cách làm theo đúng quan hệ nguyên nhân và thứ tự. Không sử dụng "để" khi "để" có thể hiểu thành mục đích của việc bị cấm (ví dụ VD17) | "Không xê dịch các đối tượng đó để tách chúng ra." | "Không tách các đối tượng đó ra bằng cách xê dịch nhẹ." | Bắt buộc |

## 2f. Ngữ pháp khác giữa tiếng Anh và tiếng Việt (VI-5)

Nguồn: Microsoft Vietnamese Style Guide (mục 2.1.3, 4.1.3, 4.1.5, 4.1.7, 4.1.9, 4.1.10, 4.1.17); Cao Xuân Hạo, *Tiếng Việt: sơ thảo ngữ pháp chức năng* (1991): câu bị động với "được" và "bị"; Phạm Thị Phương (2023), so sánh câu bị động Anh - Việt. Microsoft sử dụng "Hãy" và "Vui lòng" cho giao diện gửi người dùng cuối; văn bản nội bộ theo VI-4 (động từ đứng đầu, không "Hãy", "Vui lòng").

| Mã | Quy tắc | Sai | Đúng | Mức |
|---|---|---|---|---|
| VI-5a | Câu bị động: ưu tiên câu chủ động có người làm. Khi bản gốc không nêu ai làm, sử dụng câu không có dấu bị động, hoặc sử dụng "bị" cho việc bất lợi với chủ ngữ và "được" cho việc có lợi hoặc trung tính. Không sử dụng "được" cho việc bất lợi. Khi không rõ lợi hay hại (gỡ, dừng, giữ lại), sử dụng câu chủ động hoặc câu không có dấu bị động ("Cảnh báo không ai xử lý thì gỡ bỏ") | "Tài khoản được tạm khóa." | "Tài khoản bị tạm khóa." | Bắt buộc |
| VI-5b | "Đã", "đang", "sẽ" chỉ sử dụng khi ngữ cảnh chưa cho biết thời gian hoặc cần nhấn mạnh. Tiếng Anh bắt buộc chia thì; tiếng Việt thì không | "Hệ thống sẽ gửi báo cáo mỗi sáng thứ Hai." | "Hệ thống gửi báo cáo mỗi sáng thứ Hai." | Mặc định |
| VI-5c | Phủ định: "chưa" cho việc chưa xảy ra nhưng có thể xảy ra (not yet, pending), "không" cho phủ định chung. Thông báo lỗi: "Không [động từ] được [đối tượng]", không sử dụng "[động từ] thất bại". Kết quả kiểm tra: "không đạt". "Thất bại" chỉ sử dụng cho cả một kế hoạch hoặc dự án | "Tải tệp thất bại." | "Không tải được tệp." | Mặc định |
| VI-5d | Danh động từ tiếng Anh (-ing) làm chủ ngữ: sử dụng động từ làm chủ ngữ, không thêm "việc", "sự" khi câu vẫn rõ. Khi vị ngữ nói về sự có hoặc không có (available, on the roadmap), sử dụng danh từ chính phù hợp ("tính năng", "khả năng") | "Việc kiểm tra thủ công tốn nhiều thời gian." | "Kiểm tra thủ công tốn nhiều thời gian." | Mặc định |
| VI-5e | Cụm danh từ: danh từ chính đứng trước, phần bổ nghĩa đứng sau. Khi dịch chuỗi bổ nghĩa đứng trước của tiếng Anh, sắp lại và kiểm tra nghĩa, vì vị trí tính từ đổi nghĩa ("điểm yếu" khác "yếu điểm") | "Mẫu báo cáo tuần nhóm UA mới" (new UA team weekly report template) | "Mẫu mới cho báo cáo tuần của nhóm UA" | Mặc định |
| VI-5f | Tiêu đề, nhãn, tên mục: chỉ viết hoa chữ đầu và tên riêng. Không viết hoa từng chữ theo kiểu tiếng Anh | "Bản Đồ Hành Trình Khách Hàng" | "Bản đồ hành trình khách hàng" | Bắt buộc |
| VI-5g | Từ nối: sử dụng cặp từ nối của tiếng Việt (vì ... nên, nhờ ... nên, nếu ... thì, tuy ... nhưng, khi ... thì) thay cho chuỗi "Bởi vì ..., nó ...". Không mở đầu nhiều câu liên tiếp bằng "Tuy nhiên", "Ngoài ra", "Do đó" | "Bởi vì dữ liệu được mã hóa, nó an toàn." | "Nhờ dữ liệu được mã hóa nên mức độ an toàn cao." | Mặc định |
| VI-5h | Mệnh đề quan hệ kiểu tiếng Anh: không sử dụng "nơi mà", "cái mà", "điều mà", "người mà"; không sử dụng "điều này" hoặc "việc này" để nối cả một ý ("which is ..."). Tách câu hoặc sử dụng danh từ cụ thể | "Hệ thống gửi cảnh báo qua Telegram, điều mà giúp nhóm phản ứng nhanh." | "Hệ thống gửi cảnh báo qua Telegram. Nhờ cảnh báo này, nhóm phản ứng nhanh hơn." | Mặc định |
| VI-5i | Đại từ "nó", "chúng" chỉ vật: thay bằng danh từ (Microsoft 4.1.10: "nó", "chúng nó" mang sắc thái thân mật hoặc coi thường khi chỉ người) | "Nếu quảng cáo vi phạm, nó bị gỡ." | "Nếu quảng cáo vi phạm, quảng cáo bị gỡ." | Mặc định |
| VI-5j | Không lặp "thì" ở nhiều vế song song. Sử dụng danh sách, dấu hai chấm hoặc động từ trực tiếp. Viết khoảng số bằng "đến", không bằng dấu gạch (ví dụ VD18) | "Mức rủi ro 0 - 1 thì đạt, mức 2 thì chuyển cho người duyệt, mức 3 thì bị chặn." | "Mức rủi ro từ 0 đến 1: đạt. Mức 2: chuyển cho người duyệt. Mức 3: bị chặn." | Mặc định |
| VI-5k | Văn viết trang trọng sử dụng "sử dụng" cho động từ "use"; giữ "dùng" chỉ trong "người dùng". Viết "sử dụng chung", không viết "dùng chung" ("dùng" mang sắc thái khẩu ngữ; ví dụ VD01) | "Các nhóm cùng dùng hệ thống." | "Các nhóm cùng sử dụng hệ thống." | Mặc định |

## 3. Văn phong viết

- Chủ ngữ là tổ chức, nhóm, hệ thống hoặc vai trò: "Nhóm UA", "Hệ thống thanh toán", "Người phụ trách". Không sử dụng "tôi", "mình", "bên em", "quý vị".
- Không sử dụng hình ảnh, ẩn dụ, so sánh. Viết nghĩa thật.
- Không sử dụng từ biểu cảm: "vô cùng", "cực kỳ", "siêu", "rất là".
- Mỗi câu một ý chính. Câu có đủ chủ ngữ và vị ngữ, trừ tiêu đề và nhãn.
- Tiêu đề, nhãn và slide được sử dụng cụm danh từ (vietnamizer V14, Không flag).
- Không sử dụng tiểu từ tình thái: "nhé", "ạ", "đấy", "cơ", "chứ", "thôi", "nha".

## 4. Từ cần tránh trong văn viết

| Không sử dụng | Sử dụng |
|---|---|
| cái gì, cái nào | gì, nào; hoặc gọi tên: "hệ thống nào" |
| thấy (nghĩa "biết") | biết, nắm được |
| nó (khi có thể gọi tên) | tên sự vật |
| thì (đệm), mà (đệm), luôn (đệm), rồi (đệm cuối câu) | bỏ |
| tầm, cỡ, khoảng chừng | khoảng |
| mấy (nghĩa "một số") | một số, các |
| xài | sử dụng |
| ổn, ok, oke | đạt, phù hợp |
| chốt | quyết định, thống nhất |
| xịn, ngon, toang | gọi đúng tính chất: tốt, hiệu quả, thất bại |
| check | kiểm tra |
| chạy thật | vận hành thực tế |
| làm (khi có động từ cụ thể) | xây dựng, thiết lập, viết, sửa |

Động từ tiếng Anh không sử dụng trong câu tiếng Việt (quy tắc 1.7):

| Không viết | Viết |
|---|---|
| scale app | tăng chi tiêu quảng cáo cho ứng dụng; mở rộng quy mô |
| clone game | sao chép lối chơi của game |
| remake | làm lại |
| reskin | thay giao diện |
| test, check | thử nghiệm, kiểm tra |
| deploy | triển khai |
| review, approve | duyệt |
| fix | sửa |
| set up | thiết lập |
| launch, soft launch | phát hành, phát hành thử |

## 5. Giới hạn độ dài

| Mục | Giới hạn | Cơ sở |
|---|---|---|
| Câu quy trình | 30 âm tiết | STE 20 từ, nhân hệ số 1,52 |
| Câu mô tả | 38 âm tiết | STE 25 từ, nhân hệ số 1,52 |
| Đoạn | 6 câu | STE |
| Cụm danh từ | 3 danh từ | STE 2.1 |

Hệ số 1,52 âm tiết cho mỗi từ tiếng Anh được đo trên bản dịch thử ngày 23/10/2026 (193 từ tiếng Anh, 293 âm tiết, văn phong thông thường). Vòng 1 ngày 25/10/2026, văn phong viết trang trọng: 352 âm tiết, hệ số 1,82. Giới hạn giữ nguyên vì vòng 1 đạt 97% ở lần chạy đầu; hiệu chỉnh hệ số sau mỗi vòng kiểm tra (xem EVALUATION.md).

Cách đếm: mỗi âm tiết cách nhau bằng dấu cách là 1. Số, mã, tên riêng, thuật ngữ tiếng Anh và phần trong ngoặc đơn mỗi loại tính là 1.

## 6. Thứ tự làm việc

1. Xác định loại văn bản: quy trình hay mô tả.
2. Áp dụng thuật ngữ trong gói thuật ngữ.
3. Ghi ý của bản gốc thành các đơn vị nghĩa, rồi viết câu tiếng Việt từ các đơn vị nghĩa đó (VI-3e). Viết theo các quy tắc Bắt buộc và Mặc định.
4. Rà soát bằng vietnamizer (profile `ky-thuat-doanh-nghiep`). Khi một quy tắc Mặc định làm câu sai nghĩa hoặc thiếu tự nhiên, vietnamizer quyết định; ghi lại ngoại lệ.
5. Chạy `python3 -I tools/ste_vi_check.py <tệp>`. Quy tắc Bắt buộc: 0 lỗi. Quy tắc Mặc định: ít nhất 80% số câu đạt.
6. Đọc ngược: viết nghĩa của bản tiếng Việt thành một dòng tiếng Anh, so với ý ban đầu.
