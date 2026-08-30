from psyflow import StimUnit, next_trial_id, set_trial_context
from .utils import decode_plan, entry_outcome, make_advice, score_pair


def run_trial(win, kb, settings, condition, stim_bank, trigger_runtime, memory, pass_name,
              block_id='jas', block_idx=0):
    item_id, cell, distance, direction, offset = decode_plan(condition)
    item = settings.items[item_id]
    if pass_name == 'initial':
        row = dict(trial_id=next_trial_id(), block_id=block_id, block_idx=block_idx,
                   condition=condition, item_id=item_id, assigned_condition=cell,
                   distance=distance, requested_direction=direction, requested_offset=offset,
                   truth=item['truth'], material_version=settings.material_version,
                   advice_provenance=settings.advice_provenance,
                   synthetic_fixture=bool(getattr(settings, 'synthetic_fixture', False)))
    else:
        row = dict(memory[item_id])
    trial_id = row['trial_id']

    if pass_name == 'revision':
        row.update(make_advice(row['initial_value'], item['truth'], direction, offset, settings.numeric_limit))
        if row['advice_value'] is None:
            unavailable = StimUnit('unavailable', win, kb, runtime=trigger_runtime).add_stim(
                stim_bank.get_and_format('question', question=item['question'])).add_stim(stim_bank.get('unavailable'))
            set_trial_context(unavailable, trial_id=trial_id, phase='unavailable', deadline_s=settings.unavailable_duration,
                              valid_keys=[], block_id=block_id, condition_id=condition, stim_id='question+unavailable')
            unavailable.show(duration=settings.unavailable_duration, onset_trigger=settings.triggers['unavailable_onset']).to_dict(row)
            missing = entry_outcome('', False, None, settings.numeric_limit, settings.plausible_year_min, settings.plausible_year_max)
            missing['status'] = 'not_presented'
            row.update({'final_'+key: value for key, value in missing.items()})
            row.update(score_pair(row['initial_value'], None, None, item['truth']))
            row['pair_complete'] = True
            return row
        advice = StimUnit('advice', win, kb, runtime=trigger_runtime).add_stim(
            stim_bank.get_and_format('question', question=item['question'])).add_stim(
            stim_bank.get_and_format('own_estimate', initial=row['initial_value'])).add_stim(
            stim_bank.get_and_format('recommendation', advice=row['advice_value'])).add_stim(stim_bank.get('provenance'))
        set_trial_context(advice, trial_id=trial_id, phase='advice', deadline_s=settings.advice_duration, valid_keys=[],
                          block_id=block_id, condition_id=condition, stim_id='question+own_estimate+recommendation+provenance',
                          task_factors={'item_id':item_id,'advice_value':row['advice_value'],'actual_delta':row['actual_delta']})
        advice.show(duration=settings.advice_duration, onset_trigger=settings.triggers['advice_onset']).to_dict(row)

    phase = 'initial' if pass_name == 'initial' else 'final'
    duration = getattr(settings, phase+'_duration')
    fixture = getattr(settings, 'synthetic_text_by_phase_item', {}).get(phase, {}).get(item_id, '')
    editor = stim_bank.rebuild(phase+'_editor', update_cache=True, text=fixture, editable=True)
    editor.hasFocus = True
    unit = StimUnit(phase, win, kb, runtime=trigger_runtime).add_stim(
        stim_bank.get_and_format('question', question=item['question'])).add_stim(stim_bank.get(phase+'_label')).add_stim(editor).add_stim(stim_bank.get(phase+'_hint'))
    if phase == 'final':
        unit.add_stim(stim_bank.get_and_format('final_own', initial=row['initial_value'])).add_stim(
            stim_bank.get_and_format('final_advice', advice=row['advice_value'])).add_stim(stim_bank.get('final_provenance'))
    set_trial_context(unit, trial_id=trial_id, phase=phase, deadline_s=duration, valid_keys=[settings.submit_key],
                      block_id=block_id, condition_id=condition, stim_id=phase+'_entry', task_factors={'item_id':item_id,'pass_name':pass_name})
    unit.capture_response(keys=[settings.submit_key], duration=duration, terminate_on_response=True,
                          onset_trigger=settings.triggers[phase+'_onset'], response_trigger={settings.submit_key:settings.triggers[phase+'_submit']},
                          timeout_trigger=settings.triggers[phase+'_timeout'])
    editor.editable = False
    editor.hasFocus = False
    raw = str(editor.getText() or '')
    unit.set_state(response_text=raw)
    unit.to_dict(row)
    entry = entry_outcome(raw, unit.get_state('response') == settings.submit_key, unit.get_state('rt'),
                          settings.numeric_limit, settings.plausible_year_min, settings.plausible_year_max)
    row.update({phase+'_'+key:value for key,value in entry.items()})
    saved = StimUnit(phase+'_saved', win, kb, runtime=trigger_runtime).add_stim(stim_bank.get('saved'))
    set_trial_context(saved, trial_id=trial_id, phase=phase+'_saved', deadline_s=settings.saved_duration, valid_keys=[],
                      block_id=block_id, condition_id=condition, stim_id='saved')
    saved.show(duration=settings.saved_duration, onset_trigger=settings.triggers[phase+'_saved_onset']).to_dict(row)
    row['pair_complete'] = phase == 'final'
    if phase == 'initial':
        memory[item_id] = dict(row)
    else:
        row.update(score_pair(row['initial_value'], row['advice_value'], row['final_value'], item['truth']))
    return row
