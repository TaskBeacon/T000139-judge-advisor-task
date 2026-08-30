# Native validation

Use sibling `psyflow`, `taps-utils`, `taps` and `skills` checkouts, PsychoPy/PsyFlow installed for Python 3.10, and the task's normal dependencies. The validated native PsyFlow revision was `43e52fb`. From the workspace in PowerShell:

```powershell
$env:PYTHONIOENCODING='utf-8'
$env:PYTHONPATH="$((Get-Location).Path)/psyflow;$((Get-Location).Path)/taps-utils/src"
python T000139-judge-advisor-task/tests/test_semantics.py
```

Seven semantic tests cover actual task phases, 899 balanced participant schedules, scoring edge cases, absence of production defaults/truth displays, and actual main/BlockUnit initial-pass persistence with a mocked GUI and an injected transition interruption. The first import-path failure is preserved separately.

`gate_report.json` records all five genuine standard, QA, scripted simulation, sampler simulation and TAPS validation commands and outputs, including the exact working directories/config paths. All five passed on attempt3. Earlier count-metadata and required-key failures remain in `gate_report_attempt1.json` and `gate_report_attempt2.json`. These are validation fixtures, not research participant observations. TAPS recommendations about changelog headings and the conventional `outputs/sim` directory remain warnings; actual simulations use separate scripted/sampler directories.

With an exclusive desktop lease, `python T000139-judge-advisor-task/tests/native_visual.py` runs actual task drawing and captures its own OpenGL back buffer before the normal flip. The six PNGs were actually inspected. This verifies rendering; physical Return/IME, monitor scanout and hardware timing are not established. Failed OS capture and black front-buffer attempts are documented in `native_capture_failures.md`. Do not treat them as passes.

The configuration describes one logical block with twelve paired items and two passes, not twenty-four independent trial rows. Initial-pass CSV data are saved before the transition; the final CSV preserves each initial phase with the same helper-issued trial ID. `pair_complete` means both passes were processed, including missing-value branches, and does not imply two valid estimates. Native global timestamps have coarse resolution here; cross-pass ordering uses shared-window `flip_time` / `offset_flip_time`, not fractional differences in global time.

No primary article PDF is redistributed. See the source and materials audits for citations and the explicitly disclosed adaptations.
