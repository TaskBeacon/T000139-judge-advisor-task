import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import yaml

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from psyflow import load_config, TaskSettings, BlockUnit
from src.utils import make_plans, decode_plan, entry_outcome, make_advice, score_pair, validate_subject_id
import src.run_trial as trial_module
import main as task_main

CFG=yaml.safe_load((ROOT/'config/config.yaml').read_text(encoding='utf8'))


class Editor:
    editable=False
    hasFocus=False
    def getText(self):return self.text


class Bank:
    text_by_phase={}
    def __init__(self,*args):pass
    def preload_all(self):return self
    def get(self,*args):return Editor()
    def get_and_format(self,*args,**kwargs):return kwargs
    def rebuild(self,name,**kwargs):
        e=Editor();e.text=self.text_by_phase.get(name.replace('_editor',''),'');return e


class Unit:
    responses={}
    phases=[]
    stop_at_transition=False
    def __init__(self,label,*args,**kwargs):self.label=label;self.state={};self.phases.append(label)
    def add_stim(self,*args):return self
    def show(self,**kwargs):self.set_state(onset_time=1.5);return self
    def capture_response(self,**kwargs):
        response=self.responses.get(self.label,kwargs['keys'][0])
        self.set_state(response=response,rt=.25 if response else None,onset_time=1.0)
        return self
    def wait_and_continue(self,**kwargs):
        if self.label=='transition' and self.stop_at_transition:raise InterruptedError('synthetic pass1 boundary interruption')
        return self
    def get_state(self,key):return self.state.get(self.label+'_'+key)
    def set_state(self,**kwargs):self.state.update({self.label+'_'+k:v for k,v in kwargs.items()});return self
    def to_dict(self,row):row.update(self.state);return self


class Tests(unittest.TestCase):
    def setUp(self):
        cfg=load_config(str(ROOT/'config/config.yaml'))
        self.settings=TaskSettings.from_dict(cfg['task_config']);self.settings.add_subinfo({'subject_id':139});self.settings.triggers=cfg['trigger_config']
        Unit.responses={};Unit.phases=[];Unit.stop_at_transition=False

    def test_signed_weights_missing_zero_and_overshoot(self):
        for initial,advice,final,truth,weight,gain in [(1900,1920,1910,1914,.5,10),(1900,1920,1890,1914,-.5,-10),
                (1900,1920,1940,1914,2,-12),(0,20,0,10,0,0),(1900,1880,1890,1889,.5,10)]:
            result=score_pair(initial,advice,final,truth)
            self.assertEqual(result['weight_of_advice'],weight);self.assertEqual(result['accuracy_gain'],gain)
        self.assertIsNone(score_pair(1900,1900,1910,1914)['weight_of_advice'])
        self.assertEqual(score_pair(1900,1900,1910,1914)['weight_status'],'zero_advice_distance')
        self.assertFalse(score_pair(1900,1920,None,1914)['primary_eligible'])

    def test_input_values_drafts_and_bounds(self):
        for text,value in [('0',0),('-1',-1),('+1900',1900),(' 1900 ',1900),('0'*5000+'1900',1900)]:
            out=entry_outcome(text,True,.1,10**9,1000,2026);self.assertEqual(out['value'],value)
        for raw,status in [('', 'blank'),('19.5','invalid_format'),('1e3','invalid_format'),('NaN','invalid_format'),('1,900','invalid_format'),('1000000001','out_of_range')]:
            self.assertEqual(entry_outcome(raw,True,.1,10**9,1000,2026)['status'],status)
        result=entry_outcome('1914',False,None,10**9,1000,2026)
        self.assertEqual(result['draft_value'],1914);self.assertIsNone(result['value']);self.assertEqual(result['status'],'timeout')

    def test_mechanical_advice_ties_overshoot_and_bounds(self):
        self.assertEqual(make_advice(1900,1914,'toward',40,10**9)['advice_accuracy_gain'],-12)
        self.assertEqual(make_advice(1914,1914,'toward',15,10**9)['realized_direction'],'from_truth_tie')
        self.assertEqual(make_advice(1914,1914,'away',15,10**9)['advice_value'],1899)
        self.assertEqual(make_advice(10**9,1914,'away',75,10**9)['advice_status'],'advice_out_of_range')
        self.assertIsNone(make_advice(None,1914,'toward',20,10**9)['advice_value'])

    def test_all_subject_balanced_unique_plans(self):
        s=self.settings
        for sid in range(101,1000):
            plans=make_plans(12,s.conditions,s.item_ids,s.distance_offsets,s.overall_seed+sid)
            self.assertEqual(len({decode_plan(p)[0] for p in plans}),12)
            for cell in s.conditions:self.assertEqual(sum(decode_plan(p)[1]==cell for p in plans),2)
            for p in plans:self.assertIn(decode_plan(p)[4],s.distance_offsets[decode_plan(p)[2]])
        for value in [None,True,100,1000,'101.0',' 101',101.5]:
            with self.assertRaises(ValueError):validate_subject_id(value)
        cases=[dict(subject_id=sid,plans=make_plans(12,s.conditions,s.item_ids,s.distance_offsets,s.overall_seed+sid)) for sid in [101,102,139,999]]
        (ROOT/'references/validation/python_schedule.json').write_text(json.dumps(cases,indent=2),encoding='utf8')

    def test_actual_run_trial_two_pass_branches(self):
        cases=[('1900','1910',{},True,'valid'),('0','10',{},True,'valid'),('bad','1910',{},False,'not_presented'),
               ('1900','1910',{'initial':None},False,'not_presented'),('1900','1910',{'final':None},False,'timeout'),
               ('1900','bad',{},False,'invalid_format'),('1000000000','1910',{},False,'not_presented')]
        outcomes=[]
        for raw_initial,raw_final,responses,eligible,status in cases:
            Unit.phases=[];Unit.responses=responses;Bank.text_by_phase={'initial':raw_initial,'final':raw_final};memory={}
            with patch.object(trial_module,'StimUnit',Unit),patch.object(trial_module,'set_trial_context'),patch.object(trial_module,'next_trial_id',return_value=77):
                initial=trial_module.run_trial(None,None,self.settings,'panama|near_away|20',Bank(),None,memory,'initial')
                initial_copy=dict(initial)
                final=trial_module.run_trial(None,None,self.settings,'panama|near_away|20',Bank(),None,memory,'revision')
            self.assertEqual(final['trial_id'],77);self.assertEqual(final['primary_eligible'],eligible);self.assertEqual(final['final_status'],status)
            for key,value in initial_copy.items():
                if key.startswith('initial_'):self.assertEqual(final[key],value)
            self.assertEqual(initial,initial_copy);self.assertTrue(final['pair_complete'])
            self.assertEqual('advice' in Unit.phases,initial['initial_valid'] and raw_initial!='1000000000')
            outcomes.append(dict(raw_initial=raw_initial,raw_final=raw_final,responses=responses,outcome=final))
        (ROOT/'references/validation/python_trial_cases.json').write_text(json.dumps(outcomes,indent=2),encoding='utf8')

    def test_human_startup_and_pass1_interruption_persistence(self):
        # Real main and BlockUnit; only GUI/trigger/input surfaces replaced. No physical-human claim.
        cfg=load_config(str(ROOT/'config/config.yaml'))
        with tempfile.TemporaryDirectory(prefix='jas139_') as output:
            cfg['task_config']['save_path']=output
            cfg['task_config']['synthetic_fixture']=True
            cfg['task_config']['synthetic_text_by_phase_item']={'initial':{'panama':'9999'}}
            Unit.stop_at_transition=True;Bank.text_by_phase={'initial':'1900'}
            fake_trigger=SimpleNamespace(send=lambda *a:None,close=lambda:None)
            fake_window=SimpleNamespace(close=lambda:None)
            seen=[]
            def initialize(settings):seen.append(settings);return fake_window,None
            with (patch.object(task_main,'load_config',return_value=cfg),patch.object(task_main,'SubInfo') as sub,
                 patch.object(task_main,'initialize_exp',side_effect=initialize),patch.object(task_main,'initialize_triggers',return_value=fake_trigger),
                 patch.object(task_main,'StimBank',Bank),patch.object(task_main,'StimUnit',Unit),patch.object(trial_module,'StimUnit',Unit),patch.object(trial_module,'set_trial_context')):
                sub.return_value.collect.return_value={'subject_id':139}
                with self.assertRaises(InterruptedError):task_main.run(SimpleNamespace(config_path=ROOT/'config/config.yaml',mode='human'))
            self.assertFalse(seen[0].synthetic_fixture);self.assertEqual(seen[0].synthetic_text_by_phase_item,{})
            files=list(Path(output).glob('*_initial_pass.csv'));self.assertEqual(len(files),1)
            import pandas as pd
            rows=pd.read_csv(files[0]);self.assertEqual(len(rows),12);self.assertEqual(rows.trial_id.nunique(),12)
            self.assertTrue((rows.initial_value==1900).all());self.assertFalse(rows.pair_complete.any())
            self.assertNotIn('advice',Unit.phases)

    def test_no_human_prefill_truth_stimulus_or_phase_mismatch(self):
        self.assertNotIn('synthetic_text_by_phase_item',CFG['task'])
        for key in ['initial_editor','final_editor']:self.assertEqual(CFG['stimuli'][key]['text'],'')
        self.assertNotIn('{truth}',json.dumps(CFG['stimuli'],ensure_ascii=False))
        self.assertEqual(len(CFG['task']['items']),12)


if __name__=='__main__':unittest.main()
