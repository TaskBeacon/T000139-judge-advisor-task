# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| passes | task.passes | 2 passes of paired items | Y2004 | Methods, manuscript pp. 5–6,10 | source-based | all initials precede any advice |
| distance_sets | task.distance_offsets | near 15/18/20; intermediate 40/43/45; far 70/72/75 years | Y2004 | Study 3 Method, pp. 10–11 | exact | offset chosen during seeded schedule |
| direction | task.conditions | toward/away, half each per distance | Y2004 | Study 3 Results, p. 11 | source-based | tie at truth flagged; toward does not guarantee lower error |
| count | task.total_trials | 12 paired items | Y2004 | original 24 items | inferred | new original materials; 6 QA/sim |
| deadlines | timing.initial_duration; timing.final_duration | 45 s each | Y2004 | numerical entry; deadlines unreported | inferred | drafts preserved but not submitted |
| advice_view | timing.advice_duration | 3 s | Y2004 | advice before revision | inferred | advice remains visible during final |
| neutral | timing.saved_duration; timing.unavailable_duration | 0.3 s; 1 s | Y2004 | no accuracy feedback | inferred | only completion/missing notices |
| numeric_domain | task.numeric_limit | ±1000000000 | Y2004 | numerical estimates | inferred | integer domain; every intermediate remains safe integer; no clipping |
| locale | task.language; stimuli.*.font | Chinese; SimHei | Y2004 | English-source adaptation | inferred | explicit line breaks / actual visual check |
| provenance | stimuli.provenance | disclosed computer generation | Y2004 | Study 3 mechanical advice | adaptation | not other participants, no accuracy guarantee |
| reward | task | none | Y2004 | original performance bonus | adaptation | no incentive or benefit claim |
| data | task | signed WOA plus separate absolute ratio | Y2004 | advice-weight analysis | adaptation | negative/>1 retained; zero denominator null |
| seed | task.overall_seed | 139031 + subject ID | Y2004 | random condition assignment | inferred | shared PythonRandom parity |

No reference establishes psychometric properties for these new questions or deadlines.
