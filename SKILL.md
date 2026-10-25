---
name: vietnamese-it
description: Write Vietnamese, or translate English to Vietnamese, for tech text - docs and guides, system documents (specs, architecture, runbooks), and tech copy (UI strings, error messages, product pages). Uses STE-VI (ASD-STE100 adapted to Vietnamese), Microsoft vi-VN voice for copy, term packs with a glossary-building step, a vietnamizer edit pass and a checker script.
---

# Vietnamese for tech

In short: pick the text type, write from the meaning, not word by word. Documents follow the STE-VI rules in [ste-vi.md](ste-vi.md): formal written Vietnamese, short sentences, active voice, no spoken words, English terms only as nouns. Interface and product copy follow VI-6 (Microsoft vi-VN voice: clear, friendly, short). Use the term packs in [terms/](terms/README.md) for every technical term; build a domain glossary first when the text has many terms that no pack has. Then do one edit pass with the vietnamizer patterns and run the checker until it prints OK.

Files (source: https://github.com/lagz0ne/vietnamese-it). If this skill folder has only SKILL.md, get the other files first: `git clone https://github.com/lagz0ne/vietnamese-it`, or read each file from `https://raw.githubusercontent.com/lagz0ne/vietnamese-it/main/<path>`.
- [ste-vi.md](ste-vi.md): ASD-STE100 rules mapped to Vietnamese (keep, adapt, drop), must and default levels, rules VI-1 to VI-6, words to avoid, length limits.
- [terms/](terms/README.md): term packs, on by default: `common.md` (work words), `tech.md` (interface, software, data, cloud, security, development, product, AI; from Microsoft Terminology), `systems.md` (platform, architecture, operations). Optional: `optional/adtech.md`. Your own names: a copy of `org-template.md`.
- [tools/ste_vi_check.py](tools/ste_vi_check.py): checker. Must rules: 0 findings. Default rules: at least 80% of sentences pass.
- [tools/term_candidates.py](tools/term_candidates.py) and [tools/tbx_lookup.py](tools/tbx_lookup.py): glossary building (section 2b).
- [examples.md](examples.md): before and after pairs for each rule group.
- [EVALUATION.md](EVALUATION.md): how the rules were tested (blind readers, blind judge) and the results.
- [vendor/vietnamizer/](vendor/vietnamizer/SKILL.md): Vietnamese editor skill (fioenix/vietnamizer, MIT). Patterns V1 to V25, T1 to T6, profile K1 to K7.
- [sources.md](sources.md): what was compared and why.

## 1. Set the language contract

Do this before you write. Use these defaults unless the user or an organization pack sets others. Do not ask the user again.

| Item | Default |
|---|---|
| Reader | Native Vietnamese readers of tech text: engineers, product and operations staff, managers, and people who use software products. Staff read common English IT terms every day; product users may not. |
| Register | Documents: formal written Vietnamese (STE-VI): objective, exact, no spoken words (cái gì, thấy, xài, chốt), no particles (nhé, ạ, đấy), no metaphors, no emotive words, no institutional clichés (đóng vai trò quan trọng, góp phần nâng cao). Full rules: [ste-vi.md](ste-vi.md). |
| Pronouns | Documents: no first person, no "bạn" (copy: section 3b). The subject is the organization, team, system or role ("Nhóm vận hành", "Hệ thống thanh toán", "Người phụ trách"). Procedures start with the verb. Never "tôi", "mình" (as "I/we"), "bên em", "quý vị". |
| Spelling | One tone-mark style per file. Default new style: hóa, tùy, thủy, khỏe. |
| Customer text | Documents for customers (release notes, guides) use the same register. Interface and product copy: VI-6 (section 3b). When the product already has a Vietnamese voice, follow it. |
| Case | Sentence case for titles, labels, buttons. Capital letters only for the first word, proper names and product names. Never English title case. |

## 1b. Pick the text type

| Type | Examples | Rules | Checker |
|---|---|---|---|
| Tech docs | guides, how-to, README, release notes, help articles | STE-VI, VI-1 to VI-5 | `--tech` |
| System docs | specs, architecture, design docs, runbooks, decision records | STE-VI, VI-1 to VI-5; technical reader | `--tech` |
| Business text | pages, slides, reports for managers outside IT | STE-VI, VI-1 to VI-5; gloss every abbreviation (VI-2a) | default |
| Tech copy | UI strings, buttons, error messages, onboarding screens, product and feature pages, product emails | VI-6 (Microsoft vi-VN voice), VI-1, VI-3, VI-5 | `--copy` |

One file has one type. A help article with UI labels in it is a tech doc that quotes the labels exactly as the product shows them.

## 2. Terms

Apply in this order:
1. Names of the organization, products, tools and vendors: keep as is. Put them in your organization pack (copy of [terms/org-template.md](terms/org-template.md)).
2. A term in a term pack: use its form and mode. The gloss goes in brackets only at the first use in a page or deck.
3. A term not in a pack: use the Vietnamese name from the vendor's own Vietnamese interface or help pages (for example Google, Microsoft), if one exists. Else keep English. List the new term in the report (section 7) so the user can add it to a pack.
4. Do not coin a new Vietnamese word. Do not translate an English image (paved road, crown jewels, strangler fig): write the meaning or keep the English term with a gloss.
5. One term = one form in one file. Do not change a term to avoid repetition.
6. A gloss only explains a word. When a pack gloss holds more than the source says, the source wins: cut the gloss to what the source says.
7. A vague actor in the source ("the team"): name the team only when the same text or the organization pack names it; else keep "nhóm" and do not guess.

## 2b. Build a domain glossary

Do this before a large text or a new field (for example payments, healthcare, games). Skip it for short texts where every term is in a pack.

1. List candidates: `python3 -I tools/term_candidates.py <source> --min 2`. It prints abbreviations, CamelCase and hyphenated words, and repeated 2- and 3-word phrases that no pack has. Remove ordinary phrases.
2. Look up each term, in this order, and keep the source mark:
   - the Microsoft Terminology Collection: download it from Microsoft (learn.microsoft.com/globalization/reference/microsoft-terminology, file VIETNAMESE.tbx), then `python3 -I tools/tbx_lookup.py VIETNAMESE.tbx --file terms.txt` (mark M);
   - the Vietnamese interface or docs of the product the reader uses (Google: G; others: name the vendor);
   - Vietnamese standards and law texts for regulated fields (mark L).
3. Choose one form and a mode (keep, keep + gloss, vi):
   - take the form most used in the source; prefer the form that the reader sees in the product;
   - when the Vietnamese forms vary and none is common, keep English and add a gloss for readers outside the field;
   - never coin a word; use the new tone-mark style (hóa, tùy).
4. Write the rows to a pack in `terms/` (for example `terms/payments.md`), one row per term, with the source mark. The checker reads every `.md` file in `terms/`.
5. For a business text, run the reader test in [EVALUATION.md](EVALUATION.md) on the glosses: a gloss that a reader outside the field cannot use is not done.

## 3. Translate English to Vietnamese

1. Read the whole unit (one slide, one section). Write in one line what the reader must know or do after reading it.
2. Freeze names, numbers, ids, code, links and quotes. Copy them byte for byte. Change only the number format (section 5).
3. Write the Vietnamese from the meaning, not from the English sentence (ste-vi.md 2d, VI-3; interpretive method: understand, deverbalize, re-express):
   - 3a. Write meaning units: one fact per line (who, does what, to what, why or when), with no English sentence order.
   - 3b. Write the Vietnamese from the units only. Do not look at the English sentence. Do not edit an old translation word by word.
   - 3c. When an English word has no Vietnamese match, follow VI-3a (pack form, broader word, paraphrase, loan word + gloss, omit). When the paraphrase makes the sentence long or stiff, rebuild the sentence (VI-3b): change the noun to a verb, change the subject, split, or reorder (condition and time first, result last). Place and scope words go after the main clause (VI-3g). One main action per sentence (VI-3h).
   - 3d. Read each paragraph as a whole (VI-3f): merge units with the same topic into one sentence; keep glosses in brackets, not as separate definition sentences; no run of short "X là Y" sentences. In tests, meaning-first writing cut "sounds translated" spans in business prose from 12 to 4, but chopped a technical list (2 to 8) when this step was missing.
   - 3e. Instructions and rules (ste-vi.md 2e, VI-4): translate by function and strength, not by English form. Orders to the reader start with the verb ("Gửi...", "Không gửi..."); rules for a role use role + phải / cần có / nên / không được / có thể + verb; no "Hãy", "Vui lòng", "Bạn có thể", "được yêu cầu", "không bao giờ"; one Vietnamese word per strength level in a file.
   - 3f. Grammar that differs (ste-vi.md 2f, VI-5): active voice with the actor; "bị" for bad events, "được" for good or neutral; drop đã/đang/sẽ when time is clear; "chưa" for not yet; "Không ... được" for failures; verb as subject without "việc"; head noun first; sentence case in headings; paired connectives; no "nơi mà / điều mà"; name the thing instead of "nó"; no repeated "thì"; "sử dụng", not "dùng", as the verb for "use".
   You can split, merge or reorder sentences. Remove English filler.
4. Remove English structure that Vietnamese does not need (vietnamizer pattern in brackets):
   - noun stacks and "của" chains (V7): "hiệu suất hệ thống", not "hiệu suất của hệ thống";
   - plural marks on every noun (V8): "các", "những" only when the scope needs them;
   - long prepositions (V9): "khi", "để", "theo" for "trong quá trình", "nhằm mục đích", "trên cơ sở";
   - empty lead-ins (V11): "Điều quan trọng cần lưu ý là";
   - "được ... bởi" passive (V16): "Phòng kế toán hoàn thành báo cáo";
   - unclear "nó", "điều này" (V18): name the thing;
   - English relative clauses ending in "trên đó", "mà ... vào";
   - a comma before "và" or "hoặc" (T4, Microsoft guide 4.1.14).
   - 4b. Apply the STE-VI rules in [ste-vi.md](ste-vi.md) section 2 (must rules on every sentence, default rules on at least 80%).
5. Edit pass: read [vendor/vietnamizer/SKILL.md](vendor/vietnamizer/SKILL.md) and apply it with profile `ky-thuat-doanh-nghiep`. Style card: `van-hanh-doanh-nghiep` for pages, notes, slides, reports; `huong-dan-ky-thuat` for how-to and README text. Skip its step 0 and its Jev section (the runner is not included). When its genre gate limits the pass (changelog, release notes: typography only), follow vietnamizer; STE-VI and the checker still apply. Its five gate rules apply to every change: name the pattern, add no fact, keep meaning and claim strength, change only the needed span, no process notes.
   - 5b. Run `python3 -I tools/ste_vi_check.py <file> [--org "Tên tổ chức"] [--tech | --copy]` with the option from section 1b. Fix every must finding. If default pass is under 80%, fix the worst sentences. When vietnamizer and a default rule disagree, keep the natural sentence and note the exception.
6. Back-check: read only the Vietnamese. Write its meaning in one English line. Compare with the line from step 1. If they differ, fix the Vietnamese.

## 3b. Tech copy

For UI strings, error messages and product text (ste-vi.md 2g, VI-6):
- Read the whole screen or page first. Rewrite jokes and idioms by meaning.
- Drop pronouns by default: "your", "you", "we" usually need no Vietnamese word. Keep "bạn" only in a direct question or invitation. No "của bạn" when the reader is clear; no "chúng tôi đang ..." for a system state.
- Buttons and menu items: a short verb from the tech pack ("Lưu", "Hủy", "Thử lại", "Tải xuống").
- Error messages: declarative, end with a period, fixed patterns ("Không lưu được tệp.", "Không tìm thấy tệp.", "Không đủ bộ nhớ.").
- "Xin chờ" for "Please wait"; "Vui lòng" or "hãy" only when the user must act after a problem, at most once per message.
- Product text: state the benefit at the source's strength; no emotive words.
- Keep placeholders (%s, {0}, {name}) and check that the sentence still reads well with a real value in each.
- Check length against the UI: Vietnamese is often longer than English.

## 4. Write new Vietnamese

Use steps 1, 3 to 6 above with your own outline as the source. Same register and terms.

## 5. Format

| Item | Rule | Example |
|---|---|---|
| Decimal | comma | 0,35; 5,25 cm |
| Thousands | period, no space | 1.526; 20.000.000 |
| Money | symbol as in the source, Vietnamese separators | $1.526,75; 0,35 USD in prose |
| Percent | no space | 80% |
| Short numbers | "triệu", "tỷ" in prose; source form in tables | 20 triệu lượt tải mỗi tháng |
| Date | day/month/year | 23/10/2026; tháng 10/2026 |
| Colon | no space before, one after | Các bước sau: |
| Range | "từ ... đến ...", not a dash, in prose | từ 0 đến 1 |

## 6. Pages and slides

Sentence case everywhere. On slides, a term gloss goes in the speaker notes when the line is longer than the limit. Vietnamese text is often longer than the English source: check that labels and boxes still fit. Run `tools/ste_vi_check.py` on each page or slide file (it reads .md, .txt and .html).

## 7. Report

Give the finished Vietnamese first. Add only: terms that are not in a pack, source lines whose meaning was not clear, and register choices that a person must make.
