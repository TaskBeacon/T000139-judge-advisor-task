# Task Logic Audit — T000139

Created before task implementation, 2026-08-31. Primary-source-first mode.

## 1. Paradigm Intent

Judge–Advisor System, a **disclosed mechanical-advice adaptation**, measures numerical revision after independent estimation. Y2004 is Yaniv (2004), DOI 10.1016/j.obhdp.2003.08.002. The author manuscript is at https://ratio.huji.ac.il/files/dp405.pdf (cover dated 2005; article identifies the 2004 publication). Methods were read directly, especially manuscript pp. 5–6 and 10–11, PDF pages 6–7 and 11–12. No task code existed when this audit was written.

Evidence summary: Yaniv collected all initial date estimates before repeating the questions with advice and final estimates. Study 3 generated advice by altering the initial estimate. Near offsets were 15/18/20 years, intermediate 40/43/45, far70/72/75. Twenty-four questions were assigned equally across distances; at each distance half the advice pointed toward truth and half away. There was no online accuracy feedback. Study 1’s displayed procedure showed the prior estimate beside advice. The published absolute-change advice ratio describes between-estimate revisions; this implementation separately preserves a signed ratio for every eligible revision.

Sniezek & Buckley (1995), DOI 10.1006/obhd.1995.1040, publisher abstract, supports the earlier independent-judge-before-advice boundary. Its two-advisor binary choices are not used as the numerical protocol. Full 1995 methods were not accessible and are not claimed reconstructed.

Scientific boundary: no ecological peer pool is available. Computer generation is truthfully disclosed before participation and on advice screens; no invented humans, initials, expertise, accuracy guarantees or reliability manipulation. This is not a validated measure of trust in human advisers, a clinical instrument, or an exact replication. Newly authored Chinese questions require empirical piloting before inferential use. No accuracy benefit is promised.

## 2. Block/Trial Workflow

### Block Structure

One session has two passes over 12 distinct questions; all 12 independent responses finish before **any** advice. Each question has one paired logical trial ID allocated by `next_trial_id()` during its initial pass, then reused when revisited. Same item order in both passes. One instruction screen, initial pass, a transition instruction, revision pass, goodbye. No practice or unrelated task phases.

Conditions are `near_toward`, `near_away`, `intermediate_toward`, `intermediate_away`, `far_toward`, `far_away`, two items each. The condition schedule is generated before initial responses: shuffle item IDs and a balanced condition list with Python `random.Random(overall_seed+subject_id)`, sample one offset from the corresponding configured list, then serialize each plan as `item_id|condition|offset`. A custom generator called through `BlockUnit.generate_conditions` is required for unique-item assignment and cross-pass replay. Core factors never randomly change inside `run_trial`. `condition_weights:null`: exact equal cell counts are enforced by the generator, not weight approximation. QA/sim use 6 distinct questions, one per cell, with shorter explicitly synthetic timing.

### Trial State Machine

Initial pass: `initial` displays question, blank editor, initial-estimate label; Return submits, deadline 45 s. Valid signed integer -> retain estimate; blank/invalid submitted text -> retain raw text and invalid status; timeout -> retain draft but **no** estimate. `initial_saved` neutral recording notice 0.3 s.

After all initial responses, transition instruction states that the same questions will now have computer-generated advice.

Revision pass: valid initial with safe computed advice -> `advice` 3 s displays original question, own initial estimate, advice, and honest provenance; `final` displays the same question/initial/advice with a new blank editor and 45 s Return submission window. The participant may retain, move toward, pass beyond or move away from advice. No prefilled final answer. `final_saved` neutral notice 0.3 s. Invalid/missing initial or unsafe arithmetic -> `unavailable` 1 s with question and notice, no advice or final capture; final record remains missing with explicit reason. No substitute initial, truth display, correctness feedback or reward.

## 3. Condition Semantics

Each distance condition chooses a constant from its cited set; internal labels are never shown. `toward` signs the offset toward the true year, `away` reverses it. If initial equals truth, assign positive offset to `toward` and negative to `away`, flag `initial_equals_truth`, and label realized direction `from_truth_tie`; do not claim either is helpful. A toward offset can overshoot and worsen accuracy: export **actual** advice accuracy gain separately from geometric direction. Offset is never clipped; requested and actual signed deltas are retained. If addition exceeds the common ±1000000000 input domain, skip advice with an arithmetic-status flag.

All participant text, question wording and reference years are config-defined. Original factual materials and official verification links are listed in `materials.md`; none are borrowed copyrighted question wording. No images/audio are required. Chinese uses SimHei and explicit line breaks where needed. The runtime accesses truth for condition realization and offline scoring only, not as a visible stimulus.

## 4. Response and Scoring Rules

Config keys: `submit_key:return`, `continue_key:space`. Browser event normalization yields raw `enter`; the derived H must explicitly recognize that alias while preserving the raw key. Integers use optional ASCII sign and digits only, absolute value at most 1000000000. Negative or implausible years remain measured responses, with `plausible_year` reported separately (1000–2026), never clamped. Blank, malformed, noninteger, overflow and timeout statuses are distinct. Validation does not teach a likely year range.

For valid submitted initial I, advice A, and valid submitted final F: signed revision F−I; absolute revision |F−I|; signed advice distance A−I; absolute advice distance |A−I|; signed weight `(F-I)/(A-I)`; self weight `1-WOA`; absolute revision ratio `abs(F-I)/abs(A-I)` (separately named). A=I -> weights null, reason `zero_advice_distance`; do not fabricate 0. Negative and >1 weights retained. Export initial/final/advice absolute errors to truth and accuracy gain `abs(I-truth)-abs(F-truth)` (positive=improvement). `primary_eligible` requires all three values and nonzero advice distance. Raw values and validity statuses always retained. Missing final does not default to the initial. No controller adapts task difficulty or rewards.

## 5. Stimulus Layout Plan

1280×800 window, white background, black SimHei. Question centered at (0,245), height 28, wrap 1100. Initial label(0,115), editor(0,15),650×75, letterHeight 30; hint(0,-90),height 20. Advice screen: own estimate(0,135), recommendation(0,45), provenance(0,-95),height 22; question stays at 245. Final screen: own estimate(0,155), recommendation(0,85), provenance(0,20), final label(0,-55), editor(0,-125),650×65; hint(0,-210). Rebuild blank textbox each capture and disable afterward. No simultaneous elements share anchors. Instructions use manually separated short lines height 25/wrap 1100. Native client screenshots and actual browser views must be inspected.

## 6. Trigger Plan

Experiment 1/99; initial onset 10, submit 11, timeout 19; initial_saved 20; advice 30; final onset 40, submit 41, timeout 49; final_saved 50; unavailable 60. Standard StimUnit APIs emit onset/response/timeout; mock behavioral driver by default. Timeout means no registered submit response, not malformed submitted content. These are software events, not verified hardware timing.

## 7. Architecture Decisions (Auditability)

`main.py` visibly orchestrates initial block, transition, revision block and persistence. Task-specific memory maps item IDs to their initial result dictionaries; it does not own trial IDs, input loops, timestamps or file formats. Initial rows use `StimUnit.to_dict` and are saved after pass 1 for interruption safety. Final rows merge those unchanged phase fields with advice/final phases; one item per final reduced row. Block metadata and pass markers remain explicit. Missing initial items still receive a final paired row.

The H will use two compiled segments sharing a `next_trial_id` ID per item. Initial segment is excluded from reduced output; shared ExecutionRecorder retains its initial unit state and raw rows. Revision segment adds distinct phase labels and finalizes exactly once into reduced output, including the initial phase columns. No framework patch or private access needed. Shared raw export groups by logical ID, **not** chronological execution: verify timing order with monotonic onsets, not line order. All initial onsets/closings must precede first advice onset. Helpers in `utils` only handle deterministic item plans, integer validation, advice arithmetic and scoring. No generic manager or copied unrelated trial logic.

## 8. Inference Log

Adaptations: 12 new questions instead of 24; Chinese; honest computer provenance instead of the original cover story; no bonus, confidence interval or clinical label; 45 s response deadlines; 3 s advice-only viewing; neutral recording screens; same replay order; software trigger numbers/layout; explicit missing-value branches; a shared ±1000000000 input domain (all subtraction/error intermediates bounded by 4000000000, safely exact in both runtimes); plausibility flag; tie rule; signed WOA extension. These are engineering decisions, not literature parameters. Mechanical offset sets and two-pass structure are source-based. Half toward/away assignments are preplanned, with ties and overshoot transparently reported. All artifacts require actual runtime validation before publication.
