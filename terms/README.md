---
title: Term packs
---

# Term packs

In short: every technical term has one Vietnamese form. Use it in all Vietnamese text. One term = one form in one file. An English term is a technical noun only: never use it as a verb or adjective in a Vietnamese sentence (STE 1.7).

| Pack | Content |
|---|---|
| [common.md](common.md) | Everyday work words (team, owner, review, deploy, use) |
| [tech.md](tech.md) | Default tech set: interface and actions, software and data, cloud and operations, security, development, product and business, AI. Mostly from the Microsoft Terminology Collection (mark M) |
| [systems.md](systems.md) | Platform and access, architecture, team models, operations and observability, AI engineering, data and statistics, licences and privacy |
| [optional/adtech.md](optional/adtech.md) | Off by default. Mobile app publishing, user acquisition, creatives, measurement, monetization, store and ad policy. Copy it to `terms/` to turn it on |
| [org-template.md](org-template.md) | Template for your organization: names, tools, local terms |

Modes:
- **keep**: write the English term as is. No italics, no quotes. Common nouns stay lower case in a sentence (creative, waterfall). For readers outside the field, an abbreviation still gets a role gloss at the first use (VI-2a): "SSO" becomes "đăng nhập một lần (SSO)".
- **keep + gloss**: write the English term. On the first use in a page or deck, add the gloss in brackets once: `creative (video, ảnh quảng cáo)`. Later uses: English only.
- **vi**: write the Vietnamese form. On the first use you can add the English in brackets once, when readers know the English better.

Sources for the Vietnamese forms: Microsoft Terminology Collection, Vietnamese (marked M), Google Vietnamese interfaces and help pages, AdMob included (marked G), Brands Vietnam (marked B), Vietnamese law texts (marked L). No mark = common Vietnamese word. Notes such as "readers take X as Y" come from blind reader tests (see [../EVALUATION.md](../EVALUATION.md)).

A term that is not in a pack: build a domain pack with the glossary step in [../SKILL.md](../SKILL.md) section 2b, or for one term, use the vendor's own Vietnamese interface or help pages; else keep English and list the term in the report. Do not coin a new Vietnamese word.

## How the checker reads packs

`tools/ste_vi_check.py` reads every `.md` file in this folder (not in `optional/`, not `org-template.md`):
- English words in table rows are allowed words (no "English word not in a pack" note).
- A line that starts with `Gloss at first use:` lists terms that need a gloss in brackets at the first use (rule VI-2a). Example: `Gloss at first use: UA, CPI, MMP`.

Remove a pack you do not need (for example adtech.md) and the checker stops reading it. To add your organization: copy [org-template.md](org-template.md) to `org.md` (or any name), fill it in, and keep it in this folder.
