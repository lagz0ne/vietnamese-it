---
name: vietnamese-it
description: Write formal Vietnamese, or translate English to Vietnamese, for IT and digital business text (pages, slides, specs, reports, procedures, UI). Uses STE-VI (ASD-STE100 rules adapted to Vietnamese), term packs, a vietnamizer edit pass and a checker script. Use for any Vietnamese output in a technical or business context.
---

# Vietnamese for IT

In short: write from the meaning, not word by word. Follow the STE-VI rules in [ste-vi.md](ste-vi.md): formal written Vietnamese, short sentences, active voice, no spoken words, English terms only as nouns. Use the term packs in [terms/](terms/README.md) for every technical term. Then do one edit pass with the vietnamizer patterns and run the checker until it prints OK.

Files:
- [ste-vi.md](ste-vi.md): ASD-STE100 rules mapped to Vietnamese (keep, adapt, drop), must and default levels, rules VI-1 to VI-5, words to avoid, length limits.
- [terms/](terms/README.md): term packs. `common.md` (work words), `it.md` (software, platform, operations, data), `adtech.md` (mobile apps and advertising). Add your own names in a copy of `org-template.md`.
- [tools/ste_vi_check.py](tools/ste_vi_check.py): checker. Must rules: 0 findings. Default rules: at least 80% of sentences pass.
- [examples.md](examples.md): before and after pairs for each rule group.
- [EVALUATION.md](EVALUATION.md): how the rules were tested (blind readers, blind judge) and the results.
- [vendor/vietnamizer/](vendor/vietnamizer/SKILL.md): Vietnamese editor skill (fioenix/vietnamizer, MIT). Patterns V1 to V25, T1 to T6, profile K1 to K7.
- [sources.md](sources.md): what was compared and why.

## 1. Set the language contract

Do this before you write. Use these defaults unless the user or an organization pack sets others. Do not ask the user again.

| Item | Default |
|---|---|
| Reader | Native Vietnamese readers in IT and digital business: managers, engineers, operations staff. They read common English IT terms every day. |
| Register | Formal written Vietnamese (STE-VI): objective, exact, no spoken words (cái gì, thấy, xài, chốt), no particles (nhé, ạ, đấy), no metaphors, no emotive words, no institutional clichés (đóng vai trò quan trọng, góp phần nâng cao). Full rules: [ste-vi.md](ste-vi.md). |
| Pronouns | No first person. The subject is the organization, team, system or role ("Nhóm vận hành", "Hệ thống thanh toán", "Người phụ trách"). Procedures start with the verb. Never "tôi", "mình" (as "I/we"), "bên em", "quý vị". |
| Spelling | One tone-mark style per file. Default new style: hóa, tùy, thủy, khỏe. |
| Customer text | Documents for customers (release notes, guides) use the same register. Interface strings follow the product's existing voice. |
| Case | Sentence case for titles, labels, buttons. Capital letters only for the first word, proper names and product names. Never English title case. |

## 2. Terms

Apply in this order:
1. Names of the organization, products, tools and vendors: keep as is. Put them in your organization pack (copy of [terms/org-template.md](terms/org-template.md)).
2. A term in a term pack: use its form and mode. The gloss goes in brackets only at the first use in a page or deck.
3. A term not in a pack: use the Vietnamese name from the vendor's own Vietnamese interface or help pages (for example Google, Microsoft), if one exists. Else keep English. List the new term in the report (section 7) so the user can add it to a pack.
4. Do not coin a new Vietnamese word. Do not translate an English image (paved road, crown jewels, strangler fig): write the meaning or keep the English term with a gloss.
5. One term = one form in one file. Do not change a term to avoid repetition.
6. A gloss only explains a word. When a pack gloss holds more than the source says, the source wins: cut the gloss to what the source says.
7. A vague actor in the source ("the team"): name the team only when the same text or the organization pack names it; else keep "nhóm" and do not guess.

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
   - 5b. Run `python3 -I tools/ste_vi_check.py <file> [--org "Tên tổ chức"] [--tech]` (`--tech` allows code and paths in text for technical readers). Fix every must finding. If default pass is under 80%, fix the worst sentences. When vietnamizer and a default rule disagree, keep the natural sentence and note the exception.
6. Back-check: read only the Vietnamese. Write its meaning in one English line. Compare with the line from step 1. If they differ, fix the Vietnamese.

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
