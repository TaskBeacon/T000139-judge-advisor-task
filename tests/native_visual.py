"""Actual native main/run_trial with disclosed synthetic fixtures; client-only screenshots.

Requires exclusive GUI lease. Does not claim physical keyboard or OS IME validation.
"""
import sys
from pathlib import Path
from types import SimpleNamespace
import yaml

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import main as task_main
from psyflow import StimUnit

OUT=ROOT/'references/validation'
cfg=yaml.safe_load((ROOT/'config/config_sampler_sim.yaml').read_text(encoding='utf8'))
cfg['timing'].update(initial_duration=2.5,final_duration=2.5,advice_duration=1.5,saved_duration=.15)
cfg['sim']['output_dir']='outputs/native_visual'
cfg['sim']['log_path']='outputs/native_visual/sim_events.jsonl'
cfg['sim']['responder']['kwargs']['rt_s']=1.2
path=ROOT/'outputs/native_visual_config.yaml'
path.write_text(yaml.safe_dump(cfg,sort_keys=False,allow_unicode=True),encoding='utf8')
native_window=[]
pending_capture=[]
captured=set()
original_initialize=task_main.initialize_exp


def initialize(settings):
    win,kb=original_initialize(settings)
    win.winHandle.activate()
    native_window.append(win)
    original_flip=win.flip
    def flip(*args,**kwargs):
        if pending_capture:
            phase=pending_capture.pop(0)
            win.getMovieFrame(buffer='back')
            win.movieFrames[-1].save(OUT/('native_'+phase+'.png'))
            win.movieFrames.clear()
        return original_flip(*args,**kwargs)
    win.flip=flip
    return win,kb


def schedule(unit):
    phase=unit.label if hasattr(unit,'label') else unit.unit_label
    if phase not in ['instruction','transition','initial','advice','final','good_bye'] or phase in captured:return
    captured.add(phase)
    pending_capture.append(phase)



for method in ['show','capture_response','wait_and_continue']:
    original=getattr(StimUnit,method)
    def wrapper(self,*args,_original=original,**kwargs):
        schedule(self)
        return _original(self,*args,**kwargs)
    setattr(StimUnit,method,wrapper)
task_main.initialize_exp=initialize
try:
    task_main.run(SimpleNamespace(mode='sim',config_path=path))
except SystemExit as exc:
    if exc.code not in (0,None):raise
finally:
    if len(captured)!=6:raise AssertionError(captured)
