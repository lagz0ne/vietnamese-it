---
title: Evaluation
---

# Evaluation

In short: each rule group was added for a problem that a native reader found, then tested with isolated agents and the checker. The test texts were internal business documents and are not in this repository. This file gives the method and the numbers, so you can repeat the tests on your own texts.

## Method

| Test | How | Pass mark |
|---|---|---|
| Checker | `tools/ste_vi_check.py` on the Vietnamese file | 0 must findings; default rules hold for at least 80% of sentences |
| Independent readers | Two isolated agents read only the Vietnamese, one sentence at a time, and write what each sentence means. Personas: a senior manager outside IT; an operations employee with 2 months in the job. Each sentence gets "Có" (clear), "Một phần" (partly clear) or "Không" (not clear) | No "Không"; at least 90% "Có"; every paraphrase matches the source meaning |
| Blind judge | Two isolated writers translate the same English: one with the skill before the new rule (snapshot), one with the new rule. A third agent (native senior editor persona) sees the English and the two versions as X and Y in random order, picks the more natural one and checks that strength and meaning did not change. A key file maps X and Y after judging | The new rule wins more items than it loses; no new strength or meaning change |
| Native review | A native speaker marks each example pair "Đạt" or "Chưa đạt" with a note | Every "Chưa đạt" note becomes a rule, a term or a checker change |

Rules for a fair test:
- Writers read only the skill files and the source. They never see earlier translations of the same text.
- Rule examples must not come from the test set. One test lost an item for this reason (see round 6).
- The checker cannot see English sentence frames. "Sounds translated" needs the judge or a native reader.

## Results

| Round | Problem found by a native reader | Rule | Result |
|---|---|---|---|
| 1 | Register too casual; some terms not fit for written text | STE-VI (ASD-STE100 mapped to Vietnamese) | Old text: 5 must findings, default pass 73%. New text: 0 must findings, default pass 100%. Formal register is longer: 1,82 âm tiết per English word (casual: 1,52) |
| 2 | English states scope that Vietnamese context already gives | VI-1 | Redundancy findings from 11 to 1; slide lines 10% shorter |
| 3 | Some sentences could not be understood | VI-2 and the reader test | Manager "Có" from 16 of 26 to 35 of 39 (90%); new staff from 14 of 26 to 29 of 39 (74%); "Không" from 1 to 0 |
| 4 | No Vietnamese word for an English word; the English frame stays | VI-3 (meaning first, then merge) | Judge: new 5, old 3, tie 1. "Sounds translated" spans in prose from 12 to 4, but in a technical list from 2 to 8 without the merge step (now VI-3f) |
| 5 | Orders copied from English forms | VI-4 (strength ladder) | Judge on 22 instructions: new 12, old 6, tie 4. Strength changed: 1 and 1 |
| 6 | Grammar that differs (passive, tense, negation, connectives) | VI-5 | Judge on 22 sentences: new 10, old 5, tie 7 (without the item that leaked into an example: new 9, old 5). "Sounds translated" items from 10 to 6 |
| 7 | Full skill description written in Vietnamese with these rules | All | Manager "Có" 81 of 84 (96%); new staff 78 of 84 (93%), after 2 passes |
| 8 | Native review of 22 example pairs | VI-2f, VI-3g, VI-3h, VI-4j, VI-5j, VI-5k; ladder words | 17 marked: 11 "Đạt", 6 "Chưa đạt". All 6 notes became rule changes |

## What the native review changed

| Note | Change |
|---|---|
| "dùng" is a little casual; "sử dụng chung" is better | VI-5k: "sử dụng" is the verb for "use"; "dùng" only in "người dùng" |
| Move the place adverbial to the end | VI-3g |
| "cần có" is more usual than "phải" for things a project must have | Ladder: phải (do), cần có (have) |
| "nên" or "được khuyến khích" by register; "không khuyến khích" by degree | Ladder: nên / được khuyến khích; không khuyến khích, không nên, tránh |
| Rearrange, even split the sentence | VI-3h: one main action per sentence |
| "Highest" what? Do not say the measure twice | VI-2f |
| Cause and sequence wrong in a ban | VI-4j: no "Không ... để" |
| Repeated "thì" does not flow | VI-5j |

## Limits

- Readers and judges are agent personas, not a panel of people. The native review is one person.
- Samples are small (22 to 84 items per test). Read the numbers as direction, not as proof.
- Length limits (30 and 38 âm tiết) come from ASD-STE100 word limits and one measured ratio. Tune them on your own texts.
- Business and adtech texts were the test sources. Other fields need their own term pack and a new reader test.
