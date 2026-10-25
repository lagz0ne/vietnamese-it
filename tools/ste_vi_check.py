#!/usr/bin/env python3
"""STE-VI check for Vietnamese text (see ../ste-vi.md).

Usage: python3 -I ste_vi_check.py <file.md|file.html|file.txt> [--org NAME]... [--tech] [--copy] [--json]

--org NAME   name of the organization that writes the text (rules VI-1a, VI-1b, VI-1d).
             Repeat for more names. "công ty" and "tổ chức" are always checked.
--tech       readers are technical (README, how-to): code and paths in text are allowed (VI-2c off).
--copy       interface and product copy (VI-6): "bạn", "Hãy", "Vui lòng" and "tôi" in labels allowed
             (VI-4a, VI-4d, 5.3 and first person off); VI-6 checks on.

Must rules (Bắt buộc): 0 findings.
Default rules (Mặc định): at least 80% of sentences have no finding.
Prints OK when both hold, else FAIL. Exit code 0 / 1.
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TERMS_DIR = os.path.join(HERE, "..", "terms")

PROC_LIMIT = 30   # STE 5.1: 20 words x 1.52
DESC_LIMIT = 38   # STE 6.1: 25 words x 1.52
PARA_LIMIT = 6    # STE 6.4
DEFAULT_TARGET = 0.80

W = r"(?<![\wÀ-ỹ])"   # word start
E = r"(?![\wÀ-ỹ])"    # word end

def wre(words):
    return re.compile(W + "(" + "|".join(words) + ")" + E, re.I)

MUST = [
    ("1.10", "spoken word", wre([
        "cái gì", "cái nào", "xài", "ổn áp", "oke", "chốt", "xịn", "ngon lành", "toang",
        "hơi bị", "kiểu như", r"tầm\s+\d", "cỡ chừng", "khoảng chừng", "mấy cái", "chạy thật", "check"])),
    ("1.10", "spoken word", re.compile(r"(?<![\wÀ-ỹ])(ok|Ok)(?![\wÀ-ỹ])")),  # "OK" in capitals is a literal output or button name
    ("3.x", "particle", re.compile(r"(?<![\wÀ-ỹ])(nhé|nha|ạ|đấy|cơ|chứ)(?=\s*[.!?]?\s*$)", re.I | re.M)),
    ("1.10", "first person", re.compile(W + r"(tôi|bên em|quý vị|chúng mình|bên mình|team mình|nhóm mình)" + E + r"|^\s*Mình" + E, re.I)),
    ("1.7", "English verb", re.compile(
        W + r"(?:(?:để|sẽ|đã|đang|cần|phải|hãy|được|bị|rồi|và|nhóm|team)\s+)(scale|clone|test|deploy|fix|review|approve|remake|reskin|launch|setup|set up|plug in)" + E
        + r"|" + W + r"(scale|clone|test|deploy|fix|review|approve|remake|reskin|launch)\s+(một|các|những|ứng dụng|app|game|creative|lại)" + E, re.I)),
    ("3.4", "stacked modal", wre(["có thể sẽ", "sẽ cần phải", "có lẽ sẽ", "chắc sẽ"])),
    ("3.6", "được/bị ... bởi", re.compile(W + r"(được|bị)\s+[^.,;:]{1,40}?\s+bởi" + E, re.I)),
    ("4.2", "chat abbreviation", wre(["ko", "k0", "đc", "dc", "tks", "vs", "j"])),
    ("9.3", "copied English image", wre([
        "cắm vào", "xây trên", "trên đó", "đi qua mọi", "con đường", "lát mỏng", "lát cắt", "viên ngọc", "vòng dòng tiền"])),
    ("VI-2b", "resource receives access", re.compile(W + r"(tài nguyên|hệ thống|dữ liệu)[^.,;:]{0,20}?nhận quyền" + E, re.I)),
    ("VI-2c", "code in text", re.compile(r'"[^"]*\s=\s[^"]*"|`[^`]+`')),
    ("5.3", "polite opener", re.compile(r"^(Vui lòng|Bạn hãy|Xin hãy)" + E, re.M)),
    ("VI-4", "directive copied from English form", re.compile(W + r"(được yêu cầu|hãy chắc chắn|đảm bảo rằng|bảo đảm rằng|là không được phép|không bao giờ)" + E, re.I)),
    ("VI-4d", "'bạn' or 'chúng ta' in a document", re.compile(W + r"(bạn\s+(?:có thể|nên|cần|phải|hãy|không được)|chúng ta hãy|điều bạn)" + E, re.I)),
    ("VI-4a", "Hãy or Vui lòng opens a sentence", re.compile(r"(?:^|[.!?:]\s+)(Hãy|Vui lòng|Xin vui lòng)" + E, re.M)),
    ("VI-5a", "được with a bad event", re.compile(W + r"được\s+(cấm|từ chối|phạt|tạm khóa|khóa|đình chỉ|chặn|gỡ bỏ|thu hồi|loại bỏ|tạm ngưng|hạn chế)" + E, re.I)),
    ("VI-5f", "title case heading", re.compile(r"^#{1,4}\s+[A-ZĐÀ-Ỹ]\S*\s+[A-ZĐÀ-Ỹ]\S*\s+[A-ZĐÀ-Ỹ]", re.M)),
    ("GR-6", "latin abbreviation", re.compile(r"(?<![\w])(e\.g\.|i\.e\.|etc\.)", re.I)),
    ("8.1", "em dash", re.compile(r"—")),
]

DEFAULT = [
    ("8.1", "comma before và/hoặc", re.compile(r",\s+(và|hoặc)" + E)),
    ("8.1", "semicolon", re.compile(r";")),
    ("2.1", "của ... của", re.compile(W + r"của" + E + r"[^.,;:()]{1,30}?" + W + r"của" + E)),
    ("1.13", "nominalization", wre(["tiến hành thực hiện", "thực hiện việc", "tiến hành việc", "có sự", "thực hiện sự"])),
    ("GR-2", "long preposition", wre(["trong quá trình", "nhằm mục đích", "trên cơ sở", "trong khuôn khổ", "tại thời điểm", "với sự"])),
    ("6.x", "empty lead-in", wre(["điều quan trọng cần lưu ý là", "cần lưu ý rằng", "có thể thấy rằng", "không thể phủ nhận rằng"])),
    ("GR-3", "pronoun nó / điều này", wre(["nó", "điều này", "việc này"])),
    # VI-1a, VI-1b, VI-1d use the organization names: see org_rules()
    ("VI-1c", "'là một' + noun", re.compile(W + r"là một\s+(?!người dùng)[\wÀ-ỹ]+", re.I)),
    ("VI-1e", "stacked 'only one'", re.compile(W + r"(một\s+[^.,;:]{1,20}?\s+(chung|duy nhất)|chỉ\s+[^.]{0,30}?duy nhất)" + E, re.I)),
    ("VI-2", "ambiguous word alone (term packs)", re.compile(W + r"(tài nguyên|mô hình(?!\s+AI)|nhóm phát triển(?!\s+phần mềm)|tài sản quan trọng nhất|kết nối với hệ thống)" + E, re.I)),
    ("VI-5c", "verb + thất bại", re.compile(W + r"(lưu|tải|gửi|đăng nhập|kết nối|cài đặt|xuất bản|triển khai|cập nhật)\s+[^.,;:]{0,25}?thất bại" + E, re.I)),
    ("VI-5h", "English relative clause", re.compile(W + r"(nơi mà|cái mà|điều mà|người mà|điều này là)" + E, re.I)),
    ("VI-5j", "repeated 'thì' in one sentence", re.compile(W + r"thì\s[^.!?]{1,60}?\sthì" + E, re.I)),
    ("VI-5k", "'dùng' as a verb (use 'sử dụng')", re.compile(r"(?<!người )(?<![\wÀ-ỹ])(?<!sử )dùng(?![\wÀ-ỹ])(?!\s+thử)", re.I)),
    ("VI-4j", "ban with 'để' read as purpose", re.compile(r"(?:^|[.!?:]\s+)Không\s[^.!?]{1,50}?\sđể\s", re.M)),
    ("VI-1e", "'mọi/mỗi' with 'dùng chung'", re.compile(W + r"((mọi|tất cả|mỗi)\s+[^.,;:]{1,15}?\s+dùng chung|dùng chung cho (mọi|tất cả))" + E, re.I)),
    ("VI-6c", "'không thành công' (use 'Không ... được')", re.compile(W + r"[\wÀ-ỹ]+(\s+[\wÀ-ỹ]+)?\s+không thành công" + E, re.I)),
    ("VI-1c", "3+ 'một' in one sentence", re.compile(r"(?:" + W + r"một" + E + r"[^.!?]*){3,}", re.I)),
]

COPY_OFF = {"VI-4a", "VI-4d", "5.3", "first person"}
COPY_EXTRA = [
    ("VI-6d", "'Vui lòng đợi/chờ' (use 'Xin chờ')", re.compile(W + r"vui lòng\s+(đợi|chờ)" + E, re.I)),
    ("VI-6e", "old or too formal word", wre(["mã định danh", "nhập vào", "theo các bước sau đây", "tải về không thành công"])),
    ("VI-6b", "'Hủy bỏ' as a command (use 'Hủy')", re.compile(r"^\s*Hủy bỏ\s*$", re.M)),
    ("VI-6a", "pronoun the string does not need", re.compile(W + r"(của bạn|nhóm bạn|chúng tôi đang)" + E, re.I)),
]

PROC_VERBS = ("Mở", "Chọn", "Nhập", "Gửi", "Kiểm tra", "Thêm", "Xóa", "Đọc", "Viết", "Sử dụng", "Cài",
              "Tạo", "Sửa", "Đặt", "Bấm", "Nhấn", "Chạy", "Ghi", "Lưu", "Tải", "Đăng nhập", "Gắn", "Bật", "Tắt")

OLD_TONE = re.compile(r"[\wÀ-ỹ]*(oà|oá|oả|oã|oạ|oè|oé|oẻ|oẽ|oẹ|(?<!q)(uỳ|uý|uỷ|uỹ|uỵ))" + E, re.I)   # "quý", "quỹ" are the same in both styles
NEW_TONE = re.compile(r"[\wÀ-ỹ]*(òa|óa|ỏa|õa|ọa|òe|óe|ỏe|õe|ọe|ùy|úy|ủy|ũy|ụy)" + E, re.I)


def load_text(path):
    raw = open(path, encoding="utf-8").read()
    if path.endswith((".html", ".htm")):
        raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
        raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
        raw = re.sub(r"(?i)</(p|div|li|h[1-6]|tr|section|td|th)>", "\n\n", raw)
        raw = re.sub(r"<[^>]+>", " ", raw)
        raw = html.unescape(raw)
        return [(None, l) for l in raw.splitlines()], True
    return list(enumerate(raw.splitlines(), 1)), False


def units(lines):
    """Yield (line_no, paragraph_text, kind). kind: para | item | label."""
    in_code = in_front = False
    buf, start = [], None
    out = []
    for i, (no, line) in enumerate(lines):
        s = line.strip()
        if i == 0 and s == "---":
            in_front = True
            continue
        if in_front:
            in_front = s != "---"
            continue
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if not s or s.startswith(("#", "|", "<!--")):
            if buf:
                out.append((start, " ".join(buf), "para"))
                buf = []
            if s.startswith("#"):
                out.append((no, s.lstrip("# "), "label"))
            continue
        m = re.match(r"^([-*]|\d+\.)\s+(.*)", s)
        if m:
            if buf:
                out.append((start, " ".join(buf), "para"))
                buf = []
            out.append((no, m.group(2), "item"))
            continue
        if not buf:
            start = no
        buf.append(s)
    if buf:
        out.append((start, " ".join(buf), "para"))
    return out


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|(?<=:)\s+", text)   # 8.4: a colon ends a sentence for counting
    return [p.strip() for p in parts if p.strip()]


def count_tieng(sentence):
    s = re.sub(r"\([^)]*\)", " X ", sentence)              # 8.5
    toks = [t for t in re.split(r"\s+", s) if re.search(r"[\wÀ-ỹ]", t)]
    n, prev_ascii = 0, False
    for t in toks:
        is_ascii = bool(re.fullmatch(r"[\W\dA-Za-z_]+", t)) and not re.fullmatch(r"\W*\d[\d.,%]*\W*", t)
        if is_ascii and prev_ascii:                          # 8.7: one English term = 1
            continue
        n += 1
        prev_ascii = is_ascii
    return n


VI_SYL = re.compile(r"^(ngh|gh|gi|kh|ng|nh|ph|qu|th|tr|ch|[bcdghklmnprstvx])?[aeiouy]{1,3}(ch|ng|nh|[cmnpt])?$")


def org_rules(orgs):
    names = "|".join(re.escape(o) for o in orgs + ["công ty", "tổ chức"])
    own = "|".join(re.escape(o) for o in orgs) or "(?!x)x"
    return [
        ("VI-1a", "scope repeated", re.compile(W + r"(mọi|tất cả|toàn bộ|các)\s+[^.,;:]{1,25}?\s+((tại|của|trong|ở)\s+)?(" + names + ")" + E, re.I)),
        ("VI-1b", "organization name in body text", re.compile(r"^(Tại|Ở) (" + own + "),", re.I)),
        ("VI-1d", "translated possessive", re.compile(W + "(của nó|của họ|của chúng|của mình|của chúng ta|của công ty mình|của (" + names + "))" + E, re.I)),
    ]


def load_packs():
    """Allowed English words and gloss-first terms from ../terms/*.md (template excluded)."""
    words, gloss = set(), []
    try:
        files = sorted(f for f in os.listdir(TERMS_DIR) if f.endswith(".md") and f != "org-template.md")
    except OSError:
        files = []
    for f in files:
        for line in open(os.path.join(TERMS_DIR, f), encoding="utf-8"):
            if line.startswith("|"):
                words.update(w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9'^-]*", line))
            elif line.startswith("Gloss at first use:"):
                gloss += [t.strip() for t in line.split(":", 1)[1].split(",") if t.strip()]
    return words, gloss


def first_use_gloss(text, gloss_first):
    out = []
    for t in gloss_first:
        m = re.search(r"(?<![\w])" + re.escape(t) + r"(?![\w])", text)
        if m and not re.match(r"\s*\(", text[m.end():m.end() + 3]) and not re.match(r"\s*,\s*(hệ thống|công cụ|nền tảng)", text[m.end():m.end() + 20]):
            out.append((None, "VI-2a", "no gloss at first use", t))
    return out


def check(path, orgs=(), tech=False, copy=False):
    lines, is_html = load_text(path)
    allowed, gloss_first = load_packs()
    must_rules = [r for r in MUST if not (tech and r[0] == "VI-2c")
                  and not (copy and (r[0] in COPY_OFF or r[1] in COPY_OFF))]
    default_rules = DEFAULT + org_rules(list(orgs)) + (COPY_EXTRA if copy else [])
    must, default, notes = [], [], []
    n_sent = 0
    bad_sent = 0
    old_tone = new_tone = 0
    for no, text, kind in units(lines):
        old_tone += len(OLD_TONE.findall(text))
        new_tone += len(NEW_TONE.findall(text))
        sents = sentences(text)
        if kind == "para" and len(sents) > PARA_LIMIT:
            default.append((no, "6.4", f"paragraph has {len(sents)} sentences (max {PARA_LIMIT})", text[:60]))
        for s in sents:
            n_sent += 1
            hit = False
            for rid, name, rx in must_rules:
                for m in rx.finditer(s):
                    must.append((no, rid, name, m.group(0)))
            if kind != "label":
                limit = PROC_LIMIT if s.startswith(PROC_VERBS) else DESC_LIMIT
                n = count_tieng(s)
                if n > limit:
                    default.append((no, "4.1", f"{n} âm tiết (max {limit})", s[:60]))
                    hit = True
            for rid, name, rx in default_rules:
                for m in rx.finditer(s):
                    default.append((no, rid, name, m.group(0)))
                    hit = True
            plain = re.sub(r'"[^"]*"|`[^`]*`', " ", s)
            for w in re.findall(r"(?<![\wÀ-ỹ])[A-Za-z][A-Za-z'-]{2,}(?![\wÀ-ỹ])", plain):
                if w.lower() not in allowed and not w[0].isupper() and not VI_SYL.match(w.lower()):
                    notes.append((no, "1.6", "English word not in a term pack", w))
            bad_sent += hit
    must.extend(first_use_gloss(" ".join(t for _, t, _ in units(lines)), gloss_first))
    if old_tone and new_tone:
        must.append((None, "1.14", "mixed tone-mark style", f"old {old_tone}, new {new_tone}"))
    pct = 1.0 if n_sent == 0 else (n_sent - bad_sent) / n_sent
    ok = not must and pct >= DEFAULT_TARGET
    return {"file": path, "sentences": n_sent, "default_pass": round(pct, 3), "must": must,
            "default": default, "notes": notes, "ok": ok}


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    args = sys.argv[1:]
    orgs = [args[i + 1] for i, a in enumerate(args[:-1]) if a == "--org"]
    res = check(args[0], orgs, "--tech" in args, "--copy" in args)
    if "--json" in sys.argv:
        print(json.dumps(res, ensure_ascii=False, indent=1))
    else:
        loc = lambda no: f"line {no}" if no else "page"
        for no, rid, name, ev in res["must"]:
            print(f"MUST    {loc(no)}  STE {rid}  {name}: {ev}")
        for no, rid, name, ev in res["default"]:
            print(f"DEFAULT {loc(no)}  STE {rid}  {name}: {ev}")
        for no, rid, name, ev in res["notes"]:
            print(f"NOTE    {loc(no)}  STE {rid}  {name}: {ev}")
        vi1 = sum(1 for f in res["default"] if f[1].startswith("VI-1"))
        print(f"VI-1 findings (implicit redundancy): {vi1}")
        print(f"sentences {res['sentences']}, must findings {len(res['must'])}, "
              f"default pass {res['default_pass']:.0%} (target {DEFAULT_TARGET:.0%})")
        print("OK" if res["ok"] else "FAIL")
    sys.exit(0 if res["ok"] else 1)


if __name__ == "__main__":
    main()
