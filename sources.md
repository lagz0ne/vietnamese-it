# Options compared (2026-10-23)

In short: no skill does English to Vietnamese with a company term base. vietnamizer is the strongest Vietnamese editor, so this skill includes it (MIT) and adds a layer on top: STE-VI register, term packs, translation steps and a checker.

| Option | What it does | Translates EN to VI | Business register | License | Use |
|---|---|---|---|---|---|
| [fioenix/vietnamizer](https://github.com/fioenix/vietnamizer) v0.10.6 | Editor: 25 calque and grammar patterns, 6 typography rules, enterprise profile, each rule with "do not flag" cases | No (edits the result) | Yes, profile ky-thuat-doanh-nghiep | MIT | Copied to vendor/vietnamizer as the edit pass |
| [hungv47 polish-vietnamese](https://github.com/hungv47/meta-skills/blob/HEAD/skills/polish-vietnamese/SKILL.md) | Short rules: language contract, rebuild noun stacks, translate the job not the sentence | Yes, light | Marketing | MIT | Idea for step 1 (contract) |
| [namdangntd-sys/viet-dieuchinh-vanphong](https://github.com/namdangntd-sys/viet-dieuchinh-vanphong) | SEONGON house style: 5 tones, pronoun table, 16 friction rules | No | Agency, client facing | MIT | Not used: asks 2 questions every run; agency voice |
| [AnhTuan2111/vina-me](https://github.com/AnhTuan2111/vina-me) | Natural prose, structure, explaining | No | General | MIT | Not used: overlaps vietnamizer |
| [Seastorm136/vietnamese-human-writing-skill](https://github.com/Seastorm136/vietnamese-human-writing-skill) | 53 rules, 7 revision passes | No | Prose, fiction | MIT | Not used: prose focus |
| [vophuthinh/natural-writing](https://github.com/vophuthinh/natural-writing) | Anti chatbot patterns, VI and EN | No | General | MIT | Not used |
| translate epub (Anthropic directory plugin) | Books into literary Vietnamese | Yes | Literary | Directory | Not used: books only |
| [Microsoft vi-VN style guide](https://download.microsoft.com/download/b/f/e/bfecb1b4-21ab-48fd-a48c-c2471b026f8f/vie-vnm-StyleGuide.pdf) | Modern plain voice, no word-for-word, case, numbers, punctuation | Rules | Plain, modern | Reference | Register, case and number rules |
| [Google AdMob Vietnamese help](https://support.google.com/admob/answer/3245073?hl=vi) | Official Vietnamese adtech names (dàn xếp, quảng cáo xen kẽ, đơn vị quảng cáo) | Terms | UI | Reference | Source for term packs (G) |
| [CNCF glossary, Vietnamese](https://www.cncf.io/blog/2025/06/26/cloud-native-glossary-the-vietnamese-version-is-live/) | Lesson: keep English with explanation when no stable Vietnamese term; a style guide and term base from the start | Lesson | Technical | Reference | Basis for keep + gloss mode |

Other references used in the rules: ASD-STE100 Issue 9 (2025), RFC 2119, Mona Baker *In Other Words* (1992, 2018), Vinay and Darbelnet (1958), interpretive theory of translation (Seleskovitch and Lederer), Cao Xuân Hạo *Tiếng Việt: sơ thảo ngữ pháp chức năng* (1991), and the Vietnamese papers named in [ste-vi.md](ste-vi.md) sections 2e and 2f. ASD-STE100 is a trademark of ASD; this skill paraphrases rule titles and does not copy the specification.
