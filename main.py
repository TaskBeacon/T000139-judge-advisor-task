from contextlib import nullcontext
from functools import partial
from pathlib import Path
import pandas as pd
from psychopy import core
from psyflow import (BlockUnit, StimBank, StimUnit, SubInfo, TaskSettings, context_from_config,
                     initialize_exp, initialize_triggers, load_config, parse_task_run_options, runtime_context)
from src.run_trial import run_trial
from src.utils import make_plans, validate_subject_id

MODES = ('human', 'qa', 'sim')
DEFAULT_CONFIG_BY_MODE = {'human':'config/config.yaml','qa':'config/config_qa.yaml','sim':'config/config_scripted_sim.yaml'}


def run(options):
    task_root = Path(__file__).resolve().parent
    cfg = load_config(str(options.config_path))
    ctx = context_from_config(task_dir=task_root, config=cfg, mode=options.mode) if options.mode in ('qa','sim') else None
    with runtime_context(ctx) if ctx else nullcontext():
        subject = {'subject_id':139} if ctx else SubInfo(cfg['subform_config']).collect()
        settings = TaskSettings.from_dict(cfg['task_config'])
        subject['subject_id'] = validate_subject_id(subject['subject_id'])
        settings.add_subinfo(subject)
        if ctx:
            ctx.output_dir.mkdir(parents=True, exist_ok=True)
            settings.save_path = str(ctx.output_dir)
            settings.res_file = str(ctx.output_dir / ('qa_trace.csv' if options.mode == 'qa' else 'sim_trace.csv'))
            settings.log_file = str(ctx.output_dir / 'psychopy.log')
            settings.json_file = str(ctx.output_dir / 'settings.json')
        else:
            # Human startup cannot activate synthetic prefilled validation data.
            settings.synthetic_fixture = False
            settings.synthetic_text_by_phase_item = {}
        settings.triggers = cfg['trigger_config']
        trigger_runtime = initialize_triggers(mock=True) if ctx else initialize_triggers(cfg)
        win, kb = initialize_exp(settings)
        stim_bank = StimBank(win, cfg['stim_config']).preload_all()
        for name in ('initial_editor','final_editor'):
            stim_bank.get(name).editable = False
        memory = {}
        initial_block = BlockUnit('jas', 0, settings, window=win, keyboard=kb,
                                  seed=int(settings.overall_seed)+subject['subject_id'], n_trials=int(settings.total_trials))
        initial_block.generate_conditions(func=make_plans, condition_labels=settings.conditions,
                                          item_ids=settings.item_ids, offsets=settings.distance_offsets)
        settings.assigned_plans = list(initial_block.conditions)
        settings.save_to_json()
        trigger_runtime.send(settings.triggers['experiment_start'])
        StimUnit('instruction',win,kb,runtime=trigger_runtime).add_stim(stim_bank.get('instruction')).wait_and_continue(keys=[settings.continue_key])
        initial_block.run_trial(partial(run_trial, stim_bank=stim_bank, trigger_runtime=trigger_runtime,
                                        memory=memory, pass_name='initial'))
        initial_rows = []
        initial_block.to_dict(initial_rows)
        output = Path(settings.res_file)
        output.parent.mkdir(parents=True, exist_ok=True)
        # A durable pass1 file survives interruption before/during the advice pass.
        pd.DataFrame(initial_rows).to_csv(output.with_name(output.stem+'_initial_pass.csv'), index=False)
        StimUnit('transition',win,kb,runtime=trigger_runtime).add_stim(stim_bank.get('transition')).wait_and_continue(keys=[settings.continue_key])
        revision_block = BlockUnit('jas', 0, settings, window=win, keyboard=kb,
                                   seed=int(settings.overall_seed)+subject['subject_id'], n_trials=int(settings.total_trials))
        revision_block.add_condition(list(initial_block.conditions))
        revision_block.run_trial(partial(run_trial, stim_bank=stim_bank, trigger_runtime=trigger_runtime,
                                         memory=memory, pass_name='revision'))
        rows = []
        revision_block.to_dict(rows)
        pd.DataFrame(rows).to_csv(output, index=False)
        StimUnit('good_bye',win,kb,runtime=trigger_runtime).add_stim(stim_bank.get('good_bye')).wait_and_continue(keys=[settings.continue_key])
        trigger_runtime.send(settings.triggers['experiment_end'])
        trigger_runtime.close()
        win.close()
        core.quit()


def main():
    run(parse_task_run_options(task_root=Path(__file__).resolve().parent, description='Judge–Advisor System',
                               default_config_by_mode=DEFAULT_CONFIG_BY_MODE, modes=MODES))


if __name__ == '__main__':
    main()
