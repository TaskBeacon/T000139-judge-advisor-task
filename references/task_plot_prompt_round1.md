Use case: infographic-diagram
Asset type: TaskBeacon task flow diagram
Primary request: Create a clean, publication-ready task flow diagram as a timeline collection for the behavioral task described below.

Task: Judge–Advisor System
Construct: numerical advice weighting
Rows/conditions:
- Pass 1: independent estimates, all 12 items before any advice
- Pass 2: advice and final estimates, same 12 items in the same order; three distance levels use the same sequence
Collapse equivalent conditions into representative rows and show variants as small parenthetical notes in the row label.

Timeline phases:
- Pass 1: Initial estimate (45 s max; Return; gray screen showing “弗莱明首次发现青霉素的抗菌作用是哪一年？” and a visibly EMPTY white input field) -> Recorded (0.3 s; gray screen showing “回答已记录。”) -> Next initial (45 s max; Return; gray screen showing “巴拿马运河正式通航是哪一年？” and a visibly EMPTY white input field). Note beneath row: “Repeat for all 12 items — no advice yet”.
- Pass 2: Advice (3 s; gray screen showing “青霉素发现年份？” followed by “你的原估计：1900 年” and “电脑生成的建议：1915 年”, and small “非他人回答；不保证准确”) -> Final estimate (45 s max; Return; gray screen showing “青霉素发现年份？”, same own1900/advice1915, a visibly EMPTY white input field, and “最终估计”) -> Recorded (0.3 s; gray screen showing “回答已记录。”). Note beneath row: “Repeat the same 12 items in the same order”.

Visual requirements:
- White background, landscape orientation, crisp dark text, restrained condition accent colors.
- One horizontal row per representative pass, exactly two rows. Three participant-screen snapshots per row, connected left-to-right by thin arrows.
- A highly visible separator between rows says “Complete ALL initial estimates before ANY advice”.
- Each screen snapshot shows visible stimulus or neutral notice, not internal variable names.
- Use gray participant-screen boxes, thin black arrows, consistent row spacing, and subtle row separators.
- Place timing labels under each screen in compact text. Put Return under the input screens only.
- Place Pass 1 and Pass 2 labels at the left of each row. Keep short labels and all text legible at normal document preview size.
- Leave a clean blank header band across the top18% of the image for later fixed title/subtitle/logo. Draw no text in that band.
- Small compact footer below both rows: “Offsets (years): Near 15/18/20 · Intermediate 40/43/45 · Far 70/72/75” and next line “Half toward / half away; one condition per item. Missing initial: no advice or final entry (1 s notice).”

Accuracy constraints:
- Initial textboxes and final textbox MUST BE EMPTY, with no numeric default or placeholder. 1900 is only shown as an example of a submitted prior estimate during Pass 2.
- Never show true answer1928, scores, rewards, correct/incorrect feedback, fake human names or reliability guarantees.
- The1915advice is a computer-generated example and may be wrong. Preserve explicit source disclaimer.
- Do not invent phases, stimuli, condition names, keys, rewards, or timings.
- Do not add people, lab equipment, decorative scenes, logos, or unrelated icons.
- Do not draw the task title, construct subtitle, any logo, watermark, brand mark, or TaskBeacon text inside the generated image.
- Draw only timeline content below the blank header band. If a detail is unknown, omit it rather than guessing.
- Preserve exact terms: Pass 1, Pass 2, 45 s max, 3 s, 0.3 s, Return, 1900, 1915.

Style:
TaskBeacon scientific infographic style: clean vector-like raster image, organized spacing, gray screen boxes, restrained color accents, and a blank header-safe area.
